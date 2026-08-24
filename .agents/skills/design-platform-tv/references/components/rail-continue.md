# Rail - Continue

## Назначение

Шаблон «Продолжить просмотр» с карточками контента и индикатором прогресса. Внутренние `_Main / Card`, `_Main / Cover` и `_Main / progressOverlay` работают как единая карточка.

## Когда использовать

- Для персонального ряда незавершённого просмотра.
- Когда положение просмотра должно читаться прямо на карточке.

## Когда НЕ использовать

- Для контента без прогресса используйте [Rail - Main](rail-main.md).
- Не добавляйте прогресс вручную поверх другого Rail-шаблона.

## Платформенные особенности iOS

- Пять вариантов `Device` покрывают iPhone 15, iPhone 17 Pro Max и три iPad.
- Для VoiceOver прогресс должен входить в описание карточки вместе с названием контента.
- Рейл прокручивается горизонтально, а каждая карточка остаётся отдельным интерактивным элементом с собственным доступным названием.
- Значения визуальных токенов сверяются с Tokens Studio source of truth и из Figma в карточку не переносятся.

## Связанные компоненты

- [Rail - Main](rail-main.md) — рейл без прогресса.
- [Rail - Personal Widget](rail-personal-widget.md) — более насыщенное персональное представление.
- [Rail - Base](rail-base.md).

<!-- FIGMA_SYNC:START -->
## Актуальные данные Figma

> Последняя проверка: `2026-08-24T08:12:20Z` · структура `71731d2330e8` · статус `ready` · публикация Figma `CURRENT`.

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
| `363.0×206.0` | 1 | Device=iPhone 15 |
| `410.0×224.0` | 1 | Device=iPhone 17 Pro Max |
| `1063.0×209.0` | 1 | Device=iPad Mini 6 |
| `1110.0×216.0` | 1 | Device=iPad 10 |
| `1306.0×229.0` | 1 | Device=iPad Pro 13 |

### Зависимости

- `Rail - Base` — node `29595:53876`; set `29595:53875`

### Источник

- [Rail - Continue](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=15462-313281) — fileKey `rMcDm5qGp4CXkXXddEbcMh`, API key `rMcDm5qGp4CXkXXddEbcMh`, node `15462:313281`, type `COMPONENT_SET`.
<!-- FIGMA_SYNC:END -->
