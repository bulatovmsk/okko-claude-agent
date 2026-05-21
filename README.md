# okko-claude-agent

Агент для работы с дизайн-системой Окко на базе Claude Design и Agent Skills.

## Что это

Набор артефактов, которые превращают Claude Design в специалиста по ДС Окко:

1. **`design-system/`** — source-of-truth дизайн-системы, который загружается в Claude Design на уровне организации (Слой 1).
2. **`skills/`** — Agent Skills, расширяющие возможности Claude Design (Слой 2): аудит соответствия, Q&A, помощь со сборкой макетов, платформенные нюансы.
3. **`scripts/`** — утилиты для упаковки Skills и синхронизации с Figma.

## Три слоя архитектуры

| Слой | Где живёт | Кто настраивает | Как обновляется |
|---|---|---|---|
| 1. Org Design System | Claude Design (organization-level) | Админ ДС, один раз | При изменениях в Figma — пересборка |
| 2. Agent Skills | claude.ai (per user) | Каждый дизайнер/разработчик ставит сам | Через `scripts/pack-skills.sh` + ручная загрузка |
| 3. Per-project context | Claude Design (per project) | Сам пользователь, по задаче | На лету |

## Быстрый старт

### Для админа ДС (Слой 1)

1. Открой Claude Design → admin → Design System.
2. Залей содержимое `design-system/` как контекст: `DESIGN_SYSTEM.md`, токены, карточки компонентов.
3. Если Figma-библиотека доступна через Claude Figma Plugin — подключи её там же.
4. Создай тестовый проект, убедись что Claude применяет ДС Окко.
5. Включи **Published toggle**. Готово — все новые проекты команды используют ДС автоматически.

### Для дизайнера/разработчика (Слой 2)

1. Склонируй этот репо.
2. Запусти `bash scripts/pack-skills.sh` — получишь `dist/*.zip`.
3. В claude.ai: **Settings → Features → Skills → Upload** — загрузи каждый zip.
4. Готово. Claude автоматически вызовет нужный Skill, когда задача подходит под его описание.

### Для проектов (Слой 3)

Внутри конкретного проекта в Claude Design прикладывай:
- скриншоты текущего флоу,
- референсы конкурентов,
- доку фичи или продуктовые требования.

## Skills

| Skill | Когда вызывается |
|---|---|
| `okko-ds-librarian` | «Какой компонент использовать для…», «какой токен…», поиск по библиотеке |
| `okko-ds-auditor` | Проверка макета/прототипа на соответствие ДС: токены, компоненты, паттерны |
| `okko-layout-helper` | Сборка макета экрана из компонентов ДС |
| `okko-doc-writer` | Написание гайдлайна (документации) компонента в Figma по единому шаблону |
| `okko-platform-tv` | Особенности TV (D-pad focus, размеры под 10-foot UI, Android TV / SmartTV Web) |
| `okko-platform-mobile` | Особенности iOS/Android (safe area, touch targets, gestures) |

## Обновление

При изменении ДС в Figma:

```bash
bash scripts/sync-from-figma.sh    # обновит design-system/tokens и components/
bash scripts/pack-skills.sh        # перепакует skills
```

## Работа с Figma напрямую через REST API

Когда лимиты Figma MCP мешают (или просто удобнее скриптами), используем Figma REST API:

```bash
# 1. Создай .env из .env.example, положи туда FIGMA_TOKEN (Personal Access Token)
cp .env.example .env
$EDITOR .env

# 2. Выгрузить структуру ноды как JSON
bash scripts/figma-fetch-node.sh rMcDm5qGp4CXkXXddEbcMh 28934:239837

# 3. Получить PNG-рендер ноды
bash scripts/figma-render.sh rMcDm5qGp4CXkXXddEbcMh 28934:239837 2 png

# 4. Произвольный GET к Figma API
bash scripts/figma-api.sh "/v1/files/$FIGMA_LIB_IOS_KEY/variables/local"
```

Кэш выгрузок — в `.figma-cache/` (в `.gitignore`).

## Гайдлайны компонентов

Структура и шаблоны гайдлайнов — в [`design-system/guidelines/`](design-system/guidelines/).

- [STRUCTURE.md](design-system/guidelines/STRUCTURE.md) — общий каркас гайдлайна (15 секций, обязательные/рекомендованные/опциональные).
- [section-templates/](design-system/guidelines/section-templates/) — детальные шаблоны по каждой секции.

За автоматическое создание гайдлайнов в Figma отвечает Skill `okko-doc-writer`.

После — повторить шаги «для админа» и оповестить команду, что нужно обновить Skills у себя.

## Структура

```
okko_claude_agent/
├── design-system/        # Слой 1: source-of-truth ДС
│   ├── DESIGN_SYSTEM.md
│   ├── tokens/
│   ├── components/
│   ├── platforms/
│   └── brand/
├── skills/               # Слой 2: исходники Agent Skills
│   ├── okko-ds-librarian/
│   ├── okko-ds-auditor/
│   ├── okko-layout-helper/
│   ├── okko-platform-tv/
│   └── okko-platform-mobile/
└── scripts/
    ├── pack-skills.sh
    └── sync-from-figma.sh
```

## Ограничения

- **Skills в claude.ai не шарятся командно.** Каждый ставит у себя — мы выбрали это сознательно, до появления org-wide Skills в Claude Design.
- **Network access у Skills ограничен** настройками организации. Skills рассчитаны на автономную работу с бандлованными `references/`, без живых походов в Figma.
- **Round-trip Figma↔Claude Design** пока ограничен. Для финальной правки макета в Figma — используйте Figma MCP отдельно или экспорт.
