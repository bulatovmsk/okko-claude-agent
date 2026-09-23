# Okko DS — контекст для Figma Agent

Используй этот файл как импортированную snapshot-карту библиотек, lifecycle и известных компонентов. Figma-ссылки актуальны на дату сборки. Относительные ссылки на карточки компонентов в таблице нужны только как идентификаторы и могут не открываться внутри Figma.

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
| `Featured - Main` | `ios` | `lib-ios` | `ready` | [`featured-main`](../components/featured-main.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=13093-106907&t=6NQra4uE9oLKkthr-4) |
| `Featured - Meta` | `ios` | `lib-ios` | `ready` | [`featured-meta`](../components/featured-meta.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=40306-47681&t=6NQra4uE9oLKkthr-4) |
| `Grid / Circle Zvuk` | `ios` | `lib-ios` | `ready` | [`grid-circle-zvuk`](../components/grid-circle-zvuk.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=38370-38407) |
| `Grid / Content` | `ios` | `lib-ios` | `ready` | [`grid-content`](../components/grid-content.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=38566-83080) |
| `Grid / Large` | `ios` | `lib-ios` | `ready` | [`grid-large`](../components/grid-large.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=38573-88598) |
| `Grid / Main` | `ios` | `lib-ios` | `ready` | [`grid-main`](../components/grid-main.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=38564-73131) |
| `Grid / Person` | `ios` | `lib-ios` | `ready` | [`grid-person`](../components/grid-person.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=23272-59082) |
| `Grid / Square` | `ios` | `lib-ios` | `ready` | [`grid-square`](../components/grid-square.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=21878-59446) |
| `Grid / Ticket` | `ios` | `lib-ios` | `ready` | [`grid-ticket`](../components/grid-ticket.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=28139-209869) |
| `Grid / Vertical` | `ios` | `lib-ios` | `ready` | [`grid-vertical`](../components/grid-vertical.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=38575-90604) |
| `Text input` | `ios` | `lib-ios` | `ready` | [`input`](../components/input.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=12510-97334&t=6NQra4uE9oLKkthr-4) |
| `Label : Large` | `ios` | `lib-ios` | `ready` | [`label-large`](../components/label-large.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=12185-97166&t=6NQra4uE9oLKkthr-4) |
| `Label : Small` | `ios` | `lib-ios` | `ready` | [`label-small`](../components/label-small.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=12185-97090&t=6NQra4uE9oLKkthr-4) |
| `Layouts` | `ios` | `lib-ios` | `ready` | [`layouts-ios`](../components/layouts-ios.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=32942-50025) |
| `🟡 List Item V2` | `ios` | `lib-ios` | `work-in-progress` | [`list-item-v2`](../components/list-item-v2.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=36507-21672&t=6NQra4uE9oLKkthr-4) |
| `Navbar` | `ios` | `lib-ios` | `ready` | [`navbar`](../components/navbar.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=12978-100799&t=6NQra4uE9oLKkthr-4) |
| `Onboarding Bubble` | `ios` | `lib-ios` | `ready` | [`onboarding-bubble`](../components/onboarding-bubble.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=32634-7164&t=6NQra4uE9oLKkthr-4) |
| `Radio button` | `ios` | `lib-ios` | `ready` | [`radio-button`](../components/radio-button.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=14447-113928&t=6NQra4uE9oLKkthr-4) |
| ` Rail - Announces` | `ios` | `lib-ios` | `ready` | [`rail-announces`](../components/rail-announces.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=30646-111294) |
| `Rail - Background` | `ios` | `lib-ios` | `ready` | [`rail-background`](../components/rail-background.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=6721-53275) |
| `Rail - Base` | `ios` | `lib-ios` | `ready` | [`rail-base`](../components/rail-base.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=29595-53875) |
| `Rail  - 🟡Catalog [Нет в проде]` | `ios` | `lib-ios` | `work-in-progress` | [`rail-catalog`](../components/rail-catalog.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=15586-192048) |
| `Rail - Circle` | `ios` | `lib-ios` | `ready` | [`rail-circle`](../components/rail-circle.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=32668-60746) |
| `Rail - 🟡Content [Нет в проде]` | `ios` | `lib-ios` | `work-in-progress` | [`rail-content`](../components/rail-content.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=25931-80240) |
| `Rail - Continue` | `ios` | `lib-ios` | `ready` | [`rail-continue`](../components/rail-continue.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=15462-313281) |
| `Rail - Highlights` | `ios` | `lib-ios` | `ready` | [`rail-highlights`](../components/rail-highlights.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=30477-83196) |
| `Rail - Large` | `ios` | `lib-ios` | `ready` | [`rail-large`](../components/rail-large.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=15462-375550) |
| `Rail - Main` | `ios` | `lib-ios` | `ready` | [`rail-main`](../components/rail-main.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=5988-42272) |
| `Rail - Marketing` | `ios` | `lib-ios` | `ready` | [`rail-marketing`](../components/rail-marketing.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=23009-43824) |
| `Rail - Medium` | `ios` | `lib-ios` | `ready` | [`rail-medium`](../components/rail-medium.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=24049-48738) |
| `Rail / Mixed Top` | `ios` | `lib-ios` | `ready` | [`rail-mixed-top`](../components/rail-mixed-top.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=26610-73027) |
| `Rail - Person Horizontal` | `ios` | `lib-ios` | `ready` | [`rail-person-horizontal`](../components/rail-person-horizontal.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=23197-42884) |
| `Rail - Personal Widget` | `ios` | `lib-ios` | `ready` | [`rail-personal-widget`](../components/rail-personal-widget.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=31185-161182) |
| `Rail - Square` | `ios` | `lib-ios` | `ready` | [`rail-square`](../components/rail-square.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=7768-73596) |
| `Rail - 🟡Square Medium` | `ios` | `lib-ios` | `work-in-progress` | [`rail-square-medium`](../components/rail-square-medium.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=35893-32643) |
| `Rail - SquareSmall1Story` | `ios` | `lib-ios` | `ready` | [`rail-square-small-1-story`](../components/rail-square-small-1-story.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=16941-129762) |
| `Rail - SquareSmall2Story` | `ios` | `lib-ios` | `ready` | [`rail-square-small-2-story`](../components/rail-square-small-2-story.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=7616-73598) |
| `Rail - Ticket` | `ios` | `lib-ios` | `ready` | [`rail-ticket`](../components/rail-ticket.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=28139-194880) |
| `Rail / Top Collections` | `ios` | `lib-ios` | `ready` | [`rail-top-collections`](../components/rail-top-collections.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=26610-66862) |
| `Rail / Top Titles` | `ios` | `lib-ios` | `ready` | [`rail-top-titles`](../components/rail-top-titles.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=26610-28243) |
| `Rail / Tracks` | `ios` | `lib-ios` | `ready` | [`rail-tracks`](../components/rail-tracks.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=41694-34904) |
| `Rail - Vertical` | `ios` | `lib-ios` | `ready` | [`rail-vertical`](../components/rail-vertical.md) | [node](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=15462-365012) |
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
