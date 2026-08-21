# Text input

## Назначение

Однострочное поле ввода (`Input`) для текста и других значений в формах iOS.
Поддерживает редактируемый текст, опциональный сменный значок справа и
дополнительную подпись под полем. В Figma компонент называется `Text input`.

## Когда использовать

- Для ввода одного короткого значения: имени, адреса, кода или другого
  форменного значения, которое помещается в одну строку.
- `State=default` — исходное состояние; `typing` — активный ввод; `complete` —
  введённое завершённое значение; `disabled` — недоступное поле; `error` —
  значение с ошибкой.
- `Text content` задаёт отображаемую строку.
- Включайте `Undertitle` и задавайте `Undertitle text`, когда под полем нужна
  поясняющая или диагностическая подпись.
- `Icon` управляет видимостью правого действия, а `↳ Icon instance` позволяет
  заменить его. В исходном варианте используется
  `Actions / Eye_Crossed_Bold`.

## Когда НЕ использовать

- Для многострочного текста: компонент имеет фиксированную высоту 48 pt и
  документирован только как однострочное поле.
- Для поиска по списку используйте специализированный Search Input/Searchbar,
  если он предусмотрен сценарием.
- Не используйте `disabled` вместо пояснения, почему действие недоступно.
- Не передавайте ошибку только цветом: добавляйте понятный текст через
  `Undertitle text`.

## Платформенные особенности iOS

- Высота всех вариантов — 48 pt. Эталонная ширина — 345 pt для iPhone и
  560 pt для iPad; при встраивании сохраняйте платформенный вариант `Device`.
- В наборе есть полная матрица из пяти состояний для обоих устройств — всего
  10 вариантов.
- Активное состояние `typing` визуально выделяет нижнюю границу, `error` —
  ошибку, `disabled` — недоступность; не подменяйте этими состояниями друг друга.
- Поле и правое действие должны иметь отдельные понятные VoiceOver labels.
  Для `error` озвучивайте текст ошибки вместе с полем; после валидации не
  переводите фокус неожиданно.
- Тип клавиатуры, автозаполнение, маска, `secureTextEntry` и правила валидации
  не заданы компонентом в Figma — их выбирает продуктовый сценарий.
- На момент проверки у набора Figma `publishStatus=CHANGED`: в файле есть
  изменения относительно опубликованной версии библиотеки.

## Связанные компоненты

- [Symbol input](symbol-input.md) — пятисимвольный код, разбитый на отдельные
  визуальные позиции.
- `Actions / Eye_Crossed_Bold` — правый значок по умолчанию; подходит для
  сценария показа или скрытия защищённого значения.
- `Type=Typing In Progress` — отдельные встроенные зависимости для iPhone и
  iPad, используемые в состоянии `typing`.
- `Search Input`/`Searchbar` — специализированная альтернатива для поиска.

<!-- FIGMA_SYNC:START -->
## Актуальные данные Figma

> Последняя проверка: `2026-08-21T15:55:31Z` · структура `07c670f2d589` · статус `unknown`.

### Свойства из компонента

| Свойство | Тип | Значение по умолчанию | Варианты |
|---|---|---|---|
| `Device` | `variant` | `iPhone` | iPad / iPhone |
| `Icon` | `boolean` | `true` | — |
| `State` | `variant` | `default` | complete / default / disabled / error / typing |
| `Text content` | `text` | `Text string` | — |
| `Undertitle` | `boolean` | `false` | — |
| `Undertitle text` | `text` | `Undertitle text` | — |
| `↳ Icon instance` | `instance_swap` | `39522:40505` | — |

### Варианты и размеры

| Ось | Значения |
|---|---|
| `Device` | iPad / iPhone |
| `State` | complete / default / disabled / error / typing |

Комбинаций в COMPONENT_SET: **10**.

| Размер | Количество вариантов | Примеры |
|---|---:|---|
| `345.0×48.0` | 5 | Device=iPhone, State=typing; Device=iPhone, State=error; Device=iPhone, State=complete |
| `560.0×48.0` | 5 | Device=iPad, State=default; Device=iPad, State=typing; Device=iPad, State=error |

### Состояния

- `State`: complete / default / disabled / error / typing

### Зависимости

- `Actions / Eye_Crossed_Bold` — node `39522:40505`
- `Type=Typing In Progress` — node `18716:508`
- `Type=Typing In Progress` — node `18716:515`

### Источник

- [Text input](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=12510-97334&t=6NQra4uE9oLKkthr-4) — fileKey `rMcDm5qGp4CXkXXddEbcMh`, API key `rMcDm5qGp4CXkXXddEbcMh`, node `12510:97334`, type `COMPONENT_SET`.
<!-- FIGMA_SYNC:END -->
