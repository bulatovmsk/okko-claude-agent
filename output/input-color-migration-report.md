# Миграция цветов Input

Дата: 20 октября 2026.

[Страница Input в Figma](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=19198-297441).

Заменено 525 цветовых привязок у 525 слоёв: 372 в собственных слоях мастеров и 153 во вложенных слоях мастеров. Обработаны Text input, Textarea, .Symbol input / Item, Symbol input и старые самостоятельные мастера этой страницы.

Согласованные ранее исключения для Text & icon/on Light заменены на color/text-icon/inverse: 76 primary, 20 secondary, 12 third. Остальные Light-привязки не менялись.

Повторно проверены все 2657 слоёв и 204 корневых объектов, включая невидимые вложенные слои, fills, strokes, vector regions, текстовые диапазоны и переменные. В разрешённых к обработке Dark-мастерах не осталось старых стилей или примитивных цветовых переменных. Неоднозначных замен в этом объёме нет. Ошибок чтения и записи нет.

Отдельная проверка текста и иконок на цветных фонах не выявила подходящих слоёв для замены на static. Все доступные локальные зависимости находятся на этой же странице и вошли в обработку. Удалённые зависимости перечислены в JSON; старых привязок в их обработанных вложенных слоях не осталось.

## Оставшиеся старые стили

Это число применений стилей, а не уникальных цветов или слоёв. Selection colors всей страницы продолжит показывать старые цвета из исключённых областей.

- Light: 342 применений.
- Kids вне мастеров: 1 применение.
- Остальные объекты вне мастеров: 392 применений.

| Старый стиль | Всего | Области | Пример слоя |
|---|---:|---|---|
| [Deprecated]/Border/Glassy | 240 | light: 240 | [22801:327751](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=22801-327751) |
| [Deprecated]/Fill/Solid/Secondary | 25 | light: 24, outside: 1 | [22801:327756](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=22801-327756) |
| [Deprecated]/Fill/Solid/Negative | 48 | light: 48 | [22801:327768](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=22801-327768) |
| [Deprecated]/Text & icon/on Dark/Negative | 18 | light: 18 | [22801:327769](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=22801-327769) |
| [Deprecated]/Text & icon/on Dark/Third | 38 | light: 12, outside: 26 | [22801:327804](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=22801-327804) |
| [Deprecated]/Text & icon/on Dark/Primary | 177 | outside: 177 | [22796:326437](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=22796-326437) |
| [Deprecated]/Text & icon/on Dark/Secondary | 21 | outside: 20, kids: 1 | [19455:299217](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=19455-299217) |
| [Deprecated]/Background/Solid/Secondary | 25 | outside: 25 | [20583:307143](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=20583-307143) |
| Fill/Glassy/Secondary | 63 | outside: 63 | [20583:307149](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=20583-307149) |
| Text & icon/on Dark/Primary | 63 | outside: 63 | [I20583:307149;20252:303665](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I20583-307149;20252-303665) |
| [Deprecated]/Fill/Glassy/Third | 5 | outside: 5 | [20736:305403](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=20736-305403) |
| [Deprecated]/Fill/Solid/Inverse | 1 | outside: 1 | [20736:305408](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=20736-305408) |
| [Deprecated]/Fill/Glassy: hover & focus/Third | 3 | outside: 3 | [I20588:307517;21956:326177](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I20588-307517;21956-326177) |
| [Deprecated]/Fill/Solid/Accent | 2 | outside: 2 | [20601:306360](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=20601-306360) |
| [Deprecated]/Background/Solid/Primary | 1 | outside: 1 | [20601:306370](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=20601-306370) |
| [Deprecated]/Border/Active | 2 | outside: 2 | [20601:306376](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=20601-306376) |
| [Deprecated]/Fill/Solid/Positive | 3 | outside: 3 | [22802:329541](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=22802-329541) |

Примитивные переменные остались только в Light (red600, 18 применений) и вне мастеров (electric900, 2 применения). Цвета без токена не изменялись. Новые переменные и стили не создавались. Геометрия, свойства вариантов, тексты и состав компонентов не менялись.

Все напрямую изменённые ID и данные повторной проверки находятся в соседнем файле input-color-migration-audit.json.
