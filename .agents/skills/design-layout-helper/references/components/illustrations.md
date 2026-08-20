# Иллюстрации — Okko Head Library

> Источник: file **Okko Head Library** (`HYB1u9ysALVWtVWKoagiDH`). Три раздела:
> - **Static** — node `39089:10560`
> - **Product images** — node `39101:215`
> - **Bobokko** (маскот) — node `39104:349`

Иллюстрации Окко делятся на три группы: служебные (Static), продуктовые объекты-плейсхолдеры (Product images) и маскот-медведь **Bobokko**.

---

## 1. Static (служебные)

Системные иллюстрации для технических и навигационных состояний.

| Элемент | Тип | Размер | Назначение |
|---|---|---|---|
| `Loader` | компонент | 300×300 | анимация загрузки (есть `Loader Revers` — инстанс реверс) |
| `Age Mark` | component set | 2961×1024 | возрастная маркировка: `0+`, `6+`, `12+`, `16+`, `18+` |
| `Devices` | frame | 3891×1264 | изображения устройств: Стандартные / Мобильные / Все девайсы |
| `Static splash` | frame | 4932×1984 | статичный сплэш-экран запуска |
| `Menu promo Image` | frame | 1632×1314 | промо-картинка для меню |

---

## 2. Product images (продуктовые объекты)
Декоративные иллюстрации-плейсхолдеры (очки, мячи, попкорн и т.п.) — для пустых состояний, профилей, промо.

| Set | Вариантов | Состав |
|---|---|---|
| `Profile logo` | 5 | True, Number=1, False, Number=1, False, Number=2, False, Number=3, False, Number=4 |
| `Basic icon glasses` | 12 | Triangle, Circle, Download, History, Heart Bold, Play, Heart Solid, Arrows both …+4 |
| `Basic logo glasses` | 10 | Sharp 1, Sharp 2, Sharp 3, Sharp 4, Sharp 5, Soft 1, Soft 2, Soft 3 …+2 |
| `Basic logo pillow` | 11 | Square 1, Square 2, Square 3, Square 4, Square 5, Round 1, Variant8, Variant9 …+3 |
| `Ball` | 7 | Ball 1, Ball 2, Ball 3, Ball 4, Ball 5, Ball 6, Ball 7 |
| `Ball` | 7 | Ball 1, Ball 2, Ball 3, Ball 4, Ball 5, Ball 6, Ball 7 |
| `Popcorn` | 8 | Popcorn 1, Popcorn 2, Popcorn 3, Popcorn 4, Popcorn 5, Popcorn 6, Popcorn 7, Corn |
| `Product objects` | 11 | Composition, Note, Stars, Tubes green, Tubes gold, Popcorn, Headphones, Gamepad …+3 |

---

## 3. Bobokko (маскот)
**Bobokko** — фирменный медведь-маскот Окко. Один component set `Bobokko` с переключателем поз через `Property 1`.

**41 поз.** <details><summary>Все позы</summary>

Привет · Палец за спину · Задумался · Поцелуйчик · Улыбается две руки · Улыбается одна рука · ОК · Что-то держит · Руки в боки · Подмигивает · С попкорном · Упал на подушку · Футболист 1 · WTF · На раслабоне · Обиделся · Выглядывает из двери · Счастливо удивлён · Палец вверх · Бросается с улыбкой · С подарком зелёным · С подарком розовым · Сердечко · Чешет голову · В варежках · Футболист 2 · С книжкой · С зелёным джостиком · С серым джостиком · В зел. наушниках глаза закрыты · В роз. наушниках глаза открыты · В зел. наушниках глаза открыты · В роз. наушниках глаза закрыты · С кубком · С яблоком · Чистит зубы · Сильно устал · Спит с книжкой · Спит с пультом · С подарком в колпаке · Собрался купаться

</details>

**Применение:** эмоциональные состояния, пустые экраны, онбординг, праздники, спорт. Поза подбирается по контексту (ошибка → «Обиделся»/«WTF», успех → «Палец вверх»/«ОК», ночь → «Спит…»).

---

## Правила применения

- **Static** — только по прямому назначению (загрузка, сплэш, возрастной знак). `Age Mark` обязателен по требованиям маркировки.
- **Product images** — декор и плейсхолдеры; не использовать как функциональные иконки (для иконок — [Main Pack](icons.md)).
- **Bobokko** — фирменный маскот, нельзя искажать/перекрашивать; позу выбирать по тону и контексту экрана.
- Все иллюстрации — общие для всех платформ (Web/iOS/Android/TV).

## Источник

- Static — Figma `HYB1u9ysALVWtVWKoagiDH` node `39089:10560`
- Product images — node `39101:215`
- Bobokko — node `39104:349`

## Обновление

```bash
bash scripts/figma-sync-head-library.sh illustrations
```
