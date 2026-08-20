# confluence-sync

Optional protocol for refreshing a local Markdown cache from Confluence.

## When to use

Use only when the user explicitly asks to refresh the policy and a suitable
Atlassian or Confluence connector is available. Ordinary copy review uses the
bundled local policy and must not mutate it.

## Protocol

### Input parameters (provided by the calling agent)

| Parameter | Description |
|---|---|
| `local_file` | Path to the local Markdown cache (relative to project root) |
| `root_page_id` | Confluence page ID of the root document |
| `index_page_id` | Confluence page ID of the child-index page (optional; set to `null` if the root has no structured children) |
| `label` | Human label for synced doc, used for reference |

### Steps

1. **Confirm the refresh target.** The default is
   `references/editorial-policy.md` inside this skill. Do not overwrite a
   different file without explicit user direction.
2. **Read local file.**
   - If missing → treat `confluence_version` as `0`, `descendant_versions` as `{}`.
   - If exists → read `confluence_version` and `descendant_versions` from YAML frontmatter.

3. **Fetch root page metadata** with the connected Atlassian/Confluence tool. Request metadata without full content when the tool supports it.
   - Extract `version.number` and `version.message` (commit comment; may be empty).

4. **Fast path — all versions match:**
   If `confluence_version` == root page version:
   a. If `index_page_id` is `null` → **skip to step 6**. Use the local file as-is.
   b. If `index_page_id` is not `null` AND `descendant_versions` is populated (not `{}`):
      - List child pages of `index_page_id` with `include_content=false`.
      - Compare each child's version with `descendant_versions`.
      - If ALL match → **skip to step 6**. Use the local file as-is.

5. **Slow path — versions differ or local file is stale:**
   a. If root version changed → fetch root page content.
      If root version matches → reuse local root content (do not re-fetch).
   b. List child pages of `index_page_id` with `include_content=false`
      (skip if `index_page_id` is `null` or already done in step 3).
   c. Fetch content ← **1 request per changed page**
      ONLY for children whose version differs from `descendant_versions`
      or is absent in `descendant_versions`.
      For children whose version matches → reuse local content (do not re-fetch).
   d. Remove stale entries from `descendant_versions` (pages that no longer exist
      as children of `index_page_id`).
   e. Create/overwrite the local file:
      - frontmatter:
        ```
        confluence_page_id: <root_page_id>
        confluence_version: <new root version>
        confluence_version_message: <version.message or null>
        descendant_versions: {<page_id>: <version>, …}
        last_synced: <today ISO>
        ```
      - body: root policy content + content from children (format defined by calling agent)
   f. Report to user:
      `📌 Обновил локальный файл <label> до (v<new>): <version.message (if it exists)>`

6. Note which source was used (local / updated).

7. Proceed with the calling skill's workflow using the file content.

### Fallback (no Atlassian MCP)

Read the local file and use its content.
If the file is missing or contains only a placeholder, fall back to general
best practices and begin your response with:
`⚠️ Нет локального файла <label> и доступа к Confluence. Отвечаю без документации.`
