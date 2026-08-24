# Rail - Square

## Назначение

Rail-шаблон со стандартными квадратными карточками `_Square Card` и внутренними обложками `_Cover`.

## Когда использовать

- Для контента, чья основная обложка имеет квадратную форму.
- Когда нужен один горизонтальный ряд полноразмерных квадратных карточек.

## Когда НЕ использовать

- Для компактных квадратных карточек используйте SquareSmall1Story или SquareSmall2Story.
- Не смешивайте квадратную и горизонтальную геометрию в одном шаблоне.

## Платформенные особенности iOS

- `Device` содержит пять iPhone/iPad-вариантов.
- На узких экранах сохраняйте горизонтальную прокрутку и целостность квадратной карточки.
- Рейл прокручивается горизонтально, а каждая карточка остаётся отдельным интерактивным элементом с собственным доступным названием.
- Значения визуальных токенов сверяются с Tokens Studio source of truth и из Figma в карточку не переносятся.

## Связанные компоненты

- [Rail - SquareSmall1Story](rail-square-small-1-story.md), [Rail - SquareSmall2Story](rail-square-small-2-story.md), [Rail - Square Medium](rail-square-medium.md).
- [Rail - Base](rail-base.md).

<!-- FIGMA_SYNC:START -->
## Актуальные данные Figma

> Последняя проверка: `2026-08-24T08:12:21Z` · структура `ae82828af707` · статус `ready` · публикация Figma `CHANGED`.

### Свойства из компонента

| Свойство | Тип | Значение по умолчанию | Варианты |
|---|---|---|---|
| `Device` | `variant` | `iPhone 15` | iPad 10 / iPad Mini 6 / iPad Pro 13 / iPhone 15 / iPhone 17 Pro Max |

### Варианты и размеры

| Ось | Значения |
|---|---|
| `Device` | iPad 10 / iPad Mini 6 / iPad Pro 13 / iPhone 15 / iPhone 17 Pro Max |

Комбинаций в COMPONENT_SET: **5**.

| Размер | Количество вариантов | Примеры |
|---|---:|---|
| `363.0×202.0` | 1 | Device=iPhone 15 |
| `410.0×227.0` | 1 | Device=iPhone 17 Pro Max |
| `1063.0×251.0` | 1 | Device=iPad Mini 6 |
| `1110.0×259.0` | 1 | Device=iPad 10 |
| `1306.0×286.0` | 1 | Device=iPad Pro 13 |

### Зависимости

- `Rail - Base` — node `29595:53876`; set `29595:53875`

### Источник

- [Rail - Square](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=7768-73596) — fileKey `rMcDm5qGp4CXkXXddEbcMh`, API key `rMcDm5qGp4CXkXXddEbcMh`, node `7768:73596`, type `COMPONENT_SET`.
<!-- FIGMA_SYNC:END -->
