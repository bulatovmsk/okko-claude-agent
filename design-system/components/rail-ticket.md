# Rail - Ticket

## Назначение

Шаблон рейла для билетов или специальных предложений с внутренними `_Ticket / Card`, `_Ticket / Cover` и `_headingRail`.

## Когда использовать

- Для сущностей, оформленных как билет или специальное предложение.
- На поддерживаемых актуальных раскладках iPhone 15 и iPad.

## Когда НЕ использовать

- Не выбирайте вариант `[Deprecated] iPhone 320` для нового макета, даже несмотря на то что он задан по умолчанию в Figma.
- Не ожидайте готового варианта iPhone 17 Pro Max — его в set нет.

## Платформенные особенности iOS

- COMPONENT_SET имеет статус `CURRENT`, но его default `Device` указывает на deprecated-вариант iPhone 320 — это конфликт структуры и статуса.
- Актуальные варианты: iPhone 15, iPad Mini 6, iPad 10 и iPad Pro 13.
- Рейл прокручивается горизонтально, а каждая карточка остаётся отдельным интерактивным элементом с собственным доступным названием.
- Значения визуальных токенов сверяются с Tokens Studio source of truth и из Figma в карточку не переносятся.

## Связанные компоненты

- [Rail - Marketing](rail-marketing.md) — для промо без билетной формы.
- [Семейство Rail](rail-family.md) — выбор готового шаблона.

<!-- FIGMA_SYNC:START -->
## Актуальные данные Figma

> Последняя проверка: `2026-08-24T08:12:21Z` · структура `871400c3b04e` · статус `ready` · публикация Figma `CURRENT`.

### Свойства из компонента

| Свойство | Тип | Значение по умолчанию | Варианты |
|---|---|---|---|
| `Device` | `variant` | `[Deprecated] iPhone 320` | [Deprecated] iPhone 320 / iPad 10 / iPad Mini 6 / iPad Pro 13 / iPhone 15 |

### Варианты и размеры

| Ось | Значения |
|---|---|
| `Device` | [Deprecated] iPhone 320 / iPad 10 / iPad Mini 6 / iPad Pro 13 / iPhone 15 |

Комбинаций в COMPONENT_SET: **5**.

| Размер | Количество вариантов | Примеры |
|---|---:|---|
| `290.0×221.0` | 1 | Device=[Deprecated] iPhone 320 |
| `363.0×219.0` | 1 | Device=iPhone 15 |
| `1063.0×362.0` | 1 | Device=iPad Mini 6 |
| `1110.0×368.0` | 1 | Device=iPad 10 |
| `1306.0×399.0` | 1 | Device=iPad Pro 13 |

### Зависимости

В Figma-ответе внешние component dependencies не найдены.

### Источник

- [Rail - Ticket](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=28139-194880) — fileKey `rMcDm5qGp4CXkXXddEbcMh`, API key `rMcDm5qGp4CXkXXddEbcMh`, node `28139:194880`, type `COMPONENT_SET`.
<!-- FIGMA_SYNC:END -->
