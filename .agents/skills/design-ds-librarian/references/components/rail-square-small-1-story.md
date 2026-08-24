# Rail - SquareSmall1Story

## Назначение

Компактный Rail-шаблон с одним рядом маленьких квадратных карточек `_Square Small Story / Card`.

## Когда использовать

- Когда требуется плотный одноэтажный ряд второстепенных сущностей.
- Для компактной квадратной навигации или подборки без второго ряда.

## Когда НЕ использовать

- Для двух рядов используйте [Rail - SquareSmall2Story](rail-square-small-2-story.md).
- Для более заметной квадратной карточки используйте [Rail - Square](rail-square.md).

## Платформенные особенности iOS

- Пять значений `Device` покрывают iPhone/iPad.
- Не увеличивайте маленькие карточки вручную: смените шаблон семейства.
- Рейл прокручивается горизонтально, а каждая карточка остаётся отдельным интерактивным элементом с собственным доступным названием.
- Значения визуальных токенов сверяются с Tokens Studio source of truth и из Figma в карточку не переносятся.

## Связанные компоненты

- [Rail - SquareSmall2Story](rail-square-small-2-story.md), [Rail - Square](rail-square.md).
- [Rail - Base](rail-base.md) и [семейство Rail](rail-family.md).

<!-- FIGMA_SYNC:START -->
## Актуальные данные Figma

> Последняя проверка: `2026-08-24T08:12:21Z` · структура `c54f17b170e6` · статус `ready` · публикация Figma `CHANGED`.

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
| `363.0×143.0` | 1 | Device=iPhone 15 |
| `410.0×158.0` | 1 | Device=iPhone 17 Pro Max |
| `1063.0×140.0` | 1 | Device=iPad Mini 6 |
| `1110.0×144.0` | 1 | Device=iPad 10 |
| `1306.0×172.0` | 1 | Device=iPad Pro 13 |

### Зависимости

- `Rail - Base` — node `29595:53876`; set `29595:53875`

### Источник

- [Rail - SquareSmall1Story](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=16941-129762) — fileKey `rMcDm5qGp4CXkXXddEbcMh`, API key `rMcDm5qGp4CXkXXddEbcMh`, node `16941:129762`, type `COMPONENT_SET`.
<!-- FIGMA_SYNC:END -->
