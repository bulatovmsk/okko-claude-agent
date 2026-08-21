# Tabgroup - Item

## Назначение

Один интерактивный элемент внутри [TabGroup](tabgroup.md). Короткое поисковое
имя — **Tab**, точное имя COMPONENT_SET в Figma — `Tabgroup - Item`. Поддерживает
текст с иконкой или числовое содержимое, выбранное состояние и состояния
нажатия/недоступности.

## Когда использовать

- Как дочерний элемент `TabGroup` для одного взаимоисключающего варианта.
- `Content=Text+Icon` — текстовая вкладка с опциональной иконкой; `Icon`
  управляет её присутствием, `Swap Icon` — заменой.
- `Content=Number` — компактная квадратная вкладка с числовым содержимым.
- `State=Active` отмечает выбранную вкладку; `Pressed` и `Active Pressed`
  показывают нажатие для невыбранного и выбранного состояний соответственно.
- `Label=true` добавляет [Label : Small](label-small.md) к варианту
  `Text+Icon`; в живом контексте числовые варианты метку не показывают.
- `Background` управляет фоновой подложкой доступных вариантов компонента.

## Когда НЕ использовать

- Не используйте отдельно как обычную кнопку — применяйте [Button](button.md).
- Для множественного или независимого выбора используйте [Chips](chips.md),
  [Checkbox](checkbox.md) либо [Button - Toggle](button-toggle.md) по сценарию.
- Не используйте вместо [Tabbar - Meta](tabbar-meta.md): Tabbar переключает
  основные разделы приложения, а Tab — соседние представления внутри контекста.
- Не добавляйте состояние, размер или тип содержимого, отсутствующий в живом
  наборе из 60 комбинаций.

## Платформенные особенности iOS

- Высоты/квадратные размеры iPhone: 36, 48 и 58 pt; iPad: 40, 52 и 76 pt для
  Small, Default и Large.
- Ширина `Text+Icon` зависит от платформы и размера: iPhone 74/92/105 pt,
  iPad 88/103/133 pt. `Number` остаётся квадратным.
- `Rest` — обычное состояние, `Pressed` — нажатие, `Active` — выбранное,
  `Active Pressed` — нажатие выбранного, `Disabled` — недоступное.
- Small ниже минимальной iOS touch target, поэтому внутри группы обеспечьте
  интерактивную область не меньше 44×44 pt.
- VoiceOver должен объявлять название вкладки, роль tab, выбранность и
  недоступность. Декоративную иконку не озвучивайте отдельно, если смысл уже
  передан названием.
- В опубликованных properties нет отдельного текстового свойства: не считайте
  строку `Text` или `00` доступным API верхнего COMPONENT_SET без повторной
  проверки живой ноды.

## Связанные компоненты

- [TabGroup](tabgroup.md) — родительская сборка вкладок.
- [Label : Small](label-small.md) — опциональная компактная метка.
- [Chips](chips.md) — выбор фильтров, включая множественный.
- [Button](button.md) и [Button - Toggle](button-toggle.md) — действия и
  независимые переключатели.
- `Categories / Clapperboard` — сменная иконка живого примера.

<!-- FIGMA_SYNC:START -->
## Актуальные данные Figma

> Последняя проверка: `2026-08-21T16:21:01Z` · структура `bff36717740a` · статус `unknown`.

### Свойства из компонента

| Свойство | Тип | Значение по умолчанию | Варианты |
|---|---|---|---|
| `Background` | `boolean` | `true` | — |
| `Content` | `variant` | `—` | Number / Text+Icon |
| `Device` | `variant` | `—` | iPad / iPhone |
| `Icon` | `boolean` | `true` | — |
| `Label` | `boolean` | `false` | — |
| `Size` | `variant` | `—` | Default / Large / Small |
| `State` | `variant` | `—` | Active / Active Pressed / Disabled / Pressed / Rest |
| `Swap Icon` | `instance_swap` | `—` | — |

### Варианты и размеры

