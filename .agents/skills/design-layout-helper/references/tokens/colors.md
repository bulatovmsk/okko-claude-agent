# Цвета — Okko Head Library
> Источник: file **Okko Head Library** (`HYB1u9ysALVWtVWKoagiDH`), страница `Color Tokens` (`32102:23149`). Тема — **Dark** (основная и единственная активная в библиотеке).

Цвета устроены как **переменные** (variables) и **стили** (опубликованные FILL-стили Figma):

- **Variables** — применяются программно (Code Connect, токены) и через bound variables в Figma. Это и сырая палитра (`primitives.*`), и семантика (`color.*`), и `brand.*`.
- **Styles** — опубликованные FILL-стили; **только для градиентов и многостоповых fade**, которые нельзя выразить одной переменной.

Синхронизация: `bash scripts/sync-from-figma.sh head colors --variables-dir <dump-dir>` (см. раздел «Обновление» внизу).

---

## A. Variables (переменные)
### A.1. Primitives — сырая палитра
Не использовать напрямую в макетах. Шкала: `100` (светлый) … `1300` (тёмный).

**Чёрный/белый:**

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

**red**

| Тон | HEX |
|---|---|
| `red100` | `#FFCCCE` |
| `red200` | `#FFB9B9` |
| `red300` | `#FF979A` |
| `red400` | `#FF767B` |
| `red600` | `#DD453B` |
| `red700` | `#CD352E` |
| `red800` | `#BB201E` |
| `red900` | `#A9000C` |
| `red1000` | `#94000A` |
| `red1100` | `#810007` |
| `red1200` | `#6F0005` |
| `red1300` | `#5F0004` |

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

### A.2. External primitives — фирменные/партнёрские (сырые)

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

### A.3. Semantic-токены — `color.*` (применять в макетах)
> ⚙️ Значения resolved-hex для semantic-токенов добираются через MCP `get_variable_defs(nodeId='32102:23149', fileKey='HYB1u9ysALVWtVWKoagiDH')` и подставляются в маркер ниже. REST `/variables/local` отдаёт 403 без Enterprise scope.

#### Текст и иконки (`color.text-icon.*`)

| Токен | HEX |
|---|---|
| `color.text-icon.accent` | `#616CFB` |
| `color.text-icon.fourth` | `#FFFFFF66` |
| `color.text-icon.inverse.fourth` | `#00000066` |
| `color.text-icon.inverse.primary` | `#000000F5` |
| `color.text-icon.inverse.secondary` | `#000000CC` |
| `color.text-icon.inverse.third` | `#0000008F` |
| `color.text-icon.negative` | `#F25857F5` |
| `color.text-icon.offer` | `#FFCD13` |
| `color.text-icon.positive` | `#12B77C` |
| `color.text-icon.primary` | `#FFFFFFF5` |
| `color.text-icon.secondary` | `#FFFFFFC7` |
| `color.text-icon.third` | `#FFFFFF8F` |
| `color.text-icon.warning` | `#EAA734` |

#### Фон (`color.background.*`)

| Токен | HEX |
|---|---|
| `color.background.glassy.fourth` | `#00000052` |
| `color.background.glassy.primary` | `#000000E0` |
| `color.background.glassy.secondary` | `#000000B8` |
| `color.background.glassy.third` | `#0000008F` |
| `color.background.solid.inverse` | `#F5F4F6` |
| `color.background.solid.primary` | `#000000` |
| `color.background.solid.secondary` | `#101011` |

#### Заливки (`color.fill.*`)

| Токен | HEX |
|---|---|
| `color.fill.decorative.promo` | `#24145C` |
| `color.fill.glassy.inverse` | `#FFFFFFCC` |
| `color.fill.glassy.negative` | `#5F00047A` |
| `color.fill.glassy.primary` | `#101011EB` |
| `color.fill.glassy.secondary` | `#3B3A3E7A` |
| `color.fill.glassy.third` | `#8B889252` |
| `color.fill.glassy.warning` | `#EAA73452` |
| `color.fill.solid.accent` | `#4137DF` |
| `color.fill.solid.fourth` | `#8B8892` |
| `color.fill.solid.inverse` | `#FFFFFF` |
| `color.fill.solid.live` | `#A9000C` |
| `color.fill.solid.negative` | `#5F0004` |
| `color.fill.solid.positive` | `#12B77C` |
| `color.fill.solid.primary` | `#101011` |
| `color.fill.solid.secondary` | `#1B1A1D` |
| `color.fill.solid.third` | `#2C2B2F` |
| `color.fill.solid.warning` | `#EAA734` |
| `color.fill.technical.material.primary` | `#1C1C1C99` |
| `color.fill.technical.material.secondary` | `#3B3A3E7A` |
| `color.fill.technical.material.third` | `#8B889252` |
| `color.fill.technical.placeholder` | `#1B1A1D` |
| `color.fill.technical.skeletonbg` | `#FFFFFF1A` |

#### Бордеры (`color.border.*`)

