# Цвета — Okko Head Library
> Источник: файл **Okko Head Library** (fileKey `HYB1u9ysALVWtVWKoagiDH`), секция «Эти цвета экспортируются .json файлом» — node `32102:23344`. Значения переменных получены через `get_variable_defs` (резолв по тёмной теме, тема по умолчанию в библиотеке). Опубликованные стили (FILL) — через `/v1/files/.../styles`. Тема — **Dark** (основная).
Цвета устроены в три слоя:

1. **Primitives** — сырая палитра (рампы по 13 тонов: 100 — светлый … 1300 — тёмный). Не использовать напрямую в макетах.
2. **Semantic** — токены по назначению (`color.*`). Ссылаются на примитивы. **Это то, что применяется в макетах.**
3. **Brand / External** — фирменные цвета Окко и партнёров/соцсетей.

Часть semantic-токенов — **градиенты** (несколько стопов); они продублированы как опубликованные FILL-стили Figma (можно применить как стиль). Solid-токены применяются как переменные.

## 1. Primitives (сырая палитра)
Чёрный/белый:

| Токен | HEX |
|---|---|
| `primitives.black` | `#000000` |
| `primitives.white` | `#FFFFFF` |

**gray**

| Тон | HEX |
|---|---|
| `gray200` | `#F5F4F6` |
| `gray300` | `#E2E2E3` |
| `gray400` | `#C6C6C6` |
| `gray500` | `#BCBAC1` |
| `gray600` | `#8B8892` |
| `gray700` | `#6A6A6A` |
| `gray800` | `#5C5A5F` |
| `gray900` | `#3B3A3E` |
| `gray1000` | `#2C2B2F` |
| `gray1100` | `#1B1A1D` |
| `gray1200` | `#101011` |

**yellow**

| Тон | HEX |
|---|---|
| `yellow100` | `#FDF3A3` |
| `yellow200` | `#FFE089` |
| `yellow300` | `#FFCD13` |
| `yellow400` | `#F6BE24` |
| `yellow500` | `#EAA734` |
| `yellow600` | `#CE922B` |
| `yellow700` | `#BD8628` |
| `yellow800` | `#9C6D1E` |
| `yellow900` | `#8C631C` |
| `yellow1000` | `#6D4C12` |
| `yellow1100` | `#5E410F` |
| `yellow1200` | `#50360A` |
| `yellow1300` | `#342302` |

**green**

| Тон | HEX |
|---|---|
| `green100` | `#E4F5EB` |
| `green200` | `#C7EBD7` |
| `green300` | `#A9E1C2` |
| `green400` | `#90D5B1` |
| `green500` | `#6FCA9D` |
| `green600` | `#12B77C` |
| `green700` | `#13A871` |
| `green800` | `#12875A` |
| `green900` | `#0A7A52` |
| `green1000` | `#035F3E` |
| `green1100` | `#005235` |
| `green1200` | `#04452C` |
| `green1300` | `#022C1B` |

**brown**

| Тон | HEX |
|---|---|
| `brown100` | `#F4F0E6` |
| `brown200` | `#E8E2D1` |
| `brown300` | `#DED4BA` |
| `brown400` | `#D3C6A5` |
| `brown500` | `#C8B78D` |
| `brown600` | `#B09859` |
| `brown700` | `#A68E51` |
| `brown800` | `#8B733C` |
| `brown900` | `#7F6832` |
| `brown1000` | `#654F20` |
| `brown1100` | `#57441C` |
| `brown1200` | `#4A3915` |
| `brown1300` | `#30240B` |

**blue**

| Тон | HEX |
|---|---|
| `blue100` | `#DEF5FA` |
| `blue200` | `#C2E9F3` |
| `blue300` | `#A3DEEE` |
| `blue400` | `#86D1E7` |
| `blue500` | `#70CAE4` |
| `blue600` | `#4BA6DD` |
| `blue700` | `#3D97DB` |
| `blue800` | `#2681D5` |
| `blue900` | `#1F6DB5` |
| `blue1000` | `#15548E` |
| `blue1100` | `#15487A` |
| `blue1200` | `#0B3D69` |
| `blue1300` | `#042746` |

**cobalt**

| Тон | HEX |
|---|---|
| `cobalt100` | `#F0F0F9` |
| `cobalt200` | `#E6E5F5` |
| `cobalt300` | `#D1D0FE` |
| `cobalt400` | `#C0C1FE` |
| `cobalt500` | `#B4B2F9` |
| `cobalt600` | `#C3C1FA` |
| `cobalt700` | `#8D80F9` |
| `cobalt800` | `#6860FA` |
| `cobalt900` | `#564EFD` |
| `cobalt1000` | `#5D0EF5` |
| `cobalt1100` | `#4F03CD` |
| `cobalt1200` | `#301A59` |
| `cobalt1300` | `#301A59` |

**purple**

