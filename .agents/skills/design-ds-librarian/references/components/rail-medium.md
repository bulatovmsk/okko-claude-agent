# Rail - Medium

## Назначение

Размерный Rail-шаблон со средней горизонтальной карточкой, внутренними `_Medium / Card`, `_Medium / Cover` и `_Medium / coverTitle`.

## Когда использовать

- Для промежуточного визуального приоритета между Main и Large.
- Когда заголовок на обложке предусмотрен структурой Medium-карточки.

## Когда НЕ использовать

- Не заменяйте им Main без причины в контентной иерархии.
- Не собирайте `coverTitle` как отдельный опубликованный компонент.

## Платформенные особенности iOS

- Свойство `Device` содержит пять модельных раскладок.
- Варианты отличаются не только шириной, но и высотой; сохраняйте мастерную геометрию.
- Рейл прокручивается горизонтально, а каждая карточка остаётся отдельным интерактивным элементом с собственным доступным названием.
- Значения визуальных токенов сверяются с Tokens Studio source of truth и из Figma в карточку не переносятся.

## Связанные компоненты

- [Rail - Main](rail-main.md), [Rail - Large](rail-large.md).
- [Rail - Base](rail-base.md) и [семейство Rail](rail-family.md).

<!-- FIGMA_SYNC:START -->
## Актуальные данные Figma

> Последняя проверка: `2026-08-24T08:12:20Z` · структура `6e71c6278991` · статус `ready` · публикация Figma `CHANGED`.

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
| `363.0×234.0` | 1 | Device=iPhone 15 |
| `410.0×258.0` | 1 | Device=iPhone 17 Pro Max |
| `1063.0×268.0` | 1 | Device=iPad Mini 6 |
| `1110.0×274.0` | 1 | Device=iPad 10 |
| `1306.0×261.0` | 1 | Device=iPad Pro 13 |

### Зависимости

- `Rail - Base` — node `29595:53876`; set `29595:53875`

### Источник

- [Rail - Medium](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=24049-48738) — fileKey `rMcDm5qGp4CXkXXddEbcMh`, API key `rMcDm5qGp4CXkXXddEbcMh`, node `24049:48738`, type `COMPONENT_SET`.
<!-- FIGMA_SYNC:END -->
