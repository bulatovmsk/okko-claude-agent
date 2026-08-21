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
| [Text input](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=12510-97334&t=6NQra4uE9oLKkthr-4) | `rMcDm5qGp4CXkXXddEbcMh` | `12510:97334` | `ready` | [`input.md`](../../../../design-system/components/input.md) | `2026-08-21T15:55:31Z` |
| [Label : Large](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=12185-97166&t=6NQra4uE9oLKkthr-4) | `rMcDm5qGp4CXkXXddEbcMh` | `12185:97166` | `ready` | [`label-large.md`](../../../../design-system/components/label-large.md) | `2026-08-21T16:01:51Z` |
| [Label : Small](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=12185-97090&t=6NQra4uE9oLKkthr-4) | `rMcDm5qGp4CXkXXddEbcMh` | `12185:97090` | `ready` | [`label-small.md`](../../../../design-system/components/label-small.md) | `2026-08-21T16:01:52Z` |
| [🟡 List Item V2](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=36507-21672&t=6NQra4uE9oLKkthr-4) | `rMcDm5qGp4CXkXXddEbcMh` | `36507:21672` | `work-in-progress` | [`list-item-v2.md`](../../../../design-system/components/list-item-v2.md) | `2026-08-21T16:04:40Z` |
| [Navbar](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=12978-100799&t=6NQra4uE9oLKkthr-4) | `rMcDm5qGp4CXkXXddEbcMh` | `12978:100799` | `ready` | [`navbar.md`](../../../../design-system/components/navbar.md) | `2026-08-21T15:50:49Z` |
| [Onboarding Bubble](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=32634-7164&t=6NQra4uE9oLKkthr-4) | `rMcDm5qGp4CXkXXddEbcMh` | `32634:7164` | `ready` | [`onboarding-bubble.md`](../../../../design-system/components/onboarding-bubble.md) | `2026-08-21T15:46:56Z` |
| [Radio button](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=14447-113928&t=6NQra4uE9oLKkthr-4) | `rMcDm5qGp4CXkXXddEbcMh` | `14447:113928` | `ready` | [`radio-button.md`](../../../../design-system/components/radio-button.md) | `2026-08-21T15:34:05Z` |
| [Select](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=34884-24858&t=6NQra4uE9oLKkthr-4) | `rMcDm5qGp4CXkXXddEbcMh` | `34884:24858` | `ready` | [`select.md`](../../../../design-system/components/select.md) | `2026-08-21T16:09:38Z` |
| [Шаблоны шторки / Фильтры](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/branch/jdBqhypltqMzx0mXE7uw94/Lib-iOS?node-id=37390-49620) | `jdBqhypltqMzx0mXE7uw94` | `37390:49620` | `ready` | [`sheet-template-filters.md`](../../../../design-system/components/sheet-template-filters.md) | `not checked` |
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