| Тон | HEX |
|---|---|
| `purple100` | `#F9EDFF` |
| `purple200` | `#F1DAFF` |
| `purple300` | `#EBC8FF` |
| `purple400` | `#E2B6FE` |
| `purple500` | `#DBA3FE` |
| `purple600` | `#CE7FFF` |
| `purple700` | `#C16AF3` |
| `purple800` | `#AC44DE` |
| `purple900` | `#A22BD5` |
| `purple1000` | `#7A12CA` |
| `purple1100` | `#6712AB` |
| `purple1200` | `#56148F` |

**pink**

| Тон | HEX |
|---|---|
| `pink100` | `#FFEBFC` |
| `pink200` | `#FFD6F8` |
| `pink300` | `#FFC1F4` |
| `pink400` | `#FFABEF` |
| `pink500` | `#FF82E7` |
| `pink600` | `#F168E4` |
| `pink700` | `#E84EE4` |
| `pink800` | `#DC30E0` |
| `pink900` | `#BC0ECB` |
| `pink1000` | `#90079C` |
| `pink1100` | `#7C0B86` |
| `pink1200` | `#6A0673` |
| `pink1300` | `#46054C` |

**violet**

| Тон | HEX |
|---|---|
| `violet100` | `#F1EFFF` |
| `violet200` | `#E3DFFE` |
| `violet300` | `#D6CFFF` |
| `violet400` | `#C8BFFE` |
| `violet500` | `#A076F6` |
| `violet600` | `#8E57FF` |
| `violet700` | `#7E3EFF` |
| `violet800` | `#743AC6` |
| `violet900` | `#6C43BF` |
| `violet1000` | `#3C1A70` |
| `violet1100` | `#321069` |
| `violet1200` | `#1A082C` |
| `violet1300` | `#12051F` |

**electric**

| Тон | HEX |
|---|---|
| `electric100` | `#D8E0FF` |
| `electric200` | `#C3CEFF` |
| `electric300` | `#A0B0FF` |
| `electric400` | `#8D9DF5` |
| `electric500` | `#7586F9` |
| `electric600` | `#616CFB` |
| `electric700` | `#585FF5` |
| `electric800` | `#4A44F3` |
| `electric900` | `#4137DF` |
| `electric1000` | `#4116C9` |
| `electric1100` | `#3705AB` |
| `electric1200` | `#2A1284` |
| `electric1300` | `#24145C` |

## 2. External primitives (партнёры/соцсети, сырьё)

| Токен | HEX |
|---|---|
| `epl1` | `#37003C` |
| `sber1` | `#21A038` |
| `sber2` | `#00D900` |
| `yandex1` | `#E81B2C` |
| `vk1` | `#0077FF` |
| `winline1` | `#FF6A13` |
| `ok1` | `#F98D20` |
| `facebook1` | `#325797` |
| `twitter1` | `#31ADF4` |
| `viber1` | `#7360F2` |

## 3. Semantic-токены (применять в макетах)
Колонка **Стиль** = есть ли опубликованный FILL-стиль Figma с тем же путём (✓ — да, можно применить как стиль; иначе только переменная).

### Текст и иконки (`color.text-icon.*`)

| Токен | HEX | Стиль |
|---|---|---|
| `color.text-icon.primary` | `#FFFFFFF5` | |
| `color.text-icon.secondary` | `#FFFFFFC7` | |

### Фон (`color.background.*`)

| Токен | HEX | Стиль |
|---|---|---|
| `color.background.solid.primary` | `#000000` | |
| `color.background.solid.secondary` | `#101011` | |
| `color.background.solid.inverse` | `#F5F4F6` | |
| `color.background.glassy.primary` | `#000000E0` | |
| `color.background.glassy.secondary` | `#000000B8` | |
| `color.background.glassy.third` | `#0000008F` | |
| `color.background.glassy.fourth` | `#00000052` | |

### Заливки (`color.fill.*`)

| Токен | HEX | Стиль |
|---|---|---|
| `color.fill.solid.accent` | `#4137DF` | |
| `color.fill.solid.primary` | `#101011` | |
| `color.fill.solid.secondary` | `#1B1A1D` | |
| `color.fill.solid.third` | `#2C2B2F` | |
| `color.fill.solid.fourth` | `#8B8892` | |
| `color.fill.solid.inverse` | `#FFFFFF` | |
| `color.fill.solid.positive` | `#12B77C` | |
| `color.fill.solid.negative` | `#5F0004` | |
| `color.fill.solid.warning` | `#EAA734` | |
| `color.fill.solid.live` | `#A9000C` | |
| `color.fill.glassy.primary` | `#C6C6C6CC` | |
| `color.fill.glassy.secondary` | `#E2E2E3CC` | |
| `color.fill.glassy.negative` | `#CD352E4D` | |
| `color.fill.glassy.warning` | `#EAA73452` | |
| `color.fill.glassy.third` | `#FFFFFFCC` | |
| `color.fill.glassy.inverse` | `#101011CC` | |
| `color.fill.technical.placeholder` | `#1B1A1D` | |
| `color.fill.technical.skeletonbg` | `#FFFFFF1A` | |
| `color.fill.technical.material.primary` | `#1C1C1C99` | |
| `color.fill.technical.material.secondary` | `#3B3A3E7A` | |
| `color.fill.technical.material.third` | `#8B889252` | |

