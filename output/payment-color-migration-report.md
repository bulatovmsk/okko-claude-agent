# Оплата — миграция цветов

[Страница в Figma](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9821-75488)

## Результат

- Проверены **190 мастеров** и **7563 слоя** в них и их вложениях. Вне мастеров проверены ещё **83 узла**, всего **7646**.
- Обновлены **1035 уникальных слоёв**. Автоматически изменившиеся через наследование инстансы отдельно к числу прямых изменений не добавлялись.
- В **30 текстовых слоях** заменены **50 диапазонов** со смешанными цветами, включая ранее согласованные inverse-исключения в Light.
- В **3 слоях** на цветных фонах применены static-токены с сохранением видимой прозрачности.
- Включённые радио и переключатели с AccentB переведены на существующий **color.fill.solid.accent**. Прямо изменены 3 слоя; ещё 3 применения обновились через наследование.
- Все итоговые проверки заливок, обводок, текстовых диапазонов, регионов векторов, эффектов и привязок завершились без ошибок чтения. Один мастер оплаты проверен визуально после изменений. Ручная проверка Selection colors в интерфейсе не выполнялась.

## Остатки для решения

В рабочей области осталось **72 применения старых PAINT-стилей**. Дополнительно сохранены **6 привязок solid Sber**, согласно прежней договорённости. Счётчики означают применения в свойствах и регионах, а не число уникальных цветов.

