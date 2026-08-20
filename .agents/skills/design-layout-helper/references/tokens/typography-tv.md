# Типографика — Tokens [tv]
> Источник: file **🦍 Tokens [tv]** (`Zn2JrOHhSURjCuUEp6JcI8`), страница **Text Styles** — node `0:1`. Опубликованных TEXT-стилей — **30**. Резолв: REST `/styles` + дозапрос `/nodes`.

**Формат ячейки:** `<size>/<line-height> · <weight>` (опц. `· ls <letter-spacing>`).

**Шрифты в файле:** `Suisse Int'l` (30)

Все стили — для разрешения 1920×1080 (Smart TV / Android TV). Платформенных вариантов нет — один стиль на устройство.

---

## Headings

| Стиль | Размер · Line-height · Weight |
|---|---|
| **H1** | 66/72 · 700 · ls -1.32 |
| **H2** | 50/56 · 700 · ls -1.00 |
| **H3** | 42/48 · 600 · ls -0.42 |

---

## Body

| Стиль | Размер · Line-height · Weight |
|---|---|
| **Body 1/Accent** | 33/44 · 500 |
| **Body 1/Default** | 33/44 · 400 |
| **Body 1/Text** | 33/52 · 400 |
| **Body 2/Accent** | 28/36 · 500 |
| **Body 2/Default** | 28/36 · 400 |
| **Body 3/Accent** | 25/34 · 500 |
| **Body 3/Default** | 25/34 · 400 |
| **Body 4/Accent** | 21/30 · 500 |
| **Body 4/Default** | 21/30 · 400 |

---

## Buttons

| Стиль | Размер · Line-height · Weight |
|---|---|
| **Button/Default** | 28/32 · 500 |
| **Button/Large** | 33/40 · 500 |
| **Button/Small** | 25/28 · 500 |

---

## Labels

| Стиль | Размер · Line-height · Weight |
|---|---|
| **Label Rich/Title** | 13/24 · 600 · ls 0.78 |
| **Label Rich/Value** | 30/36 · 600 · ls -0.30 |
| **Label/Bonus** | 19/28 · 600 · ls -0.57 |
| **Label/Large** | 20/36 · 600 · ls 1.00 |
| **Label/Small** | 18/32 · 600 · ls 0.90 |

---

## Others

| Стиль | Размер · Line-height · Weight |
|---|---|
| **AI Assistant** | 42/56 · 400 · ls -0.42 |
| **H4** | 33/40 · 600 · ls -0.33 |
| **Kong** | 120/108 · 700 · ls -4.80 |
| **Others/Age Mark** | 82/92 · 700 · ls -2.46 |
| **Others/Caption** | 18/24 · 600 · ls 0.18 |
| **Others/Decorative** | 72/94 · 300 |
| **Others/Menu Item** | 28/36 · 700 · ls -0.28 |
| **Others/Rewind** | 120/108 · 700 · ls -4.80 |
| **Others/Subtitles** | 44/52 · 600 |
| **Title** | 82/92 · 700 · ls -2.46 |

---

## Правила выбора стиля

> Раздел редактируется вручную и **не перезаписывается** при `sync`.

| Контекст | Стиль |
|---|---|
| Главный заголовок экрана | `H2` |
| Подзаголовок раздела | `H3` |
| Основной текст | `Body 1/Default` |
| Акцентный текст в карточке | `Body 1/Accent` или `Body 2/Accent` |
| Caption / мелкие пояснения | `Body 3/Default` |
| Подпись кнопки | `Button/Large` |
| Лейбл бонуса/значка | `Label/Bonus` |
| Пункт меню | `Others/Menu Item` |

**TV-специфика:** все размеры рассчитаны на расстояние просмотра ≈ 3 м. Не использовать `Body 3` для контента — только для caption/служебных подписей.

---

## Обновление

```bash
bash scripts/figma-sync-tokens.sh typography-tv
```

Скрипт перепишет основной контент. Раздел «Правила выбора стиля» сохраняется.