| Токен | HEX |
|---|---|
| `color.border.active` | `#FFFFFF8F` |
| `color.border.contour` | `#FFFFFF1A` |
| `color.border.decorative.assistant-solid` | `#4A44F3B2` |
| `color.border.focus` | `#4116C9` |
| `color.border.glassy` | `#8B889252` |
| `color.border.negative` | `#94000A` |
| `color.border.negative-glassy` | `#FFFFFF` |
| `color.border.solid` | `#2C2B2F` |
| `color.border.warning` | `#EAA734` |
| `color.border.warning-glassy` | `#EAA73452` |

#### Статичные (не зависят от темы) (`color.static.*`)

| Токен | HEX |
|---|---|
| `color.static.glassy.black` | `#000000B2` |
| `color.static.glassy.white` | `#FFFFFFB2` |
| `color.static.solid.black` | `#000000` |
| `color.static.solid.white` | `#FFFFFF` |

#### Компонентные (`color.component.*`)

| Токен | HEX |
|---|---|
| `color.component.label.offer` | `#FFCD13` |
| `color.component.sber-button` | `#148F2B` |


### A.4. Brand / партнёры / соцсети

#### `brand.okko.*`

| Токен | HEX |
|---|---|
| `brand.okko.accent` | `#4A44F3` |
| `brand.okko.additional-a` | `#3705AB` |
| `brand.okko.additional-b` | `#24145C` |
| `brand.okko.primary` | `#000000` |

#### `brand.partners.*`

| Токен | HEX |
|---|---|
| `brand.partners.epl` | `#37003C` |
| `brand.partners.sber` | `#148F2B` |
| `brand.partners.sber-spasibo` | `#00D900` |
| `brand.partners.winline` | `#FF6A13` |

#### `brand.social.*`

| Токен | HEX |
|---|---|
| `brand.social.facebook` | `#325797` |
| `brand.social.odnoklassniki` | `#F98D20` |
| `brand.social.twitter` | `#31ADF4` |
| `brand.social.viber` | `#7360F2` |
| `brand.social.vk` | `#0077FF` |
| `brand.social.yandex` | `#E81B2C` |

---

## B. Styles (опубликованные FILL-стили Figma)

**39 не-deprecated стилей.** Применять как «стиль» в Figma (для градиентов и многостоповых fade).

### `color/border/decorative/…`

| Стиль | Тип | Значение |
|---|---|---|
| `color/border/decorative/active-horizontal` | linear | `#000000 a0.00` 0% … `#000000 a0.00` 100% (5 стопов) |
| `color/border/decorative/active-vertical` | linear | `#000000 a0.00` 0% … `#000000 a0.00` 100% (5 стопов) |
| `color/border/decorative/assistant-gradient` | linear | `#24145C` 0%, `#FFFFFF` 100% |
| `color/border/decorative/focus` | linear | `#4137DF` 0%, `#4137DF` 52%, `#4137DF` 100% |

### `color/component/…`

| Стиль | Тип | Значение |
|---|---|---|
| `color/component/button` | linear | `#4116C9` 0%, `#4116C9` 100% |
| `color/component/menu` | linear | `#C8BFFE` 0%, `#FFFFFF` 100% |
| `color/component/progress-bar` | linear | `#F5F4F6` 0%, `#F5F4F6` 33%, `#F5F4F6` 67%, `#F5F4F6` 100% |

### `color/component/label/…`

| Стиль | Тип | Значение |
|---|---|---|
| `color/component/label/continuum` | linear | `#4A3AFF` 0%, `#4A3AFF` 100% |
| `color/component/label/gold` | linear | `#654F20` 0%, `#B09859` 100% |
| `color/component/label/lemon` | linear | `#FFE089` 0%, `#FFCD13` 100% |
| `color/component/label/lighthouse` | linear | `#3705AB` 0%, `#3705AB` 100% |
| `color/component/label/melancholy` | linear | `#2681D5` 0%, `#6C43BF` 100% |
| `color/component/label/neon` | linear | `#BC0ECB` 0%, `#743AC6` 100% |
| `color/component/label/sky` | linear | `#DEF5FA` 0%, `#70CAE4` 100% |
| `color/component/label/twilight` | linear | `#A9000C` 0%, `#743AC6` 100% |

### `color/fill/fade/top/…`

| Стиль | Тип | Значение |
|---|---|---|
| `color/fill/fade/top/fourth` | linear | `#000000 a0.24` 0% … `#000000 a0.00` 100% (16 стопов) |
| `color/fill/fade/top/primary` | linear | `#000000` 0% … `#000000 a0.00` 100% (16 стопов) |
| `color/fill/fade/top/secondary` | linear | `#000000 a0.80` 0% … `#000000 a0.00` 100% (16 стопов) |
| `color/fill/fade/top/third` | linear | `#000000 a0.56` 0% … `#000000 a0.00` 100% (16 стопов) |

### `color/fill/fade/right/…`

