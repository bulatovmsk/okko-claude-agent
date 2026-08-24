# Rail - Large

## Назначение

Размерный Rail-шаблон с крупной горизонтальной карточкой `_Large / Card` и обложкой `_Large / Cover`.

## Когда использовать

- Когда контенту нужен больший визуальный приоритет, чем в Main или Medium.
- Для короткого ряда крупных горизонтальных постеров.

## Когда НЕ использовать

- Не выбирайте только ради увеличения изображения: сопоставьте иерархию с [Rail - Medium](rail-medium.md) и [Rail - Main](rail-main.md).
- Не подменяйте им маркетинговый креатив — для него есть [Rail - Marketing](rail-marketing.md).

## Платформенные особенности iOS

- Ось называется `device` со строчной буквы.
- Пять готовых размеров используют разную высоту; не масштабируйте один вариант пропорционально.
- Рейл прокручивается горизонтально, а каждая карточка остаётся отдельным интерактивным элементом с собственным доступным названием.
- Значения визуальных токенов сверяются с Tokens Studio source of truth и из Figma в карточку не переносятся.

## Связанные компоненты

- [Rail - Medium](rail-medium.md), [Rail - Main](rail-main.md), [Rail - Marketing](rail-marketing.md).
- [Rail - Base](rail-base.md) и [семейство Rail](rail-family.md).

<!-- FIGMA_SYNC:START -->
## Актуальные данные Figma

> Последняя проверка: `2026-08-24T08:12:20Z` · структура `b09df9f3b40c` · статус `ready` · публикация Figma `CHANGED`.

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
| `363.0×227.0` | 1 | device=iPhone 15 |
| `410.0×255.0` | 1 | device=iPhone 17 Pro Max |
| `1063.0×281.0` | 1 | device=iPad Mini 6 |
| `1110.0×290.0` | 1 | device=iPad 10 |
| `1306.0×274.0` | 1 | device=iPad Pro 13 |

### Зависимости

- `Rail - Base` — node `29595:53876`; set `29595:53875`

### Источник

- [Rail - Large](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=15462-375550) — fileKey `rMcDm5qGp4CXkXXddEbcMh`, API key `rMcDm5qGp4CXkXXddEbcMh`, node `15462:375550`, type `COMPONENT_SET`.
<!-- FIGMA_SYNC:END -->
