# Настройка UX-copy агента

Агент проверяет интерфейсные тексты по Редполитике Окко и продакшн-референсу. Работает с текстом напрямую и с Figma-ссылками.

## Что понадобится

| Компонент | Для чего | Обязателен? |
|---|---|---|
| OpenCode | Среда запуска агента | Да |
| Figma MCP | Извлечение текста из Figma-ссылок | Нет (без него — только текстовый режим) |
| Confluence MCP | Автосинк Редполитики | Нет (без него — используется локальный кэш) |

---

## Шаг 1 — Разместить папку

Скопировать `ux-copy/` в корень проекта, рядом с `AGENTS.md`:

```
<ваш-проект>/
├── AGENTS.md
└── ux-copy/
    ├── _skills/
    ├── sources/
    ├── ux-editor.md
    └── SETUP.md       ← этот файл
```

## Шаг 2 — Добавить маршрутизацию в AGENTS.md

Если `AGENTS.md` уже есть — добавить строку в таблицу:

```
| UX-копирайтинг | копирайт, текст, ux-copy, интерфейсный текст, надпись, кнопка, лейбл, плейсхолдер, тост, тултип, редактура, формулировка | `ux-copy/ux-editor.md` |
```

Если `AGENTS.md` ещё нет — создать с таким содержимым:

```markdown
# Agent routing

## Rules

Before executing any task, check the table below. If a trigger matches — read the linked file first, then follow its steps exactly.

| Task type | Trigger keywords | Agent file |
|---|---|---|
| UX-копирайтинг | копирайт, текст, ux-copy, интерфейсный текст, надпись, кнопка, лейбл, плейсхолдер, тост, тултип, редактура, формулировка | `ux-copy/ux-editor.md` |

## Default

If no trigger matches — execute the task directly without loading any agent file.
```

## Шаг 3 — Настроить Figma MCP

Нужен, чтобы агент мог сам вытащить текст из Figma по ссылке. Без него — передавай текст вручную.

В OpenCode: **Settings → MCP Servers** добавить сервер Figma.

Или добавить в конфиг OpenCode (`~/.config/opencode/config.json`):

```json
{
  "mcp": {
    "figma": {
      "type": "sse",
      "url": "https://mcp.figma.com/sse",
      "headers": {
        "X-Figma-Token": "ТВОЙ_FIGMA_TOKEN"
      }
    }
  }
}
```

Токен Figma: [figma.com](https://figma.com) → Settings → Account → Personal access tokens.

## Шаг 4 — Настроить Confluence MCP (опционально)

Нужен для автоматического обновления Редполитики. Без него агент работает с локальным файлом `sources/editorial-policy.md` — он уже заполнен и пригоден к использованию.

```json
{
  "mcp": {
    "atlassian": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@mcp-atlassian/server"],
      "env": {
        "CONFLUENCE_URL": "https://okko.atlassian.net",
        "CONFLUENCE_EMAIL": "твой@email.com",
        "CONFLUENCE_API_TOKEN": "ТВОЙ_CONFLUENCE_TOKEN"
      }
    }
  }
}
```

Токен Confluence: atlassian.com → Account Settings → Security → API tokens.

## Шаг 5 — Проверить

Напиши в чате:

> `Проверь текст кнопки: "Нажмите для продолжения"`

Агент должен разобрать нарушения и предложить варианты редактуры.  
Если что-то не настроено — он сам скажет что именно нужно подключить.

---

## Обновление

| Что | Как |
|---|---|
| Редполитика | Обновляется автоматически при каждом запросе (если подключён Confluence MCP) |
| Продакшн-токены | Заменить файлы в `sources/production-reference/` новым экспортом из Figma |
| Инструкции агента | Получить обновлённую папку `ux-copy/` у автора (или `git pull`) |
