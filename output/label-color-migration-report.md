# Миграция цветов Label

Дата: 20 октября 2026.

[Страница Label](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16623-178658).

Изменено 259 уникальных слоёв страницы, выполнено 283 замен привязок. Проверены все 1621 слой, в том числе скрытые вложенные слои и регионы векторов. Наборы: Label Rich, Label - Small, Label - Large, Bet Label, Indicator Label, Spasibo Badge; всего 132 варианта.

## Изменения

- 207 согласованных замен в собственных слоях мастеров, 26 во вложенных слоях.
- Три фона Label - Large / theme=Continuum: Brand/Okko/Accent → существующий color/component/label/continuum, по роли варианта.
- 47 текстовых слоёв и иконок на цветных фонах → color/static/solid/white или black. Цвет и эффективная прозрачность при этой замене сохранены; старый alpha 0.96 перенесён в opacity слоя.
- Повторная static-проверка: 56 подходящих слоёв уже на static, новых подходящих замен нет. Три raw-заливки Spasibo Badge не менялись: [I45683:10495;45683:10507](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I45683-10495;45683-10507), [I45683:10497;45683:10507](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I45683-10497;45683-10507), [I45683:10499;45683:10507](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I45683-10499;45683-10507).
- В Head Library исправлен исходный мастер Bet Logo(Full) / Partner=Placeholder: [вектор 24384:3936](https://www.figma.com/design/HYB1u9ysALVWtVWKoagiDH/?node-id=24384-3936). Три региона Fill/Solid/Inverse привязаны к color/fill/solid/inverse. Геометрия и топология сохранены, максимальное смещение вершин 0. Библиотека не публиковалась.

## Оставшиеся случаи внутри обрабатываемых мастеров

В трёх экземплярах Bet Logo(Full) осталась опубликованная старая версия векторных регионов. API запрещает изменение vector-data внутри экземпляра; экземпляры не отсоединялись. Обычная смена fills здесь не заменит цвета отдельных регионов.

| Мастер Bet Label | Экземпляр | Вектор |
|---|---|---|
| [Breakpoint=320+, Partner=Placeholder](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=30392-1742) | [30392:1753](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=30392-1753) | I30392:1753;24384:3936 |
| [Breakpoint=600+, Partner=Placeholder](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=30392-1960) | [30392:1971](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=30392-1971) | I30392:1971;24384:3936 |
| [Breakpoint=1320+, Partner=Placeholder](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=30392-2046) | [30392:2057](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=30392-2057) | I30392:2057;24384:3936 |

- Три региона (по одному в каждом экземпляре): старый Fill/Solid/Primary, key 974f85…, который в Head определяется как Fill/Solid/Inverse. Замена согласована, источник исправлен. Для экземпляров нужен выпуск и применение библиотечного обновления; регион может иметь локальное переопределение.
- Шесть регионов (по два в каждом экземпляре): старый Color/fill/solid/hover-focus/Third, key 7190d7…. Это радиальный градиент, хотя имя выглядит актуальным. Возможные замены: актуальный color/fill/solid/hover-focus/third (линейный градиент, key 362c7a…) либо семантическая заливка нейтрального логотипа. Оставлены из-за неоднозначности роли и отличия геометрии градиента; источник использует inverse, тогда как в этих экземплярах стоят локальные градиентные переопределения.

## Исключённые области

Осталось 12 применений старых PAINT-стилей в Light и 164 вне мастеров (подписи, демонстрации, контейнеры и примеры). Они будут видны в Selection colors всей страницы. Примитивные цветовые переменные после работы находятся только в Light и вне мастеров. Стили эффектов Blur не относятся к миграции цветов.

| Старый стиль | Количество | Области |
|---|---:|---|
| [Deprecated]/Border/Contour | 4 | outside: 4 |
| [Deprecated]/Text & icon/on Dark/Primary | 73 | outside: 67, light: 6 |
| [Deprecated]/Text & icon/on Dark/Secondary | 17 | outside: 17 |
| [Deprecated]/Background/Solid/Secondary | 7 | outside: 7 |
| [Deprecated]/Fill/Glassy/Secondary | 11 | outside: 11 |
| Fill/Glassy/Secondary | 2 | outside: 2 |
| Text & icon/on Dark/Primary | 24 | outside: 24 |
| [Deprecated]/Text & icon/on Dark/Accent | 1 | outside: 1 |
| [Deprecated]/Fill/Solid/Secondary | 1 | outside: 1 |
| Border/Glassy | 16 | outside: 16 |
| [Deprecated]/Brand/Okko/AdditionalB | 7 | outside: 1, light: 6 |
| [Deprecated]/Brand/Okko/Accent | 1 | outside: 1 |
| [Deprecated]/Fill/Solid/Live | 1 | outside: 1 |
| [Deprecated]/Background/Glassy/Secondary | 1 | outside: 1 |
| [Deprecated]/Fill/Solid/Inverse | 1 | outside: 1 |
| [Deprecated]/Text & icon/on Light/Primary | 2 | outside: 2 |
| [Deprecated]/Fill/Solid/Positive | 1 | outside: 1 |
| [Deprecated]/Fill/Decorative/Lemon | 1 | outside: 1 |
| [Deprecated]/Border/Glassy | 2 | outside: 2 |
| [Deprecated]/Background/Solid/Primary | 2 | outside: 2 |
| [Deprecated]/Text & icon/on Dark/Warning | 1 | outside: 1 |
| Fill/Solid/Primary | 3 | instance: 3 |

Новые дизайн-переменные и стили не создавались. Raw-цвета не менялись. Состав компонентов, тексты, свойства вариантов и геометрия сохранены. Полные ID напрямую изменённых слоёв и результаты проверки сохранены в label-color-migration-audit.json.
