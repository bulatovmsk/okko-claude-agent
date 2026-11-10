# Миграция цветов List

Дата: 20 октября 2026.

[Страница List](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=20853-305387). Проверены все 3406 слоёв, включая скрытые вложенные слои и векторные регионы. На странице 225 мастер-компонентов.

Изменено 607 уникальных слоёв страницы; выполнено 607 замен привязок. Дополнительно исправлен один исходный слой в Head Library.

## Сделано

- 451 замена старых токенов в собственных слоях мастеров.
- 90 замен во вложенных слоях мастеров, включая заливки Switch и Button Loading. Пять из найденных 95 привязок уже обновились по наследованию и повторно не записывались.
- 57 обновлений старых версий существующих стилей: 48 Skeleton и 9 Sber Gradient. Их имена были актуальными, но остановки градиента ссылались на старые Technical-коллекции. Повторная проверка: старых Technical-привязок нет.
- Девять белых галочек Checkbox на цветном фоне → color/static/solid/white с сохранением эффективной прозрачности.
- В [исходном векторе Kaspi 27432:1144](https://www.figma.com/design/HYB1u9ysALVWtVWKoagiDH/?node-id=27432-1144) старый Text & icon/on Dark/Primary региона заменён на color/text-icon/primary. Красный raw-регион и геометрия сохранены; максимальное смещение вершин 0. Библиотека не публиковалась.

## Осталось внутри мастеров

| Группа | Количество применений | Причина |
|---|---:|---|
| Kaspi, старый Primary в двух векторных регионах | 2 | Исходник исправлен, экземпляры содержат старую библиотечную версию. API запрещает менять vector-data внутри экземпляра. Нужны выпуск и применение библиотечного обновления. |
| Brand/Partners/Sber, однотонный зелёный | 2 | По вашему правилу не меняем. |
| Мастер/Зелёный в SquareSpasibo | 11 | Зелёный партнёрский цвет Sber, оставлен по правилу о сохранении однотонного Sber. |
| Нераспознанный стиль c38d96… белого вектора Mini Spasibo | 11 | Figma не возвращает описание стиля; значение белое, но исходное соответствие не установлено. Кандидат color/static/solid/white, требует решения. Регион вложенного вектора дополнительно ограничен API. |

Kaspi: [первый экземпляр](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=41974-1430), [второй экземпляр](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=46165-721).

Нераспознанные белые векторы:

- [I21039:307265;21201:329341;25781:341](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I21039-307265;21201-329341;25781-341) — 🔴 itemList > breakpoint=1720, Background=True, Right=Logo, Pay Card=False > Logo / SquareSpasibo > Sber / Mini Spasibo > Vector
- [I21039:307374;21201:329341;25781:341](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I21039-307374;21201-329341;25781-341) — 🔴 itemList > breakpoint=1720, Background=False, Right=Logo, Pay Card=False > Logo / SquareSpasibo > Sber / Mini Spasibo > Vector
- [I21039:307366;21201:329341;25781:341](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I21039-307366;21201-329341;25781-341) — 🔴 itemList > breakpoint=1320, Background=True, Right=Logo, Pay Card=False > Logo / SquareSpasibo > Sber / Mini Spasibo > Vector
- [I21039:307350;21201:329341;25781:341](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I21039-307350;21201-329341;25781-341) — 🔴 itemList > breakpoint=600, Background=True, Right=Logo, Pay Card=False > Logo / SquareSpasibo > Sber / Mini Spasibo > Vector
- [I21039:307358;21201:329341;25781:341](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I21039-307358;21201-329341;25781-341) — 🔴 itemList > breakpoint=375, Background=True, Right=Logo, Pay Card=False > Logo / SquareSpasibo > Sber / Mini Spasibo > Vector
- [I21039:307326;21201:329341;25781:341](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I21039-307326;21201-329341;25781-341) — 🔴 itemList > breakpoint=320, Background=True, Right=Logo, Pay Card=False > Logo / SquareSpasibo > Sber / Mini Spasibo > Vector
- [I21039:307342;21201:329341;25781:341](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I21039-307342;21201-329341;25781-341) — 🔴 itemList > breakpoint=1320, Background=False, Right=Logo, Pay Card=False > Logo / SquareSpasibo > Sber / Mini Spasibo > Vector
- [I21039:307334;21201:329341;25781:341](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I21039-307334;21201-329341;25781-341) — 🔴 itemList > breakpoint=600, Background=False, Right=Logo, Pay Card=False > Logo / SquareSpasibo > Sber / Mini Spasibo > Vector
- [I21039:307318;21201:329341;25781:341](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I21039-307318;21201-329341;25781-341) — 🔴 itemList > breakpoint=375, Background=False, Right=Logo, Pay Card=False > Logo / SquareSpasibo > Sber / Mini Spasibo > Vector
- [I21039:307295;21201:329341;25781:341](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I21039-307295;21201-329341;25781-341) — 🔴 itemList > breakpoint=320, Background=False, Right=Logo, Pay Card=False > Logo / SquareSpasibo > Sber / Mini Spasibo > Vector
- [I21201:329341;25781:341](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I21201-329341;25781-341) — Logo > Logo / SquareSpasibo > Sber / Mini Spasibo > Vector

## Спорные замены на static

В List Item V2 / Action / Filled / Negative оставлены 18 красных текстовых и иконных заливок: 9 вариантов (320+, 600+, 1720+ × Rest, Touch, Disabled). Сейчас color/text-icon/negative. Существующего static-red нет. Кандидаты — static/solid/white или black, но они изменят цвет. Без согласования не менял.

| Вариант и слой | Ссылка |
|---|---|
| 🟡 List Item V2 > Breakpoint=320+, Variant=Action, Style=Filled, Type=🔴 Negative, State=Rest > Content > Left > Mark / Star_Bold > Union | [I46165:982;32958:4332](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I46165-982;32958-4332) |
| 🟡 List Item V2 > Breakpoint=320+, Variant=Action, Style=Filled, Type=🔴 Negative, State=Rest > Content > Left > Text Box > Title | [46165:984](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=46165-984) |
| 🟡 List Item V2 > Breakpoint=320+, Variant=Action, Style=Filled, Type=🔴 Negative, State=Touch > Content > Left > Mark / Star_Bold > Union | [I46165:988;32958:4332](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I46165-988;32958-4332) |
| 🟡 List Item V2 > Breakpoint=320+, Variant=Action, Style=Filled, Type=🔴 Negative, State=Touch > Content > Left > Text Box > Title | [46165:990](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=46165-990) |
| 🟡 List Item V2 > Breakpoint=320+, Variant=Action, Style=Filled, Type=🔴 Negative, State=Disabled > Content > Left > Mark / Star_Bold > Union | [I46165:994;32958:4332](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I46165-994;32958-4332) |
| 🟡 List Item V2 > Breakpoint=320+, Variant=Action, Style=Filled, Type=🔴 Negative, State=Disabled > Content > Left > Text Box > Title | [46165:996](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=46165-996) |
| 🟡 List Item V2 > Breakpoint=600+, Variant=Action, Style=Filled, Type=🔴 Negative, State=Rest > Content > Left > Mark / Star_Bold > Union | [I46165:1512;32958:4332](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I46165-1512;32958-4332) |
| 🟡 List Item V2 > Breakpoint=600+, Variant=Action, Style=Filled, Type=🔴 Negative, State=Rest > Content > Left > Text Container > Title | [46165:1514](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=46165-1514) |
| 🟡 List Item V2 > Breakpoint=1720+, Variant=Action, Style=Filled, Type=🔴 Negative, State=Rest > Content > Left > Mark / Star_Bold > Union | [I46165:1518;32958:4332](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I46165-1518;32958-4332) |
| 🟡 List Item V2 > Breakpoint=1720+, Variant=Action, Style=Filled, Type=🔴 Negative, State=Rest > Content > Left > Text Container > Title | [46165:1520](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=46165-1520) |
| 🟡 List Item V2 > Breakpoint=600+, Variant=Action, Style=Filled, Type=🔴 Negative, State=Touch > Content > Left > Mark / Star_Bold > Union | [I46165:1524;32958:4332](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I46165-1524;32958-4332) |
| 🟡 List Item V2 > Breakpoint=600+, Variant=Action, Style=Filled, Type=🔴 Negative, State=Touch > Content > Left > Text Container > Title | [46165:1526](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=46165-1526) |
| 🟡 List Item V2 > Breakpoint=1720+, Variant=Action, Style=Filled, Type=🔴 Negative, State=Touch > Content > Left > Mark / Star_Bold > Union | [I46165:1530;32958:4332](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I46165-1530;32958-4332) |
| 🟡 List Item V2 > Breakpoint=1720+, Variant=Action, Style=Filled, Type=🔴 Negative, State=Touch > Content > Left > Text Container > Title | [46165:1532](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=46165-1532) |
| 🟡 List Item V2 > Breakpoint=600+, Variant=Action, Style=Filled, Type=🔴 Negative, State=Disabled > Content > Left > Mark / Star_Bold > Union | [I46165:1536;32958:4332](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I46165-1536;32958-4332) |
| 🟡 List Item V2 > Breakpoint=600+, Variant=Action, Style=Filled, Type=🔴 Negative, State=Disabled > Content > Left > Text Container > Title | [46165:1538](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=46165-1538) |
| 🟡 List Item V2 > Breakpoint=1720+, Variant=Action, Style=Filled, Type=🔴 Negative, State=Disabled > Content > Left > Mark / Star_Bold > Union | [I46165:1542;32958:4332](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I46165-1542;32958-4332) |
| 🟡 List Item V2 > Breakpoint=1720+, Variant=Action, Style=Filled, Type=🔴 Negative, State=Disabled > Content > Left > Text Container > Title | [46165:1544](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=46165-1544) |

Повторная проверка не нашла оставшихся однозначных белых/чёрных static-замен. Акцентные иконки Switch на нейтральном круге оставлены тематическими: цветной внешний трек не является их непосредственной подложкой. 54 raw-заливки в проверке цветных фонов не менялись.

## Вне мастеров

213 применений старых цветовых стилей оставлены в примерах, описаниях свойств и контейнерах. Они будут видны в Selection colors всей страницы. Один primitive/electric900 также находится вне мастеров.

Итого по всей странице осталось 228 применений известных старых PAINT-стилей: 213 вне мастеров и 15 внутри (13 отложенных зелёных Sber и 2 Kaspi). Ещё 11 нераспознанных применений посчитаны отдельно. В собственных слоях мастеров старых стилей нет.

Новые дизайн-переменные, aliases и стили не создавались. Цвета без токена сохранены. Тексты, свойства вариантов, геометрия и состав компонентов не менялись. Полные ID изменённых слоёв и остатков сохранены в list-color-migration-audit.json.
