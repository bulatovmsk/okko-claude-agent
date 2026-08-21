# Chips

> Рабочая карточка компонента. Основной источник — `Chips` COMPONENT_SET в
> main-файле Lib-iOS, node `34254:8865`. `Component guide_Chips` на рабочей
> ветке, node `39348:13491`, сохранён как дополнительный источник.

## Назначение

Компактный элемент выбора одного или нескольких вариантов из списка тегов,
категорий или фильтров. В отличие от [Button](button.md), Chips живут группами
и поддерживают состояние «выбран». Входит в группу `Filters` вместе с `Select` —
продуктовое поведение группы см. [filters-group.md](filters-group.md).

## Когда использовать

- Фильтры контента — категории, жанры, годы, языки
- Выбор из небольшого списка (3–10 вариантов), где dropdown был бы избыточен

**Поведение:** при тапе мгновенно меняет состояние `Selected` (False ↔ True).

## Когда НЕ использовать

| Сценарий | Вместо |
|---|---|
| Основное действие на экране | `Button` (Primary/Secondary) |
| Длинный список (>10 опций) | `Select` или экран фильтров |
| Взаимоисключающий выбор между соседними разделами | [TabGroup](tabgroup.md) |

## Анатомия

1. Слот для иконки
2. Слот для текста
3. Отступ-компенсация при включённой иконке/картинке
4. Кнопка сброса состояния (Cross Box, появляется при `Selected=True`)
5. Слот для картинки

## Свойства (Properties)

| Свойство | Тип | Значения |
|---|---|---|
| `Device` | variant | iPhone / iPad |
| `Style` | variant | Icon / Img |
| `State` | variant | Rest / Touch / Disabled |
| `Selected` | variant | False / True |
| `String Text` | text | произвольный |
| `Icon` | boolean | true / false |
| `Icon Instance` | instance | swap |

Настройки доступны дизайнеру в правой панели (режим редактирования) и в Playground (DevMode).

## Стили

- `Style=Icon` — ведущая сменная иконка.
- `Style=Img` — ведущая картинка.

Отдельной оси размера в живом COMPONENT_SET нет. Размер определяется `Device`,
`Style`, `Selected` и длиной текста.

## Размеры

| Вариант на строке `Chips` | iPhone | iPad |
|---|---:|---:|
| `Icon`, `Selected=False` | 88×36 pt | 104×40 pt |
| `Img`, `Selected=False` | 96×36 pt | 110×40 pt |
| `Icon`, `Selected=True` | 104×36 pt | 125×40 pt |
| `Img`, `Selected=True` | 112×36 pt | 131×40 pt |

Значения corner radius, внутренних отступов и размеров иконок не фиксируются
здесь как токены: актуальные значения нужно проверять в Tokens Studio.

## Состояния

`Rest`, `Touch`, `Disabled`. (Loading/Progress нет — это специфика Button.)

## Состояние выбора (Selected)

При нажатии компонент переключает выбранное/невыбранное состояние.
`Selected=True` визуально инвертируется и добавляет
`Actions / Cross_Small_Bold`; ширина варианта iPhone Icon меняется с 88 до
104 pt.

## Область нажатия

Компонент реагирует на нажатие по всей площади.

Визуальная высота 36/40 pt меньше минимальной touch target iOS, поэтому при
реализации обеспечьте интерактивную область не меньше 44×44 pt без изменения
визуального размера. VoiceOver должен объявлять текст и состояние выбора.

## Текст

Одна строка с обрезкой в конце. Точные типографические токены проверяются в
Tokens Studio, а не копируются из Figma-гайда.

## Компонентные токены

Chips входит в группу **Control** и использует компонентные токены для синхронизации размеров. Переключение токенов по девайсам — через **моды**.

## Связанные компоненты

- `Select` — та же группа `Filters`, для длинных списков (>10) и multi-select со счётчиком
- [Button](button.md) — для действий, а не выбора
- [TabGroup](tabgroup.md) — взаимоисключающий выбор между соседними разделами
- `Actions / Calendar_Bold` — ведущая иконка в живом примере.
- `Actions / Cross_Small_Bold` — снятие выбранного состояния.

