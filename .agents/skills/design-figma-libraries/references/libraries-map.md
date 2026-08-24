# Карта Figma-библиотек ДС Окко

Карта ключевых nodeId и подробностей библиотек. Машиночитаемый состав, статус и зависимости библиотек находятся в [`registry/libraries.json`](registry/libraries.json).

## Библиотеки

### Lib-iOS (основная iOS-библиотека компонентов)

| Параметр | Значение |
|---|---|
| fileKey | `rMcDm5qGp4CXkXXddEbcMh` |
| URL | https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS |
| Активный бранч (рабочий) | `jdBqhypltqMzx0mXE7uw94` (используется как fileKey в API) |
| Платформа | iOS (используется и как референс для остальных) |
| Зависит от | Okko Head Library (цвета, иконки, иллюстрации) |

**Ключевые страницы / nodeId:**

| Назначение | nodeId |
|---|---|
| Страница `Filters` (где собран наш `Filters Guide`) | `18885:4305` |
| Страница `📄 Doc Template (Draft)` (модульные секции документации) | `39407:77` |
| `Page 60` (демо-сборки гайдов) | `39408:13691` |
| Готовый `Filters Guide` (бранч) | `39542:1003` |

**Компоненты группы Filters:**

| Компонент | nodeId |
|---|---|
| `Chips` COMPONENT_SET | `34254:8865` |
| `Select` COMPONENT_SET | `34884:24858` |
| `🟢Sheet Native` COMPONENT_SET | `37371:7396` |
| `Шаблоны шторки / Фильтры` COMPONENT_SET | `37390:49620` |

**Канонические гайды компонентов (эталоны для design-doc-writer):**

| Гайд | nodeId | Статус |
|---|---|---|
| `Component guide_Chips` | `39348:13491` | ⭐ канонический эталон (самый свежий) |
| `Component guide_Select` | `39484:30540` | канонический эталон |
| `Component guide_Button` | `31214:29705` | эталон |
| `Component guide_BottomSheet` | `28934:239837` | эталон |
| `Component guide_TabGroup` | `24233:7754` | эталон |

