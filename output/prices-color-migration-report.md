# Ценники — миграция цветов

[Страница в Figma](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9821-75489)

## Результат

- Проверены все **20 мастеров**, **450 слоёв** в них и вложениях; полный аудит страницы охватил **461 узел**.
- Обновлены **136 уникальных слоёв**: 135 согласованных замен старых стилей на color и одна замена **Brand/Partners/Sber Gradient → color.partners.sber-gradient** в слое `24049:334227`.
- В Light выполнены только ранее согласованные прямые замены on Light Primary/Secondary/Third → inverse: **30 привязок**. Остальные Light-применения исключены.
- Дополнительных белых/чёрных текстов или иконок, требующих static поверх цветного фона, не найдено.
- Итоговая программная проверка охватила заливки, обводки, текстовые диапазоны, регионы векторов, эффекты и переменные. Ошибок чтения и записи нет. Проверка Selection colors вручную в интерфейсе не выполнялась.

## Остатки для согласования

В рабочей области осталось **26 применений старых PAINT-стилей**:

| Старый стиль | Количество | Где | Причина / существующие кандидаты |
|---|---:|---|---|
| Мастер/Зелёный | 21 | Sber / Mini Spasibo → MasterGradient → Rectangle 13, например [Prices 1720+](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=22601-326409) | Это сплошной фирменный зелёный, несмотря на название контейнера MasterGradient. Соответствие актуальному color-токену для логотипа не подтверждено. color.fill.solid.positive возможен только при согласовании изменения брендового цвета; Sber Gradient не является прямой заменой сплошного цвета. |
| Brand/Partners/Sber Spasibo | 5 | «+4» в [🟡 Prices 1720+](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=24073-332273) и остальных размерах | Кандидат color.text-icon.positive потребует согласования перехода от фирменного цвета к семантическому позитивному статусу. |

Дополнительно **21 применение внутри Mini Spasibo в рабочей области** ссылается на **недоступный стиль** `c38d96e2b589d88e9c68e120758d601ad2670f88`, например `I24047:331831;25781:341` → region0. Ещё 10 его применений находятся в Light. Figma не разрешает объект стиля, поэтому его нельзя подтвердить как актуальный или подобрать замену по исходному токену. Эти применения **не включены** в 26 известных старых стилей; они оставлены как отдельный нерешённый остаток. Нужны восстановление источника/логотипа или явное решение о целевом токене.

## Исключённые области

- В Light осталось **25 применений известных старых стилей**: 10 Мастер/Зелёный, 5 Sber Spasibo и 10 Warning. Отдельно там остаются 5 привязок старой переменной Fill/Solid/Primary и 10 ссылок на недоступный стиль Mini Spasibo.
- **3 старые привязки** к on Dark Primary у заголовков вне мастеров оставлены без прямых изменений.
- Новые токены, переменные, коллекции и дубликаты не создавались. Цвета без токена сохранены. Структура, геометрия, тексты и свойства вариантов не менялись; инстансы не отсоединялись и не сбрасывались.

## Полный список 26 известных старых применений

1. [Мастер 22601:326409](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=22601-326409), слой `I24047:331831;25781:343`, `fills` — Мастер/Зелёный в Mini Spasibo.
2. [Мастер 22601:326417](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=22601-326417), слой `I22601:326434;25781:343`, `fills` — Мастер/Зелёный в Mini Spasibo.
3. [Мастер 22601:325698](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=22601-325698), слой `I24049:333006;25781:343`, `fills` — Мастер/Зелёный в Mini Spasibo.
4. [Мастер 15815:175846](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=15815-175846), слой `I15815:175843;25781:343`, `fills` — Мастер/Зелёный в Mini Spasibo.
5. [Мастер 22601:326345](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=22601-326345), слой `I24049:333843;25781:343`, `fills` — Мастер/Зелёный в Mini Spasibo.
6. [Мастер 22601:326354](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=22601-326354), слой `I22601:326370;25781:343`, `fills` — Мастер/Зелёный в Mini Spasibo.
7. [Мастер 22601:326281](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=22601-326281), слой `I24049:334213;25781:343`, `fills` — Мастер/Зелёный в Mini Spasibo.
8. [Мастер 22601:326290](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=22601-326290), слой `I24049:334228;25781:343`, `fills` — Мастер/Зелёный в Mini Spasibo.
9. [Мастер 22601:326290](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=22601-326290), слой `I22601:326306;25781:343`, `fills` — Мастер/Зелёный в Mini Spasibo.
10. [Мастер 22601:325728](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=22601-325728), слой `I24049:334234;25781:343`, `fills` — Мастер/Зелёный в Mini Spasibo.
11. [Мастер 21274:311255](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=21274-311255), слой `I21274:311270;25781:343`, `fills` — Мастер/Зелёный в Mini Spasibo.
12. [Мастер 24073:332273](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=24073-332273), слой `24073:332280`, `fills` — Brand/Partners/Sber Spasibo в +4.
13. [Мастер 24073:332273](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=24073-332273), слой `I24073:332281;25781:343`, `fills` — Мастер/Зелёный в Mini Spasibo.
14. [Мастер 24073:332273](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=24073-332273), слой `I24073:332284;25781:343`, `fills` — Мастер/Зелёный в Mini Spasibo.
15. [Мастер 24073:332302](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=24073-332302), слой `24073:332309`, `fills` — Brand/Partners/Sber Spasibo в +4.
16. [Мастер 24073:332302](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=24073-332302), слой `I24073:332310;25781:343`, `fills` — Мастер/Зелёный в Mini Spasibo.
17. [Мастер 24073:332302](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=24073-332302), слой `I24073:332313;25781:343`, `fills` — Мастер/Зелёный в Mini Spasibo.
18. [Мастер 24073:332331](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=24073-332331), слой `24073:332338`, `fills` — Brand/Partners/Sber Spasibo в +4.
19. [Мастер 24073:332331](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=24073-332331), слой `I24073:332339;25781:343`, `fills` — Мастер/Зелёный в Mini Spasibo.
20. [Мастер 24073:332331](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=24073-332331), слой `I24073:332342;25781:343`, `fills` — Мастер/Зелёный в Mini Spasibo.
21. [Мастер 24073:332359](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=24073-332359), слой `24073:332366`, `fills` — Brand/Partners/Sber Spasibo в +4.
22. [Мастер 24073:332359](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=24073-332359), слой `I24073:332367;25781:343`, `fills` — Мастер/Зелёный в Mini Spasibo.
23. [Мастер 24073:332359](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=24073-332359), слой `I24073:332370;25781:343`, `fills` — Мастер/Зелёный в Mini Spasibo.
24. [Мастер 24073:332387](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=24073-332387), слой `24073:332394`, `fills` — Brand/Partners/Sber Spasibo в +4.
25. [Мастер 24073:332387](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=24073-332387), слой `I24073:332395;25781:343`, `fills` — Мастер/Зелёный в Mini Spasibo.
26. [Мастер 24073:332387](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=24073-332387), слой `I24073:332398;25781:343`, `fills` — Мастер/Зелёный в Mini Spasibo.

