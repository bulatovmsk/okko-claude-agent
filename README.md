# Okko Codex Skills

Repo-scoped навыки Codex для работы с дизайн-системой и интерфейсными текстами Okko.

Исходный репозиторий: <https://github.com/bulatovmsk/okko-claude-agent>.

## Как устроено

```text
.
├── .agents/skills/          # навыки, которые Codex обнаруживает из проекта
│   ├── design-ds-librarian/
│   ├── design-ds-auditor/
│   ├── design-layout-helper/
│   ├── design-doc-writer/
│   ├── design-figma-libraries/
│   ├── design-platform-mobile/
│   ├── design-platform-tv/
│   └── ux-copy/
├── design-system/          # source of truth для компонентов и правил
├── scripts/                # синхронизация, проверка и упаковка
└── dist/                   # собранные zip-пакеты
```

Каждый skill содержит обязательный `SKILL.md`, опциональные `references/` и UI-метаданные `agents/openai.yaml`. Большие справочники читаются только тогда, когда они нужны задаче.

## Использование в Codex

Клонируй репозиторий и открой его каталог как рабочую папку:

```bash
git clone https://github.com/bulatovmsk/okko-claude-agent.git
cd okko-claude-agent
```

Codex автоматически сканирует `.agents/skills` и выбирает навык по `description`.

Навык можно вызвать явно:

```text
$design-ds-librarian Какой компонент использовать для фильтра по жанру?
$design-ds-auditor Проверь этот экран по ДС Okko
$ux-copy Проверь текст кнопки: «Нажмите для продолжения»
```

Если обновлённый skill не появился в списке, перезапусти Codex.

## Навыки

| Skill | Назначение |
|---|---|
| `design-ds-librarian` | Поиск компонентов, токенов и правил ДС |
| `design-ds-auditor` | Аудит макетов, скриншотов и Figma-фреймов |
| `design-layout-helper` | Структура экранов и платформенная компоновка |
| `design-doc-writer` | Гайдлайны компонентов в Figma |
| `design-figma-libraries` | Карта библиотек и синхронизация данных Figma |
| `design-platform-mobile` | Правила iOS и Android |
| `design-platform-tv` | D-pad, focus и ограничения TV |
| `ux-copy` | Редактура интерфейсных текстов по Редполитике |

## Обновление данных

`design-system/` остаётся единственным редактируемым источником для компонентов, токенов, платформенных правил и шаблонов гайдлайнов. После изменений обнови бандлованные references:

```bash
bash scripts/sync-skill-references.sh
```

Проверить все навыки:

```bash
bash scripts/validate-skills.sh
```

Для синхронизации из Figma создай `.env` по `.env.example`, затем выбери минимальный набор данных:

```bash
bash scripts/sync-from-figma.sh head colors
bash scripts/sync-from-figma.sh tokens typography
bash scripts/sync-from-figma.sh tokens all-tv
```

Команда работает через staged-копию: получает данные, разрешает variable aliases, обновляет `design-system/`, пересобирает references, валидирует skills и только после этого переносит результат в рабочие файлы. Отчёт каждого запуска сохраняется в `.figma-cache/reports/`. Если данных для aliases нет, рабочие файлы не меняются.

Variables API может быть недоступен текущему REST-токену. В этом случае Codex получает variable dump через Figma MCP и передаёт каталог команде:

```bash
bash scripts/sync-from-figma.sh tokens spacing \
  --variables-dir .figma-cache/variable-dumps/current
```

Поддерживаются имена `{fileKey}.json`, `head.json`, `mobile-web.json` и `tv.json`. Dump может быть сырым ответом Variables API, компактным экспортом Plugin API или объектом `resolvedValues` из `get_variable_defs`. Resolver обнаруживает циклические и отсутствующие aliases и останавливает публикацию staged-результата.

Доступны группы `head`, `tokens` и `all`. Для разовой выгрузки нод и рендеров используй REST-утилиты в `scripts/`.

## Сборка

Команда ниже синхронизирует references, запускает валидацию и создаёт отдельный zip для каждого skill:

```bash
bash scripts/pack-skills.sh
```

Архивы появятся в `dist/`. Для работы внутри этого проекта архивы не нужны: Codex использует `.agents/skills` напрямую. Для распространения всего набора как одного устанавливаемого продукта лучше оформить его как Codex plugin.

## Принципы поддержки

- Не редактируй сгенерированные копии дизайн-системы внутри `references/`; меняй `design-system/` и запускай синхронизацию.
- Не добавляй в инструкции компоненты и токены, которых нет в source of truth.
- Живая Figma имеет приоритет над локальной выжимкой, но расхождение нужно явно отмечать.
- Подключения Figma и Atlassian опциональны; без них skills работают по локальным данным и не обещают внешних изменений.
