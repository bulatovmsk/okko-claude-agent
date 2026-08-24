# Grid / Square

## Назначение

Адаптивная сетка квадратных карточек с компактным и раскрытым представлением.
Ось `Expanded` переключает сокращённую сетку с кнопкой раскрытия и полную
сетку без отдельной кнопки.

## Когда использовать

- Для контента с квадратной обложкой, когда количество карточек может быть
  показано частично или целиком.
- `Expanded=False` используйте как компактное представление с действием
  раскрытия; `Expanded=True` — как полный список.
- Выбирайте `Device` и `Landscape` из существующих комбинаций мастера.

## Когда НЕ использовать

- Для вертикальных постеров используйте [Grid / Vertical](grid-vertical.md),
  для стандартного каталога — [Grid / Main](grid-main.md).
- Не используйте `_Square Grid Item` как самостоятельную сетку.

## Платформенные особенности iOS

- Десять вариантов: iPhone только portrait и по две ориентации двух классов
  iPad, каждая в состояниях `Expanded=False/True`.
- Точное значение `iPad  6/10` содержит два пробела.
- Кнопка раскрытия присутствует только в `Expanded=False`; её доступное имя
  должно объяснять результат действия, например раскрытие всей подборки.
- После раскрытия сохраняйте предсказуемую позицию VoiceOver и порядок карточек.
- Визуальные токены проверяются в Tokens Studio source of truth.

## Связанные компоненты

- [Button](button.md) — действие раскрытия компактной сетки.
- [Семейство Grid](grid-family.md) — выбор другого типа сетки.
- `_Square Grid Item` — внутренняя карточка, отдельно не регистрируется.
- `Навигационные / Переход в коллекцию` — действие заголовка.

<!-- FIGMA_SYNC:START -->
## Актуальные данные Figma

> Последняя проверка: `2026-08-24T14:23:14Z` · структура `dcfce4e4d50f` · статус `ready` · публикация Figma `CHANGED`.

### Свойства из компонента

| Свойство | Тип | Значение по умолчанию | Варианты |
|---|---|---|---|
| `Device` | `variant` | `iPhone` | iPad  6/10 / iPad Pro 13 / iPhone |
| `Expanded` | `variant` | `False` | False / True |
| `Heading` | `boolean` | `true` | — |
| `Landscape` | `variant` | `False` | False / True |
| `↳ Heading` | `text` | `Заголовок` | — |

### Варианты и размеры

| Ось | Значения |
|---|---|
| `Device` | iPad  6/10 / iPad Pro 13 / iPhone |
| `Expanded` | False / True |
| `Landscape` | False / True |

Комбинаций в COMPONENT_SET: **10**.

| Размер | Количество вариантов | Примеры |
|---|---:|---|
| `363.0×459.0` | 1 | Device=iPhone, Landscape=False, Expanded=False |
| `363.0×768.0` | 1 | Device=iPhone, Landscape=False, Expanded=True |
| `750.0×598.67` | 1 | Device=iPad  6/10, Landscape=False, Expanded=False |
| `750.0×1041.0` | 1 | Device=iPad  6/10, Landscape=False, Expanded=True |
| `962.0×578.0` | 1 | Device=iPad Pro 13, Landscape=False, Expanded=False |
| `962.0×1000.0` | 1 | Device=iPad Pro 13, Landscape=False, Expanded=True |
| `1110.0×652.0` | 1 | Device=iPad  6/10, Landscape=True, Expanded=False |
| `1110.0×1038.0` | 1 | Device=iPad  6/10, Landscape=True, Expanded=True |
| `1306.0×618.4` | 1 | Device=iPad Pro 13, Landscape=True, Expanded=False |
| `1306.0×1081.0` | 1 | Device=iPad Pro 13, Landscape=True, Expanded=True |

### Зависимости

- `_Square Grid Item` — node `38317:16351`
- `Button` — node `40158:69092`
- `Навигационные / Переход в коллекцию` — node `1305:27`

### Источник

- [Grid / Square](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=21878-59446) — fileKey `rMcDm5qGp4CXkXXddEbcMh`, API key `rMcDm5qGp4CXkXXddEbcMh`, node `21878:59446`, type `COMPONENT_SET`.
<!-- FIGMA_SYNC:END -->
