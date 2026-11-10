# Миграция цветов TabGroup

20 октября 2026.

[Страница TabGroup](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=21974-328116).

Изменено 617 уникальных слоёв, выполнено 617 прямых замен привязок. Проверены все 19759 слоёв страницы и 406 мастер-компонентов, включая скрытые вложенные слои, текстовые диапазоны, градиенты и векторные регионы.

## Выполнено

- 102 замены в собственных слоях мастеров.
- 452 замены во вложенных слоях мастеров. Изменения исходных локальных мастеров также распространились на многочисленные экземпляры по наследованию.
- Старые Fill/Fade/Right/Primary и Border/Decorative/on Dark/Active Horisontal из более ранних наборов привязаны к существующим семантически соответствующим стилям color/fill/fade/right/primary и color/border/decorative/active-horizontal.
- 63 прямые static-замены текста на цветных метках. Они распространились ещё на 288 заливок: итоговая проверка нашла 351 подходящую static-заливку, оставшихся подходящих замен — 0. Прозрачность сохранена.
- Учтены разные обозначения исключений: On Light, light theme=True, Тёмный фон=False, Режим=На светлом, Theme=Kids. Применены только ранее согласованные исключения: старые On Light Primary/Secondary/Forth → inverse и Fill/Decorative/Kids → progress-bar. Поэтому в исключённых Light/Kids областях тоже есть эти согласованные адресные замены.

## Итог проверки

В обрабатываемых мастерах и их вложенных слоях вне Light/Kids старых цветовых стилей и примитивных цветовых привязок не осталось. Неоднозначных замен нет. Проверка актуальных стилей по ключам не выявила старых стилей, замаскированных именем Color. Внутри всех мастеров, включая Light/Kids, используемые переменные находятся в текущей коллекции Color; старые Theme/Technical остались только вне мастеров.

Старые PAINT-стили на всей странице — 1933 применений:

- Kids: 62.
- Light: 98.
- Вне мастеров: 1773.

Selection colors всей страницы продолжит показывать эти исключённые старые цвета. В примерах и гайдах вне мастеров также остались 1144 привязки Theme, 52 Technical и 29 примитивных привязок. Это отдельные счётчики применений переменных, их нельзя складывать со счётчиком стилей как уникальные слои.

| Старый стиль | Применений | Области |
|---|---:|---|
| [Deprecated]/Background/Solid/Kids | 9 | outside: 9 |
| [Deprecated]/Fill/Fade/On Light/Left/Primary | 13 | kids: 13 |
| [Deprecated]/Fill/Solid/On Light/Third | 18 | kids: 18 |
| [Deprecated]/Border/Glassy | 78 | kids: 18, light: 20, outside: 40 |
| [Deprecated]/Fill/Fade/On Light/Right/Primary | 13 | kids: 13 |
| [Deprecated]/Background/Solid/Secondary | 2 | outside: 2 |
| Primitives/Grey/Primary | 4 | outside: 4 |
| Primitives/Purple/Dark | 3 | outside: 3 |
| Text & icon/on Dark/Primary | 3 | outside: 3 |
| [Deprecated]/Text & icon/on Dark/Third | 42 | outside: 42 |
| Primitives/Grey/Medium | 6 | light: 6 |
| [Deprecated]/Fill/Glassy/Third | 49 | light: 49 |
| Fill/Solid/AccentB | 8 | light: 8 |
| [Deprecated]/Text & icon/on Dark/Primary | 265 | light: 8, outside: 257 |
| [Deprecated]/Fill/Solid/Inverse | 2 | light: 1, outside: 1 |
| [Deprecated]/Fill/Technical/on Dark/Skeleton | 23 | outside: 23 |
| [Deprecated]/Border/Decorative/on Light/Active Horisontal | 6 | light: 6 |
| Background/Solid/Inverse | 16 | outside: 16 |
| Text & icon/on Light/Primary | 16 | outside: 16 |
| Fill/Decorative/Lighthouse | 16 | outside: 16 |
| Text & icon/on Dark/Primary | 247 | outside: 247 |
| Text & icon/on Dark/Secondary | 400 | outside: 400 |
| Fill/Solid/Primary | 41 | outside: 41 |
| Fill/Glassy/Secondary | 6 | outside: 6 |
| Text & icon/on Dark/Positive | 28 | outside: 28 |
| Text & icon/on Dark/Third | 28 | outside: 28 |
| Text & icon/on Dark/Accent | 23 | outside: 23 |
| Text & icon/on Dark/Forth | 73 | outside: 73 |
| [Deprecated]/Fill/Glassy/Secondary | 38 | outside: 38 |
| [Deprecated]/Text & icon/on Dark/Secondary | 42 | outside: 42 |
| [Deprecated]/Text & icon/on Light/Primary | 2 | outside: 2 |
| [Deprecated]/Text & icon/on Light/Secondary | 2 | outside: 2 |
| Background/Solid/Primary | 6 | outside: 6 |
| Text & icon/on Dark/Negative | 72 | outside: 72 |
| Primitives/cobalt300 | 8 | outside: 8 |
| Fill/Solid/Third | 16 | outside: 16 |
| Border/Decorative/on Dark/Focus | 16 | outside: 16 |
| Brand/Partners/Sber Gradient | 16 | outside: 16 |
| Border/Decorative/on Dark/Active Horisontal | 24 | outside: 24 |
| Fill/Solid/Secondary | 24 | outside: 24 |
| Border/Solid | 30 | outside: 30 |
| Peenk | 8 | outside: 8 |
| Wannabe Black | 112 | outside: 112 |
| On Surface / Disabled | 6 | outside: 6 |
| Text & icon/on Dark/Offer | 16 | outside: 16 |
| Fill/Decorative/Melancholy | 16 | outside: 16 |
| [Deprecated]/Background/Solid/Primary | 2 | outside: 2 |
| [Deprecated]/Border/Solid | 10 | outside: 10 |
| [Deprecated]/Text & icon/on Dark/Offer | 2 | outside: 2 |
| [Deprecated]/Text & icon/on Dark/Positive | 27 | outside: 27 |

Новые дизайн-переменные, токены, aliases и стили не создавались. Raw-цвета, тексты, геометрия, свойства вариантов и состав компонентов не менялись. Стили эффектов Blur не входят в счётчик старых цветовых стилей. Полные ID изменённых слоёв, агрегация оставшихся стилей и примеры остатков находятся в tabgroup-color-migration-audit.json.
