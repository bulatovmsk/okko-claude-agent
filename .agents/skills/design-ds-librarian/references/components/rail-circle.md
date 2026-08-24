# Rail - Circle

## Назначение

Шаблон рейла с круглыми обложками и подписями. Внутренние `_Circle / Card`, `_Circle / Cover` и `_Circle / Title` составляют карточку, но отдельно не публикуются.

## Когда использовать

- Для персон, тематик или сущностей, которые в ДС представлены круглой обложкой.
- Когда подпись под круглым изображением является частью карточки.

## Когда НЕ использовать

- Для горизонтальных постеров используйте [Rail - Main](rail-main.md), для персон с горизонтальной карточкой — [Rail - Person Horizontal](rail-person-horizontal.md).
- Не смешивайте круглые и квадратные карточки в одном шаблоне.

## Платформенные особенности iOS

- Пять значений `Device` покрывают актуальные iPhone/iPad-раскладки.
- Проверяйте длинные подписи и VoiceOver на уровне карточки, не озвучивая обложку отдельно.
- Рейл прокручивается горизонтально, а каждая карточка остаётся отдельным интерактивным элементом с собственным доступным названием.
- Значения визуальных токенов сверяются с Tokens Studio source of truth и из Figma в карточку не переносятся.

## Связанные компоненты

- [Rail - Person Horizontal](rail-person-horizontal.md) — альтернативное представление персон.
- [Rail - Base](rail-base.md) и [семейство Rail](rail-family.md).

<!-- FIGMA_SYNC:START -->
## Актуальные данные Figma

> Последняя проверка: `2026-08-24T08:12:20Z` · структура `e8f1793b54b1` · статус `ready` · публикация Figma `CURRENT`.

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
| `363.0×384.0` | 1 | Device=iPhone 15 |
| `410.0×418.0` | 1 | Device=iPhone 17 Pro Max |
| `1063.0×390.0` | 1 | Device=iPad Mini 6 |
| `1110.0×398.0` | 1 | Device=iPad 10 |
| `1306.0×454.0` | 1 | Device=iPad Pro 13 |

### Зависимости

- `Rail - Base` — node `29595:53876`; set `29595:53875`

### Источник

- [Rail - Circle](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=32668-60746) — fileKey `rMcDm5qGp4CXkXXddEbcMh`, API key `rMcDm5qGp4CXkXXddEbcMh`, node `32668:60746`, type `COMPONENT_SET`.
<!-- FIGMA_SYNC:END -->
