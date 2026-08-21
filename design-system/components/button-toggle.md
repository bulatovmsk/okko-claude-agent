# Button - Toggle

## Назначение

Кнопка с сохраняемым выбранным и невыбранным состоянием. Подходит для действия,
которое пользователь может включить и повторным нажатием отменить, например
добавить объект в избранное.

## Когда использовать

- Для независимого действия с двумя устойчивыми состояниями: `Selected=False`
  и `Selected=True`.
- Когда состояние нужно показать той же кнопкой, которой пользователь его меняет.
- Для варианта с текстом, только с иконкой либо с подписью рядом или снизу.

### Формы и стили

- `Rectangle` — стандартная кнопка-контейнер.
- `Circle →` — круглая кнопка с подписью справа.
- `Circle ↓` — круглая кнопка с подписью снизу.
- `Primary` — действие с заметным контейнером.
- `Ghost` — действие с минимальным визуальным акцентом; опубликовано только для
  части круглых вариантов.

## Когда НЕ использовать

- Для одноразового действия без сохраняемого выбора — использовать [Button](button.md).
- Для системной настройки с немедленным эффектом — использовать
  [Switch](switch.md).
- Для выбора одного значения из группы — использовать Select, Chips или другой
  компонент выбора.
- Не собирать отсутствующее сочетание свойств вручную: матрица из 208 вариантов
  неполная, в частности `Ghost` и `Loading` доступны не во всех формах.

## Платформенные особенности iOS

### Размеры

| Size | iPhone | iPad |
|---|---:|---:|
| `Small` | 36 | 40 |
| `Default` | 48 | 52 |

Размер в таблице — высота Rectangle или диаметр основной круглой кнопки. Формы
с подписью снизу имеют большую общую высоту.

- Состояния взаимодействия: `Rest`, `Touch`, `Disabled`, `Loading`.
- `Selected` не заменяет `State`: выбранная кнопка также может быть нажатой,
  заблокированной или загружающейся.
- Для VoiceOver передавать выбранность как состояние элемента; смысл не должен
  определяться только цветом или сменой заливки.
- `Icon` управляет видимостью иконки. Для разных состояний предусмотрены два
  независимых swap-свойства: `↳ Icon Instance` и `↳ Selected Icon Instance`.

## Связанные компоненты

- [Button](button.md) — обычное действие без сохраняемого состояния выбора.
- `Mark / Star_Bold` — пример иконки невыбранного состояния.
- `Mark / Star_Solid` — пример иконки выбранного состояния.
- `.x / loading shape` — индикатор `Loading`.
- `_compensation` — внутренний служебный компонент выравнивания.

<!-- FIGMA_SYNC:START -->
## Актуальные данные Figma

> Последняя проверка: `2026-08-21T15:27:50Z` · структура `4614dd0d8d8f` · статус `unknown`.

### Свойства из компонента

| Свойство | Тип | Значение по умолчанию | Варианты |
|---|---|---|---|
| `Device` | `variant` | `—` | iPad / iPhone |
| `Icon` | `boolean` | `—` | — |
| `Selected` | `variant` | `—` | False / True |
| `Shape` | `variant` | `—` | Circle → / Circle ↓ / Rectangle |
| `Size` | `variant` | `—` | Default / Small |
| `State` | `variant` | `—` | Disabled / Loading / Rest / Touch |
| `String Text` | `text` | `—` | — |
| `Style` | `variant` | `—` | Ghost / Primary |
| `Text` | `variant` | `—` | False / True |
| `↳ Icon Instance` | `instance_swap` | `—` | — |
| `↳ Selected Icon Instance` | `instance_swap` | `—` | — |

### Варианты и размеры

| Ось | Значения |
|---|---|
| `Device` | iPad / iPhone |
| `Selected` | False / True |
| `Shape` | Circle → / Circle ↓ / Rectangle |
| `Size` | Default / Small |
| `State` | Disabled / Loading / Rest / Touch |
| `Style` | Ghost / Primary |
| `Text` | False / True |

Комбинаций в COMPONENT_SET: **208**.

