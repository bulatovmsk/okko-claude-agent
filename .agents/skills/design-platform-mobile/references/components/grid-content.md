# Grid / Content

## Назначение

Адаптивная сетка контентных карточек с расширенной информацией и действиями:
заголовком карточки, прогрессом просмотра, меткой и возможностью загрузки.

## Когда использовать

- Для каталога, где кроме обложки нужно показывать прогресс, название, метку
  или download-действие.
- Когда информационная насыщенность [Grid / Main](grid-main.md) недостаточна.
- Заголовок секции управляется `Heading` и `↳ Heading`.

## Когда НЕ использовать

- Для простой карточки без прогресса и действий используйте [Grid / Main](grid-main.md).
- Не собирайте шаблон вручную из `_Grid Main / Card`, `_Watch Progress` и
  `_itemContent / Title box`.

## Платформенные особенности iOS

- iPhone представлен портретной раскладкой; iPad — обеими ориентациями.
- Точное значение `iPad  6/10` содержит два пробела.
- Основная карточка и download-действие должны иметь понятные отдельные роли;
  прогресс включайте в доступное описание карточки без повторного чтения.
- Визуальные токены проверяются в Tokens Studio source of truth.

## Связанные компоненты

- [Label : Small](label-small.md) — вложенная метка.
- `🟡Button - Download 3.0` — зависимость со статусом work-in-progress в имени;
  не подменяйте её обычным [Button](button.md) без проверки сценария.
- [Семейство Grid](grid-family.md) — соседние шаблоны.
- `_Grid Main / Card`, `_Watch Progress` и `_itemContent / Title box` —
  внутренние детали.

<!-- FIGMA_SYNC:START -->
## Актуальные данные Figma

> Последняя проверка: `2026-08-24T14:23:14Z` · структура `2e8c3f2773b5` · статус `ready` · публикация Figma `CHANGED`.

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
| `363.0×708.0` | 1 | Device=iPhone, Landscape=False |
| `750.0×768.0` | 1 | Device=iPad  6/10, Landscape=False |
| `962.0×756.0` | 1 | Device=iPad Pro 13, Landscape=False |
| `1110.0×756.0` | 1 | Device=iPad  6/10, Landscape=True |
| `1306.0×786.0` | 1 | Device=iPad Pro 13, Landscape=True |

### Зависимости

- `_Grid Main / Card` — node `38566:83016`
- `_itemContent / Title box` — node `25931:69628`
- `_Watch Progress` — node `38566:83063`
- `Arrows / Arrow_Down_Tail_Bold` — node `39522:41583`
- `Label : Small` — node `12185:97090`
- `Навигационные / Переход в коллекцию` — node `1305:27`
- `🟡Button - Download 3.0` — node `37497:16040`

### Источник

- [Grid / Content](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=38566-83080) — fileKey `rMcDm5qGp4CXkXXddEbcMh`, API key `rMcDm5qGp4CXkXXddEbcMh`, node `38566:83080`, type `COMPONENT_SET`.
<!-- FIGMA_SYNC:END -->
