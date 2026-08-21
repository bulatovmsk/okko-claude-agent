# Layouts

## Назначение

Набор базовых iOS-шаблонов для начала работы над новым экраном. Каждый Layout
уже имеет размер выбранного устройства, адаптивную сетку, безопасные зоны и
структурные элементы интерфейса.

## Когда использовать

- Как основу каждого нового экрана iOS.
- Когда нужен согласованный размер iPhone или iPad без ручной настройки фрейма.
- Для единых боковых отступов, выравнивания и структуры колонок.

Порядок работы из гайда: открыть `Assets` → `Lib iOS` → `Layouts`, перетащить
нужный Layout в макет, сделать detach и собирать экран дальше.

## Когда НЕ использовать

- Не начинать целевой экран с произвольного пустого фрейма, если для устройства
  есть готовый Layout.
- Не считать колонки жёстким каркасом контента: в гайде они названы
  вспомогательным ориентиром; основная практическая функция сетки — соблюдение
  боковых отступов.
- Не включать optional-пресеты в обязательный набор проверок без требования
  конкретного проекта.

## Платформенные особенности iOS

### Поддерживаемые устройства

| Устройство | Ориентация | Размер | Статус |
|---|---|---:|---|
| iPhone 13 mini | Portrait | 375×812 | Optional |
| iPhone 15 | Portrait | 393×852 | Основной |
| iPhone 17 Pro Max | Portrait | 440×956 | Основной |
| iPad Mini 6 | Landscape | 1133×744 | Optional |
| iPad Mini 6 | Portrait | 744×1133 | Optional |
| iPad 10 | Landscape | 1180×820 | Основной |
| iPad 10 | Portrait | 820×1180 | Основной |
| iPad Pro 13 | Landscape | 1376×1032 | Основной |
| iPad Pro 13 | Portrait | 1032×1376 | Основной |

### Встроенные элементы

- Адаптивная сетка с едиными отступами, выравниванием и гибкой структурой колонок.
- `Status Bar`, настроенный под конкретное устройство и тип выреза; по умолчанию скрыт.
- `Home Indicator`, соответствующий устройству; по умолчанию скрыт.
- `Tabbar - Main` и `Navbar` для сборки целевых экранов.
- Публичные boolean-свойства: `Status Bar`, `Home Indicator`, `Tabbar`, `Navigation Bar`.

> ⚠️ В живой ноде `Layout - iPad 10 Portrait` опубликованы только первые три
> свойства: публичный `Navigation Bar` отсутствует, хотя инстанс `Navbar` внутри
> компонента есть. Перед использованием этого переключателя компонент нужно
> перепроверить в Figma.

## Преимущества

- Единообразие отступов и пропорций между макетами.
- Не нужно повторно настраивать основу каждого экрана.
- Корректное размещение контента относительно безопасных зон устройства.

## Связанные компоненты

- `Status Bar` — системная верхняя область.
- `Home Indicator` — системная нижняя область.
- `Navbar` — верхняя навигация продукта.
- `Tabbar - Main` — основная нижняя навигация.

<!-- FIGMA_SYNC:START -->
## Актуальные данные Figma

> Последняя проверка: `2026-08-21T15:14:53Z` · структура `336905246dd9` · коллекция из **9** компонентов.

### Layout-компоненты

| Компонент | Размер | Свойства | nodeId |
|---|---:|---|---|
| [Layout - iPad 10 Landscape](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=32942-62171) | `1180×820` | Home Indicator, Navigation Bar, Status Bar, Tabbar | `32942:62171` |
| [Layout - iPad 10 Portrait](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=32942-62169) | `820×1180` | Home Indicator, Status Bar, Tabbar | `32942:62169` |
| [Layout - iPad Mini 6 Landscape (Optional)](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=32942-62172) | `1133×744` | Home Indicator, Navigation Bar, Status Bar, Tabbar | `32942:62172` |
| [Layout - iPad Mini 6 Portrait (Optional)](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=32942-62168) | `744×1133` | Home Indicator, Navigation Bar, Status Bar, Tabbar | `32942:62168` |
| [Layout - iPad Pro 13 Landscape](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=32942-62170) | `1376×1032` | Home Indicator, Navigation Bar, Status Bar, Tabbar | `32942:62170` |
| [Layout - iPad Pro 13 Portrait](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=32942-62167) | `1032×1376` | Home Indicator, Navigation Bar, Status Bar, Tabbar | `32942:62167` |
| [Layout - iPhone 13 mini (Optional)](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=32942-62173) | `375×812` | Home Indicator, Navigation Bar, Status Bar, Tabbar | `32942:62173` |
| [Layout - iPhone 15](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=32942-62175) | `393×852` | Home Indicator, Navigation Bar, Status Bar, Tabbar | `32942:62175` |
| [Layout - iPhone 17 Pro Max](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=32942-62174) | `440×956` | Home Indicator, Navigation Bar, Status Bar, Tabbar | `32942:62174` |

### Встроенные элементы

- `Home Indicator`
- `Navbar`
- `Status Bar`
- `Tabbar - Main`

### Источники

- [Layouts](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=32942-50025) — fileKey `rMcDm5qGp4CXkXXddEbcMh`, API key `rMcDm5qGp4CXkXXddEbcMh`, node `32942:50025`, type `CANVAS`.
- [Component guide_Layout](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=33005-119053) — `guide`, node `33005:119053`.
<!-- FIGMA_SYNC:END -->