### Бордеры (`color.border.*`)

| Токен | HEX | Стиль |
|---|---|---|
| `color.border.active` | `#FFFFFF8F` | |
| `color.border.solid` | `#BCBAC1` | |
| `color.border.glassy` | `#E2E2E366` | |
| `color.border.focus` | `#5D0EF5` | |
| `color.border.contour` | `#0000001A` | |
| `color.border.negative` | `#DD453B` | |
| `color.border.decorative.assistant-solid` | `#4A44F3B2` | |

### Статичные (не зависят от темы) (`color.static.*`)

| Токен | HEX | Стиль |
|---|---|---|
| `color.static.solid.black` | `#000000` | |
| `color.static.solid.white` | `#FFFFFF` | |
| `color.static.glassy.black` | `#000000B2` | |
| `color.static.glassy.white` | `#FFFFFFB2` | |

### Градиенты (semantic + опубликованный FILL-стиль)

Каждый — это градиент из нескольких стопов. Доступны как опубликованный стиль Figma.

| Токен | Стопы (HEX) | Стиль |
|---|---|---|
| `color.border.decorative.active-horizontal` | #00000000 … #00000000 (5 стопов) | ✓ |
| `color.border.decorative.active-vertical` | #4200D1, #8D9DF5 | ✓ |
| `color.border.decorative.assistant` | #FFFFFF, #24145C | |
| `color.border.decorative.focus` | #4137DF | ✓ |
| `color.component.button` | #8E57FF, #5D0EF5 | ✓ |
| `color.component.label.continuum` | #4F03CD, #6712AB | ✓ |
| `color.component.label.gold` | #654F20, #B09859 | ✓ |
| `color.component.label.lemon` | #FFE089, #FFCD13 | ✓ |
| `color.component.label.lighthouse` | #6712AB, #BC0ECB | ✓ |
| `color.component.label.melancholy` | #2681D5, #6C43BF | ✓ |
| `color.component.label.neon` | #BC0ECB, #743AC6 | ✓ |
| `color.component.label.sber-spasibo` | #A3DD0F, #37BC12, #16B47D, #0D9EB5 | |
| `color.component.label.sky` | #DEF5FA, #70CAE4 | ✓ |
| `color.component.label.twilight` | #A9000C, #743AC6 | ✓ |
| `color.component.progress-bar` | #FF82E7, #DC30E0, #7A12CA, #5D0EF5 | ✓ |
| `color.fill.fade.fourth` | #0000003D | |
| `color.fill.fade.primary` | #000000, #00000000 | |
| `color.fill.fade.secondary` | #000000CC | |
| `color.fill.fade.third` | #0000008F | |
| `color.fill.glassy.hover-focus.secondary` | #3B3A3E7A, #5C5A5F7A | ✓ |
| `color.fill.glassy.hover-focus.third` | #8B889252, #BCBAC152 | ✓ |
| `color.fill.solid.hover-focus.primary` | #101011, #1B1A1D | ✓ |
| `color.fill.solid.hover-focus.secondary` | #1B1A1D, #3B3A3E | ✓ |
| `color.fill.solid.hover-focus.third` | #2C2B2F, #5C5A5F | ✓ |
| `color.fill.technical.button-loading` | #FFFFFF3D, #FFFFFF4D | ✓ |
| `color.fill.technical.skeleton` | #FFFFFF26, #FFFFFF0D | ✓ |

> **Fade-градиенты** (`color.fill.fade.*`): альфа-рампы чёрного по 16 стопов, по 4 уровня плотности (primary/secondary/third/fourth) и 4 направления (top/right/bottom/left). Стили опубликованы по направлениям (`color/fill/fade/top/primary` и т.д.).

## 4. Brand / партнёры / соцсети

| Токен | HEX |
|---|---|
| `brand.okko.primary` | `#5D0EF5` |
| `brand.partners.epl` | `#37003C` |
| `brand.partners.winline` | `#FF6A13` |
| `brand.partners.sber` | `#148F2B` |
| `brand.social.facebook` | `#325797` |
| `brand.social.vk` | `#0077FF` |
| `brand.social.twitter` | `#31ADF4` |
| `brand.social.yandex` | `#E81B2C` |
| `brand.social.odnoklassniki` | `#F98D20` |
| `brand.social.viber` | `#7360F2` |

## Правила применения

- В макетах использовать **semantic-токены** (`color.*`), не примитивы напрямую.
- Тёмная тема — основная и единственная актуальная в библиотеке.
- Прозрачность кодируется 8-значным HEX (`#RRGGBBAA`): напр. `#FFFFFFF5` = white 96%.
- Градиенты применять опубликованным **стилем** Figma, а не вручную (отмечены ✓).
- `[Deprecated]/*` стили (в `/styles` их большинство) — **не использовать**.
- `static.*` — единственные токены, не меняющиеся между темами.
