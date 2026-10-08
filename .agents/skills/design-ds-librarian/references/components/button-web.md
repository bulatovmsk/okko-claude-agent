# Button — Web: состояния

Источник: [Lib-Web → Button](https://www.figma.com/design/e72TWMOh7ibwauqgKwLnC9/Lib-Web?node-id=26093-350409), `COMPONENT_SET` `26093:350409`. Проверено 2026-10-08: 882 варианта, 162 сочетания без оси `State`. Это правило относится к этому Web-компоненту; не переносить его на iOS, Android или TV.

## Оси компонента

- `Breakpoint`: `Mobile 320+`, `Tablet 600+`, `Desktop 1720+`.
- `Shape`: `Rectangle`, `Circle ↓`, `Circle →`.
- `Size`: `Small`, `Default`, `Large`.
- `Style`: `Primary`, `Secondary`, `Ghost`, `Negative`, `Sber`.
- `Text`: `true`, `false`.
- `State`: `Rest`, `Hover`, `Focus`, `Pressed`, `Disabled`, `Loading`, `Progress`.

Выбирай опубликованный вариант для нужного сочетания свойств. Не предполагай, что все семь состояний существуют для каждой комбинации.

### `Breakpoint` Web и `Device` iOS

`Breakpoint` в Web выполняет ту же роль оси платформенного варианта, что `Device` в [iOS Button](button.md): выбирает реализацию кнопки для целевого контекста. При переносе спецификации сопоставляй **роль свойства**, а не его имя: в Web записывай `Breakpoint`, в iOS — `Device`.

Значения различаются: Web — `Mobile 320+`, `Tablet 600+`, `Desktop 1720+`; iOS — `iPhone`, `iPad`. Сходная роль свойства не означает прямого соответствия значений, размеров, состояний или поведения. Для каждого целевого варианта проверяй его фактические свойства в своей библиотеке.

## Как показываются состояния

| `State` | Где есть | Отображение в Figma |
|---|---|---|
| `Rest` | Все 162 базовые комбинации | Исходные заливка, текст и иконка; `opacity=1`, без слоя обводки состояния. |
| `Hover` | Tablet/Desktop, 108 вариантов | `opacity=1`; поверх кнопки отдельный `_Button - Border`. Для `Primary`, `Secondary`, `Ghost` обводка градиентная, для `Negative` и `Sber` — сплошная. У `Secondary` заливка меняется на радиальный градиент. |
| `Focus` | Tablet/Desktop, 108 вариантов | `opacity=1`; обычно есть `_Button - Border` со светлой сплошной обводкой (белый, opacity краски 0,56, толщина 1 в проверенных вариантах). Отличается от `Hover`. У одного Desktop-варианта обводка отсутствует — см. исключения ниже. |
| `Pressed` | Все 162 комбинации | Общая `opacity≈0,7`; на Tablet/Desktop обычно есть обводка состояния, на Mobile её нет. У одного Desktop-варианта обводка отсутствует — см. исключения ниже. |
| `Disabled` | Все 162 комбинации | Общая `opacity=0,5`; нет обводки и слоя загрузки. |
| `Loading` | Все 162 комбинации | Общая `opacity=0,5`; в 156 вариантах есть видимый `_loading gradient`. У круглых кнопок слой расположен внутри дочернего `circle`, поэтому его нельзя искать только среди прямых детей варианта. У шести вариантов слоя нет — см. исключения ниже. |
| `Progress` | Только 18 вариантов: `Rectangle`, `Text=true`, `Primary`/`Secondary`, все три размера и брейкпоинта | Видимый `_loading gradient` при `opacity=1`. Не подменять им `Loading`: прозрачность отличается. |

`Hover` и `Focus` в наборе отсутствуют для `Mobile 320+`. На вебе `Hover` соответствует наведению указателя, `Focus` — клавиатурному фокусу; `Pressed` — нажатию. Не трактуй `Focus` как TV D-pad focus.

Наличие варианта `Loading` или `Progress` показывает визуальное состояние компонента, но само по себе не документирует длительность анимации, блокировку повторного нажатия или поведение прогресса в коде. Не выводи эти правила из одного Figma-набора.

### Исключения в текущей библиотеке

- `Loading` без `_loading gradient`: `Circle ↓`, `Small`, `Text=false`, стили `Primary` и `Negative` на каждом из трёх брейкпоинтов. Не добавляй индикатор в спецификацию этого варианта без отдельного решения команды.
- `Focus` и `Pressed` без `_Button - Border`: `Desktop 1720+`, `Rectangle`, `Small`, `Primary`, `Text=true`. Названия состояний и прозрачность сохраняются; не дорисовывай обводку по аналогии с соседними вариантами.

Примеры для сверки: [Rest](https://www.figma.com/design/e72TWMOh7ibwauqgKwLnC9/Lib-Web?node-id=26093-350483), [Hover](https://www.figma.com/design/e72TWMOh7ibwauqgKwLnC9/Lib-Web?node-id=42694-63876), [Focus](https://www.figma.com/design/e72TWMOh7ibwauqgKwLnC9/Lib-Web?node-id=43265-81996), [Pressed](https://www.figma.com/design/e72TWMOh7ibwauqgKwLnC9/Lib-Web?node-id=43265-83350), [Disabled](https://www.figma.com/design/e72TWMOh7ibwauqgKwLnC9/Lib-Web?node-id=42760-62276), [Loading](https://www.figma.com/design/e72TWMOh7ibwauqgKwLnC9/Lib-Web?node-id=42760-63374), [Progress](https://www.figma.com/design/e72TWMOh7ibwauqgKwLnC9/Lib-Web?node-id=42766-67552).