| Старый стиль | Применений | Где | Причина / кандидаты |
|---|---:|---|---|
| Мастер/Зелёный | 30 | Sber / Mini Spasibo → MasterGradient → Rectangle 13. [Пример мастера](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16108-174510) | Это сплошной фирменный зелёный (#21A038), а не градиент. Подходящий актуальный семантический токен для зелёного логотипа «Спасибо» не подтверждён. Не применять color.partners.sber-gradient автоматически. |
| Primitives/Grey/Medium | 7 | Линии карты, «Отвязать карту», правила акции. [Пример мастера](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=4419-24852) | Кандидаты: color.border.glassy или color.border.solid. Нужно согласовать роль и прозрачность линий; одна замена по оттенку неоднозначна. |
| Primitives/Black/Primary / Black / Primary | 9 | «Отвязать карту», фон старого инпута, регион логотипа Сбер. [Пример мастера](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=4419-24852) | Для текста кандидаты color.text-icon.primary / negative, для фона — color.fill.solid.* / color.background.solid.*, для логотипа — статический чёрный. Роли различаются, общая замена не подходит. Смешанные регионы вложенного вектора нельзя перекрашивать целиком. |
| [Deprecated]/Brand/Partners/Sber | 3 | Логотипы Сбер в блоках оплаты. [Пример мастера](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=4419-24537) | Solid Sber ранее решено пока не менять. Дополнительно сохранены 6 привязок brand/partners/sber, они не входят в 72 применения PAINT-стилей. |
| Primitives/Grey/Primary | 11 | «или», правила акции, пометка «Основная». [Пример мастера](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16119-174569) | Кандидаты color.text-icon.secondary / third. Требуется согласовать иерархию и контраст этих второстепенных текстов. |
| Text & icon/on Dark/Primary | 2 | Номер «1984» на банковской карте SberPay, Desktop/Mobile. [Пример мастера](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16119-174631) | Соответствие color.text-icon.primary известно, но Figma не может загрузить текущий Avenir Next Demi Bold. Два слоя оставлены без изменения шрифта. На цветной карте нужно также проверить применение статического белого после устранения ограничения. |
| Brand/Partners/Sber Spasibo | 10 | Purchase → Income Spasibo → «+4». [Пример мастера](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=24064-332173) | Фирменный Sber Spasibo. Кандидат color.text-icon.positive возможен только при согласовании замены брендового цвета на семантический позитивный статус; прямое соответствие не подтверждено. |

## Шрифт

Figma вернула ошибку загрузки **Avenir Next Demi Bold**: семейство Avenir Next отсутствует в доступной среде. Шрифт не подменялся. Два оставшихся текстовых слоя: `I16119:174638;876:77` и `I16119:174629;876:77`. При необходимости их можно заменить вручную в среде с установленным исходным шрифтом.

## Исключения и актуальные ресурсы

- В Light осталось **371 применение старых стилей**. Прямые изменения там ограничены заранее согласованными on Light Primary/Secondary/Third/Forth → inverse.
- Вне мастеров осталось **23 применения старых стилей**: 7 в Light и 16 в остальных контейнерах/примерах. Они учтены отдельно от 72 и не менялись напрямую.
- Четыре градиента Sber в банковских картах уже используют актуальные ключи **color.partners.sber-gradient** и его четырёх стопов. Разные идентификаторы импортированных коллекций сами по себе не делают эти привязки устаревшими; они оставлены актуальными.
- **Мастер/Зелёный** в логотипах «Спасибо» — SOLID, поэтому его не заменял согласованным градиентом Sber только из-за имени контейнера MasterGradient.
- Цвета без стиля/переменной сохранены. Новые переменные, токены и коллекции не создавались. Структура, геометрия, тексты и свойства вариантов не менялись. Инстансы не отсоединялись и не сбрасывались.

## Все оставшиеся применения в рабочей области

1. **Мастер/Зелёный** — [мастер 16108:174510](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16108-174510), слой `I16108:174502;25781:343`, свойство `fills`.
   Сводка покупки > Сводка покупки > Сводка покупки > Type=SVOD, Breackpoints=1720+ > Наполнение > Цены > Списание бонусов > Бонусы > Sber / Mini Spasibo > MasterGradient > Rectangle 13
2. **Мастер/Зелёный** — [мастер 21791:323493](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=21791-323493), слой `I21791:323507;25781:343`, свойство `fills`.
   Сводка покупки > Сводка покупки > Сводка покупки > Type=SVOD, Breackpoints=1320+ > Наполнение > Цены > Списание бонусов > Бонусы > Sber / Mini Spasibo > MasterGradient > Rectangle 13
3. **Мастер/Зелёный** — [мастер 21791:324213](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=21791-324213), слой `I21791:324227;25781:343`, свойство `fills`.
   Сводка покупки > Сводка покупки > Сводка покупки > Type=SVOD, Breackpoints=600+ > Наполнение > Цены > Списание бонусов > Бонусы > Sber / Mini Spasibo > MasterGradient > Rectangle 13
4. **Мастер/Зелёный** — [мастер 16122:175487](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16122-175487), слой `I16122:175526;25781:343`, свойство `fills`.
   Сводка покупки > Сводка покупки > Сводка покупки > Type=SVOD, Breackpoints=375+ > Наполнение > Название+Цены > Цены > Списание бонусов > Бонусы > Sber / Mini Spasibo > MasterGradient > Rectangle 13
5. **Мастер/Зелёный** — [мастер 21791:325045](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=21791-325045), слой `I21791:325060;25781:343`, свойство `fills`.
   Сводка покупки > Сводка покупки > Сводка покупки > Type=SVOD, Breackpoints=320+ > Наполнение > Название+Цены > Цены > Списание бонусов > Бонусы > Sber / Mini Spasibo > MasterGradient > Rectangle 13
6. **Мастер/Зелёный** — [мастер 16108:174746](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16108-174746), слой `I16108:174724;25781:343`, свойство `fills`.
   Сводка покупки > Сводка покупки > Сводка покупки > Type=TVOD, Breackpoints=1720+ > Наполнение > Цены > Бонусы > Бонусы > Sber / Mini Spasibo > MasterGradient > Rectangle 13
7. **Мастер/Зелёный** — [мастер 21791:323829](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=21791-323829), слой `I21791:323850;25781:343`, свойство `fills`.
   Сводка покупки > Сводка покупки > Сводка покупки > Type=TVOD, Breackpoints=1320+ > Наполнение > Цены > Бонусы > Бонусы > Sber / Mini Spasibo > MasterGradient > Rectangle 13
8. **Мастер/Зелёный** — [мастер 21791:324416](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=21791-324416), слой `I21791:324437;25781:343`, свойство `fills`.
   Сводка покупки > Сводка покупки > Сводка покупки > Type=TVOD, Breackpoints=600+ > Наполнение > Цены > Бонусы > Бонусы > Sber / Mini Spasibo > MasterGradient > Rectangle 13
9. **Мастер/Зелёный** — [мастер 16122:175563](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16122-175563), слой `I16122:175578;25781:343`, свойство `fills`.
   Сводка покупки > Сводка покупки > Сводка покупки > Type=TVOD, Breackpoints=375+ > Наполнение > Название+Цены > Цены > Бонусы > Бонусы > Sber / Mini Spasibo > MasterGradient > Rectangle 13
10. **Мастер/Зелёный** — [мастер 21791:325071](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=21791-325071), слой `I21791:325092;25781:343`, свойство `fills`.
   Сводка покупки > Сводка покупки > Сводка покупки > Type=TVOD, Breackpoints=320+ > Наполнение > Название+Цены > Цены > Бонусы > Бонусы > Sber / Mini Spasibo > MasterGradient > Rectangle 13
11. **Primitives/Grey/Medium** — [мастер 4419:24852](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=4419-24852), слой `4419:24819`, свойство `strokes`.
   Ячейка / Оплата  > Ячейка / Оплата  > Ячейка / Оплата / On Dark > Ресурсы / On Dark > x / Оплата / Привязанная карта / On Dark > Размер=Mobile, Спасибо=False > отвязать > Line 6
12. **Primitives/Black/Primary** — [мастер 4419:24852](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=4419-24852), слой `4419:24820`, свойство `fills`.
   Ячейка / Оплата  > Ячейка / Оплата  > Ячейка / Оплата / On Dark > Ресурсы / On Dark > x / Оплата / Привязанная карта / On Dark > Размер=Mobile, Спасибо=False > отвязать > Отвязать карту
13. **[Deprecated]/Brand/Partners/Sber** — [мастер 4419:24537](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=4419-24537), слой `I4419:24407;4419:24363;1066:16;3022:13`, свойство `region0`.
   Ячейка / Оплата  > Ячейка / Оплата  > Ячейка / Оплата / On Dark > Ресурсы / On Dark > x / Оплата / Заголовок и описание / On Dark > Размер=Mobile, Заголовок=True, Логотип=True > x / Оплата / Заголовок и описание / On Dark > Банки / Сбер > Сбербанк > Vector
14. **[Deprecated]/Brand/Partners/Sber** — [мастер 4419:24391](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=4419-24391), слой `I4419:24363;1066:16;3022:13`, свойство `region0`.
   Ячейка / Оплата  > Ячейка / Оплата  > Ячейка / Оплата / On Dark > Ресурсы / On Dark > x / Оплата / Заголовок и описание / On Dark > Размер=Mobile, Заголовок=False, Логотип=True > Банки / Сбер > Сбербанк > Vector
15. **Primitives/Grey/Primary** — [мастер 16119:174569](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16119-174569), слой `16119:174574`, свойство `fills`.
   Ячейка / Оплата  > Ячейка / Оплата  > Ячейка / Оплата / On Dark > Frame 335023 > Ячейка / Оплата / On Dark > Размер=Mobile, Тип оплаты=Карта, Привязка=False > Кнопки и поле ввода > Apple Pay > Или > или
16. **Primitives/Grey/Primary** — [мастер 16119:174498](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16119-174498), слой `16119:174505`, свойство `fills`.
   Ячейка / Оплата  > Ячейка / Оплата  > Ячейка / Оплата / On Dark > Frame 335023 > Ячейка / Оплата / On Dark > Размер=Desktop, Тип оплаты=Карта, Привязка=False > Оплата > Apple Pay > Или > или
17. **Primitives/Grey/Medium** — [мастер 16119:174498](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16119-174498), слой `I16119:174513;258:137`, свойство `strokes`.
   Ячейка / Оплата  > Ячейка / Оплата  > Ячейка / Оплата / On Dark > Frame 335023 > Ячейка / Оплата / On Dark > Размер=Desktop, Тип оплаты=Карта, Привязка=False > Оплата > Описание, форма и кнопка > Описание и карта > Карта > Frame 37 > Банковская карта / On Dark > Линия
18. **Primitives/Grey/Primary** — [мастер 16119:174593](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16119-174593), слой `16119:174597`, свойство `fills`.
   Ячейка / Оплата  > Ячейка / Оплата  > Ячейка / Оплата / On Dark > Frame 335023 > Ячейка / Оплата / On Dark > Размер=Mobile, Тип оплаты=Карта, Привязка=True > Apple Pay > Или > или
19. **Primitives/Grey/Medium** — [мастер 16119:174593](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16119-174593), слой `I16119:174602;4419:24819`, свойство `strokes`.
   Ячейка / Оплата  > Ячейка / Оплата  > Ячейка / Оплата / On Dark > Frame 335023 > Ячейка / Оплата / On Dark > Размер=Mobile, Тип оплаты=Карта, Привязка=True > Текст, карта и кнопка > x / Оплата / Привязанная карта / On Dark > отвязать > Line 6
20. **Primitives/Black/Primary** — [мастер 16119:174593](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16119-174593), слой `I16119:174602;4419:24820`, свойство `fills`.
   Ячейка / Оплата  > Ячейка / Оплата  > Ячейка / Оплата / On Dark > Frame 335023 > Ячейка / Оплата / On Dark > Размер=Mobile, Тип оплаты=Карта, Привязка=True > Текст, карта и кнопка > x / Оплата / Привязанная карта / On Dark > отвязать > Отвязать карту
21. **Primitives/Grey/Primary** — [мастер 16119:174551](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16119-174551), слой `16119:174557`, свойство `fills`.
   Ячейка / Оплата  > Ячейка / Оплата  > Ячейка / Оплата / On Dark > Frame 335023 > Ячейка / Оплата / On Dark > Размер=Desktop, Тип оплаты=Карта, Привязка=True > Apple Pay > Или > или
22. **Primitives/Grey/Medium** — [мастер 16119:174631](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16119-174631), слой `16119:174636`, свойство `strokes`.
   Ячейка / Оплата  > Ячейка / Оплата  > Ячейка / Оплата / On Dark > Frame 335023 > Ячейка / Оплата / On Dark > Размер=Mobile, Тип оплаты=SberPay, Привязка=True > Автоплатежи > Правила Акции > Line 9
23. **Primitives/Grey/Primary** — [мастер 16119:174631](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16119-174631), слой `16119:174637`, свойство `fills`.
   Ячейка / Оплата  > Ячейка / Оплата  > Ячейка / Оплата / On Dark > Frame 335023 > Ячейка / Оплата / On Dark > Размер=Mobile, Тип оплаты=SberPay, Привязка=True > Автоплатежи > Правила Акции > Нажимая на кнопку «Продолжить» вы соглашаетесь с Правилами Акции
24. **Text & icon/on Dark/Primary** — [мастер 16119:174631](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16119-174631), слой `I16119:174638;876:77`, свойство `fills`.
   Ячейка / Оплата  > Ячейка / Оплата  > Ячейка / Оплата / On Dark > Frame 335023 > Ячейка / Оплата / On Dark > Размер=Mobile, Тип оплаты=SberPay, Привязка=True > Банковская карта > 1984
25. **Text & icon/on Dark/Primary** — [мастер 16119:174627](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16119-174627), слой `I16119:174629;876:77`, свойство `fills`.
   Ячейка / Оплата  > Ячейка / Оплата  > Ячейка / Оплата / On Dark > Frame 335023 > Ячейка / Оплата / On Dark > Размер=Desktop, Тип оплаты=SberPay, Привязка=True > Банковская карта > 1984
26. **Primitives/Grey/Primary** — [мастер 16119:174604](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16119-174604), слой `I16119:174605;16119:174574`, свойство `fills`.
   Ячейка / Оплата  > Ячейка / Оплата  > Ячейка / Оплата / On Dark > Frame 335023 > Ячейка / Оплата / On Dark > Размер=Mobile, Тип оплаты=Спасибо, Привязка=False > Оплата / Mobile / Спасибо / Не привязана > Кнопки и поле ввода > Apple Pay > Или > или
27. **[Deprecated]/Brand/Partners/Sber** — [мастер 16119:174604](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16119-174604), слой `I16119:174605;16119:174578;4419:24363;1066:16;3022:13`, свойство `region0`.
   Ячейка / Оплата  > Ячейка / Оплата  > Ячейка / Оплата / On Dark > Frame 335023 > Ячейка / Оплата / On Dark > Размер=Mobile, Тип оплаты=Спасибо, Привязка=False > Оплата / Mobile / Спасибо / Не привязана > Кнопки и поле ввода > Карта и текст > x / Оплата / Заголовок и описание / On Dark > Банки / Сбер > Сбербанк > Vector
28. **Primitives/Grey/Primary** — [мастер 16119:174521](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16119-174521), слой `I16119:174522;16119:174505`, свойство `fills`.
   Ячейка / Оплата  > Ячейка / Оплата  > Ячейка / Оплата / On Dark > Frame 335023 > Ячейка / Оплата / On Dark > Размер=Desktop, Тип оплаты=Спасибо, Привязка=False > Оплата / Desktop / Спасибо / Не привязана > Оплата > Apple Pay > Или > или
29. **Primitives/Grey/Medium** — [мастер 16119:174521](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16119-174521), слой `I16119:174522;16119:174513;258:137`, свойство `strokes`.
   Ячейка / Оплата  > Ячейка / Оплата  > Ячейка / Оплата / On Dark > Frame 335023 > Ячейка / Оплата / On Dark > Размер=Desktop, Тип оплаты=Спасибо, Привязка=False > Оплата / Desktop / Спасибо / Не привязана > Оплата > Описание, форма и кнопка > Описание и карта > Карта > Frame 37 > Банковская карта / On Dark > Линия
30. **Black / Primary** — [мастер 16119:174616](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16119-174616), слой `I16119:174618;287:95;1066:16;3022:13`, свойство `region0`.
   Ячейка / Оплата  > Ячейка / Оплата  > Ячейка / Оплата / On Dark > Frame 335023 > Ячейка / Оплата / On Dark > Размер=Desktop, Тип оплаты=SberPay, Привязка=False > Форма > x / Оплата /  Desktop / Спасибо / Карта не привязана / Текст с лого > Банки / Сбер > Сбербанк > Vector
31. **Primitives/Black/Primary** — [мастер 16119:174616](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16119-174616), слой `I16119:174620;5105:30461`, свойство `fills`.
   Ячейка / Оплата  > Ячейка / Оплата  > Ячейка / Оплата / On Dark > Frame 335023 > Ячейка / Оплата / On Dark > Размер=Desktop, Тип оплаты=SberPay, Привязка=False > Форма > Инпут + кнопка > Инпут (старые и неадаптивные) > Frame 202 > Rectangle 1243
32. **Primitives/Black/Primary** — [мастер 16119:174622](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16119-174622), слой `I16119:174625;5105:30461`, свойство `fills`.
   Ячейка / Оплата  > Ячейка / Оплата  > Ячейка / Оплата / On Dark > Frame 335023 > Ячейка / Оплата / On Dark > Размер=Mobile, Тип оплаты=SberPay, Привязка=False > Инпут + кнопка > Инпут (старые и неадаптивные) > Frame 202 > Rectangle 1243
33. **Primitives/Black/Primary** — [мастер 16119:174606](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16119-174606), слой `I16119:174608;5105:30461`, свойство `fills`.
   Ячейка / Оплата  > Ячейка / Оплата  > Ячейка / Оплата / On Dark > Frame 335023 > Ячейка / Оплата / On Dark > Размер=Mobile, Тип оплаты=Телефон, Привязка=False > Форма и описание > Инпут (старые и неадаптивные) > Frame 202 > Rectangle 1243
34. **Primitives/Black/Primary** — [мастер 16119:174523](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16119-174523), слой `I16119:174526;5105:30461`, свойство `fills`.
   Ячейка / Оплата  > Ячейка / Оплата  > Ячейка / Оплата / On Dark > Frame 335023 > Ячейка / Оплата / On Dark > Размер=Desktop, Тип оплаты=Телефон, Привязка=False > Ввод телефона и описание > Ввод телефона и логотипы > Инпут (старые и неадаптивные) > Frame 202 > Rectangle 1243
35. **Primitives/Black/Primary** — [мастер 16119:174611](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16119-174611), слой `I16119:174613;5105:30461`, свойство `fills`.
   Ячейка / Оплата  > Ячейка / Оплата  > Ячейка / Оплата / On Dark > Frame 335023 > Ячейка / Оплата / On Dark > Размер=Mobile, Тип оплаты=Телефон, Привязка=True > Форма и описание > Инпут (старые и неадаптивные) > Frame 202 > Rectangle 1243
36. **Primitives/Black/Primary** — [мастер 16119:174537](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16119-174537), слой `I16119:174540;5105:30461`, свойство `fills`.
   Ячейка / Оплата  > Ячейка / Оплата  > Ячейка / Оплата / On Dark > Frame 335023 > Ячейка / Оплата / On Dark > Размер=Desktop, Тип оплаты=Телефон, Привязка=True > Ввод телефона и описание > Ввод телефона и логотипы > Инпут (старые и неадаптивные) > Frame 202 > Rectangle 1243
37. **Primitives/Grey/Medium** — [мастер 15508:173703](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=15508-173703), слой `15508:173720`, свойство `strokes`.
   Банковская карта > Банковская карта > Frame 335025 > Форма ввода БК > Property 1=Mobile, On dark=true > Автоплатежи > Правила Акции > Line 9
38. **Primitives/Grey/Primary** — [мастер 15508:173703](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=15508-173703), слой `15508:173721`, свойство `fills`.
   Банковская карта > Банковская карта > Frame 335025 > Форма ввода БК > Property 1=Mobile, On dark=true > Автоплатежи > Правила Акции > Нажимая на кнопку «Продолжить» вы соглашаетесь с Правилами Акции
39. **Primitives/Grey/Medium** — [мастер 15508:173683](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=15508-173683), слой `15508:173701`, свойство `strokes`.
   Банковская карта > Банковская карта > Frame 335025 > Форма ввода БК > Property 1=Desktop, On dark=true > Автоплатеж > Правила Акции > Line 9
40. **Primitives/Grey/Primary** — [мастер 15508:173683](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=15508-173683), слой `15508:173702`, свойство `fills`.
   Банковская карта > Банковская карта > Frame 335025 > Форма ввода БК > Property 1=Desktop, On dark=true > Автоплатеж > Правила Акции > Нажимая на кнопку «Продолжить» вы соглашаетесь с Правилами Акции.
41. **Primitives/Grey/Primary** — [мастер 16228:175893](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16228-175893), слой `16228:175898`, свойство `fills`.
   Банковская карта > Банковская карта > Frame 335025 > БК привязана > БК привязана / On Dark > Property 1=Desktop, Property 2=Привязана > Frame 37 > Основная
42. **Primitives/Grey/Primary** — [мастер 16228:175902](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16228-175902), слой `16228:175911`, свойство `fills`.
   Банковская карта > Банковская карта > Frame 335025 > БК привязана > БК привязана / On Dark > Property 1=Mobile, Property 2=Привязана > Frame 37 > Основная
43. **Brand/Partners/Sber Spasibo** — [мастер 24064:332173](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=24064-332173), слой `24064:332197`, свойство `fills`.
   Purchase > 🟡 Purchase > Breackpoints=1720+, Type=SVOD, Light theme=False > Prices > Income Spasibo > Бонусы > +4
44. **Мастер/Зелёный** — [мастер 24064:332173](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=24064-332173), слой `I24064:332198;25781:343`, свойство `fills`.
   Purchase > 🟡 Purchase > Breackpoints=1720+, Type=SVOD, Light theme=False > Prices > Income Spasibo > Бонусы > Sber / Mini Spasibo > MasterGradient > Rectangle 13
45. **Мастер/Зелёный** — [мастер 24064:332173](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=24064-332173), слой `I24064:332193;25781:343`, свойство `fills`.
   Purchase > 🟡 Purchase > Breackpoints=1720+, Type=SVOD, Light theme=False > Prices > Outgo Spasibo > Бонусы > Sber / Mini Spasibo > MasterGradient > Rectangle 13
46. **Brand/Partners/Sber Spasibo** — [мастер 24064:332204](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=24064-332204), слой `24064:332228`, свойство `fills`.
   Purchase > 🟡 Purchase > Breackpoints=1320+, Type=SVOD, Light theme=False > Prices > Income Spasibo > Бонусы > +4
47. **Мастер/Зелёный** — [мастер 24064:332204](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=24064-332204), слой `I24064:332229;25781:343`, свойство `fills`.
   Purchase > 🟡 Purchase > Breackpoints=1320+, Type=SVOD, Light theme=False > Prices > Income Spasibo > Бонусы > Sber / Mini Spasibo > MasterGradient > Rectangle 13
48. **Мастер/Зелёный** — [мастер 24064:332204](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=24064-332204), слой `I24064:332224;25781:343`, свойство `fills`.
   Purchase > 🟡 Purchase > Breackpoints=1320+, Type=SVOD, Light theme=False > Prices > Outgo Spasibo > Бонусы > Sber / Mini Spasibo > MasterGradient > Rectangle 13
49. **Brand/Partners/Sber Spasibo** — [мастер 24064:332235](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=24064-332235), слой `24064:332259`, свойство `fills`.
   Purchase > 🟡 Purchase > Breackpoints=600+, Type=SVOD, Light theme=False > Prices > Income Spasibo > Бонусы > +4
50. **Мастер/Зелёный** — [мастер 24064:332235](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=24064-332235), слой `I24064:332260;25781:343`, свойство `fills`.
   Purchase > 🟡 Purchase > Breackpoints=600+, Type=SVOD, Light theme=False > Prices > Income Spasibo > Бонусы > Sber / Mini Spasibo > MasterGradient > Rectangle 13
51. **Мастер/Зелёный** — [мастер 24064:332235](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=24064-332235), слой `I24064:332255;25781:343`, свойство `fills`.
   Purchase > 🟡 Purchase > Breackpoints=600+, Type=SVOD, Light theme=False > Prices > Outgo Spasibo > Бонусы > Sber / Mini Spasibo > MasterGradient > Rectangle 13
52. **Brand/Partners/Sber Spasibo** — [мастер 24064:332266](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=24064-332266), слой `24064:332291`, свойство `fills`.
   Purchase > 🟡 Purchase > Breackpoints=375+, Type=SVOD, Light theme=False > Prices > Income Spasibo > Бонусы > +4
53. **Мастер/Зелёный** — [мастер 24064:332266](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=24064-332266), слой `I24064:332292;25781:343`, свойство `fills`.
   Purchase > 🟡 Purchase > Breackpoints=375+, Type=SVOD, Light theme=False > Prices > Income Spasibo > Бонусы > Sber / Mini Spasibo > MasterGradient > Rectangle 13
54. **Мастер/Зелёный** — [мастер 24064:332266](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=24064-332266), слой `I24064:332287;25781:343`, свойство `fills`.
   Purchase > 🟡 Purchase > Breackpoints=375+, Type=SVOD, Light theme=False > Prices > Outgo Spasibo > Бонусы > Sber / Mini Spasibo > MasterGradient > Rectangle 13
55. **Brand/Partners/Sber Spasibo** — [мастер 24064:332298](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=24064-332298), слой `24064:332323`, свойство `fills`.
   Purchase > 🟡 Purchase > Breackpoints=320+, Type=SVOD, Light theme=False > Prices > Income Spasibo > Бонусы > +4
56. **Мастер/Зелёный** — [мастер 24064:332298](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=24064-332298), слой `I24064:332324;25781:343`, свойство `fills`.
   Purchase > 🟡 Purchase > Breackpoints=320+, Type=SVOD, Light theme=False > Prices > Income Spasibo > Бонусы > Sber / Mini Spasibo > MasterGradient > Rectangle 13
57. **Мастер/Зелёный** — [мастер 24064:332298](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=24064-332298), слой `I24064:332319;25781:343`, свойство `fills`.
   Purchase > 🟡 Purchase > Breackpoints=320+, Type=SVOD, Light theme=False > Prices > Outgo Spasibo > Бонусы > Sber / Mini Spasibo > MasterGradient > Rectangle 13
58. **Brand/Partners/Sber Spasibo** — [мастер 24064:332330](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=24064-332330), слой `24064:332355`, свойство `fills`.
   Purchase > 🟡 Purchase > Breackpoints=1720+, Type=TVOD, Light theme=False > Right > Prices > Income Spasibo > Бонусы > +4
59. **Мастер/Зелёный** — [мастер 24064:332330](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=24064-332330), слой `I24064:332356;25781:343`, свойство `fills`.
   Purchase > 🟡 Purchase > Breackpoints=1720+, Type=TVOD, Light theme=False > Right > Prices > Income Spasibo > Бонусы > Sber / Mini Spasibo > MasterGradient > Rectangle 13
60. **Мастер/Зелёный** — [мастер 24064:332330](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=24064-332330), слой `I24064:332351;25781:343`, свойство `fills`.
   Purchase > 🟡 Purchase > Breackpoints=1720+, Type=TVOD, Light theme=False > Right > Prices > Outgo Spasibo > Бонусы > Sber / Mini Spasibo > MasterGradient > Rectangle 13
61. **Brand/Partners/Sber Spasibo** — [мастер 24064:332361](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=24064-332361), слой `24064:332386`, свойство `fills`.
   Purchase > 🟡 Purchase > Breackpoints=1320+, Type=TVOD, Light theme=False > Right > Prices > Income Spasibo > Бонусы > +4
62. **Мастер/Зелёный** — [мастер 24064:332361](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=24064-332361), слой `I24064:332387;25781:343`, свойство `fills`.
   Purchase > 🟡 Purchase > Breackpoints=1320+, Type=TVOD, Light theme=False > Right > Prices > Income Spasibo > Бонусы > Sber / Mini Spasibo > MasterGradient > Rectangle 13
63. **Мастер/Зелёный** — [мастер 24064:332361](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=24064-332361), слой `I24064:332382;25781:343`, свойство `fills`.
   Purchase > 🟡 Purchase > Breackpoints=1320+, Type=TVOD, Light theme=False > Right > Prices > Outgo Spasibo > Бонусы > Sber / Mini Spasibo > MasterGradient > Rectangle 13
64. **Brand/Partners/Sber Spasibo** — [мастер 24064:332392](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=24064-332392), слой `24064:332417`, свойство `fills`.
   Purchase > 🟡 Purchase > Breackpoints=600+, Type=TVOD, Light theme=False > Right > Prices > Income Spasibo > Бонусы > +4
65. **Мастер/Зелёный** — [мастер 24064:332392](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=24064-332392), слой `I24064:332418;25781:343`, свойство `fills`.
   Purchase > 🟡 Purchase > Breackpoints=600+, Type=TVOD, Light theme=False > Right > Prices > Income Spasibo > Бонусы > Sber / Mini Spasibo > MasterGradient > Rectangle 13
66. **Мастер/Зелёный** — [мастер 24064:332392](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=24064-332392), слой `I24064:332413;25781:343`, свойство `fills`.
   Purchase > 🟡 Purchase > Breackpoints=600+, Type=TVOD, Light theme=False > Right > Prices > Outgo Spasibo > Бонусы > Sber / Mini Spasibo > MasterGradient > Rectangle 13
67. **Brand/Partners/Sber Spasibo** — [мастер 24064:332423](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=24064-332423), слой `24064:332448`, свойство `fills`.
   Purchase > 🟡 Purchase > Breackpoints=375+, Type=TVOD, Light theme=False > Prices > Income Spasibo > Бонусы > +4
68. **Мастер/Зелёный** — [мастер 24064:332423](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=24064-332423), слой `I24064:332449;25781:343`, свойство `fills`.
   Purchase > 🟡 Purchase > Breackpoints=375+, Type=TVOD, Light theme=False > Prices > Income Spasibo > Бонусы > Sber / Mini Spasibo > MasterGradient > Rectangle 13
69. **Мастер/Зелёный** — [мастер 24064:332423](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=24064-332423), слой `I24064:332444;25781:343`, свойство `fills`.
   Purchase > 🟡 Purchase > Breackpoints=375+, Type=TVOD, Light theme=False > Prices > Outgo Spasibo > Бонусы > Sber / Mini Spasibo > MasterGradient > Rectangle 13
70. **Brand/Partners/Sber Spasibo** — [мастер 24064:332454](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=24064-332454), слой `24064:332479`, свойство `fills`.
   Purchase > 🟡 Purchase > Breackpoints=320+, Type=TVOD, Light theme=False > Prices > Income Spasibo > Бонусы > +4
71. **Мастер/Зелёный** — [мастер 24064:332454](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=24064-332454), слой `I24064:332480;25781:343`, свойство `fills`.
   Purchase > 🟡 Purchase > Breackpoints=320+, Type=TVOD, Light theme=False > Prices > Income Spasibo > Бонусы > Sber / Mini Spasibo > MasterGradient > Rectangle 13
72. **Мастер/Зелёный** — [мастер 24064:332454](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=24064-332454), слой `I24064:332475;25781:343`, свойство `fills`.
   Purchase > 🟡 Purchase > Breackpoints=320+, Type=TVOD, Light theme=False > Prices > Outgo Spasibo > Бонусы > Sber / Mini Spasibo > MasterGradient > Rectangle 13

