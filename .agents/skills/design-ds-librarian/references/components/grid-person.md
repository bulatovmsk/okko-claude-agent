# Grid / Person

## Назначение

Адаптивная сетка персон и участников с круглыми обложками. Мастер задаёт
заголовок, карусель карточек и готовую раскладку для четырёх breakpoint.

## Когда использовать

- Для подборок актёров, спортсменов, ведущих и других персон.
- Когда нужен готовый ряд карточек персон с единым поведением на iPhone и iPad.
- `Heading` выключайте только если заголовок уже задан окружающим разделом.

## Когда НЕ использовать

- Не используйте для обычных постеров контента: выбирайте [Grid / Main](grid-main.md),
  [Grid / Vertical](grid-vertical.md) или [Grid / Square](grid-square.md).
- Не собирайте ряд из `_Person / Card` и `_Person / Cover`: это внутренние
  запчасти мастера.

## Платформенные особенности iOS

- `Breakpoint` содержит `iPhone SE`, `iPhone`, `iPad` и `iPad Pro`; тема сейчас
  только `Dark`.
- На iPhone сетка высокая, на iPad — широкая. Размер выбирается вариантом, а не
  ручным растягиванием.
- В VoiceOver каждая персона остаётся отдельным элементом с именем и ролью;
  декоративную обложку отдельно не озвучивайте.
- Значения цветов, отступов и типографики сверяются с Tokens Studio source of
  truth и из Figma в карточку не переносятся.

## Связанные компоненты

- [Семейство Grid](grid-family.md) — выбор типа сетки.
- `_Person / Card` и `_Person / Cover` — внутренние детали, отдельно не
  публикуются и в память не регистрируются.
- `Навигационные / Переход в коллекцию` — действие в заголовке раздела.

<!-- FIGMA_SYNC:START -->
## Актуальные данные Figma

> Последняя проверка: `2026-08-24T14:23:13Z` · структура `cff16c27a0bf` · статус `ready` · публикация Figma `CHANGED`.

### Свойства из компонента

| Свойство | Тип | Значение по умолчанию | Варианты |
|---|---|---|---|
| `Breakpoint` | `variant` | `iPad Pro` | iPad / iPad Pro / iPhone / iPhone SE |
| `Heading` | `boolean` | `true` | — |
| `Theme` | `variant` | `Dark` | Dark |

### Варианты и размеры

| Ось | Значения |
|---|---|
| `Breakpoint` | iPad / iPad Pro / iPhone / iPhone SE |
| `Theme` | Dark |

Комбинаций в COMPONENT_SET: **4**.

| Размер | Количество вариантов | Примеры |
|---|---:|---|
| `288.0×622.0` | 1 | Breakpoint=iPhone SE, Theme=Dark |
| `358.0×702.0` | 1 | Breakpoint=iPhone, Theme=Dark |
| `704.0×336.0` | 1 | Breakpoint=iPad, Theme=Dark |
| `960.0×400.0` | 1 | Breakpoint=iPad Pro, Theme=Dark |

### Зависимости

- `_Person / Card` — node `23197:42868`
- `_Person / Card/iPhone SE` — node `23197:55666`
- `_Person / Cover` — node `23197:42858`
- `_Person / Cover/iPhone 320` — node `23197:55662`
- `Europe / Russia` — node `32890:399177`
- `Навигационные / Переход в коллекцию` — node `1305:27`

### Источник

- [Grid / Person](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=23272-59082) — fileKey `rMcDm5qGp4CXkXXddEbcMh`, API key `rMcDm5qGp4CXkXXddEbcMh`, node `23272:59082`, type `COMPONENT_SET`.
<!-- FIGMA_SYNC:END -->
