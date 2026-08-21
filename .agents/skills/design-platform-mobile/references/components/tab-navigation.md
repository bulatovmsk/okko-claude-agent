# TabNavigation

## Назначение

Компонент предназначен для навигации по различным категориям контента в
приложении. Пользовательское название — **промо-табы**, точное имя
COMPONENT_SET в Figma — `TabNavigation`. Поддерживает текст, опциональную иконку
и промо-фон через сменный слот.

## Когда использовать

- Для перехода между категориями контента, в том числе в горизонтальной группе
  на главной или другом контентном экране.
- `Background=true` — когда таб должен использовать изображение/Subject из
  фонового слота. Точное имя свойства слота в Figma содержит опечатку:
  `Backgroung Slot`.
- `Right Padding=true` резервирует правую часть промо-фона под Subject; это
  назначение прямо отмечено в связанном Figma-гайде.
- `Icon=true` включает ведущую иконку, `Icon Slot` позволяет заменить её.
- `Size=Default` или `Small` и `Device=iPhone/iPad` выбирайте в соответствии с
  платформенной сборкой. Подпись задаётся свойством `Text`.
- Длинная подпись остаётся в одну строку и обрезается многоточием до
  опубликованного максимума ширины.

## Когда НЕ использовать

- Для локального переключения между соседними представлениями с явным выбранным
  состоянием используйте [TabGroup](tabgroup.md): у `TabNavigation` нет оси
  `Active` или выбранного индекса.
- Для глобальной нижней навигации используйте [Tabbar - Meta](tabbar-meta.md).
- Для независимых фильтров или множественного выбора используйте
  [Chips](chips.md), а для обычного действия — [Button](button.md).
- Не трактуйте `Right Padding` как универсальный внешний отступ: это часть
  композиции промо-фона с Subject.

## Платформенные особенности iOS

- Высота `Default`: 48 pt на iPhone и 52 pt на iPad; `Small`: 36 и 40 pt.
- Максимальная ширина из живого контекста: iPhone 288 pt (`Default`) и 192 pt
  (`Small`), iPad 312 и 228 pt соответственно.
- Small ниже минимальной iOS touch target, поэтому обеспечьте интерактивную
  область не меньше 44×44 pt без изменения визуального размера.
- Состояния COMPONENT_SET называются `Rest` и `Touch`. В связанном гайде подпись
  примера использует `Pressed`; до исправления источника ориентируйтесь на
  точное значение свойства `Touch`.
- Для VoiceOver объявляйте понятное имя категории и семантику ссылки/вкладки по
  фактическому поведению. Фоновое изображение и декоративную иконку скрывайте от
  отдельного озвучивания, если их смысл уже передан текстом.
- Не переносите размеры, цвета и отступы как значения токенов из Figma:
  актуальные токены проверяются отдельно в Tokens Studio.

## Связанные компоненты

- [TabGroup](tabgroup.md) — локальный взаимоисключающий выбор с `Active`.
- [Tabbar - Meta](tabbar-meta.md) — глобальная нижняя навигация.
- [Chips](chips.md) — независимый или множественный выбор фильтров.
- `TabNavigationGroup` — групповая сборка, показанная в связанном гайде; её
  исходный COMPONENT_SET не подменяется присланной нодой.
- `Mark / Star_Bold` — сменная иконка живого примера.
- `_🔴[Delete Candidate]Slot` — текущая внутренняя зависимость фонового слота.
  Маркер указывает на кандидата на удаление, но не делает весь `TabNavigation`
  deprecated: статус корневого компонента в Figma не задан.

## Конфликты живого источника

- `Backgroung Slot` — опубликованная опечатка в имени свойства; сохраняйте её
  при обращении к текущей Figma-версии.
- Гайд использует термин `Pressed`, а компонент публикует `State=Touch`.
- Внутренняя зависимость фонового слота помечена как delete candidate, поэтому
  при актуализации нужно отдельно проверять её переименование или удаление.

<!-- FIGMA_SYNC:START -->
## Актуальные данные Figma

> Последняя проверка: `2026-08-21T16:25:10Z` · структура `57f33d776aaa` · статус `unknown`.

### Свойства из компонента

| Свойство | Тип | Значение по умолчанию | Варианты |
|---|---|---|---|
| `Background` | `boolean` | `false` | — |
| `Backgroung Slot` | `instance_swap` | `—` | — |
| `Device` | `variant` | `—` | iPad / iPhone |
| `Icon` | `boolean` | `true` | False / True |
| `Icon Slot` | `instance_swap` | `—` | — |
| `Right Padding` | `boolean` | `true` | False / True |
| `Size` | `variant` | `—` | Default / Small |
| `State` | `variant` | `—` | Rest / Touch |
| `Text` | `text` | `Text` | — |

