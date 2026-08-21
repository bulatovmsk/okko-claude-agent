# Okko DS agent context

> Сгенерировано из `design-system/`. Не редактировать вручную.

## Lifecycle

| Статус | Маркер | Автоматическое использование | Значение |
|---|---|---|---|
| `planned` | ⚪ | нет | Запланирован на ближайшие кварталы, но ещё не находится в работе. |
| `work-in-progress` | 🟡 | нет | Находится в активной работе и доступен только для явно запрошенных тестов. |
| `design-only` | 🔵 | нет | Готов для макетов в Figma, но ещё не реализован в продукте. |
| `ready` | 🟢 | да | Готов в дизайне и доступен в продуктовой реализации. |
| `deprecated` | 🔴 | нет | Выведен из использования; нужна замена или зафиксированный gap. |

## Библиотеки

| ID | Название | Платформы | Статус | Зависимости |
|---|---|---|---|---|
| `okko-head` | Okko Head Library | android, ios, tv, web | `active` | — |
| `tokens-mobile-web` | Tokens [mobile & web] | android, ios, web | `active` | — |
| `tokens-tv` | Tokens [tv] | tv | `active` | — |
| `lib-android` | Lib-Android | android | `pending-source` | okko-head, tokens-mobile-web |
| `lib-ios` | Lib-iOS | ios | `active` | okko-head, tokens-mobile-web |
| `lib-tv` | Lib-TV | tv | `active` | okko-head, tokens-tv |
| `lib-web` | Lib-Web | web | `pending-source` | okko-head, tokens-mobile-web |

## Компоненты

| Компонент | Платформа | Библиотека | Lifecycle | Карточка | Figma |
|---|---|---|---|---|---|
| `AI Button` | `ios` | `lib-ios` | `ready` | [`ai-button`](../components/ai-button.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=30946-883&t=6NQra4uE9oLKkthr-4) |
| `Bet Button` | `ios` | `lib-ios` | `ready` | [`bet-button`](../components/bet-button.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=22908-9507&t=6NQra4uE9oLKkthr-4) |
| `🟢Sheet Native` | `ios` | `lib-ios` | `ready` | [`bottom-sheet-native`](../components/bottom-sheet-native.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=37371-7396&t=6NQra4uE9oLKkthr-4) |
| `Button` | `ios` | `lib-ios` | `ready` | [`button`](../components/button.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=31182-4417&t=6NQra4uE9oLKkthr-4) |
| `Button - Toggle` | `ios` | `lib-ios` | `ready` | [`button-toggle`](../components/button-toggle.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=31182-4838&t=6NQra4uE9oLKkthr-4) |
| `Checkbox` | `ios` | `lib-ios` | `ready` | [`checkbox`](../components/checkbox.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=14447-113935&t=6NQra4uE9oLKkthr-4) |
| `Chips` | `ios` | `lib-ios` | `ready` | [`chips`](../components/chips.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=34254-8865&t=6NQra4uE9oLKkthr-4) |
| `Error - Fulscreen` | `ios` | `lib-ios` | `ready` | [`error-fullscreen`](../components/error-fullscreen.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=40967-4323&t=6NQra4uE9oLKkthr-4) |
| `Error - Sheet` | `ios` | `lib-ios` | `ready` | [`error-sheet`](../components/error-sheet.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=40954-1419&t=6NQra4uE9oLKkthr-4) |
| `Error - View` | `ios` | `lib-ios` | `ready` | [`error-view`](../components/error-view.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=22536-7360&t=6NQra4uE9oLKkthr-4) |
| `Text input` | `ios` | `lib-ios` | `ready` | [`input`](../components/input.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=12510-97334&t=6NQra4uE9oLKkthr-4) |
| `Label : Large` | `ios` | `lib-ios` | `ready` | [`label-large`](../components/label-large.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=12185-97166&t=6NQra4uE9oLKkthr-4) |
| `Label : Small` | `ios` | `lib-ios` | `ready` | [`label-small`](../components/label-small.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=12185-97090&t=6NQra4uE9oLKkthr-4) |
| `Layouts` | `ios` | `lib-ios` | `ready` | [`layouts-ios`](../components/layouts-ios.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=32942-50025) |
| `🟡 List Item V2` | `ios` | `lib-ios` | `work-in-progress` | [`list-item-v2`](../components/list-item-v2.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=36507-21672&t=6NQra4uE9oLKkthr-4) |
| `Navbar` | `ios` | `lib-ios` | `ready` | [`navbar`](../components/navbar.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=12978-100799&t=6NQra4uE9oLKkthr-4) |
| `Onboarding Bubble` | `ios` | `lib-ios` | `ready` | [`onboarding-bubble`](../components/onboarding-bubble.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=32634-7164&t=6NQra4uE9oLKkthr-4) |
| `Radio button` | `ios` | `lib-ios` | `ready` | [`radio-button`](../components/radio-button.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=14447-113928&t=6NQra4uE9oLKkthr-4) |
| `Select` | `ios` | `lib-ios` | `ready` | [`select`](../components/select.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=34884-24858&t=6NQra4uE9oLKkthr-4) |
| `Шаблоны шторки / Фильтры` | `ios` | `lib-ios` | `ready` | [`sheet-template-filters`](../components/sheet-template-filters.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/branch/jdBqhypltqMzx0mXE7uw94/Lib-iOS?node-id=37390-49620) |
| `Snackbar` | `ios` | `lib-ios` | `ready` | [`snackbar`](../components/snackbar.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=13712-111074&t=6NQra4uE9oLKkthr-4) |
| `Switch` | `ios` | `lib-ios` | `ready` | [`switch`](../components/switch.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=14447-113942&t=6NQra4uE9oLKkthr-4) |
| `Symbol input` | `ios` | `lib-ios` | `ready` | [`symbol-input`](../components/symbol-input.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=12514-97868&t=6NQra4uE9oLKkthr-4) |
| `TabNavigation` | `ios` | `lib-ios` | `ready` | [`tab-navigation`](../components/tab-navigation.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=24687-2182&t=6NQra4uE9oLKkthr-4) |
| `Tabbar - Meta` | `ios` | `lib-ios` | `ready` | [`tabbar-meta`](../components/tabbar-meta.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=38937-15264&t=6NQra4uE9oLKkthr-4) |
| `TabGroup` | `ios` | `lib-ios` | `ready` | [`tabgroup`](../components/tabgroup.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=24233-1389&t=6NQra4uE9oLKkthr-4) |
| `Tabgroup - Item` | `ios` | `lib-ios` | `ready` | [`tabgroup-item`](../components/tabgroup-item.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=24233-1463&t=6NQra4uE9oLKkthr-4) |

## Подтверждённые платформенные mappings

Подтверждённых mappings пока нет.

## Подтверждённые кейсы

Подтверждённых кейсов пока нет.

## Открытые gaps

Открытых gaps пока нет.

## Детальные источники

- Платформенные правила: `design-system/platforms/`.
- Snapshot токенов: `design-system/tokens/`; актуальные значения проверять в Tokens Studio Git.
- Полные карточки компонентов: `design-system/components/`.
