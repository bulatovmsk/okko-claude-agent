# Spacing — Tokens [mobile & web]
> Источник: file **🦖 Tokens [mobile & web]** (`vztN8doGwBZOCbpDf2PhKR`), страница **Spacing** — node `2280:155798`. Токены — NUMBER variables Figma (REST не отдаёт значений, забираются через Plugin API).

Токены отступов: внутренние padding'и компонентов, gap'ы между элементами, размеры секций и грид-промежутки. Это **NUMBER variables** Figma.

## Токены

Базовая рампа `spacing/100..1000` — масштабируется от мелких inset'ов (2pt) до межсекционных отступов (96pt).

| Токен | Значение | Типовое применение |
|---|---|---|
| `spacing.50` | 2 | subpixel-inset (только специальные кейсы) |
| `spacing.100` | 4 | минимальный gap между значками |
| `spacing.125` | 6 | тонкий gap |
| `spacing.150` | 8 | gap между мелкими элементами |
| `spacing.175` | 10 |  |
| `spacing.200` | 12 | малый внутренний padding |
| `spacing.225` | 14 |  |
| `spacing.250` | 16 | базовый gap между чипсами/иконками |
| `spacing.275` | 18 |  |
| `spacing.300` | 20 | gap между сложными элементами |
| `spacing.325` | 22 |  |
| `spacing.350` | 24 | внутренний padding карточек/строк |
| `spacing.375` | 28 |  |
| `spacing.400` | 32 | gap между картами в строке |
| `spacing.450` | 40 | внутренний padding средних компонентов |
| `spacing.500` | 48 | отступ от края до первого блока |
| `spacing.600` | 56 | отступ между блоками |
| `spacing.700` | 64 | отступ между секциями |
| `spacing.800` | 72 | крупные секционные отступы |
| `spacing.900` | 80 | отступ перед футером |
| `spacing.1000` | 96 | максимальный секционный отступ |

### Платформенные screen-padding (паддинг от края экрана до контента)

| Токен | Значение |
|---|---|
| `screen-padding.android.phone` | 16 |
| `screen-padding.android.tablet` | 24 |
| `screen-padding.ios.ipad` | 35 |
| `screen-padding.ios.iphone` | 15 |
| `screen-padding.web.desktop-l` | 72 |
| `screen-padding.web.desktop-m` | 56 |
| `screen-padding.web.mobile` | 12 |
| `screen-padding.web.tablet` | 32 |

---

## Правила выбора

| Контекст | Токен |
|---|---|
| Внутренний padding кнопки/чипса (H/V) | `spacing.s` / `spacing.xs` (зависит от размера компонента) |
| Gap между элементами в строке (Chips, Tabs) | `spacing.s` |
| Внутренний padding карточек контента | `spacing.m` или `spacing.l` |
| Отступ между секциями экрана | `spacing.xl` или больше |
| Inset от безопасной зоны до контента | `spacing.l` (mobile) / `spacing.xl` (tablet) |

Конкретные значения см. в таблице выше. Между mobile и web/tablet token-имена общие — меняются **значения** под брейкпоинт через моды.

---

## Обновление

```bash
bash scripts/figma-sync-tokens.sh spacing
```

Скрипт обновит шапку и скелет. Resolved-значения NUMBER-переменных подставляет скил через `use_figma` (figma.variables.getLocalVariableCollectionsAsync → фильтр FLOAT → temp TEXT-узел → REST).
Раздел «Правила выбора» сохраняется при пересборе.
