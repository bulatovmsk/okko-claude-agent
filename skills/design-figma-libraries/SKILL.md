---
name: design-figma-libraries
description: Карта Figma-библиотек дизайн-системы Окко. Отвечает на вопросы о структуре библиотек, зависимостях, fileKey/nodeId для доступа к данным через Figma API. Используется другими навыками для навигации по библиотекам и получения актуальных данных из Figma. Использовать, когда пользователь спрашивает «где лежит библиотека X», «какой fileKey у…», «какие библиотеки зависят от…», «вытащи данные из Figma».
---

# Okko Figma Libraries

Навигатор по Figma-библиотекам ДС Окко. Хранит реестр fileKey/nodeId, структуру библиотек и зависимости между ними.

## Когда срабатывать

- Вопросы о структуре библиотек: «какая библиотека для…», «где лежат токены…», «какой fileKey у…»
- Запросы на парсинг данных: «вытащи цвета из Figma», «какие иконки в Head Library»
- Навигация по зависимостям: «какие библиотеки зависят от Head Library»
- Вопросы о платформенных отличиях: «чем TV-токены отличаются от mobile»

## Как работать

### 1. Навигация

При вопросе о библиотеке → `docs/libraries-map.md` для fileKey, branchKey и nodeId.

### 2. Получение данных из Figma

В этом проекте два способа достать данные из Figma:

- **REST API через PAT** — массовые/скриптовые запросы. Скрипты-обёртки лежат в `scripts/`:
  - `scripts/figma-api.sh "<endpoint>"` — произвольный GET, напр. `/v1/files/<key>/nodes?ids=<ids>`
  - `scripts/figma-fetch-node.sh <fileKey> <nodeId>` — выгрузка JSON ноды в `.figma-cache/`
  - `scripts/figma-render.sh <fileKey> <nodeId> [<scale>] [<format>]` — PNG/SVG-рендеры
  - PAT берётся из `.env` (`FIGMA_TOKEN`)
- **Figma MCP (`claude.ai Figma`)** — точечные интерактивные операции: `get_design_context`, `get_metadata`, `get_screenshot`, `get_variable_defs`, `use_figma`, `upload_assets`.

> Variables API REST → 403 без Enterprise scope. Resolved-значения цветовых переменных получать через MCP `get_variable_defs(nodeId, fileKey)`.

### 3. Локальный кэш

Источник истины по уже распарсенным данным — папка **`design-system/`** в корне репо (не `docs/` этого скила):

| Что | Где |
|---|---|
| Цвета (primitives + semantic + Brand) | [`design-system/tokens/colors.md`](../../design-system/tokens/colors.md) |
| Spacing (рампа + screen-padding) | [`design-system/tokens/spacing.md`](../../design-system/tokens/spacing.md) |
| Corner-radius (шкала + `round`) | [`design-system/tokens/corner-radius.md`](../../design-system/tokens/corner-radius.md) |
| Типографика (TEXT-стили mobile/web) | [`design-system/tokens/typography.md`](../../design-system/tokens/typography.md) |
| Spacing TV (24 + 2 screen-padding) | [`design-system/tokens/spacing-tv.md`](../../design-system/tokens/spacing-tv.md) |
| Corner-radius TV (16 regular + 15 focus) | [`design-system/tokens/corner-radius-tv.md`](../../design-system/tokens/corner-radius-tv.md) |
| Типографика TV (30 TEXT-стилей) | [`design-system/tokens/typography-tv.md`](../../design-system/tokens/typography-tv.md) |
| Иконки Main Pack (493 в 16 категориях) | [`design-system/components/icons.md`](../../design-system/components/icons.md) |
| Иллюстрации (Static / Product images / Bobokko) | [`design-system/components/illustrations.md`](../../design-system/components/illustrations.md) |
| Карточки компонентов (chips, select, sheet-native и др.) | [`design-system/components/*.md`](../../design-system/components/) |
| Гайдлайны и структура секций | [`design-system/guidelines/`](../../design-system/guidelines/) |

В `docs/` этого скила лежит только то, чего нет в `design-system/`:
- `libraries-map.md` — реестр библиотек, fileKey/branchKey, ключевые nodeId, граф зависимостей

### 4. Приоритет источников

**Figma (live) > Локальный кэш в `design-system/` > `docs/libraries-map.md`**

Если данные противоречат живой Figma — Figma приоритетнее, предупреди об этом.

## Связь с другими навыками

- [`design-ds-librarian`](../design-ds-librarian/SKILL.md) — справочник по ДС, использует этот скил для получения fileKey/nodeId, чтобы при необходимости подтянуть свежие данные.
- [`design-ds-auditor`](../design-ds-auditor/SKILL.md) — при аудите макетов может запрашивать актуальные данные компонентов из Figma.
- [`design-layout-helper`](../design-layout-helper/SKILL.md) — при сборке экранов может запрашивать пропсы компонентов.
- [`design-doc-writer`](../design-doc-writer/SKILL.md) — использует fileKey/nodeId шаблонов секций и эталонных гайдов из этого скила.

## Обновление данных (команда sync)

Два sync-скрипта — по одному на каждый файл-источник:

