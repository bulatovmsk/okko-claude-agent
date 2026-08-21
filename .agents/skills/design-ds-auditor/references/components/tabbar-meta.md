# Tabbar - Meta

## Назначение

Нижняя постоянная навигация между пятью основными разделами приложения iOS.
Компонент собирает пять `_Tabbar Item`, фон нижней области и системный Home
Indicator; состояние авторизации меняет последний пункт навигации.

## Когда использовать

- На верхнем уровне приложения для постоянного доступа к пяти основным
  направлениям.
- `Device=iPhone` — для телефонной сборки, `Device=iPad` — для планшетной.
- `Authorized=True` показывает последний пункт профиля; `Authorized=False` —
  пункт входа.
- Активный раздел задаётся свойством `Selected` во вложенном `_Tabbar Item`.
  Верхний `Tabbar - Meta` публикует только оси `Device` и `Authorized`.
- Подписи пунктов задаются свойством `Label` вложенных элементов; сохраняйте
  короткие устойчивые названия разделов.

## Когда НЕ использовать

- Для навигации назад, заголовка или действий текущего экрана используйте
  [Navbar](navbar.md).
- Для временных действий используйте [Button](button.md) или контекстные
  элементы, а не добавляйте их в постоянную навигацию.
- Не меняйте число пунктов произвольно: живая сборка содержит ровно пять
  `_Tabbar Item`, а отдельной оси количества нет.
- Не подменяйте этим компонентом `Tabbar - Main`: это другое имя зависимости,
  встречающееся в [Error - Fulscreen](error-fullscreen.md).

## Платформенные особенности iOS

- Опубликованы четыре комбинации. iPhone имеет размер 393×138 pt, iPad —
  820×138 pt; высота включает нижний фон и область Home Indicator.
- На iPad навигационная капсула центрирована внутри более широкой нижней области;
  не растягивайте сами пункты до полной ширины экрана без отдельного варианта.
- Не добавляйте второй системный индикатор или дополнительный нижний safe-area
  padding поверх уже включённой области компонента.
- Каждый пункт должен иметь отдельную touch area, понятный VoiceOver label и
  состояние selected. VoiceOver читает компонент как tab bar, а элементы — как
  вкладки, не как пять независимых кнопок без контекста.
- Иконка не заменяет подпись: selected/unselected должны различаться не только
  цветом, но и accessibility state.
- Конфликт живой структуры: экземпляр `Home Indicator` сохраняет внутренние
  свойства `Device=iPhone, Orientation=Portrait` во всех четырёх вариантах,
  включая iPad. Перед опорой на внутренний адаптив это нужно перепроверить в
  Figma или исправить в библиотеке.

## Связанные компоненты

- [Navbar](navbar.md) — верхняя навигационная оболочка экрана.
- [Error - Fulscreen](error-fullscreen.md) — использует отдельную зависимость
  `Tabbar - Main`, не `Tabbar - Meta`.
- `_Tabbar Item` — внутренний пункт с `Label`, `Selected`, `Icon` и `Image`.
- `Home Indicator` — системная нижняя область.
- `Menu / House` — иконка, подтверждённая живой структурой элемента.

<!-- FIGMA_SYNC:START -->
## Актуальные данные Figma

> Последняя проверка: `2026-08-21T16:13:59Z` · структура `3b1b341e0e34` · статус `unknown`.

### Свойства из компонента

| Свойство | Тип | Значение по умолчанию | Варианты |
|---|---|---|---|
| `Authorized` | `variant` | `—` | False / True |
| `Device` | `variant` | `—` | iPad / iPhone |

### Варианты и размеры

| Ось | Значения |
|---|---|
| `Authorized` | False / True |
| `Device` | iPad / iPhone |

Комбинаций в COMPONENT_SET: **4**.

| Размер | Количество вариантов | Примеры |
|---|---:|---|
| `393.0×138.0` | 2 | Device=iPhone, Authorized=True; Device=iPhone, Authorized=False |
| `820.0×138.0` | 2 | Device=iPad, Authorized=True; Device=iPad, Authorized=False |

### Зависимости

- `_Tabbar Item` — node `dependency:tabbar-item`
- `Home Indicator` — node `dependency:home-indicator`
- `Menu / House` — node `dependency:menu-house`

### Источник

- [Tabbar - Meta](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=38937-15264&t=6NQra4uE9oLKkthr-4) — fileKey `rMcDm5qGp4CXkXXddEbcMh`, API key `rMcDm5qGp4CXkXXddEbcMh`, node `38937:15264`, type `COMPONENT_SET`.
<!-- FIGMA_SYNC:END -->
