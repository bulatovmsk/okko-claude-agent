# Rail - Person Horizontal

## Назначение

Шаблон горизонтальных карточек персон с внутренними `_Person / Card` и `_Person / Cover`.

## Когда использовать

- Для актёров, авторов, ведущих или других персон, когда нужна горизонтальная карточка.
- Когда имя и изображение персоны должны читаться как единый элемент ряда.

## Когда НЕ использовать

- Для круглого портрета используйте [Rail - Circle](rail-circle.md).
- Не предполагайте поддержку всех стандартных Device-вариантов.

## Платформенные особенности iOS

- В Figma есть только `iPhone`, `iPad 10` и `iPad Pro 13`; вариантов iPhone 17 Pro Max и iPad Mini 6 нет.
- Ось называется `device`, а значение телефона — обобщённое `iPhone`.
- Рейл прокручивается горизонтально, а каждая карточка остаётся отдельным интерактивным элементом с собственным доступным названием.
- Значения визуальных токенов сверяются с Tokens Studio source of truth и из Figma в карточку не переносятся.

## Связанные компоненты

- [Rail - Circle](rail-circle.md) — альтернативная форма карточки персоны.
- [Rail - Base](rail-base.md) и [семейство Rail](rail-family.md).

<!-- FIGMA_SYNC:START -->
## Актуальные данные Figma

> Последняя проверка: `2026-08-24T08:12:21Z` · структура `bb3c67d1d5a6` · статус `ready` · публикация Figma `CHANGED`.

### Свойства из компонента

| Свойство | Тип | Значение по умолчанию | Варианты |
|---|---|---|---|
| `device` | `variant` | `iPad Pro 13` | iPad 10 / iPad Pro 13 / iPhone |

### Варианты и размеры

| Ось | Значения |
|---|---|
| `device` | iPad 10 / iPad Pro 13 / iPhone |

Комбинаций в COMPONENT_SET: **3**.

| Размер | Количество вариантов | Примеры |
|---|---:|---|
| `363.0×154.0` | 1 | device=iPhone |
| `1110.0×174.0` | 1 | device=iPad 10 |
| `1306.0×206.0` | 1 | device=iPad Pro 13 |

### Зависимости

- `Rail - Base` — node `29595:53876`; set `29595:53875`

### Источник

- [Rail - Person Horizontal](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=23197-42884) — fileKey `rMcDm5qGp4CXkXXddEbcMh`, API key `rMcDm5qGp4CXkXXddEbcMh`, node `23197:42884`, type `COMPONENT_SET`.
<!-- FIGMA_SYNC:END -->
