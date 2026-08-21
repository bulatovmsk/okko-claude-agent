# Select

> Рабочая карточка компонента. Основной источник — `Select` COMPONENT_SET в
> main-файле Lib-iOS, node `34884:24858`. `Component guide_Select` на рабочей
> ветке, node `39484:30540`, сохранён как дополнительный источник.

## Назначение

Компактный фильтр, который по тапу открывает список опций в шторке, поддерживает
одиночный или множественный выбор и может показывать счётчик выбранного. В
отличие от [Chips](chips.md), прячет варианты за одним контролом — для длинных
списков. Продуктовое поведение группы см. в [Filters](filters-group.md).

## Когда использовать

- Длинный список опций — когда показывать все Chips на экране неудобно
- Множественный выбор с подсчётом — «Жанры · 3», «Страны · 5»
- Единичный выбор
- Экономия места — один контрол вместо россыпи тегов

**Поведение:** тап по основной зоне открывает шторку. `Selected` отражает уже
применённый выбор и не должен переключаться только из-за открытия шторки.

## Когда НЕ использовать

| Сценарий | Вместо |
|---|---|
| Короткий список, варианты помещаются на экран | `Chips` |

## Анатомия

1. Слот для иконки
2. Слот для текста
3. Отступ-компенсация при включённой иконке/картинке
4. Кнопка сброса состояния (× / Cross Box, при `Selected=True`)
5. Каунтер количества выбранных элементов (Counter)

## Свойства (Properties)

| Свойство | Тип | Значения |
|---|---|---|
| `Device` | variant | iPhone / iPad |
| `State` | variant | Rest / Touch / Disabled |
| `Selected` | variant | False / True |
| `Icon` | boolean | true / false |
| `Icon Instance` | instance | swap |
| `Counter` | boolean | true / false |
| `String Text` | text | произвольный |
| `String Counter` | text | число выбранного |

Настройки доступны дизайнеру в правой панели (режим редактирования) и в Playground (DevMode). Компонентные токены по девайсу и переключение темы (в т.ч. для iOS-материала) — только для дизайнеров ДС.

## Размеры

| Параметр | iPhone | iPad |
|---|---|---|
| `Selected=False` | 108×36 pt | 129×40 pt |
| `Selected=True` | 134×36 pt | 159×40 pt |

Размеры выше подтверждены на живой строке `Select`; ширина меняется вместе с
текстом и видимостью счётчика. Значения corner radius и внутренних отступов не
фиксируются здесь как токены — проверяйте их в Tokens Studio.

## Состояния

`Rest`, `Touch`, `Disabled`. (Loading/Progress нет — это специфика Button.)

## Состояние выбора (Selected)

`Selected=True` показывает применённый фильтр: инвертированный стиль,
опциональный `Counter` со значением `String Counter` и
`Actions / Cross_Small_Bold` для сброса. При одном выбранном значении контрол
может показывать его имя; при нескольких — количество согласно гайду Filters.

## Область нажатия

- `Selected=False` — реагирует по всей площади (открывает BottomSheet).
- `Selected=True` — **две** зоны нажатия: левая часть → вызов BottomSheet, правая (с крестиком) → сброс выбора.

Визуальная высота 36/40 pt меньше минимальной touch target iOS, поэтому обеим
зонам нужна доступная область не меньше 44×44 pt без визуального увеличения.
VoiceOver должен различать открытие списка и сброс, объявлять название фильтра,
выбранность и счётчик.

## Компонентные токены

Select входит в группу **Control** и использует компонентные токены для синхронизации размеров. Переключение токенов по девайсам — через **моды**.

## Связанные компоненты

- [Chips](chips.md) — та же группа `Filters`, для коротких списков
- `BottomSheet` — раскрывающийся список опций Select
- [Button](button.md) — для действий, а не выбора
- `Actions / Calendar_Bold` — ведущая иконка в живом примере.
- `Actions / Cross_Small_Bold` — сброс применённого выбора.

## Источник

- Основной компонент: main-файл Figma `rMcDm5qGp4CXkXXddEbcMh`, node
  `34884:24858` (`Select` COMPONENT_SET).
- Связанный гайд: рабочая ветка `jdBqhypltqMzx0mXE7uw94`, node
  `39484:30540` (`Component guide_Select`).

<!-- FIGMA_SYNC:START -->
## Актуальные данные Figma

> Последняя проверка: `2026-08-21T16:09:38Z` · структура `7c94a6985755` · статус `unknown`.

### Свойства из компонента

| Свойство | Тип | Значение по умолчанию | Варианты |
|---|---|---|---|
| `Counter` | `boolean` | `—` | — |
| `Device` | `variant` | `—` | iPad / iPhone |
| `Icon` | `boolean` | `—` | — |
| `Icon Instance` | `instance_swap` | `—` | — |
| `Selected` | `variant` | `—` | False / True |
| `State` | `variant` | `—` | Disabled / Rest / Touch |
| `String Counter` | `text` | `—` | — |
| `String Text` | `text` | `—` | — |

### Варианты и размеры

| Ось | Значения |
|---|---|
| `Device` | iPad / iPhone |
| `Selected` | False / True |
| `State` | Disabled / Rest / Touch |

Комбинаций в COMPONENT_SET: **12**.

| Размер | Количество вариантов | Примеры |
|---|---:|---|
| `108.0×36.0` | 3 | Device=iPhone, State=Rest, Selected=False; Device=iPhone, State=Touch, Selected=False; Device=iPhone, State=Disabled, Selected=False |
| `129.0×40.0` | 3 | Device=iPad, State=Rest, Selected=False; Device=iPad, State=Touch, Selected=False; Device=iPad, State=Disabled, Selected=False |
| `134.0×36.0` | 3 | Device=iPhone, State=Rest, Selected=True; Device=iPhone, State=Touch, Selected=True; Device=iPhone, State=Disabled, Selected=True |
| `159.0×40.0` | 3 | Device=iPad, State=Rest, Selected=True; Device=iPad, State=Touch, Selected=True; Device=iPad, State=Disabled, Selected=True |

### Состояния

- `Selected`: False / True
- `State`: Disabled / Rest / Touch

### Зависимости

- `Actions / Calendar_Bold` — node `dependency:actions-calendar-bold`
- `Actions / Cross_Small_Bold` — node `dependency:actions-cross-small-bold`

### Источник

- [Select](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=34884-24858&t=6NQra4uE9oLKkthr-4) — fileKey `rMcDm5qGp4CXkXXddEbcMh`, API key `rMcDm5qGp4CXkXXddEbcMh`, node `34884:24858`, type `COMPONENT_SET`.
- [guide](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/branch/jdBqhypltqMzx0mXE7uw94/Lib-iOS?node-id=39484-30540) — `guide`, node `39484:30540`.
<!-- FIGMA_SYNC:END -->
