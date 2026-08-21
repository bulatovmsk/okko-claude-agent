# TabGroup

## Назначение

Группа взаимоисключающих вкладок для переключения между соседними разделами
или представлениями внутри одного контекста. Компонент собирается из
[Tabgroup - Item](tabgroup-item.md); в присланной Figma-ноде активен первый
элемент.

## Когда использовать

- Для переключения между равноправными разделами без перехода на другой уровень
  навигации.
- `Tab width=Scrollable` — когда группа шире доступной области: живые сборки
  содержат восемь элементов и сохраняют собственную ширину.
- `Tab width=Stretch` — для трёх элементов равной ширины, заполняющих контейнер.
- `Shape=Rectangle` использует элементы `Content=Text+Icon`; `Shape=Square` —
  компактные элементы `Content=Number`.
- `Size=Small`, `Default` или `Large` выбирайте согласованно для всей группы;
  `Device` переключает размеры iPhone/iPad.

## Когда НЕ использовать

- Для глобальной нижней навигации используйте [Tabbar - Meta](tabbar-meta.md).
- Для независимых фильтров с возможным множественным выбором используйте
  [Chips](chips.md), а для обычного действия — [Button](button.md).
- Не собирайте `Stretch + Square`: такой комбинации в живом COMPONENT_SET нет.
- Не используйте отдельный Tab как автономную кнопку и не допускайте несколько
  активных вкладок в одной группе.

## Платформенные особенности iOS

- Высоты iPhone: 36 / 48 / 58 pt для Small / Default / Large; iPad:
  40 / 52 / 76 pt.
- `Scrollable` должен прокручиваться горизонтально и сохранять активную вкладку
  видимой. В живых примерах восемь элементов, первый имеет состояние `Active`.
- `Stretch` распределяет три элемента поровну. Размеры 248/369 pt на iPhone и
  480/960 pt на iPad отражают опубликованные сборки, а не новые значения
  токенов.
- Для Small визуальная высота меньше 44 pt, поэтому интерактивная область должна
  расширяться минимум до 44×44 pt без изменения внешнего размера.
- Для VoiceOver группа должна объявляться как tab group/tab list, каждый элемент
  — как tab с `selected`-состоянием. После переключения обновляйте доступное
  содержимое и фокус предсказуемо.
- Верхний компонент не публикует свойство выбранного индекса: активное состояние
  задаётся во вложенном `Tabgroup - Item`.

## Связанные компоненты

- [Tabgroup - Item](tabgroup-item.md) — вложенная вкладка и её состояния.
- [TabNavigation](tab-navigation.md) — промо-табы для перехода между категориями
  контента, без оси `Active`.
- [Chips](chips.md) — независимые или множественные фильтры.
- [Tabbar - Meta](tabbar-meta.md) — глобальная нижняя навигация приложения.
- [Button](button.md) — действие без семантики выбора вкладки.
- `Categories / Clapperboard` — иконка, подтверждённая живыми примерами.

<!-- FIGMA_SYNC:START -->
## Актуальные данные Figma

> Последняя проверка: `2026-08-21T16:21:01Z` · структура `56ac48f4c335` · статус `unknown`.

### Свойства из компонента

| Свойство | Тип | Значение по умолчанию | Варианты |
|---|---|---|---|
| `Device` | `variant` | `—` | iPad / iPhone |
| `Shape` | `variant` | `—` | Rectangle / Square |
| `Size` | `variant` | `—` | Default / Large / Small |
| `Tab width` | `variant` | `—` | Scrollable / Stretch |

### Варианты и размеры

| Ось | Значения |
|---|---|
| `Device` | iPad / iPhone |
| `Shape` | Rectangle / Square |
| `Size` | Default / Large / Small |
| `Tab width` | Scrollable / Stretch |

Комбинаций в COMPONENT_SET: **18**.

| Размер | Количество вариантов | Примеры |
|---|---:|---|
| `248.0×36.0` | 1 | Device=iPhone, Tab width=Stretch, Shape=Rectangle, Size=Small |
| `316.0×36.0` | 1 | Device=iPhone, Tab width=Scrollable, Shape=Square, Size=Small |
| `362.0×40.0` | 1 | Device=iPad, Tab width=Scrollable, Shape=Square, Size=Small |
| `369.0×48.0` | 1 | Device=iPhone, Tab width=Stretch, Shape=Rectangle, Size=Default |
| `369.0×58.0` | 1 | Device=iPhone, Tab width=Stretch, Shape=Rectangle, Size=Large |
| `412.0×48.0` | 1 | Device=iPhone, Tab width=Scrollable, Shape=Square, Size=Default |
| `458.0×52.0` | 1 | Device=iPad, Tab width=Scrollable, Shape=Square, Size=Default |
| `480.0×40.0` | 1 | Device=iPad, Tab width=Stretch, Shape=Rectangle, Size=Small |
| `492.0×58.0` | 1 | Device=iPhone, Tab width=Scrollable, Shape=Square, Size=Large |
| `620.0×36.0` | 1 | Device=iPhone, Tab width=Scrollable, Shape=Rectangle, Size=Small |
| `650.0×76.0` | 1 | Device=iPad, Tab width=Scrollable, Shape=Square, Size=Large |
| `746.0×40.0` | 1 | Device=iPad, Tab width=Scrollable, Shape=Rectangle, Size=Small |
| `764.0×48.0` | 1 | Device=iPhone, Tab width=Scrollable, Shape=Rectangle, Size=Default |
| `866.0×52.0` | 1 | Device=iPad, Tab width=Scrollable, Shape=Rectangle, Size=Default |
| `868.0×58.0` | 1 | Device=iPhone, Tab width=Scrollable, Shape=Rectangle, Size=Large |
| `960.0×52.0` | 1 | Device=iPad, Tab width=Stretch, Shape=Rectangle, Size=Default |
| `960.0×76.0` | 1 | Device=iPad, Tab width=Stretch, Shape=Rectangle, Size=Large |
| `1106.0×76.0` | 1 | Device=iPad, Tab width=Scrollable, Shape=Rectangle, Size=Large |

### Зависимости

- `Categories / Clapperboard` — node `39522:41695`
- `Tabgroup - Item` — node `dependency:tabgroup-item`; set `24233:1463`

### Источник

- [TabGroup](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=24233-1389&t=6NQra4uE9oLKkthr-4) — fileKey `rMcDm5qGp4CXkXXddEbcMh`, API key `rMcDm5qGp4CXkXXddEbcMh`, node `24233:1389`, type `COMPONENT_SET`.
<!-- FIGMA_SYNC:END -->
