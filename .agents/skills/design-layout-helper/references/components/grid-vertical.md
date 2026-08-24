# Grid / Vertical

## Назначение

Адаптивная сетка вертикальных постеров. Объединяет заголовок и готовую раскладку
карточек портретного формата для iPhone и iPad.

## Когда использовать

- Для фильмов, сериалов и коллекций, где основной носитель — вертикальная
  обложка.
- Когда нужен полный grid-блок, а не горизонтальный [Rail - Vertical](rail-vertical.md).
- Выбирайте устройство и ориентацию вариантами мастера.

## Когда НЕ использовать

- Для стандартной горизонтальной формы используйте [Grid / Main](grid-main.md),
  для квадратной — [Grid / Square](grid-square.md).
- `Vertical Grid Item` — вложенная деталь этой сетки, не основной шаблон экрана.

## Платформенные особенности iOS

- iPhone поддерживает только `Landscape=False`; iPad — портрет и landscape.
- Точное значение `iPad  6/10` содержит два пробела.
- Каждая карточка остаётся отдельным интерактивным элементом с доступным
  названием; метки добавляйте в это описание без дублирования.
- Визуальные токены проверяются в Tokens Studio source of truth.

## Связанные компоненты

- [Label : Large](label-large.md) и [Label : Small](label-small.md) — вложенные
  метки карточек.
- [Семейство Grid](grid-family.md) — соседние шаблоны.
- `Vertical Grid Item` и `Навигационные / Переход в коллекцию` — зависимости
  без отдельной регистрации в этой партии.

<!-- FIGMA_SYNC:START -->
## Актуальные данные Figma

> Последняя проверка: `2026-08-24T14:23:13Z` · структура `32cba264d1b1` · статус `ready` · публикация Figma `CHANGED`.

### Свойства из компонента

| Свойство | Тип | Значение по умолчанию | Варианты |
|---|---|---|---|
| `Device` | `variant` | `iPhone` | iPad  6/10 / iPad Pro 13 / iPhone |
| `Heading` | `boolean` | `true` | — |
| `Landscape` | `variant` | `False` | False / True |
| `↳ Heading` | `text` | `Заголовок` | — |

### Варианты и размеры

| Ось | Значения |
|---|---|
| `Device` | iPad  6/10 / iPad Pro 13 / iPhone |
| `Landscape` | False / True |

Комбинаций в COMPONENT_SET: **5**.

| Размер | Количество вариантов | Примеры |
|---|---:|---|
| `363.0×852.0` | 1 | Device=iPhone, Landscape=False |
| `750.0×1150.0` | 1 | Device=iPad  6/10, Landscape=False |
| `962.0×1098.0` | 1 | Device=iPad Pro 13, Landscape=False |
| `1110.0×1265.0` | 1 | Device=iPad  6/10, Landscape=True |
| `1306.0×1201.0` | 1 | Device=iPad Pro 13, Landscape=True |

### Зависимости

- `Label : Large` — node `39976:32660`
- `Label : Small` — node `12185:97090`
- `Vertical Grid Item` — node `38575:90719`
- `Навигационные / Переход в коллекцию` — node `1305:27`

### Источник

- [Grid / Vertical](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=38575-90604) — fileKey `rMcDm5qGp4CXkXXddEbcMh`, API key `rMcDm5qGp4CXkXXddEbcMh`, node `38575:90604`, type `COMPONENT_SET`.
<!-- FIGMA_SYNC:END -->