| Ось | Значения |
|---|---|
| `Content` | Number / Text+Icon |
| `Device` | iPad / iPhone |
| `Size` | Default / Large / Small |
| `State` | Active / Active Pressed / Disabled / Pressed / Rest |

Комбинаций в COMPONENT_SET: **60**.

| Размер | Количество вариантов | Примеры |
|---|---:|---|
| `36.0×36.0` | 5 | Device=iPhone, State=Rest, Size=Small, Content=Number; Device=iPhone, State=Disabled, Size=Small, Content=Number; Device=iPhone, State=Pressed, Size=Small, Content=Number |
| `40.0×40.0` | 5 | Device=iPad, State=Rest, Size=Small, Content=Number; Device=iPad, State=Disabled, Size=Small, Content=Number; Device=iPad, State=Pressed, Size=Small, Content=Number |
| `48.0×48.0` | 5 | Device=iPhone, State=Rest, Size=Default, Content=Number; Device=iPhone, State=Disabled, Size=Default, Content=Number; Device=iPhone, State=Pressed, Size=Default, Content=Number |
| `52.0×52.0` | 5 | Device=iPad, State=Rest, Size=Default, Content=Number; Device=iPad, State=Disabled, Size=Default, Content=Number; Device=iPad, State=Pressed, Size=Default, Content=Number |
| `58.0×58.0` | 5 | Device=iPhone, State=Rest, Size=Large, Content=Number; Device=iPhone, State=Disabled, Size=Large, Content=Number; Device=iPhone, State=Pressed, Size=Large, Content=Number |
| `74.0×36.0` | 5 | Device=iPhone, State=Rest, Size=Small, Content=Text+Icon; Device=iPhone, State=Disabled, Size=Small, Content=Text+Icon; Device=iPhone, State=Pressed, Size=Small, Content=Text+Icon |
| `76.0×76.0` | 5 | Device=iPad, State=Rest, Size=Large, Content=Number; Device=iPad, State=Disabled, Size=Large, Content=Number; Device=iPad, State=Pressed, Size=Large, Content=Number |
| `88.0×40.0` | 5 | Device=iPad, State=Rest, Size=Small, Content=Text+Icon; Device=iPad, State=Disabled, Size=Small, Content=Text+Icon; Device=iPad, State=Pressed, Size=Small, Content=Text+Icon |
| `92.0×48.0` | 5 | Device=iPhone, State=Rest, Size=Default, Content=Text+Icon; Device=iPhone, State=Disabled, Size=Default, Content=Text+Icon; Device=iPhone, State=Pressed, Size=Default, Content=Text+Icon |
| `103.0×52.0` | 5 | Device=iPad, State=Rest, Size=Default, Content=Text+Icon; Device=iPad, State=Disabled, Size=Default, Content=Text+Icon; Device=iPad, State=Pressed, Size=Default, Content=Text+Icon |
| `105.0×58.0` | 5 | Device=iPhone, State=Rest, Size=Large, Content=Text+Icon; Device=iPhone, State=Disabled, Size=Large, Content=Text+Icon; Device=iPhone, State=Pressed, Size=Large, Content=Text+Icon |
| `133.0×76.0` | 5 | Device=iPad, State=Rest, Size=Large, Content=Text+Icon; Device=iPad, State=Disabled, Size=Large, Content=Text+Icon; Device=iPad, State=Pressed, Size=Large, Content=Text+Icon |

### Состояния

- `State`: Active / Active Pressed / Disabled / Pressed / Rest

### Зависимости

- `Categories / Clapperboard` — node `39522:41695`
- `Label : Small` — node `dependency:label-small`

### Источник

- [Tabgroup - Item](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=24233-1463&t=6NQra4uE9oLKkthr-4) — fileKey `rMcDm5qGp4CXkXXddEbcMh`, API key `rMcDm5qGp4CXkXXddEbcMh`, node `24233:1463`, type `COMPONENT_SET`.
<!-- FIGMA_SYNC:END -->
