# Rail - Square Medium

## Назначение

Экспериментальный Rail-шаблон со средними квадратными карточками `_Square Medium / Card` и `_Square Medium / Cover`. В имени мастера стоит маркер `🟡`.

## Когда использовать

- Для прототипирования промежуточного квадратного размера после согласования с владельцами ДС.
- Когда Square слишком крупный, а SquareSmall недостаточно заметный.

## Когда НЕ использовать

- Не выбирайте автоматически для продуктового макета до снятия WIP-статуса.
- Для готового решения используйте [Rail - Square](rail-square.md) или SquareSmall-шаблоны.

## Платформенные особенности iOS

- Пять `Device`-вариантов покрывают iPhone/iPad.
- Статус публикации `CHANGED`; при изменении статуса нужно актуализировать карточку.
- Рейл прокручивается горизонтально, а каждая карточка остаётся отдельным интерактивным элементом с собственным доступным названием.
- Значения визуальных токенов сверяются с Tokens Studio source of truth и из Figma в карточку не переносятся.

## Связанные компоненты

- [Rail - Square](rail-square.md), [Rail - SquareSmall1Story](rail-square-small-1-story.md), [Rail - SquareSmall2Story](rail-square-small-2-story.md).
- [Rail - Base](rail-base.md).

<!-- FIGMA_SYNC:START -->
## Актуальные данные Figma

> Последняя проверка: `2026-08-24T08:12:22Z` · структура `fed7747167c7` · статус `work-in-progress` · публикация Figma `CHANGED`.

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
| `410.0×196.0` | 1 | Device=iPhone 17 Pro Max |
| `1063.0×295.0` | 1 | Device=iPad Mini 6 |
| `1110.0×303.0` | 1 | Device=iPad 10 |
| `1306.0×330.0` | 1 | Device=iPad Pro 13 |

### Зависимости

- `Rail - Base` — node `29595:53876`; set `29595:53875`

### Источник

- [Rail - 🟡Square Medium](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=35893-32643) — fileKey `rMcDm5qGp4CXkXXddEbcMh`, API key `rMcDm5qGp4CXkXXddEbcMh`, node `35893:32643`, type `COMPONENT_SET`.
<!-- FIGMA_SYNC:END -->
