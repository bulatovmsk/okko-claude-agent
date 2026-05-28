# Карта Figma-библиотек ДС Окко

Реестр fileKey, branchKey, ключевых nodeId и зависимостей. Источник истины для всех скилов, которые ходят в Figma.

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
| Цвета (Primitives + Semantic + Brand) | `32102:23344` | [`design-system/tokens/colors.md`](../../../design-system/tokens/colors.md) |
| Иконки Main Pack (490 шт., 16 категорий, 24×24) | `29361:322` | [`design-system/components/icons.md`](../../../design-system/components/icons.md) |
| Иллюстрации · Static (Loader, Age Mark 0+…18+, Devices) | `39089:10560` | [`design-system/components/illustrations.md`](../../../design-system/components/illustrations.md) |
| Иллюстрации · Product images (плейсхолдеры) | `39101:215` | там же |
| Иллюстрации · Bobokko (маскот, 41 поза) | `39104:349` | там же |

> **Variables API:** для resolved-цветов semantic-токенов использовать MCP `get_variable_defs(nodeId='32102:23344', fileKey='HYB1u9ysALVWtVWKoagiDH')` — REST `/variables/local` отдаёт 403 без Enterprise scope.

---

### Lib-Android, Lib-TV, Lib-Web — TBD

Платформенные библиотеки пока не зафиксированы в реестре. Когда будут — добавить сюда fileKey, активный бранч и ключевые nodeId.

| Библиотека | fileKey | Статус |
|---|---|---|
| Lib-Android | — | TBD |
| Lib-TV (Android TV + SmartTV Web: webOS, Tizen) | — | TBD |
| Lib-Web | — | TBD |

---

## Продуктовые файлы (consumers, не библиотеки)

Файлы продукта, которые потребляют библиотеки. Из них берутся **продуктовые кейсы** для гайдов.

| Файл | fileKey | Зачем |
|---|---|---|
| Афиша в рамках Okko 3.0 — iOS | `xFhW4a26fD7hE0zK88ClF2` | Продуктовый кейс группы Filters (секция `Фильтрация ✅`, node `8563:230330`) |
| ios-коллекции | `Z4cJG20xxYb6oEECodt5WD` | Продуктовый кейс каталог-категория (секция `Category + collection`, node `2441:143240`) |

---

## Граф зависимостей

```
Okko Head Library  ── цвета, иконки, иллюстрации ──┐
                                                    ├─→  Lib-iOS  ──компоненты──┐
                                                    │                            ├─→  Продуктовые файлы
                                                    ├─→  Lib-Android (TBD) ─────┤    (Афиша, ios-коллекции, …)
                                                    ├─→  Lib-TV (TBD)      ─────┤
                                                    └─→  Lib-Web (TBD)     ─────┘
```

## Соглашения

- **branchKey используется как fileKey в API**. Если URL вида `figma.com/design/<key>/branch/<branchKey>/…`, в REST-вызовах подставляем `branchKey`.
- В nodeId из URL `node-id=A-B` дефис меняется на двоеточие: `A:B`.
- Deprecated-стили имеют префикс `[Deprecated]/…` (FILL styles) и не используются.
- Префиксы статуса в именах компонентов: `🟢` готов / опубликован, `🟡` в работе, `🔴 [Deprecated]` устаревший.
