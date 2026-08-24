# Rail - Content

## Назначение

Экспериментальный контентный Rail-шаблон с обложкой, заголовком, метаданными и прогрессом просмотра. В Figma помечен `🟡` и «Нет в проде».

## Когда использовать

- Только для изучения или согласованного эксперимента Content.
- После подтверждения готовности и повторной проверки структуры Figma.

## Когда НЕ использовать

- Не используйте автоматически в новых продуктовых макетах.
- Для готовой карточки с прогрессом выберите [Rail - Continue](rail-continue.md) или [Rail - Personal Widget](rail-personal-widget.md).

## Платформенные особенности iOS

- Доступны четыре значения `Device`: iPhone 15, `iPad 6`, iPad 10 и iPad Pro 13; iPhone 17 Pro Max отсутствует.
- Имя `iPad 6` зафиксировано буквально и требует проверки при будущей актуализации.
- Рейл прокручивается горизонтально, а каждая карточка остаётся отдельным интерактивным элементом с собственным доступным названием.
- Значения визуальных токенов сверяются с Tokens Studio source of truth и из Figma в карточку не переносятся.

## Связанные компоненты

- [Rail - Continue](rail-continue.md), [Rail - Personal Widget](rail-personal-widget.md), [Rail - Main](rail-main.md).
- [Семейство Rail](rail-family.md).

<!-- FIGMA_SYNC:START -->
## Актуальные данные Figma

> Последняя проверка: `2026-08-24T08:12:21Z` · структура `63d1765d67fb` · статус `work-in-progress` · публикация Figma `CHANGED`.

### Свойства из компонента

| Свойство | Тип | Значение по умолчанию | Варианты |
|---|---|---|---|
| `Device` | `variant` | `iPhone 15` | iPad 10 / iPad 6 / iPad Pro 13 / iPhone 15 |

### Варианты и размеры

| Ось | Значения |
|---|---|
| `Device` | iPad 10 / iPad 6 / iPad Pro 13 / iPhone 15 |

Комбинаций в COMPONENT_SET: **4**.

| Размер | Количество вариантов | Примеры |
|---|---:|---|
| `363.0×199.0` | 1 | Device=iPhone 15 |
| `1063.0×206.0` | 1 | Device=iPad 6 |
| `1110.0×206.0` | 1 | Device=iPad 10 |
| `1306.0×221.0` | 1 | Device=iPad Pro 13 |

### Зависимости

В Figma-ответе внешние component dependencies не найдены.

### Источник

- [Rail - 🟡Content [Нет в проде]](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=25931-80240) — fileKey `rMcDm5qGp4CXkXXddEbcMh`, API key `rMcDm5qGp4CXkXXddEbcMh`, node `25931:80240`, type `COMPONENT_SET`.
<!-- FIGMA_SYNC:END -->
