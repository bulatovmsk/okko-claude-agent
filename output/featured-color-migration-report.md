# Featured: замена цветов

Дата: 20 октября 2026. [Страница Featured](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=17591-300408).

Изменены **195 уникальных слоёв**: 46 собственных слоёв мастеров и 149 слоёв вложенных инстансов. Изменения источников наследуются их вложениями, поэтому число обновлённых применений больше числа прямых изменений.

Проверены все **144 мастера**, их деревья из **7949 слоёв**, а также **2161 узел вне мастеров**. Общий охват: **10 110 узлов** с учётом самой страницы и контейнеров.

Обновлены Background/Primary, Primary и Third у текста/иконок, Contour, Positive, Live, Glassy Secondary, Fill Third. Brand/Okko/Accent у Label с Theme=Continuum заменён актуальным существующим стилем color/component/label/continuum; старые примитивные привязки этого фона исчезли из доступных тем. Во вложенных спортивных блоках обновлены заливки и подписи ставок.

Проверка текста и иконок на цветном фоне не выявила дополнительных однозначных замен на static-токены. Уже существующие static-привязки сохранены.

## Остатки в доступных темах: 84 применения

Все остатки находятся в **28 вложенных векторах Bet Logo**: 56 ссылок на старый радиальный Color/fill/solid/hover-focus/Third и 28 на старый Inverse, локально названный Fill/Solid/Primary.

| Источник | Применений | Причина / следующее действие |
|---|---:|---|
| Color/fill/solid/hover-focus/Third, key 7190d7e2… | 56 | Старый градиент радиальный, актуальный одноимённый — линейный; по роли возможен inverse. Замена оставлена как неоднозначная. |
| Fill/Solid/Primary, key 974f85fc… | 28 | По исходной библиотеке это Inverse → color/fill/solid/inverse. Исходный Bet Logo исправлен ранее, но старые локальные версии/переопределения сохраняют регионы. Figma запрещает запись vector network внутри инстанса. Требуется обновление библиотечной версии и проверка переопределений. Detach, swap и сбросы не выполнялись. |

### Мастера с остатками Bet Logo

- [.itemRail → breakpoint=1920, type=Sport](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=17613-323320)
- [.itemRail → breakpoint=1792, type=Sport](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=17613-323322)
- [.itemRail → breakpoint=1440, type=Sport](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=17613-323324)
- [.itemRail → breakpoint=1024, type=Sport](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=17613-323326)
- [.itemRail → breakpoint=768, type=Sport](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=17613-323328)
- [.itemRail → breakpoint=375, type=Sport](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=17613-323330)
- [.itemRail → breakpoint=320, type=Sport](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=17613-323332)
- [FeaturedSport → breakpoint=1920](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=17613-326948)
- [FeaturedSport → breakpoint=1792](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=17613-326953)
- [FeaturedSport → breakpoint=1440](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=17613-326958)
- [FeaturedSport → breakpoint=1024](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=17613-326963)
- [FeaturedSport → breakpoint=768](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=17613-326968)
- [FeaturedSport → breakpoint=375](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=17613-326973)
- [FeaturedSport → breakpoint=320](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=17613-326978)

Все ID векторов, номера регионов и родительских инстансов сохранены в JSON-аудите. Других старых paint-стилей и устаревших цветовых переменных в доступных темах не обнаружено.

## Исключения

В мастерах осталось **235 применений старых paint-стилей в Light/Lighthouse**. Внешние примеры содержат ещё **122 применения**: 44 в обычном внешнем контексте, 76 в Light, 2 в Kids. Примеры напрямую не редактировались.

Light/Kids исключены из обычных адресных замен. Применено ранее явно согласованное исключение для старых on Light Primary/Secondary → color/text-icon/inverse/primary/secondary: 8 вложенных слоёв (4 + 4). Общие мастера без Theme обновлены; их изменения наследуются в том числе Light-инстансами. Отдельные Light-переопределения для удержания устаревших цветов не создавались и не сбрасывались. Остальные Light/Lighthouse не мигрировались.

Сырые цвета без токена оставлены. Новые дизайн-переменные, aliases, коллекции и стили не создавались. Применены существующие библиотечные ресурсы. Тексты, геометрия, свойства вариантов и прочие переопределения не менялись.

## Проверка

Программный полный обход страницы по мастерам и остальным узлам: скрытые вложения, fills/strokes, регионы векторов, градиентные остановки, текстовые диапазоны и эффекты. Ошибок итогового аудита и неразрешённых ссылок нет. Панель Selection colors вручную не проверялась.

При выборе всей страницы старые цвета ещё будут видны из перечисленных остатков Bet Logo, исключённых Light/Lighthouse/Kids и внешних примеров.

