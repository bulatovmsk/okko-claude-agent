# Grid / Circle Zvuk

## Назначение

Адаптивная сетка круглых карточек для контента Звука. Мастер задаёт заголовок,
круглые обложки и раскладку для iPhone и двух классов iPad.

## Когда использовать

- Для музыкального и аудиоконтента Звука, где сущность представлена круглой
  обложкой.
- Когда нужна готовая grid-раскладка, согласованная между портретным и
  альбомным iPad.
- Управляйте заголовком через `Heading` и `↳ Heading`.

## Когда НЕ использовать

- Для персон используйте [Grid / Person](grid-person.md), а для обычных
  постеров — [Grid / Main](grid-main.md).
- `_Circle Grid Item` и `_Cover` не являются самостоятельными компонентами.

## Платформенные особенности iOS

- iPhone существует только в портретной раскладке. Для iPad доступны обе
  ориентации.
- В Figma значение `iPad  6/10` содержит два пробела; при актуализации это
  точное имя свойства нельзя нормализовать молча.
- В VoiceOver круглая карточка озвучивается как единый объект с названием;
  декоративная обложка скрывается от повторного чтения.
- Визуальные токены проверяются в Tokens Studio source of truth.

## Связанные компоненты

- [Семейство Grid](grid-family.md) — выбор формы сетки.
- `_Circle Grid Item` и `_Cover` — внутренние детали.
- `Навигационные / Переход в коллекцию` — действие заголовка.

<!-- FIGMA_SYNC:START -->
## Актуальные данные Figma

> Последняя проверка: `2026-08-24T14:23:13Z` · структура `cb5d311bd268` · статус `ready` · публикация Figma `CHANGED`.

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
| `363.0×730.0` | 1 | Device=iPhone, Landscape=False |
| `750.0×929.0` | 1 | Device=iPad  6/10, Landscape=False |
| `962.0×988.0` | 1 | Device=iPad Pro 13, Landscape=False |
| `1110.0×877.0` | 1 | Device=iPad  6/10, Landscape=True |
| `1306.0×1115.0` | 1 | Device=iPad Pro 13, Landscape=True |

### Зависимости

- `_Circle Grid Item` — node `38370:38122`
- `_Cover` — node `38370:38129`
- `Навигационные / Переход в коллекцию` — node `1305:27`

### Источник

- [Grid / Circle Zvuk](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=38370-38407) — fileKey `rMcDm5qGp4CXkXXddEbcMh`, API key `rMcDm5qGp4CXkXXddEbcMh`, node `38370:38407`, type `COMPONENT_SET`.
<!-- FIGMA_SYNC:END -->