```bash
bash scripts/figma-sync-head-library.sh [colors|icons|illustrations|all]   # Okko Head Library
bash scripts/figma-sync-tokens.sh        [spacing|corner-radius|typography|spacing-tv|corner-radius-tv|typography-tv|all|all-mw|all-tv]   # 🦖/🦍 Tokens
```

Триггеры в чате (распознавать как запрос на sync):
- Head Library: «обнови данные Head Library», «синхронизируй цвета», «refresh head library», «sync icons», «обнови иконки» · слэш-форма `/sync-head-library [target]`
- Tokens (mobile/web): «обнови spacing», «sync typography», «обнови токены mobile/web», «синхронизируй corner radius» · слэш-форма `/sync-tokens [target]`
- Tokens (tv): «обнови spacing TV», «sync typography tv», «синхронизируй радиусы тв», «обнови ТВ токены» · слэш-форма `/sync-tokens [spacing-tv|corner-radius-tv|typography-tv|all-tv]`

**Шаги, которые делает скил при срабатывании триггера:**

1. Запустить соответствующий скрипт через Bash. Скрипты пишут актуальный контент в `design-system/`. Ручные разделы («Правила выбора модификатора» в `icons.md`, «Правила выбора стиля» в `typography.md`, «Правила выбора» в `spacing.md` / `corner-radius.md`) сохраняются.
2. **Если в файле есть маркер `<!-- VARDEFS_FROM_MCP:* -->` (цвета) или `<!-- VARDEFS_FROM_PLUGIN_API:* -->` (spacing / corner-radius / `-tv`-варианты)** — нужно подставить значения переменных через Plugin API.
   Выполнить `use_figma`-снимок (fileKey зависит от целевого файла: `HYB1u9ysALVWtVWKoagiDH` — Head Library, `vztN8doGwBZOCbpDf2PhKR` — 🦖 Tokens mobile/web, `Zn2JrOHhSURjCuUEp6JcI8` — 🦍 Tokens TV):
   - для цветов: `figma.variables.getLocalVariableCollectionsAsync()` → коллекции `Theme` + `Primitives` → резолв по Dark mode (с разворачиванием алиасов) → запись JSON в temp TEXT-узел.
   - для NUMBER-переменных (spacing/corner-radius): то же, но фильтр по `resolvedType === 'FLOAT'`.
   Temp-узлы: `__VARDEFS_DUMP__` (цвета), `__NUMBER_VARDEFS_DUMP__` (mobile/web NUMBER), `__NUMBER_VARDEFS_DUMP_TV__` (TV NUMBER). Затем прочитать узел через REST `/v1/files/<key>/nodes?ids=<id>`, распарсить JSON из `characters`, подставить в маркеры в файлах. Удалить temp-узел. (`get_variable_defs` MCP-tool требует ручное выделение слоя — не надёжен, **используем Plugin API**.)
3. Показать пользователю `git diff -- design-system/` и предложить закоммитить.

Что обновляется в каждом таргете:

| Скрипт | Target | Файл | Источник в Figma |
|---|---|---|---|
| `figma-sync-head-library.sh` | `colors` | `design-system/tokens/colors.md` | `/styles` + node `32102:23149` (Color Tokens) + Plugin API variables |
| `figma-sync-head-library.sh` | `icons` | `design-system/components/icons.md` | node `29361:322` (Main Pack) |
| `figma-sync-head-library.sh` | `illustrations` | `design-system/components/illustrations.md` | nodes `39089:10560`, `39101:215`, `39104:349` |
| `figma-sync-tokens.sh` | `typography` | `design-system/tokens/typography.md` | `/styles` (TEXT) + дозапрос нод (font properties) — file `vztN8doGwBZOCbpDf2PhKR` |
| `figma-sync-tokens.sh` | `spacing` | `design-system/tokens/spacing.md` | Plugin API: коллекция `Semantic` mode `Web&Mobile`, FLOAT-переменные `spacing/*` + `screen-padding/*` |
| `figma-sync-tokens.sh` | `corner-radius` | `design-system/tokens/corner-radius.md` | Plugin API: коллекция `Semantic`, FLOAT-переменные `corner-radius/*` |
| `figma-sync-tokens.sh` | `typography-tv` | `design-system/tokens/typography-tv.md` | `/styles` (TEXT) — file `Zn2JrOHhSURjCuUEp6JcI8` |
| `figma-sync-tokens.sh` | `spacing-tv` | `design-system/tokens/spacing-tv.md` | Plugin API: коллекция `Semantic` mode `TV`, FLOAT `spacing/*` + `screen-padding/*` |
| `figma-sync-tokens.sh` | `corner-radius-tv` | `design-system/tokens/corner-radius-tv.md` | Plugin API: коллекция `Semantic` mode `TV`, FLOAT `corner-radius/*` (regular + focus) |
| `figma-sync-tokens.sh` | `all-mw` / `all-tv` / `all` | всё подряд по группам | — |

## Ограничения

- Variables API недоступен через REST (403 без Enterprise scope). Resolved-значения цветовых переменных (Light/Dark) — только через MCP `get_variable_defs` (требует ручное выделение) или через Plugin API в `use_figma` (см. шаг 2 выше — рекомендованный путь).
- Deprecated-страницы и токены не парсятся и не хранятся.
- Платформенные библиотеки Android / TV / Web — fileKey пока не зафиксированы (см. `docs/libraries-map.md`, секция TBD).