### Варианты и размеры

| Ось | Значения |
|---|---|
| `Device` | iPad / iPhone |
| `Icon` | False / True |
| `Right Padding` | False / True |
| `Size` | Default / Small |
| `State` | Rest / Touch |

Комбинаций в COMPONENT_SET: **32**.

| Размер | Количество вариантов | Примеры |
|---|---:|---|
| `54.0×36.0` | 2 | Device=iPhone, Size=Small, State=Rest, Icon=False, Right Padding=False; Device=iPhone, Size=Small, State=Touch, Icon=False, Right Padding=False |
| `62.0×40.0` | 2 | Device=iPad, Size=Small, State=Rest, Icon=False, Right Padding=False; Device=iPad, Size=Small, State=Touch, Icon=False, Right Padding=False |
| `66.0×48.0` | 2 | Device=iPhone, Size=Default, State=Rest, Icon=False, Right Padding=False; Device=iPhone, Size=Default, State=Touch, Icon=False, Right Padding=False |
| `73.0×52.0` | 2 | Device=iPad, Size=Default, State=Rest, Icon=False, Right Padding=False; Device=iPad, Size=Default, State=Touch, Icon=False, Right Padding=False |
| `74.0×36.0` | 1 | Device=iPhone, Size=Small, State=Touch, Icon=True, Right Padding=False |
| `78.0×36.0` | 1 | Device=iPhone, Size=Small, State=Rest, Icon=True, Right Padding=False |
| `88.0×40.0` | 1 | Device=iPad, Size=Small, State=Touch, Icon=True, Right Padding=False |
| `92.0×40.0` | 1 | Device=iPad, Size=Small, State=Rest, Icon=True, Right Padding=False |
| `92.0×48.0` | 1 | Device=iPhone, Size=Default, State=Touch, Icon=True, Right Padding=False |
| `94.0×36.0` | 2 | Device=iPhone, Size=Small, State=Rest, Icon=False, Right Padding=True; Device=iPhone, Size=Small, State=Touch, Icon=False, Right Padding=True |
| `96.0×48.0` | 1 | Device=iPhone, Size=Default, State=Rest, Icon=True, Right Padding=False |
| `103.0×52.0` | 1 | Device=iPad, Size=Default, State=Touch, Icon=True, Right Padding=False |
| `107.0×52.0` | 1 | Device=iPad, Size=Default, State=Rest, Icon=True, Right Padding=False |
| `108.0×40.0` | 2 | Device=iPad, Size=Small, State=Rest, Icon=False, Right Padding=True; Device=iPad, Size=Small, State=Touch, Icon=False, Right Padding=True |
| `114.0×36.0` | 1 | Device=iPhone, Size=Small, State=Touch, Icon=True, Right Padding=True |
| `118.0×36.0` | 1 | Device=iPhone, Size=Small, State=Rest, Icon=True, Right Padding=True |
| `126.0×48.0` | 2 | Device=iPhone, Size=Default, State=Rest, Icon=False, Right Padding=True; Device=iPhone, Size=Default, State=Touch, Icon=False, Right Padding=True |
| `134.0×40.0` | 1 | Device=iPad, Size=Small, State=Touch, Icon=True, Right Padding=True |
| `137.0×52.0` | 2 | Device=iPad, Size=Default, State=Rest, Icon=False, Right Padding=True; Device=iPad, Size=Default, State=Touch, Icon=False, Right Padding=True |
| `138.0×40.0` | 1 | Device=iPad, Size=Small, State=Rest, Icon=True, Right Padding=True |
| `152.0×48.0` | 1 | Device=iPhone, Size=Default, State=Touch, Icon=True, Right Padding=True |
| `156.0×48.0` | 1 | Device=iPhone, Size=Default, State=Rest, Icon=True, Right Padding=True |
| `167.0×52.0` | 1 | Device=iPad, Size=Default, State=Touch, Icon=True, Right Padding=True |
| `171.0×52.0` | 1 | Device=iPad, Size=Default, State=Rest, Icon=True, Right Padding=True |

### Состояния

- `State`: Rest / Touch

### Зависимости

- `_🔴[Delete Candidate]Slot` — node `dependency:delete-candidate-slot`
- `Mark / Star_Bold` — node `39522:41332`

### Источник

- [TabNavigation](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=24687-2182&t=6NQra4uE9oLKkthr-4) — fileKey `rMcDm5qGp4CXkXXddEbcMh`, API key `rMcDm5qGp4CXkXXddEbcMh`, node `24687:2182`, type `COMPONENT_SET`.
- [Component guide](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=24687-2253&t=oTcgMYHS9iBxqxgl-4) — `guide`, node `24687:2253`.
<!-- FIGMA_SYNC:END -->
