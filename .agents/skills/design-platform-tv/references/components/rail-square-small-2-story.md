# Rail - SquareSmall2Story

## Назначение

Компактный Rail-шаблон с двумя рядами маленьких квадратных карточек `_Square Small Story / Card`.

## Когда использовать

- Когда нужно показать больше компактных сущностей в двухэтажной горизонтальной раскладке.
- Для плотной подборки, где карточки одного типа образуют два ряда.

## Когда НЕ использовать

- Для одного ряда используйте [Rail - SquareSmall1Story](rail-square-small-1-story.md).
- Не используйте отдельный Phone 320: он помечен `[Deprecated]` и сохранён только как связанный исторический источник.

## Платформенные особенности iOS

- Ось называется `device` со строчной буквы и содержит пять актуальных раскладок.
- Отдельный мастер Phone 320 размером 290×218 не входит в актуальный COMPONENT_SET.
- Рейл прокручивается горизонтально, а каждая карточка остаётся отдельным интерактивным элементом с собственным доступным названием.
- Значения визуальных токенов сверяются с Tokens Studio source of truth и из Figma в карточку не переносятся.

## Связанные компоненты

- [Rail - SquareSmall1Story](rail-square-small-1-story.md), [Rail - Square](rail-square.md).
- [Rail - Base](rail-base.md) и [семейство Rail](rail-family.md).

<!-- FIGMA_SYNC:START -->
## Актуальные данные Figma

> Последняя проверка: `2026-08-24T08:12:21Z` · структура `4f355bf01c88` · статус `ready` · публикация Figma `CHANGED`.

### Свойства из компонента

| Свойство | Тип | Значение по умолчанию | Варианты |
|---|---|---|---|
| `device` | `variant` | `iPhone 15` | iPad 10 / iPad Mini 6 / iPad Pro 13 / iPhone 15 / iPhone 17 Pro Max |

### Варианты и размеры

| Ось | Значения |
|---|---|
| `device` | iPad 10 / iPad Mini 6 / iPad Pro 13 / iPhone 15 / iPhone 17 Pro Max |

Комбинаций в COMPONENT_SET: **5**.

| Размер | Количество вариантов | Примеры |
|---|---:|---|
| `363.0×264.0` | 1 | device=iPhone 15 |
| `410.0×298.0` | 1 | device=iPhone 17 Pro Max |
| `1063.0×254.0` | 1 | device=iPad Mini 6 |
| `1110.0×262.0` | 1 | device=iPad 10 |
| `1306.0×318.0` | 1 | device=iPad Pro 13 |

### Зависимости

- `Rail - Base` — node `29595:53876`; set `29595:53875`

### Источник

- [Rail - SquareSmall2Story](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=7616-73598) — fileKey `rMcDm5qGp4CXkXXddEbcMh`, API key `rMcDm5qGp4CXkXXddEbcMh`, node `7616:73598`, type `COMPONENT_SET`.
- [Rail / 🟡SquareSmall2Story [Нет в проде]/[Deprecated] Phone 320](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=7616-73662) — `example`, node `7616:73662`.
<!-- FIGMA_SYNC:END -->
