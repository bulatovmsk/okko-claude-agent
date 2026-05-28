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
| Иконки Main Pack (490 в 16 категориях) | [`design-system/components/icons.md`](../../design-system/components/icons.md) |
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

Кэш в `design-system/` синхронизируется со свежей Figma по команде:

```bash
bash scripts/figma-sync-head-library.sh [colors|icons|illustrations|all]
```

Триггеры в чате (распознавать как запрос на sync):
- «обнови данные Head Library», «синхронизируй цвета», «refresh head library», «sync icons», «обнови иконки»
- слэш-форма: `/sync-head-library [target]`

**Шаги, которые делает скил при срабатывании триггера:**

1. Запустить `scripts/figma-sync-head-library.sh <target>` через Bash. Скрипт перепишет соответствующие файлы в `design-system/`. Раздел «Правила выбора модификатора» в `icons.md` сохраняется (он ручной).
2. **Для цветов**: после скрипта в `design-system/tokens/colors.md` появится маркер `<!-- VARDEFS_FROM_MCP:semantic ... -->`. Чтобы заполнить resolved-hex semantic-токенов — выполнить use_figma-скрипт, который вызывает `figma.variables.getLocalVariableCollectionsAsync()` для коллекций `Theme` и `Primitives`, резолвит по Dark mode и пишет результат в temp TEXT-узел `__VARDEFS_DUMP__`. Затем прочитать узел через REST, распарсить и подставить в маркеры. (`get_variable_defs` MCP-tool требует ручное выделение слоя в Figma, поэтому ненадёжен — используем Plugin API.)
3. Показать пользователю `git diff -- design-system/` и предложить закоммитить.

Что обновляется в каждом таргете:

| Target | Файл | Источник в Figma |
|---|---|---|
| `colors` | `design-system/tokens/colors.md` | `/styles` + node `32102:23149` (Color Tokens) + Plugin API variables |
| `icons` | `design-system/components/icons.md` | node `29361:322` (Main Pack) |
| `illustrations` | `design-system/components/illustrations.md` | nodes `39089:10560`, `39101:215`, `39104:349` |
| `all` | всё подряд | — |

## Ограничения

- Variables API недоступен через REST (403 без Enterprise scope). Resolved-значения цветовых переменных (Light/Dark) — только через MCP `get_variable_defs` (требует ручное выделение) или через Plugin API в `use_figma` (см. шаг 2 выше — рекомендованный путь).
- Deprecated-страницы и токены не парсятся и не хранятся.
- Платформенные библиотеки Android / TV / Web — fileKey пока не зафиксированы (см. `docs/libraries-map.md`, секция TBD).