| Размер | Количество вариантов | Примеры |
|---|---:|---|
| `36.0×36.0` | 23 | Device=iPhone, Shape=Rectangle, Style=Primary, Size=Small, Selected=False, State=Rest, Text=False; Device=iPhone, Shape=Rectangle, Style=Primary, Size=Small, Selected=False, State=Loading, Text=False; Device=iPhone, Shape=Rectangle, Style=Primary, Size=Small, Selected=False, State=Disabled, Text=False |
| `36.0×38.0` | 5 | Device=iPhone, Shape=Circle ↓, Style=Ghost, Size=Small, Selected=False, State=Rest, Text=True; Device=iPhone, Shape=Circle ↓, Style=Ghost, Size=Small, Selected=False, State=Disabled, Text=True; Device=iPhone, Shape=Circle ↓, Style=Ghost, Size=Small, Selected=True, State=Rest, Text=True |
| `40.0×40.0` | 22 | Device=iPad, Shape=Rectangle, Style=Primary, Size=Small, Selected=False, State=Rest, Text=False; Device=iPad, Shape=Rectangle, Style=Primary, Size=Small, Selected=False, State=Loading, Text=False; Device=iPad, Shape=Rectangle, Style=Primary, Size=Small, Selected=False, State=Disabled, Text=False |
| `40.0×44.0` | 6 | Device=iPad, Shape=Circle ↓, Style=Ghost, Size=Small, Selected=False, State=Rest, Text=True; Device=iPad, Shape=Circle ↓, Style=Ghost, Size=Small, Selected=False, State=Disabled, Text=True; Device=iPad, Shape=Circle ↓, Style=Ghost, Size=Small, Selected=False, State=Touch, Text=True |
| `48.0×44.0` | 6 | Device=iPhone, Shape=Circle ↓, Style=Ghost, Size=Default, Selected=False, State=Rest, Text=True; Device=iPhone, Shape=Circle ↓, Style=Ghost, Size=Default, Selected=False, State=Disabled, Text=True; Device=iPhone, Shape=Circle ↓, Style=Ghost, Size=Default, Selected=False, State=Touch, Text=True |
| `48.0×48.0` | 22 | Device=iPhone, Shape=Rectangle, Style=Primary, Size=Default, Selected=False, State=Rest, Text=False; Device=iPhone, Shape=Rectangle, Style=Primary, Size=Default, Selected=False, State=Loading, Text=False; Device=iPhone, Shape=Rectangle, Style=Primary, Size=Default, Selected=False, State=Disabled, Text=False |
| `52.0×50.0` | 6 | Device=iPad, Shape=Circle ↓, Style=Ghost, Size=Default, Selected=False, State=Rest, Text=True; Device=iPad, Shape=Circle ↓, Style=Ghost, Size=Default, Selected=False, State=Disabled, Text=True; Device=iPad, Shape=Circle ↓, Style=Ghost, Size=Default, Selected=False, State=Touch, Text=True |
| `52.0×52.0` | 22 | Device=iPad, Shape=Rectangle, Style=Primary, Size=Default, Selected=False, State=Rest, Text=False; Device=iPad, Shape=Rectangle, Style=Primary, Size=Default, Selected=False, State=Loading, Text=False; Device=iPad, Shape=Rectangle, Style=Primary, Size=Default, Selected=False, State=Disabled, Text=False |
| `90.0×56.0` | 8 | Device=iPhone, Shape=Circle ↓, Style=Primary, Size=Small, Selected=False, State=Rest, Text=True; Device=iPhone, Shape=Circle ↓, Style=Primary, Size=Small, Selected=False, State=Loading, Text=True; Device=iPhone, Shape=Circle ↓, Style=Primary, Size=Small, Selected=False, State=Disabled, Text=True |
| `90.0×70.0` | 8 | Device=iPhone, Shape=Circle ↓, Style=Primary, Size=Default, Selected=False, State=Rest, Text=True; Device=iPhone, Shape=Circle ↓, Style=Primary, Size=Default, Selected=False, State=Loading, Text=True; Device=iPhone, Shape=Circle ↓, Style=Primary, Size=Default, Selected=False, State=Disabled, Text=True |
| `102.0×66.0` | 8 | Device=iPad, Shape=Circle ↓, Style=Primary, Size=Small, Selected=False, State=Rest, Text=True; Device=iPad, Shape=Circle ↓, Style=Primary, Size=Small, Selected=False, State=Loading, Text=True; Device=iPad, Shape=Circle ↓, Style=Primary, Size=Small, Selected=False, State=Disabled, Text=True |
| `102.0×80.0` | 8 | Device=iPad, Shape=Circle ↓, Style=Primary, Size=Default, Selected=False, State=Rest, Text=True; Device=iPad, Shape=Circle ↓, Style=Primary, Size=Default, Selected=False, State=Loading, Text=True; Device=iPad, Shape=Circle ↓, Style=Primary, Size=Default, Selected=False, State=Disabled, Text=True |
| `141.0×36.0` | 8 | Device=iPhone, Shape=Circle →, Style=Primary, Size=Small, Selected=False, State=Rest, Text=True; Device=iPhone, Shape=Circle →, Style=Primary, Size=Small, Selected=False, State=Loading, Text=True; Device=iPhone, Shape=Circle →, Style=Primary, Size=Small, Selected=False, State=Disabled, Text=True |
| `151.0×36.0` | 8 | Device=iPhone, Shape=Rectangle, Style=Primary, Size=Small, Selected=False, State=Rest, Text=True; Device=iPhone, Shape=Rectangle, Style=Primary, Size=Small, Selected=False, State=Loading, Text=True; Device=iPhone, Shape=Rectangle, Style=Primary, Size=Small, Selected=False, State=Disabled, Text=True |
| `162.0×40.0` | 8 | Device=iPad, Shape=Circle →, Style=Primary, Size=Small, Selected=False, State=Rest, Text=True; Device=iPad, Shape=Circle →, Style=Primary, Size=Small, Selected=False, State=Loading, Text=True; Device=iPad, Shape=Circle →, Style=Primary, Size=Small, Selected=False, State=Disabled, Text=True |
| `169.0×48.0` | 8 | Device=iPhone, Shape=Circle →, Style=Primary, Size=Default, Selected=False, State=Rest, Text=True; Device=iPhone, Shape=Circle →, Style=Primary, Size=Default, Selected=False, State=Loading, Text=True; Device=iPhone, Shape=Circle →, Style=Primary, Size=Default, Selected=False, State=Disabled, Text=True |
| `176.0×40.0` | 8 | Device=iPad, Shape=Rectangle, Style=Primary, Size=Small, Selected=False, State=Rest, Text=True; Device=iPad, Shape=Rectangle, Style=Primary, Size=Small, Selected=False, State=Loading, Text=True; Device=iPad, Shape=Rectangle, Style=Primary, Size=Small, Selected=False, State=Disabled, Text=True |
| `179.0×48.0` | 8 | Device=iPhone, Shape=Rectangle, Style=Primary, Size=Default, Selected=False, State=Rest, Text=True; Device=iPhone, Shape=Rectangle, Style=Primary, Size=Default, Selected=False, State=Loading, Text=True; Device=iPhone, Shape=Rectangle, Style=Primary, Size=Default, Selected=False, State=Disabled, Text=True |
| `189.0×52.0` | 8 | Device=iPad, Shape=Circle →, Style=Primary, Size=Default, Selected=False, State=Rest, Text=True; Device=iPad, Shape=Circle →, Style=Primary, Size=Default, Selected=False, State=Loading, Text=True; Device=iPad, Shape=Circle →, Style=Primary, Size=Default, Selected=False, State=Disabled, Text=True |
| `201.0×52.0` | 8 | Device=iPad, Shape=Rectangle, Style=Primary, Size=Default, Selected=False, State=Rest, Text=True; Device=iPad, Shape=Rectangle, Style=Primary, Size=Default, Selected=False, State=Loading, Text=True; Device=iPad, Shape=Rectangle, Style=Primary, Size=Default, Selected=False, State=Disabled, Text=True |

### Состояния

- `Selected`: False / True
- `State`: Disabled / Loading / Rest / Touch

### Зависимости

- `.x / loading shape` — node `dependency:3`
- `_compensation` — node `dependency:2`
- `Mark / Star_Bold` — node `dependency:1`
- `Mark / Star_Solid` — node `dependency:4`

### Источник

- [Button - Toggle](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=31182-4838&t=6NQra4uE9oLKkthr-4) — fileKey `rMcDm5qGp4CXkXXddEbcMh`, API key `rMcDm5qGp4CXkXXddEbcMh`, node `31182:4838`, type `COMPONENT_SET`.
<!-- FIGMA_SYNC:END -->