**Doc/Section/* компоненты-секции** (страница `39407:77`):

| Секция | nodeId |
|---|---|
| `Doc/Section/Header` | `39417:82` |
| `Doc/Section/When` | `39417:122` |
| `Doc/Section/NotWhen` | `39417:148` |
| `Doc/Section/Properties` | `39417:173` |
| `Doc/Section/Variants` | `39419:138` |
| `Doc/Section/Sizes` | `39419:169` |
| `Doc/Section/States` | `39416:92` |
| `Doc/Section/Anatomy` | `39419:102` |
| `Doc/Section/DoDont` | `39419:209` |
| `Doc/Section/Application` | `39419:234` |

**Родные компоненты для оформления:**

| Компонент | nodeId | Применение |
|---|---|---|
| `Title` (S) | `28934:245762` | Шапка секции (Header + Description) |
| `Title` (xs) | `28934:245764` | Подзаголовок секции |
| `Pointer` | `31182:2801` | Аннотация-указатель к анатомии |

---

### Okko Head Library (shared assets — цвета, иконки, иллюстрации)

| Параметр | Значение |
|---|---|
| fileKey | `HYB1u9ysALVWtVWKoagiDH` |
| URL | https://www.figma.com/design/HYB1u9ysALVWtVWKoagiDH |
| Назначение | Общая для всех платформ — цвета, иконки Main Pack, иллюстрации |
| Используется в | Lib-iOS и (предположительно) платформенных библиотеках Android / TV / Web |

**Ключевые ноды:**

| Раздел | nodeId | Локальный кэш |
|---|---|---|
| Цвета (Primitives + Semantic + Brand) | `32102:23344` | [`design-system/tokens/colors.md`](../../../../design-system/tokens/colors.md) |
| Иконки Main Pack (490 шт., 16 категорий, 24×24) | `29361:322` | [`design-system/components/icons.md`](../../../../design-system/components/icons.md) |
| Иллюстрации · Static (Loader, Age Mark 0+…18+, Devices) | `39089:10560` | [`design-system/components/illustrations.md`](../../../../design-system/components/illustrations.md) |
| Иллюстрации · Product images (плейсхолдеры) | `39101:215` | там же |
| Иллюстрации · Bobokko (маскот, 41 поза) | `39104:349` | там же |

> **Variables API:** для resolved-цветов semantic-токенов использовать MCP `get_variable_defs(nodeId='32102:23344', fileKey='HYB1u9ysALVWtVWKoagiDH')` — REST `/variables/local` отдаёт 403 без Enterprise scope.

---

### 🦖 Tokens [mobile & web]  (системные токены spacing / corner-radius / typography)

| Параметр | Значение |
|---|---|
| fileKey | `vztN8doGwBZOCbpDf2PhKR` |
| URL | https://www.figma.com/design/vztN8doGwBZOCbpDf2PhKR/%F0%9F%A6%96-Tokens--mobile---web- |
| Назначение | Числовые токены (NUMBER variables) для spacing/corner-radius + текстовые стили (145 шт.) для mobile и web. Edge-кейсы: `Mobile 0+/320+/375+`, `Tablet 600+`, `Desktop 1320+/1720+`, `iPhone SE/iPhone/iPad`, `Android Mobile/Tablet`. |
| Используется в | Lib-iOS + (через моды) платформенные библиотеки Android / Web |

**Ключевые страницы:**

| Назначение | nodeId | Локальный кэш |
|---|---|---|
| Text Styles (145 TEXT-стилей) | `3:9` | [`design-system/tokens/typography.md`](../../../../design-system/tokens/typography.md) |
| Spacing (22 рампа + 8 screen-padding) | `2280:155798` | [`design-system/tokens/spacing.md`](../../../../design-system/tokens/spacing.md) |
| Corner-radius (11 + `round`) | `2287:157374` | [`design-system/tokens/corner-radius.md`](../../../../design-system/tokens/corner-radius.md) |
| Changelog (история изменений) | `4583:9689` | — |

> **NUMBER variables** (spacing/corner-radius) лежат в одной коллекции **`Semantic`** с модой `Web&Mobile` (одно значение на web и mobile — брейкпоинты учитываются через TEXT-стили). REST `/variables/local` отдаёт 403 — забираем через Plugin API в `use_figma`.

---

### 🦍 Tokens [tv]  (системные токены для TV: spacing / corner-radius / typography)

| Параметр | Значение |
|---|---|
| fileKey | `Zn2JrOHhSURjCuUEp6JcI8` |
| URL | https://www.figma.com/design/Zn2JrOHhSURjCuUEp6JcI8 |
| Назначение | Системные токены для Smart TV / Android TV (1920×1080): 24 spacing-токена + 2 screen-padding + 31 corner-radius (16 regular + 15 focus) + 30 published TEXT-стилей. |
| Используется в | Lib-TV (`Q3DVcDJnhMCtpdQAUoDPrp`) |

**Ключевые страницы:**

| Назначение | nodeId | Локальный кэш |
|---|---|---|
| Text Styles (30 published TEXT-стилей: H1/H2/H3, Body 1–4, Button, Label, Others) | `0:1` | [`design-system/tokens/typography-tv.md`](../../../../design-system/tokens/typography-tv.md) |
| Spacing (24 token + 2 screen-padding) | `857:2088` (+ Guide `859:2964`) | [`design-system/tokens/spacing-tv.md`](../../../../design-system/tokens/spacing-tv.md) |
| Corner-radius regular (16 токенов) | `859:3226` | [`design-system/tokens/corner-radius-tv.md`](../../../../design-system/tokens/corner-radius-tv.md) |
| Corner-radius focus (15 токенов, outline при наведении пультом) | `3143:465` | там же |
| Changelog | `3123:2137` | — |

> **NUMBER variables** (spacing/corner-radius) лежат в коллекции **`Semantic`** с единственным модом **`TV`**. REST `/variables/local` → 403 — забираем через Plugin API в `use_figma` (`__NUMBER_VARDEFS_DUMP_TV__`).
>
> **Focus-radius** — TV-специфика: outline при навигации пультом. Значение `corner-radius/focus/X` = `corner-radius/X` + 6px (компенсация толщины контура).

---

### Lib-TV (платформенная библиотека компонентов для Smart TV / Android TV)

| Параметр | Значение |
|---|---|
| fileKey | `Q3DVcDJnhMCtpdQAUoDPrp` |
| URL | https://www.figma.com/design/Q3DVcDJnhMCtpdQAUoDPrp/Lib-TV |
| Платформа | Smart TV (webOS, Tizen) + Android TV, разрешение 1920×1080 |
| Зависит от | 🦍 Tokens [tv] (системные токены) + Okko Head Library (цвета, иконки, иллюстрации) |

**Ключевые гайд-страницы:**

| Назначение | nodeId | Что там |
|---|---|---|
| Grid & Safezones & Spacing | `12902:105094` | **Гайд-описание правил** (модуль 8px, safe-zones 102/78/60). Не источник токенов — для понимания правил. Сами токены — в 🦍 Tokens [tv]. |
| Текстовые блоки 🦍 | `6943:28698` | Композитные блоки (h1+body, h2+body…) — примеры применения TEXT-стилей |

---

### Lib-Android, Lib-Web — ожидают подтверждения источника

| Библиотека | fileKey | Статус |
|---|---|---|
| Lib-Android | — | `pending-source` |
| Lib-Web | — | `pending-source` |

---

## Машиночитаемый реестр компонентов

Блок генерируется из `design-system/components/figma-sources.json`. Значение
`API fileKey` равно `branchKey` для ссылок на рабочую ветку.

<!-- FIGMA_COMPONENT_REGISTRY:START -->
| Компонент | API fileKey | nodeId | Статус | Карточка | Проверено |
|---|---|---|---|---|---|
| [AI Button](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=30946-883&t=6NQra4uE9oLKkthr-4) | `rMcDm5qGp4CXkXXddEbcMh` | `30946:883` | `ready` | [`ai-button.md`](../../../../design-system/components/ai-button.md) | `2026-08-21T15:17:25Z` |
| [Bet Button](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=22908-9507&t=6NQra4uE9oLKkthr-4) | `rMcDm5qGp4CXkXXddEbcMh` | `22908:9507` | `ready` | [`bet-button.md`](../../../../design-system/components/bet-button.md) | `2026-08-21T15:30:16Z` |
| [🟢Sheet Native](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=37371-7396&t=6NQra4uE9oLKkthr-4) | `rMcDm5qGp4CXkXXddEbcMh` | `37371:7396` | `ready` | [`bottom-sheet-native.md`](../../../../design-system/components/bottom-sheet-native.md) | `2026-08-21T15:20:10Z` |
| [Button](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=31182-4417&t=6NQra4uE9oLKkthr-4) | `rMcDm5qGp4CXkXXddEbcMh` | `31182:4417` | `ready` | [`button.md`](../../../../design-system/components/button.md) | `2026-08-21T15:22:52Z` |
| [Button - Toggle](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=31182-4838&t=6NQra4uE9oLKkthr-4) | `rMcDm5qGp4CXkXXddEbcMh` | `31182:4838` | `ready` | [`button-toggle.md`](../../../../design-system/components/button-toggle.md) | `2026-08-21T15:27:50Z` |
| [Checkbox](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=14447-113935&t=6NQra4uE9oLKkthr-4) | `rMcDm5qGp4CXkXXddEbcMh` | `14447:113935` | `ready` | [`checkbox.md`](../../../../design-system/components/checkbox.md) | `2026-08-21T15:32:19Z` |
| [Chips](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=34254-8865&t=6NQra4uE9oLKkthr-4) | `rMcDm5qGp4CXkXXddEbcMh` | `34254:8865` | `ready` | [`chips.md`](../../../../design-system/components/chips.md) | `2026-08-21T16:07:30Z` |
| [Error - Fulscreen](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=40967-4323&t=6NQra4uE9oLKkthr-4) | `rMcDm5qGp4CXkXXddEbcMh` | `40967:4323` | `ready` | [`error-fullscreen.md`](../../../../design-system/components/error-fullscreen.md) | `2026-08-21T15:44:33Z` |
| [Error - Sheet](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=40954-1419&t=6NQra4uE9oLKkthr-4) | `rMcDm5qGp4CXkXXddEbcMh` | `40954:1419` | `ready` | [`error-sheet.md`](../../../../design-system/components/error-sheet.md) | `2026-08-21T15:41:13Z` |
| [Error - View](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=22536-7360&t=6NQra4uE9oLKkthr-4) | `rMcDm5qGp4CXkXXddEbcMh` | `22536:7360` | `ready` | [`error-view.md`](../../../../design-system/components/error-view.md) | `2026-08-21T15:38:37Z` |
| [Featured - Main](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=13093-106907&t=6NQra4uE9oLKkthr-4) | `rMcDm5qGp4CXkXXddEbcMh` | `13093:106907` | `ready` | [`featured-main.md`](../../../../design-system/components/featured-main.md) | `2026-08-24T08:32:29Z` |
| [Featured - Meta](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=40306-47681&t=6NQra4uE9oLKkthr-4) | `rMcDm5qGp4CXkXXddEbcMh` | `40306:47681` | `ready` | [`featured-meta.md`](../../../../design-system/components/featured-meta.md) | `2026-08-24T08:27:22Z` |
| [Grid / Circle Zvuk](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=38370-38407) | `rMcDm5qGp4CXkXXddEbcMh` | `38370:38407` | `ready` | [`grid-circle-zvuk.md`](../../../../design-system/components/grid-circle-zvuk.md) | `2026-08-24T14:23:13Z` |
| [Grid / Content](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=38566-83080) | `rMcDm5qGp4CXkXXddEbcMh` | `38566:83080` | `ready` | [`grid-content.md`](../../../../design-system/components/grid-content.md) | `2026-08-24T14:23:14Z` |
| [Grid / Large](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=38573-88598) | `rMcDm5qGp4CXkXXddEbcMh` | `38573:88598` | `ready` | [`grid-large.md`](../../../../design-system/components/grid-large.md) | `2026-08-24T14:23:14Z` |
| [Grid / Main](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=38564-73131) | `rMcDm5qGp4CXkXXddEbcMh` | `38564:73131` | `ready` | [`grid-main.md`](../../../../design-system/components/grid-main.md) | `2026-08-24T14:23:13Z` |
| [Grid / Person](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=23272-59082) | `rMcDm5qGp4CXkXXddEbcMh` | `23272:59082` | `ready` | [`grid-person.md`](../../../../design-system/components/grid-person.md) | `2026-08-24T14:23:13Z` |
| [Grid / Square](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=21878-59446) | `rMcDm5qGp4CXkXXddEbcMh` | `21878:59446` | `ready` | [`grid-square.md`](../../../../design-system/components/grid-square.md) | `2026-08-24T14:23:14Z` |
| [Grid / Ticket](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=28139-209869) | `rMcDm5qGp4CXkXXddEbcMh` | `28139:209869` | `ready` | [`grid-ticket.md`](../../../../design-system/components/grid-ticket.md) | `2026-08-24T14:23:13Z` |
| [Grid / Vertical](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=38575-90604) | `rMcDm5qGp4CXkXXddEbcMh` | `38575:90604` | `ready` | [`grid-vertical.md`](../../../../design-system/components/grid-vertical.md) | `2026-08-24T14:23:13Z` |
| [Text input](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=12510-97334&t=6NQra4uE9oLKkthr-4) | `rMcDm5qGp4CXkXXddEbcMh` | `12510:97334` | `ready` | [`input.md`](../../../../design-system/components/input.md) | `2026-08-21T15:55:31Z` |
| [Label : Large](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=12185-97166&t=6NQra4uE9oLKkthr-4) | `rMcDm5qGp4CXkXXddEbcMh` | `12185:97166` | `ready` | [`label-large.md`](../../../../design-system/components/label-large.md) | `2026-08-21T16:01:51Z` |
| [Label : Small](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=12185-97090&t=6NQra4uE9oLKkthr-4) | `rMcDm5qGp4CXkXXddEbcMh` | `12185:97090` | `ready` | [`label-small.md`](../../../../design-system/components/label-small.md) | `2026-08-21T16:01:52Z` |
| [🟡 List Item V2](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=36507-21672&t=6NQra4uE9oLKkthr-4) | `rMcDm5qGp4CXkXXddEbcMh` | `36507:21672` | `work-in-progress` | [`list-item-v2.md`](../../../../design-system/components/list-item-v2.md) | `2026-08-21T16:04:40Z` |
| [Navbar](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=12978-100799&t=6NQra4uE9oLKkthr-4) | `rMcDm5qGp4CXkXXddEbcMh` | `12978:100799` | `ready` | [`navbar.md`](../../../../design-system/components/navbar.md) | `2026-08-21T15:50:49Z` |
| [Onboarding Bubble](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=32634-7164&t=6NQra4uE9oLKkthr-4) | `rMcDm5qGp4CXkXXddEbcMh` | `32634:7164` | `ready` | [`onboarding-bubble.md`](../../../../design-system/components/onboarding-bubble.md) | `2026-08-21T15:46:56Z` |
| [Radio button](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=14447-113928&t=6NQra4uE9oLKkthr-4) | `rMcDm5qGp4CXkXXddEbcMh` | `14447:113928` | `ready` | [`radio-button.md`](../../../../design-system/components/radio-button.md) | `2026-08-21T15:34:05Z` |
| [ Rail - Announces](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=30646-111294) | `rMcDm5qGp4CXkXXddEbcMh` | `30646:111294` | `ready` | [`rail-announces.md`](../../../../design-system/components/rail-announces.md) | `2026-08-24T08:12:19Z` |
| [Rail - Background](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=6721-53275) | `rMcDm5qGp4CXkXXddEbcMh` | `6721:53275` | `ready` | [`rail-background.md`](../../../../design-system/components/rail-background.md) | `2026-08-24T08:12:19Z` |
| [Rail - Base](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=29595-53875) | `rMcDm5qGp4CXkXXddEbcMh` | `29595:53875` | `ready` | [`rail-base.md`](../../../../design-system/components/rail-base.md) | `2026-08-24T08:12:20Z` |
| [Rail  - 🟡Catalog [Нет в проде]](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=15586-192048) | `rMcDm5qGp4CXkXXddEbcMh` | `15586:192048` | `work-in-progress` | [`rail-catalog.md`](../../../../design-system/components/rail-catalog.md) | `2026-08-24T08:12:19Z` |
| [Rail - Circle](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=32668-60746) | `rMcDm5qGp4CXkXXddEbcMh` | `32668:60746` | `ready` | [`rail-circle.md`](../../../../design-system/components/rail-circle.md) | `2026-08-24T08:12:20Z` |
| [Rail - 🟡Content [Нет в проде]](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=25931-80240) | `rMcDm5qGp4CXkXXddEbcMh` | `25931:80240` | `work-in-progress` | [`rail-content.md`](../../../../design-system/components/rail-content.md) | `2026-08-24T08:12:21Z` |
| [Rail - Continue](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=15462-313281) | `rMcDm5qGp4CXkXXddEbcMh` | `15462:313281` | `ready` | [`rail-continue.md`](../../../../design-system/components/rail-continue.md) | `2026-08-24T08:12:20Z` |
| [Rail - Highlights](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=30477-83196) | `rMcDm5qGp4CXkXXddEbcMh` | `30477:83196` | `ready` | [`rail-highlights.md`](../../../../design-system/components/rail-highlights.md) | `2026-08-24T08:12:20Z` |
| [Rail - Large](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=15462-375550) | `rMcDm5qGp4CXkXXddEbcMh` | `15462:375550` | `ready` | [`rail-large.md`](../../../../design-system/components/rail-large.md) | `2026-08-24T08:12:20Z` |
| [Rail - Main](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=5988-42272) | `rMcDm5qGp4CXkXXddEbcMh` | `5988:42272` | `ready` | [`rail-main.md`](../../../../design-system/components/rail-main.md) | `2026-08-24T08:12:20Z` |
| [Rail - Marketing](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=23009-43824) | `rMcDm5qGp4CXkXXddEbcMh` | `23009:43824` | `ready` | [`rail-marketing.md`](../../../../design-system/components/rail-marketing.md) | `2026-08-24T08:12:20Z` |
| [Rail - Medium](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=24049-48738) | `rMcDm5qGp4CXkXXddEbcMh` | `24049:48738` | `ready` | [`rail-medium.md`](../../../../design-system/components/rail-medium.md) | `2026-08-24T08:12:20Z` |
| [Rail / Mixed Top](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=26610-73027) | `rMcDm5qGp4CXkXXddEbcMh` | `26610:73027` | `ready` | [`rail-mixed-top.md`](../../../../design-system/components/rail-mixed-top.md) | `2026-08-24T07:55:33Z` |
| [Rail - Person Horizontal](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=23197-42884) | `rMcDm5qGp4CXkXXddEbcMh` | `23197:42884` | `ready` | [`rail-person-horizontal.md`](../../../../design-system/components/rail-person-horizontal.md) | `2026-08-24T08:12:21Z` |
| [Rail - Personal Widget](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=31185-161182) | `rMcDm5qGp4CXkXXddEbcMh` | `31185:161182` | `ready` | [`rail-personal-widget.md`](../../../../design-system/components/rail-personal-widget.md) | `2026-08-24T08:12:21Z` |
| [Rail - Square](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=7768-73596) | `rMcDm5qGp4CXkXXddEbcMh` | `7768:73596` | `ready` | [`rail-square.md`](../../../../design-system/components/rail-square.md) | `2026-08-24T08:12:21Z` |
| [Rail - 🟡Square Medium](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=35893-32643) | `rMcDm5qGp4CXkXXddEbcMh` | `35893:32643` | `work-in-progress` | [`rail-square-medium.md`](../../../../design-system/components/rail-square-medium.md) | `2026-08-24T08:12:22Z` |
| [Rail - SquareSmall1Story](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=16941-129762) | `rMcDm5qGp4CXkXXddEbcMh` | `16941:129762` | `ready` | [`rail-square-small-1-story.md`](../../../../design-system/components/rail-square-small-1-story.md) | `2026-08-24T08:12:21Z` |
| [Rail - SquareSmall2Story](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=7616-73598) | `rMcDm5qGp4CXkXXddEbcMh` | `7616:73598` | `ready` | [`rail-square-small-2-story.md`](../../../../design-system/components/rail-square-small-2-story.md) | `2026-08-24T08:12:21Z` |
| [Rail - Ticket](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=28139-194880) | `rMcDm5qGp4CXkXXddEbcMh` | `28139:194880` | `ready` | [`rail-ticket.md`](../../../../design-system/components/rail-ticket.md) | `2026-08-24T08:12:21Z` |
| [Rail / Top Collections](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=26610-66862) | `rMcDm5qGp4CXkXXddEbcMh` | `26610:66862` | `ready` | [`rail-top-collections.md`](../../../../design-system/components/rail-top-collections.md) | `2026-08-24T07:55:30Z` |
| [Rail / Top Titles](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=26610-28243) | `rMcDm5qGp4CXkXXddEbcMh` | `26610:28243` | `ready` | [`rail-top-titles.md`](../../../../design-system/components/rail-top-titles.md) | `2026-08-24T07:55:27Z` |
| [Rail / Tracks](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=41694-34904) | `rMcDm5qGp4CXkXXddEbcMh` | `41694:34904` | `ready` | [`rail-tracks.md`](../../../../design-system/components/rail-tracks.md) | `2026-08-24T08:12:22Z` |
| [Rail - Vertical](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=15462-365012) | `rMcDm5qGp4CXkXXddEbcMh` | `15462:365012` | `ready` | [`rail-vertical.md`](../../../../design-system/components/rail-vertical.md) | `2026-08-24T08:12:21Z` |
| [Select](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=34884-24858&t=6NQra4uE9oLKkthr-4) | `rMcDm5qGp4CXkXXddEbcMh` | `34884:24858` | `ready` | [`select.md`](../../../../design-system/components/select.md) | `2026-08-21T16:09:38Z` |
| [Шаблоны шторки / Фильтры](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/branch/jdBqhypltqMzx0mXE7uw94/Lib-iOS?node-id=37390-49620) | `jdBqhypltqMzx0mXE7uw94` | `37390:49620` | `unknown` | [`sheet-template-filters.md`](../../../../design-system/components/sheet-template-filters.md) | `not checked` |
| [Snackbar](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=13712-111074&t=6NQra4uE9oLKkthr-4) | `rMcDm5qGp4CXkXXddEbcMh` | `13712:111074` | `ready` | [`snackbar.md`](../../../../design-system/components/snackbar.md) | `2026-08-21T16:11:44Z` |
| [Switch](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=14447-113942&t=6NQra4uE9oLKkthr-4) | `rMcDm5qGp4CXkXXddEbcMh` | `14447:113942` | `ready` | [`switch.md`](../../../../design-system/components/switch.md) | `2026-08-21T15:35:51Z` |
| [Symbol input](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=12514-97868&t=6NQra4uE9oLKkthr-4) | `rMcDm5qGp4CXkXXddEbcMh` | `12514:97868` | `ready` | [`symbol-input.md`](../../../../design-system/components/symbol-input.md) | `2026-08-21T15:58:31Z` |
| [TabNavigation](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=24687-2182&t=6NQra4uE9oLKkthr-4) | `rMcDm5qGp4CXkXXddEbcMh` | `24687:2182` | `ready` | [`tab-navigation.md`](../../../../design-system/components/tab-navigation.md) | `2026-08-21T16:25:10Z` |
| [Tabbar - Meta](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=38937-15264&t=6NQra4uE9oLKkthr-4) | `rMcDm5qGp4CXkXXddEbcMh` | `38937:15264` | `ready` | [`tabbar-meta.md`](../../../../design-system/components/tabbar-meta.md) | `2026-08-21T16:13:59Z` |
| [TabGroup](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=24233-1389&t=6NQra4uE9oLKkthr-4) | `rMcDm5qGp4CXkXXddEbcMh` | `24233:1389` | `ready` | [`tabgroup.md`](../../../../design-system/components/tabgroup.md) | `2026-08-21T16:21:01Z` |
| [Tabgroup - Item](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=24233-1463&t=6NQra4uE9oLKkthr-4) | `rMcDm5qGp4CXkXXddEbcMh` | `24233:1463` | `ready` | [`tabgroup-item.md`](../../../../design-system/components/tabgroup-item.md) | `2026-08-21T16:21:01Z` |
| [Layouts](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=32942-50025) | `rMcDm5qGp4CXkXXddEbcMh` | `32942:50025` | `collection (9)` | [`layouts-ios.md`](../../../../design-system/components/layouts-ios.md) | `2026-08-21T15:14:53Z` |
<!-- FIGMA_COMPONENT_REGISTRY:END -->

## Продуктовые файлы (consumers, не библиотеки)

Файлы продукта, которые потребляют библиотеки. Из них берутся **продуктовые кейсы** для гайдов.

| Файл | fileKey | Зачем |
|---|---|---|
| Афиша в рамках Okko 3.0 — iOS | `xFhW4a26fD7hE0zK88ClF2` | Продуктовый кейс группы Filters (секция `Фильтрация ✅`, node `8563:230330`) |
| ios-коллекции | `Z4cJG20xxYb6oEECodt5WD` | Продуктовый кейс каталог-категория (секция `Category + collection`, node `2441:143240`) |

---

## Граф зависимостей

```
Okko Head Library          ── цвета, иконки, иллюстрации ──┐
🦖 Tokens [mobile & web]   ── spacing/corner/typography ────┤
🦍 Tokens [tv]             ── spacing/corner/typography ────┤
                                                            ├─→ Lib-iOS ──компоненты──┐
                                                            ├─→ Lib-Android (TBD) ────┤─→ Продуктовые файлы
                                                            ├─→ Lib-TV ───────────────┤   (Афиша, ios-коллекции…)
                                                            └─→ Lib-Web (TBD)     ────┘
```

## Соглашения

- **branchKey используется как fileKey в API**. Если URL вида `figma.com/design/<key>/branch/<branchKey>/…`, в REST-вызовах подставляем `branchKey`.
- В nodeId из URL `node-id=A-B` дефис меняется на двоеточие: `A:B`.
- Deprecated-стили имеют префикс `[Deprecated]/…` (FILL styles) и не используются.
- Префиксы lifecycle в именах компонентов: обычное имя или `🟢` — `ready`, `🔵` — `design-only`, `🟡` — `work-in-progress`, `⚪` — `planned`, `🔴` / `[Deprecated]` — `deprecated`.
