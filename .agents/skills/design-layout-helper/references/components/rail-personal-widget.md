# Rail - Personal Widget

## Назначение

Персонализированный Rail-шаблон с крупной обложкой, прогрессом и метаданными. Внутренние `_Widget / Cover` и `_Widget / progress&meta` не используются отдельно.

## Когда использовать

- Для персонального блока, где одной обложки недостаточно и нужны прогресс с метаданными.
- Когда пользовательский контекст является главным смыслом ряда.

## Когда НЕ использовать

- Для компактного продолжения просмотра используйте [Rail - Continue](rail-continue.md).
- Для обычной подборки без персональных данных используйте [Rail - Main](rail-main.md).

## Платформенные особенности iOS

- Пять `Device`-вариантов покрывают актуальные iPhone/iPad.
- VoiceOver-описание карточки должно объединять название, метаданные и прогресс в логичном порядке.
- Рейл прокручивается горизонтально, а каждая карточка остаётся отдельным интерактивным элементом с собственным доступным названием.
- Значения визуальных токенов сверяются с Tokens Studio source of truth и из Figma в карточку не переносятся.

## Связанные компоненты

- [Rail - Continue](rail-continue.md), [Rail - Main](rail-main.md).
- [Rail - Base](rail-base.md) и [семейство Rail](rail-family.md).

<!-- FIGMA_SYNC:START -->
## Актуальные данные Figma

> Последняя проверка: `2026-08-24T08:12:21Z` · структура `f9b88dc7ae3e` · статус `ready` · публикация Figma `CHANGED`.

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
| `363.0×430.0` | 1 | Device=iPhone 15 |
| `410.0×493.0` | 1 | Device=iPhone 17 Pro Max |
| `1063.0×376.0` | 1 | Device=iPad Mini 6 |
| `1110.0×388.0` | 1 | Device=iPad 10 |
| `1306.0×362.0` | 1 | Device=iPad Pro 13 |

### Зависимости

- `Rail - Base` — node `29595:53876`; set `29595:53875`

### Источник

- [Rail - Personal Widget](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=31185-161182) — fileKey `rMcDm5qGp4CXkXXddEbcMh`, API key `rMcDm5qGp4CXkXXddEbcMh`, node `31185:161182`, type `COMPONENT_SET`.
<!-- FIGMA_SYNC:END -->