| Стиль | Тип | Значение |
|---|---|---|
| `color/fill/fade/right/fourth` | linear | `#000000 a0.24` 0% … `#000000 a0.00` 100% (16 стопов) |
| `color/fill/fade/right/primary` | linear | `#000000` 0% … `#000000 a0.00` 100% (16 стопов) |
| `color/fill/fade/right/secondary` | linear | `#000000 a0.80` 0% … `#000000 a0.00` 100% (16 стопов) |
| `color/fill/fade/right/third` | linear | `#000000 a0.56` 0% … `#000000 a0.00` 100% (16 стопов) |

### `color/fill/fade/bottom/…`

| Стиль | Тип | Значение |
|---|---|---|
| `color/fill/fade/bottom/fourth` | linear | `#000000 a0.24` 0% … `#000000 a0.00` 100% (16 стопов) |
| `color/fill/fade/bottom/primary` | linear | `#000000` 0% … `#000000 a0.00` 100% (16 стопов) |
| `color/fill/fade/bottom/secondary` | linear | `#000000 a0.80` 0% … `#000000 a0.00` 100% (16 стопов) |
| `color/fill/fade/bottom/third` | linear | `#000000 a0.56` 0% … `#000000 a0.00` 100% (16 стопов) |

### `color/fill/fade/left/…`

| Стиль | Тип | Значение |
|---|---|---|
| `color/fill/fade/left/fourth` | linear | `#000000 a0.24` 0% … `#000000 a0.00` 100% (16 стопов) |
| `color/fill/fade/left/primary` | linear | `#000000` 0% … `#000000 a0.00` 100% (16 стопов) |
| `color/fill/fade/left/secondary` | linear | `#000000 a0.80` 0% … `#000000 a0.00` 100% (16 стопов) |
| `color/fill/fade/left/third` | linear | `#000000 a0.56` 0% … `#000000 a0.00` 100% (16 стопов) |

### `color/fill/glassy/hover-focus/…`

| Стиль | Тип | Значение |
|---|---|---|
| `color/fill/glassy/hover-focus/secondary` | linear | `#3B3A3E a0.48` 0%, `#5C5A5F a0.48` 100% |
| `color/fill/glassy/hover-focus/third` | linear | `#8B8892 a0.32` 0%, `#BCBAC1 a0.32` 100% |

### `color/fill/solid/hover-focus/…`

| Стиль | Тип | Значение |
|---|---|---|
| `color/fill/solid/hover-focus/primary` | linear | `#101011` 0%, `#1B1A1D` 100% |
| `color/fill/solid/hover-focus/secondary` | linear | `#1B1A1D` 0%, `#3B3A3E` 100% |
| `color/fill/solid/hover-focus/third` | linear | `#2C2B2F` 0%, `#5C5A5F` 100% |

### `color/fill/technical/…`

| Стиль | Тип | Значение |
|---|---|---|
| `color/fill/technical/button-loading` | linear | `#FFFFFF a0.00` 0%, `#FFFFFF a0.24` 88%, `#FFFFFF a0.30` 100% |
| `color/fill/technical/skeleton` | linear | `#FFFFFF a0.15` 0%, `#FFFFFF a0.05` 100% |

### `color/partners/…`

| Стиль | Тип | Значение |
|---|---|---|
| `color/partners/sber-gradient` | linear | `#A3DD0F` 0%, `#37BC12` 25%, `#16B47D` 74%, `#0D9EB5` 100% |

### Связь со semantic-токенами
Большинство FILL-стилей продублированы как semantic-переменные с тем же путём (стиль `color/fill/fade/top/primary` ↔ переменная `color.fill.fade.top.primary`). Это сделано, чтобы один и тот же градиент можно было применить и как «стиль» в Figma, и через bound variable в коде.

---

## Правила: что когда брать

| Когда | Брать |
|---|---|
| Solid-цвет (один тон, без градиента) | **переменную** (`color.*`) — программно или через bound variable |
| Градиент / многостоповая fade-рампа | **опубликованный стиль** Figma (`color/...`) — невозможно одной переменной |
| Hover/focus 2-стоповые состояния | **стиль** (анимация между двумя точками) |
| Цвет фирменного партнёра (Сбер, EPL, …) | `Primitives/External/*` (сырьё) или `brand.partners.*` (применяемый) |
| Цвета, не зависящие от темы | `color.static.*` — единственные не меняющиеся между Dark/Light |

**Не использовать:** все `[Deprecated]/*` стили (в `/styles` их большинство — 181 из 220).
**Прозрачность:** кодируется 8-значным HEX (`#RRGGBBAA`); напр. `#FFFFFFF5` = white α=0.96.

---

## Обновление

```bash
bash scripts/sync-from-figma.sh head colors --variables-dir <dump-dir>
```

Workflow получает актуальные данные Figma, разрешает alias chains из Variables API или Figma MCP dump, обновляет source и skill references и формирует отчёт. При незаполненных маркерах рабочие файлы не изменяются.