## Источник

- Основной компонент: main-файл Figma `rMcDm5qGp4CXkXXddEbcMh`, node
  `34254:8865` (`Chips` COMPONENT_SET).
- Связанный гайд: рабочая ветка `jdBqhypltqMzx0mXE7uw94`, node
  `39348:13491` (`Component guide_Chips`).

<!-- FIGMA_SYNC:START -->
## Актуальные данные Figma

> Последняя проверка: `2026-08-21T16:07:30Z` · структура `47a5d8a421db` · статус `unknown`.

### Свойства из компонента

| Свойство | Тип | Значение по умолчанию | Варианты |
|---|---|---|---|
| `Device` | `variant` | `—` | iPad / iPhone |
| `Icon` | `boolean` | `—` | — |
| `Icon Instance` | `instance_swap` | `—` | — |
| `Selected` | `variant` | `—` | False / True |
| `State` | `variant` | `—` | Disabled / Rest / Touch |
| `String Text` | `text` | `—` | — |
| `Style` | `variant` | `—` | Icon / Img |

### Варианты и размеры

| Ось | Значения |
|---|---|
| `Device` | iPad / iPhone |
| `Selected` | False / True |
| `State` | Disabled / Rest / Touch |
| `Style` | Icon / Img |

Комбинаций в COMPONENT_SET: **24**.

| Размер | Количество вариантов | Примеры |
|---|---:|---|
| `88.0×36.0` | 3 | Device=iPhone, Style=Icon, State=Rest, Selected=False; Device=iPhone, Style=Icon, State=Touch, Selected=False; Device=iPhone, Style=Icon, State=Disabled, Selected=False |
| `96.0×36.0` | 3 | Device=iPhone, Style=Img, State=Rest, Selected=False; Device=iPhone, Style=Img, State=Touch, Selected=False; Device=iPhone, Style=Img, State=Disabled, Selected=False |
| `104.0×36.0` | 3 | Device=iPhone, Style=Icon, State=Rest, Selected=True; Device=iPhone, Style=Icon, State=Touch, Selected=True; Device=iPhone, Style=Icon, State=Disabled, Selected=True |
| `104.0×40.0` | 3 | Device=iPad, Style=Icon, State=Rest, Selected=False; Device=iPad, Style=Icon, State=Touch, Selected=False; Device=iPad, Style=Icon, State=Disabled, Selected=False |
| `110.0×40.0` | 3 | Device=iPad, Style=Img, State=Rest, Selected=False; Device=iPad, Style=Img, State=Touch, Selected=False; Device=iPad, Style=Img, State=Disabled, Selected=False |
| `112.0×36.0` | 3 | Device=iPhone, Style=Img, State=Rest, Selected=True; Device=iPhone, Style=Img, State=Touch, Selected=True; Device=iPhone, Style=Img, State=Disabled, Selected=True |
| `125.0×40.0` | 3 | Device=iPad, Style=Icon, State=Rest, Selected=True; Device=iPad, Style=Icon, State=Touch, Selected=True; Device=iPad, Style=Icon, State=Disabled, Selected=True |
| `131.0×40.0` | 3 | Device=iPad, Style=Img, State=Rest, Selected=True; Device=iPad, Style=Img, State=Touch, Selected=True; Device=iPad, Style=Img, State=Disabled, Selected=True |

### Состояния

- `Selected`: False / True
- `State`: Disabled / Rest / Touch

### Зависимости

- `_compensation` — node `dependency:compensation`
- `Actions / Calendar_Bold` — node `dependency:actions-calendar-bold`
- `Actions / Cross_Small_Bold` — node `dependency:actions-cross-small-bold`

### Источник

- [Chips](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=34254-8865&t=6NQra4uE9oLKkthr-4) — fileKey `rMcDm5qGp4CXkXXddEbcMh`, API key `rMcDm5qGp4CXkXXddEbcMh`, node `34254:8865`, type `COMPONENT_SET`.
- [guide](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/branch/jdBqhypltqMzx0mXE7uw94/Lib-iOS?node-id=39348-13491) — `guide`, node `39348:13491`.
<!-- FIGMA_SYNC:END -->
