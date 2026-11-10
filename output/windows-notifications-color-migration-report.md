# Окна и уведомления — миграция цветов

[Страница в Figma](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9821-75493)

## Результат

- Проверены **242 мастера**, **6563 слоя** в них и вложениях. Итоговый аудит всей страницы охватил **8860 узлов**, включая 2297 узлов вне мастеров.
- Обновлены **1112 уникальных слоёв**. Наследующие инстансы не увеличивают счётчик прямых изменений.
- Число известных старых PAINT-привязок в рабочей области уменьшилось с **1507 до 308**.
- В **22 текстовых слоях** обновлены **69 диапазонов** со смешанными цветами, включая заранее согласованные inverse-исключения в Light.
- В **84 слоях** текста/иконок на цветных фонах применены static-токены с сохранением видимой прозрачности.
- По подтверждённой роли обновлены **7 цен/зачёркиваний** → color.text-icon.offer и **33 чёрные линии в партнёрских логотипах** → color.static.solid.black. Вид чёрных линий проверен и сохранён.
- Дополнительно одна ссылка «Узнать подробнее» переведена с Violet/Primary на color.text-icon.accent, а 6 заливок включённых радио — на color.fill.solid.accent.
- Итоговое чтение всей страницы завершилось без ошибок и недоступных стилей. Проверены заливки, обводки, текстовые диапазоны, градиентные стопы, регионы векторов, эффекты и переменные. Тёмное окно проверено визуально после последней замены. Selection colors вручную в интерфейсе не проверялся.

## Остатки для решения

Осталось **308 применений известных старых PAINT-стилей**. В это число входят 4 случая с известной целью, заблокированные шрифтом, и 4 стилевых применения solid Sber, отложенные ранее. Дополнительно сохранены **25 переменных brand/partners/sber** в других слоях логотипов.

Счётчики означают ссылки в свойствах, регионах и текстовых диапазонах, а не уникальные цвета или слои. Примеры мастеров приведены в таблице; полный список 308 применений находится ниже и в JSON.

| Старый стиль | Применений | Где | Причина / существующие кандидаты |
|---|---:|---|---|
| НЕ используем/Elevation/03 | 14 | Подложки WIP-тултипов. [Пример мастера](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=8559-65475) | color.background.solid.secondary либо color.fill.solid.secondary; требуется определить уровень поверхности для старого Elevation/03. |
| Primitives/Black/Primary / Black / Primary | 111 | Чёрные тексты старых окон, поля ввода, отдельные иконки. [Пример мастера](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5491-30712) | Для интерфейсных текстов — color.text-icon.primary / inverse.primary; для фиксированной графики — static black; для фона инпута — color.fill.solid.* / background.solid.*. Общая замена Black/Primary исказит разные роли. |
| [Deprecated]/Background/Decorative/Primary | 7 | Картинки успеха/преимуществ Прайма. [Пример мастера](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=7140-49342) | Нужно выбрать семантику декоративного фона изображения. Подходящий color-токен не подтверждён; primitives/electric1100 связан с этими же заливками. |
| Primitives/Blueberry/Primary / Blueberry / Primary | 6 | Иконки копирования и элементов цены. [Пример мастера](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5530-649) | text-icon.primary / inverse.primary либо статический цвет по контексту. Часть применений находится в регионах векторов. |
| Fill/Solid/AccentB | 12 | Базовые кнопки во вложениях. [Пример мастера](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5531-30795) | color.fill.solid.accent либо градиент color.component.button. Нужно выбрать сплошной фон или градиент. |
| Primitives/Blueberry/15 | 2 | Обводка второстепенной кнопки СберПрайма. [Пример мастера](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=10520-85045) | color.border.glassy либо color.border.solid; требуется определить контраст обводки. |
| Primitives/Violet/Primary | 18 | Оставшиеся фиолетовые кнопки, текст и графика. [Пример мастера](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=3355-21776) | Для текста — color.text-icon.accent, для заливок контролов — color.fill.solid.accent, для основных кнопок возможен color.component.button. Одного соответствия для всех оставшихся ролей нет. Подтверждённая ссылка и включённые радио уже исправлены отдельно. |
| Primitives/Black/90 | 11 | Тексты скидок и подтверждения почты. [Пример мастера](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5491-30712) | text-icon.primary / inverse.primary либо static black с исходной альфой после выбора поведения поверхности. |
| Primitives/Grey/Light | 6 | Subtract в иллюстрациях СберПрайма. [Пример мастера](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=7092-48114) | Нужно выбрать существующий технический/статический цвет графики; соответствие текущему grey-токену не подтверждено. |
| Primitives/Blueberry/48 | 9 | Подписи в Dark-вариантах защиты профиля. [Пример мастера](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=18605-299307) | color.text-icon.secondary / third либо inverse по роли поверхности; требуется согласовать иерархию и контраст старого Blueberry/48. |
| [Deprecated]/Text & icon/on Dark/Secondary | 4 | Плейсхолдеры старых инпутов в окнах входа/регистрации. [Пример мастера](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16713-185931) | Цель color.text-icon.secondary известна. 4 слоя заблокированы отсутствующим Avenir Next Regular; шрифт не подменялся. |
| Primitives/Black/78 | 21 | Второстепенные тексты скидок, бонусов и почты. [Пример мастера](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5491-30637) | text-icon.secondary / inverse.secondary либо static black с альфой; нужно определить зависимость от темы. |
| Primitives/Grey/Sidebar | 6 | Фон вариантов списания бонусов. [Пример мастера](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6687-40096) | color.fill.solid.secondary / third либо background.solid.secondary; требуется определить уровень карточки. |
| Primitives/Grey/Medium | 14 | Линии, обводки, отдельные заливки. [Пример мастера](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6687-40096) | Для обводки — color.border.glassy / solid; для заливки — color.fill.glassy.*. Нужен выбор по роли и контрасту. |
| Primitives/Violet/15 | 2 | Картинка в WIP-окне СберЛояльности. [Пример мастера](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6640-40676) | Нужно определить, это декоративный фон изображения или выделение поверхности. Возможен color.fill.solid.accent с альфой; точное соответствие не подтверждено. |
| Primitives/Blueberry/Dark blueberry 100 | 15 | Графика преимуществ. [Пример мастера](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9736-75216) | Требуется выбрать между фоном/плейсхолдером и фиксированной графикой. Кандидаты color.fill.technical.placeholder, fill.solid.* или background.solid.* зависят от роли; одна замена оттенка не подходит. |
| Violet / 5 / Primitives/Violet/5 | 6 | Подарок, фон копирования ссылки. [Пример мастера](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5562-146) | color.fill.solid.accent с альфой либо color.fill.glassy.*. Нужно выбрать акцентную или нейтральную поверхность. |
| [Deprecated]/Brand/Social/VK | 11 | VK в шаринге и авторизации. [Пример мастера](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5530-649) | Подходящий актуальный фирменный color-токен в изученном наборе не найден. Общий UI-accent не назначался; новый токен не создавался. |
| [Deprecated]/Brand/Social/Facebook | 11 | Facebook в шаринге и авторизации. [Пример мастера](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5530-649) | Подходящий актуальный фирменный color-токен в изученном наборе не найден. Общий UI-accent не назначался; новый токен не создавался. |
| Primitives/Grey/Primary | 13 | Серые тексты и подписи преимуществ. [Пример мастера](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=7092-48114) | color.text-icon.secondary / third либо inverse по поверхности. Требуется согласовать иерархию текста. |
| [Deprecated]/Brand/Partners/Sber | 4 | Сбер ID / зелёная. [Пример мастера](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=7092-48114) | Solid Sber ранее решено пока не менять. Дополнительно оставлены 25 привязок brand/partners/sber в других слоях логотипов. |
| НЕ используем/Sticker Content/Offer | 2 | Ellipse 46 в ценнике сезона. [Пример мастера](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9385-71121) | Фон старого стикера Offer: существующие color.component.label.* либо fill.solid.warning/accent требуют выбора семантики и градиента. |
| [Deprecated]/Fill/Decorative/Midnight | 1 | Screen в инструкции SberPay. [Пример мастера](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16179-175769) | Старый декоративный Midnight: точный существующий градиент для иллюстрации не выбран. Нужны согласование направления, стопов и роли; не заменять произвольным похожим градиентом. |
| [Deprecated]/Fill/Decorative/Dark Violet | 1 | Screen в инструкции SberPay. [Пример мастера](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16179-175769) | Старый декоративный Dark Violet: точный существующий градиент для иллюстрации не выбран. Новые токены не создавались. |
| Primitives/Grey/50 | 1 | «или» в подтверждении почты. [Пример мастера](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=19355-299853) | color.text-icon.third / fourth либо inverse.third; требуется выбрать контраст вспомогательного текста. |

## Ограничение шрифта

Figma не может загрузить **Avenir Next Regular**: семейство Avenir Next отсутствует в доступной среде. Следующие 4 текста с известной заменой Secondary оставлены без подмены шрифта:

- [Мастер 16713:185931](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16713-185931), `I16512:178476;16498:177838;5105:30460`.
- [Мастер 16498:177832](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16498-177832), `I16498:177838;5105:30460`.
- [Мастер 16713:186123](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16713-186123), `I16713:186092;5105:30460`.
- [Мастер 16498:177985](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16498-177985), `I16498:177992;5105:30543`.

## Light, примеры и остальные привязки

- Light распознавался по «Светлый фон=True», On Light, «Светлая/Светлое/светлый» в пути, **Dark theme=False**, **Theme dark=False**, **Тёмная шторка=False** и другим согласованным обозначениям. В наборе с опечаткой **On Lignt** использовано явное свойство Dark theme.
- В Light-мастерах осталось **461 применение известных старых стилей**. Прямые изменения там ограничены ранее согласованными inverse-исключениями; общие вложения также могут наследовать обновление Dark-мастеров.
- Вне мастеров осталось **831 применение старых стилей**: 28 в Light-контекстах и 803 в остальных примерах/контейнерах. Они не входят в 308 и не редактировались напрямую.
- **7 primitives/electric1100** находятся внутри тех же семи старых Background/Decorative/Primary, а не означают ещё семь заливок сверх соответствующей строки таблицы.
- color.fill.solid.inverse из импортированной коллекции 41700 актуален по ключу. Идентификатор коллекции не является критерием устаревания.
- В проверенных цветных контекстах **24 слоя без стиля/переменной** сохранены по правилу не трогать сырые цвета. Небелые/нечёрные цветные надписи и логотипы не перекрашивались в static white/black автоматически; среди них есть отложенный Sber и отдельные цветные ссылки. Их нельзя считать дополнительными уникальными Deprecated-слоями: часть уже учтена в остатках Sber.

Новые переменные, токены и коллекции не создавались. Геометрия, структура, тексты и свойства вариантов не менялись. Инстансы не отсоединялись и не сбрасывались; цветовые привязки во вложениях обновлялись адресно.

## Все 308 оставшихся применений стилей в рабочей области

1. **НЕ используем/Elevation/03** — [мастер 8559:65475](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=8559-65475), слой `8559:65475`, свойство `fills`.
2. **НЕ используем/Elevation/03** — [мастер 6616:39313](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6616-39313), слой `6616:39313`, свойство `fills`.
3. **НЕ используем/Elevation/03** — [мастер 6614:39322](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6614-39322), слой `6614:39291`, свойство `fills`.
4. **НЕ используем/Elevation/03** — [мастер 5541:30805](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5541-30805), слой `5541:30805`, свойство `fills`.
5. **НЕ используем/Elevation/03** — [мастер 5540:30769](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5540-30769), слой `5535:30783`, свойство `fills`.
6. **НЕ используем/Elevation/03** — [мастер 5531:30795](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5531-30795), слой `5531:30795`, свойство `fills`.
7. **Fill/Solid/AccentB** — [мастер 5531:30795](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5531-30795), слой `I5643:31482;4504:267`, свойство `fills`.
8. **НЕ используем/Elevation/03** — [мастер 5531:30763](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5531-30763), слой `5531:30754`, свойство `fills`.
9. **Fill/Solid/AccentB** — [мастер 5531:30763](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5531-30763), слой `I5643:31475;4504:267`, свойство `fills`.
10. **НЕ используем/Elevation/03** — [мастер 8559:65403](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=8559-65403), слой `8559:65368`, свойство `fills`.
11. **НЕ используем/Elevation/03** — [мастер 1721:14048](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=1721-14048), слой `1721:14048`, свойство `fills`.
12. **НЕ используем/Elevation/03** — [мастер 1722:291](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=1722-291), слой `1722:291`, свойство `fills`.
13. **НЕ используем/Elevation/03** — [мастер 1722:0](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=1722-0), слой `1722:0`, свойство `fills`.
14. **НЕ используем/Elevation/03** — [мастер 1722:261](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=1722-261), слой `1722:261`, свойство `fills`.
15. **НЕ используем/Elevation/03** — [мастер 1722:292](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=1722-292), слой `1722:292`, свойство `fills`.
16. **НЕ используем/Elevation/03** — [мастер 1722:260](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=1722-260), слой `1722:260`, свойство `fills`.
17. **Primitives/Blueberry/48** — [мастер 18605:299307](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=18605-299307), слой `18605:299318`, свойство `fills`.
18. **Primitives/Blueberry/48** — [мастер 18605:299319](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=18605-299319), слой `18605:299327`, свойство `fills`.
19. **Primitives/Blueberry/48** — [мастер 18605:299331](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=18605-299331), слой `18605:299341`, свойство `fills`.
20. **Primitives/Blueberry/48** — [мастер 18605:299342](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=18605-299342), слой `18605:299350`, свойство `fills`.
21. **Primitives/Blueberry/48** — [мастер 18605:299354](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=18605-299354), слой `18605:299364`, свойство `fills`.
22. **Primitives/Blueberry/48** — [мастер 18605:299376](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=18605-299376), слой `18605:299386`, свойство `fills`.
23. **Primitives/Blueberry/48** — [мастер 18605:299387](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=18605-299387), слой `18605:299395`, свойство `fills`.
24. **Primitives/Blueberry/48** — [мастер 18605:299399](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=18605-299399), слой `18605:299409`, свойство `fills`.
25. **Primitives/Blueberry/48** — [мастер 18605:299410](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=18605-299410), слой `18605:299418`, свойство `fills`.
26. **Primitives/Black/Primary** — [мастер 5491:30712](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5491-30712), слой `I5491:30655;5491:30643;5487:30564`, свойство `fills`.
27. **Primitives/Black/Primary** — [мастер 5491:30712](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5491-30712), слой `I5491:30655;5491:30643;5487:30565`, свойство `fills`.
28. **Primitives/Black/90** — [мастер 5491:30712](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5491-30712), слой `I5491:30654;5487:30564`, свойство `fills`.
29. **Primitives/Black/Primary** — [мастер 5491:30712](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5491-30712), слой `I5491:30654;5487:30565`, свойство `fills`.
30. **Primitives/Black/90** — [мастер 5491:30712](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5491-30712), слой `I5491:30672;5487:30564`, свойство `fills`.
31. **Primitives/Black/Primary** — [мастер 5491:30712](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5491-30712), слой `I5491:30672;5487:30565`, свойство `fills`.
32. **Primitives/Black/90** — [мастер 5491:30712](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5491-30712), слой `I5491:30682;5487:30564`, свойство `fills`.
33. **Primitives/Black/Primary** — [мастер 5491:30712](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5491-30712), слой `I5491:30682;5487:30565`, свойство `fills`.
34. **Primitives/Black/90** — [мастер 5491:30637](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5491-30637), слой `I5491:30570;5491:30555;5487:30549`, свойство `fills`.
35. **Primitives/Black/78** — [мастер 5491:30637](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5491-30637), слой `I5491:30570;5491:30555;5487:30550`, свойство `fills`.
36. **Primitives/Black/90** — [мастер 5491:30637](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5491-30637), слой `I5491:30569;5487:30549`, свойство `fills`.
37. **Primitives/Black/78** — [мастер 5491:30637](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5491-30637), слой `I5491:30569;5487:30550`, свойство `fills`.
38. **Primitives/Black/90** — [мастер 5491:30637](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5491-30637), слой `I5491:30587;5487:30549`, свойство `fills`.
39. **Primitives/Black/78** — [мастер 5491:30637](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5491-30637), слой `I5491:30587;5487:30550`, свойство `fills`.
40. **Primitives/Black/90** — [мастер 5491:30637](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5491-30637), слой `I5491:30619;5487:30549`, свойство `fills`.
41. **Primitives/Black/78** — [мастер 5491:30637](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5491-30637), слой `I5491:30619;5487:30550`, свойство `fills`.
42. **Primitives/Black/90** — [мастер 5491:30642](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5491-30642), слой `5487:30564`, свойство `fills`.
43. **Primitives/Black/Primary** — [мастер 5491:30642](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5491-30642), слой `5487:30565`, свойство `fills`.
44. **Primitives/Black/Primary** — [мастер 5491:30653](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5491-30653), слой `I5491:30643;5487:30564`, свойство `fills`.
45. **Primitives/Black/Primary** — [мастер 5491:30653](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5491-30653), слой `I5491:30643;5487:30565`, свойство `fills`.
46. **Primitives/Black/90** — [мастер 5491:30554](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5491-30554), слой `5487:30549`, свойство `fills`.
47. **Primitives/Black/78** — [мастер 5491:30554](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5491-30554), слой `5487:30550`, свойство `fills`.
48. **Primitives/Black/90** — [мастер 5491:30564](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5491-30564), слой `I5491:30555;5487:30549`, свойство `fills`.
49. **Primitives/Black/78** — [мастер 5491:30564](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5491-30564), слой `I5491:30555;5487:30550`, свойство `fills`.
50. **Primitives/Grey/Sidebar** — [мастер 6687:40096](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6687-40096), слой `6687:40067`, свойство `fills`.
51. **Primitives/Black/78** — [мастер 6687:40096](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6687-40096), слой `I6687:40067;6687:40010`, свойство `fills`.
52. **Primitives/Grey/Medium** — [мастер 6687:40096](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6687-40096), слой `6687:40068`, свойство `strokes`.
53. **Primitives/Black/78** — [мастер 6687:40096](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6687-40096), слой `I6687:40068;6687:40022`, свойство `fills`.
54. **Fill/Solid/AccentB** — [мастер 6687:40096](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6687-40096), слой `I6687:40069;4496:35918`, свойство `fills`.
55. **Primitives/Grey/Medium** — [мастер 6687:39380](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6687-39380), слой `6687:40023`, свойство `strokes`.
56. **Primitives/Black/78** — [мастер 6687:39380](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6687-39380), слой `I6687:40023;6687:40022`, свойство `fills`.
57. **Primitives/Grey/Sidebar** — [мастер 6687:39380](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6687-39380), слой `6687:40029`, свойство `fills`.
58. **Primitives/Black/78** — [мастер 6687:39380](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6687-39380), слой `I6687:40029;6687:40010`, свойство `fills`.
59. **Fill/Solid/AccentB** — [мастер 6687:39380](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6687-39380), слой `I6687:39385;4496:35918`, свойство `fills`.
60. **Primitives/Grey/Sidebar** — [мастер 6687:39896](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6687-39896), слой `6687:39819`, свойство `fills`.
61. **Primitives/Black/78** — [мастер 6687:39896](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6687-39896), слой `I6687:39819;6687:39723`, свойство `fills`.
62. **Primitives/Grey/Medium** — [мастер 6687:39896](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6687-39896), слой `6687:39820`, свойство `strokes`.
63. **Primitives/Black/78** — [мастер 6687:39896](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6687-39896), слой `I6687:39820;6687:39845`, свойство `fills`.
64. **Fill/Solid/AccentB** — [мастер 6687:39896](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6687-39896), слой `I6687:39821;4496:35918`, свойство `fills`.
65. **Primitives/Grey/Medium** — [мастер 6687:39386](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6687-39386), слой `6687:39768`, свойство `strokes`.
66. **Primitives/Black/78** — [мастер 6687:39386](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6687-39386), слой `I6687:39768;6687:39845`, свойство `fills`.
67. **Primitives/Grey/Sidebar** — [мастер 6687:39386](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6687-39386), слой `6687:39741`, свойство `fills`.
68. **Primitives/Black/78** — [мастер 6687:39386](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6687-39386), слой `I6687:39741;6687:39723`, свойство `fills`.
69. **Fill/Solid/AccentB** — [мастер 6687:39386](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6687-39386), слой `I6687:39392;4496:35918`, свойство `fills`.
70. **Primitives/Violet/15** — [мастер 6640:40676](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6640-40676), слой `6640:40595`, свойство `fills`.
71. **Primitives/Black/Primary** — [мастер 6640:40676](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6640-40676), слой `6640:40598`, свойство `fills`.
72. **Primitives/Black/Primary** — [мастер 6640:40676](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6640-40676), слой `6640:40668`, свойство `fills`.
73. **Primitives/Black/Primary** — [мастер 6640:40676](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6640-40676), слой `6640:40599`, свойство `fills`.
74. **Primitives/Black/Primary** — [мастер 6640:40676](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6640-40676), слой `6640:40671`, свойство `fills`.
75. **Primitives/Black/Primary** — [мастер 6640:40676](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6640-40676), слой `6640:40672`, свойство `fills`.
76. **Primitives/Black/Primary** — [мастер 6640:40676](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6640-40676), слой `6640:40674`, свойство `fills`.
77. **Primitives/Black/Primary** — [мастер 6640:40676](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6640-40676), слой `6640:40675`, свойство `fills`.
78. **Primitives/Violet/15** — [мастер 6640:40665](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6640-40665), слой `6640:40575`, свойство `fills`.
79. **Primitives/Black/Primary** — [мастер 6640:40665](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6640-40665), слой `6640:40578`, свойство `fills`.
80. **Primitives/Black/Primary** — [мастер 6640:40665](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6640-40665), слой `6640:40579`, свойство `fills`.
81. **Primitives/Black/Primary** — [мастер 6640:40665](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6640-40665), слой `6640:40661`, свойство `fills`.
82. **Primitives/Black/Primary** — [мастер 6640:40665](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6640-40665), слой `6640:40664`, свойство `fills`.
83. **Primitives/Black/Primary** — [мастер 5562:123](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5562-123), слой `5562:33`, свойство `fills`.
84. **Primitives/Black/Primary** — [мастер 5562:146](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5562-146), слой `5562:140`, свойство `fills`.
85. **Violet / 5** — [мастер 5562:146](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5562-146), слой `8696:68105`, свойство `fills`.
86. **Fill/Solid/AccentB** — [мастер 5562:146](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5562-146), слой `I5562:141;4496:35918`, свойство `fills`.
87. **Primitives/Black/Primary** — [мастер 5562:0](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5562-0), слой `5561:31663`, свойство `fills`.
88. **Primitives/Black/Primary** — [мастер 5562:0](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5562-0), слой `5561:31664`, свойство `fills`.
89. **Violet / 5** — [мастер 5562:0](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5562-0), слой `8696:68095`, свойство `fills`.
90. **Fill/Solid/AccentB** — [мастер 5562:0](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5562-0), слой `I5561:31665;4496:35918`, свойство `fills`.
91. **Primitives/Black/Primary** — [мастер 5530:649](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5530-649), слой `5530:613`, свойство `fills`.
92. **Primitives/Black/Primary** — [мастер 5530:649](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5530-649), слой `8695:69881`, свойство `fills`.
93. **Primitives/Violet/5** — [мастер 5530:649](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5530-649), слой `5861:62`, свойство `fills`.
94. **[Deprecated]/Brand/Social/VK** — [мастер 5530:649](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5530-649), слой `I5861:62;5861:22;1087:10;16654:5052`, свойство `region0`.
95. **[Deprecated]/Brand/Social/Facebook** — [мастер 5530:649](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5530-649), слой `I5861:62;5861:23;1088:8110;2615:1922`, свойство `region0`.
96. **Primitives/Blueberry/Primary** — [мастер 5530:649](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5530-649), слой `I5861:62;5865:32110;5636:31463;5337:1017`, свойство `region0`.
97. **Primitives/Black/Primary** — [мастер 5530:605](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5530-605), слой `5530:193`, свойство `fills`.
98. **Primitives/Black/Primary** — [мастер 5530:605](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5530-605), слой `5530:194`, свойство `fills`.
99. **Primitives/Violet/5** — [мастер 5530:605](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5530-605), слой `5861:42`, свойство `fills`.
100. **[Deprecated]/Brand/Social/VK** — [мастер 5530:605](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5530-605), слой `I5861:42;5861:3;1087:10;16654:5052`, свойство `region0`.
101. **[Deprecated]/Brand/Social/Facebook** — [мастер 5530:605](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5530-605), слой `I5861:42;5861:4;1088:8110;2615:1922`, свойство `region0`.
102. **Primitives/Blueberry/Primary** — [мастер 5530:605](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5530-605), слой `I5861:42;5865:32249;5636:31463;5337:1017`, свойство `region0`.
103. **Primitives/Grey/Light** — [мастер 7092:48114](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=7092-48114), слой `8449:65065`, свойство `fills`.
104. **Primitives/Grey/Primary** — [мастер 7092:48114](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=7092-48114), слой `8449:65069`, свойство `fills`.
105. **Primitives/Grey/Light** — [мастер 7092:48114](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=7092-48114), слой `8449:65071`, свойство `strokes`.
106. **Primitives/Black/Primary** — [мастер 7092:48114](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=7092-48114), слой `I8449:65072;2089:12`, свойство `region0`.
107. **Primitives/Black/Primary** — [мастер 7092:48114](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=7092-48114), слой `10210:80212`, свойство `fills`.
108. **[Deprecated]/Brand/Partners/Sber** — [мастер 7092:48114](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=7092-48114), слой `I8449:65076;7680:48592`, свойство `fills`.
109. **Primitives/Grey/Medium** — [мастер 7092:48114](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=7092-48114), слой `8449:65082`, свойство `fills`.
110. **Primitives/Grey/Light** — [мастер 7092:48067](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=7092-48067), слой `8449:64980`, свойство `fills`.
111. **Primitives/Grey/Primary** — [мастер 7092:48067](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=7092-48067), слой `8449:64984`, свойство `fills`.
112. **Primitives/Grey/Light** — [мастер 7092:48067](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=7092-48067), слой `8449:64986`, свойство `strokes`.
113. **Primitives/Black/Primary** — [мастер 7092:48067](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=7092-48067), слой `I8449:64987;2089:12`, свойство `region0`.
114. **[Deprecated]/Brand/Partners/Sber** — [мастер 7092:48067](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=7092-48067), слой `I8449:65029;7680:48592`, свойство `fills`.
115. **[Deprecated]/Background/Decorative/Primary** — [мастер 7140:49342](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=7140-49342), слой `I7140:48948;5299:31118`, свойство `fills`.
116. **Primitives/Black/Primary** — [мастер 7140:49342](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=7140-49342), слой `I7140:48948;5299:31121`, свойство `fills`.
117. **Primitives/Black/Primary** — [мастер 7140:49342](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=7140-49342), слой `7140:48951`, свойство `fills`.
118. **Primitives/Black/Primary** — [мастер 7140:49342](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=7140-49342), слой `7140:48952`, свойство `fills`.
119. **Primitives/Grey/Medium** — [мастер 7140:49342](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=7140-49342), слой `I7140:48956;82:668`, свойство `fills`.
120. **Primitives/Black/Primary** — [мастер 7140:49342](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=7140-49342), слой `7140:49330`, свойство `fills`.
121. **Primitives/Black/Primary** — [мастер 7140:49342](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=7140-49342), слой `7140:48960`, свойство `fills`.
122. **Primitives/Black/Primary** — [мастер 7140:49342](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=7140-49342), слой `7140:48962`, свойство `fills`.
123. **Primitives/Black/Primary** — [мастер 7140:49342](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=7140-49342), слой `7140:48963`, свойство `fills`.
124. **Primitives/Black/Primary** — [мастер 7140:49342](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=7140-49342), слой `7140:48965`, свойство `fills`.
125. **Primitives/Black/Primary** — [мастер 7140:49342](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=7140-49342), слой `7140:48966`, свойство `fills`.
126. **Primitives/Black/Primary** — [мастер 7140:49342](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=7140-49342), слой `7140:48968`, свойство `fills`.
127. **Primitives/Black/Primary** — [мастер 7140:49342](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=7140-49342), слой `7140:48969`, свойство `fills`.
128. **Primitives/Grey/Medium** — [мастер 7140:49342](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=7140-49342), слой `I7140:48971;82:668`, свойство `fills`.
129. **Primitives/Black/Primary** — [мастер 7140:49342](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=7140-49342), слой `7140:49332`, свойство `fills`.
130. **Primitives/Black/Primary** — [мастер 7140:49342](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=7140-49342), слой `7140:49333`, свойство `fills`.
131. **[Deprecated]/Background/Decorative/Primary** — [мастер 7140:49302](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=7140-49302), слой `I7140:48692;5299:31118`, свойство `fills`.
132. **Primitives/Black/Primary** — [мастер 7140:49302](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=7140-49302), слой `I7140:48692;5299:31121`, свойство `fills`.
133. **Primitives/Black/Primary** — [мастер 7140:49302](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=7140-49302), слой `7140:48696`, свойство `fills`.
134. **Primitives/Grey/Medium** — [мастер 7140:49302](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=7140-49302), слой `I7140:49300;82:668`, свойство `fills`.
135. **Primitives/Black/Primary** — [мастер 7140:49302](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=7140-49302), слой `7140:49321`, свойство `fills`.
136. **Primitives/Black/Primary** — [мастер 7140:49302](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=7140-49302), слой `7140:49263`, свойство `fills`.
137. **Primitives/Black/Primary** — [мастер 7140:49302](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=7140-49302), слой `7140:49054`, свойство `fills`.
138. **Primitives/Black/Primary** — [мастер 7140:49302](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=7140-49302), слой `8403:63947`, свойство `fills`.
139. **Primitives/Black/Primary** — [мастер 7140:49302](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=7140-49302), слой `8403:63948`, свойство `fills`.
140. **Primitives/Black/Primary** — [мастер 7140:49302](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=7140-49302), слой `7140:49176`, свойство `fills`.
141. **Primitives/Black/Primary** — [мастер 7140:49302](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=7140-49302), слой `7140:49060`, свойство `fills`.
142. **Primitives/Black/Primary** — [мастер 7140:49302](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=7140-49302), слой `7140:49175`, свойство `fills`.
143. **Primitives/Black/Primary** — [мастер 7140:49302](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=7140-49302), слой `7140:49057`, свойство `fills`.
144. **Primitives/Grey/Medium** — [мастер 7140:49302](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=7140-49302), слой `I7140:49272;82:668`, свойство `fills`.
145. **Primitives/Black/Primary** — [мастер 5496:30741](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5496-30741), слой `5496:30719`, свойство `fills`.
146. **Primitives/Black/Primary** — [мастер 5496:30741](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5496-30741), слой `5496:30720`, свойство `fills`.
147. **Primitives/Black/Primary** — [мастер 5496:30738](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5496-30738), слой `5496:30705`, свойство `fills`.
148. **Primitives/Black/Primary** — [мастер 5496:30738](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5496-30738), слой `5496:30706`, свойство `fills`.
149. **[Deprecated]/Background/Decorative/Primary** — [мастер 5299:31345](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5299-31345), слой `5299:31130`, свойство `fills`.
150. **Primitives/Black/Primary** — [мастер 5299:31345](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5299-31345), слой `5299:31133`, свойство `fills`.
151. **Primitives/Black/Primary** — [мастер 5299:31345](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5299-31345), слой `5299:31134`, свойство `fills`.
152. **[Deprecated]/Background/Decorative/Primary** — [мастер 5299:31344](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5299-31344), слой `5299:31118`, свойство `fills`.
153. **Primitives/Black/Primary** — [мастер 5299:31344](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5299-31344), слой `5299:31121`, свойство `fills`.
154. **[Deprecated]/Background/Decorative/Primary** — [мастер 3482:22614](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=3482-22614), слой `I3482:21495;3482:21525`, свойство `fills`.
155. **Primitives/Violet/Primary** — [мастер 3355:21776](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=3355-21776), слой `I3355:21667;288:51`, свойство `fills`.
156. **Primitives/Violet/Primary** — [мастер 3355:21776](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=3355-21776), слой `I3355:21667;2823:16861`, свойство `fills`.
157. **Primitives/Violet/Primary** — [мастер 3355:21776](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=3355-21776), слой `I3355:21667;2823:16832`, свойство `fills`.
158. **Primitives/Violet/Primary** — [мастер 3355:21776](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=3355-21776), слой `I3355:21667;288:52`, свойство `fills`.
159. **Primitives/Grey/Primary** — [мастер 3355:21776](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=3355-21776), слой `I3355:21667;5227:29754`, свойство `fills`.
160. **Primitives/Grey/Medium** — [мастер 3355:21776](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=3355-21776), слой `3355:21631`, свойство `fills`.
161. **Primitives/Black/Primary** — [мастер 3355:21776](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=3355-21776), слой `I3355:21632;934:20;5105:30461`, свойство `fills`.
162. **Primitives/Violet/Primary** — [мастер 3355:21776](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=3355-21776), слой `I3355:21634;2618:0`, свойство `region0`.
163. **Primitives/Grey/Primary** — [мастер 288:56](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=288-56), слой `288:47`, свойство `fills`.
164. **Primitives/Grey/Primary** — [мастер 288:56](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=288-56), слой `288:46`, свойство `fills`.
165. **Primitives/Violet/Primary** — [мастер 288:56](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=288-56), слой `288:51`, свойство `fills`.
166. **Primitives/Violet/Primary** — [мастер 288:56](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=288-56), слой `2823:16861`, свойство `fills`.
167. **Primitives/Violet/Primary** — [мастер 288:56](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=288-56), слой `2823:16832`, свойство `fills`.
168. **Primitives/Grey/Primary** — [мастер 288:56](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=288-56), слой `288:48`, свойство `fills`.
169. **Primitives/Violet/Primary** — [мастер 288:56](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=288-56), слой `288:52`, свойство `fills`.
170. **Primitives/Grey/Primary** — [мастер 288:56](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=288-56), слой `5227:29754`, свойство `fills`.
171. **Primitives/Black/Primary** — [мастер 683:6066](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=683-6066), слой `I934:20;5105:30461`, свойство `fills`.
172. **Primitives/Grey/Primary** — [мастер 4516:26044](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=4516-26044), слой `4516:26041`, свойство `fills`.
173. **Primitives/Black/Primary** — [мастер 1105:345](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=1105-345), слой `I1105:293;5105:30461`, свойство `fills`.
174. **Primitives/Black/Primary** — [мастер 1105:345](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=1105-345), слой `I1105:294;5105:30461`, свойство `fills`.
175. **[Deprecated]/Brand/Social/VK** — [мастер 1105:345](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=1105-345), слой `I1105:300;1088:8178;1087:10;16654:5052`, свойство `region0`.
176. **[Deprecated]/Brand/Social/Facebook** — [мастер 1105:345](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=1105-345), слой `I1105:300;1088:8173;1088:8110;2615:1922`, свойство `region0`.
177. **Primitives/Violet/Primary** — [мастер 1105:345](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=1105-345), слой `I1105:305;2618:0`, свойство `region0`.
178. **Primitives/Violet/Primary** — [мастер 1105:345](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=1105-345), слой `I1105:310;2618:0`, свойство `region0`.
179. **Primitives/Black/Primary** — [мастер 1621:13368](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=1621-13368), слой `I1621:13038;5105:30461`, свойство `fills`.
180. **Primitives/Black/Primary** — [мастер 1621:13368](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=1621-13368), слой `I1621:13039;5105:30461`, свойство `fills`.
181. **[Deprecated]/Brand/Social/VK** — [мастер 1621:13368](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=1621-13368), слой `I2756:2;1087:10;16654:5052`, свойство `region0`.
182. **[Deprecated]/Brand/Social/Facebook** — [мастер 1621:13368](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=1621-13368), слой `I2756:4;1088:8110;2615:1922`, свойство `region0`.
183. **Primitives/Violet/Primary** — [мастер 1621:13368](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=1621-13368), слой `I1621:13354;2618:0`, свойство `region0`.
184. **Primitives/Violet/Primary** — [мастер 1621:13368](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=1621-13368), слой `I1621:13359;2618:0`, свойство `region0`.
185. **Primitives/Black/Primary** — [мастер 270:34](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=270-34), слой `1623:245`, свойство `fills`.
186. **Primitives/Black/Primary** — [мастер 270:33](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=270-33), слой `2280:12836`, свойство `fills`.
187. **[Deprecated]/Background/Decorative/Primary** — [мастер 3482:22615](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=3482-22615), слой `I3482:21507;3482:21525`, свойство `fills`.
188. **Primitives/Black/Primary** — [мастер 3482:22615](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=3482-22615), слой `3482:21511`, свойство `fills`.
189. **Primitives/Violet/Primary** — [мастер 282:23](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=282-23), слой `282:18`, свойство `fills`.
190. **Primitives/Violet/Primary** — [мастер 282:23](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=282-23), слой `2829:16987`, свойство `fills`.
191. **Primitives/Violet/Primary** — [мастер 282:23](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=282-23), слой `2829:16960`, свойство `fills`.
192. **Primitives/Violet/Primary** — [мастер 282:23](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=282-23), слой `282:21`, свойство `fills`.
193. **Primitives/Grey/Primary** — [мастер 282:23](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=282-23), слой `5251:1`, свойство `fills`.
194. **Primitives/Black/Primary** — [мастер 699:124](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=699-124), слой `I1509:415;5105:30461`, свойство `fills`.
195. **Fill/Solid/AccentB** — [мастер 5558:32038](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5558-32038), слой `I5558:32028;4496:35918`, свойство `fills`.
196. **Fill/Solid/AccentB** — [мастер 5558:32061](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5558-32061), слой `I5558:32051;4496:35918`, свойство `fills`.
197. **Primitives/Violet/5** — [мастер 5861:40](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5861-40), слой `5861:40`, свойство `fills`.
198. **[Deprecated]/Brand/Social/VK** — [мастер 5861:40](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5861-40), слой `I5861:3;1087:10;16654:5052`, свойство `region0`.
199. **[Deprecated]/Brand/Social/Facebook** — [мастер 5861:40](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5861-40), слой `I5861:4;1088:8110;2615:1922`, свойство `region0`.
200. **Primitives/Blueberry/Primary** — [мастер 5861:40](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5861-40), слой `I5865:32249;5636:31463;5337:1017`, свойство `region0`.
201. **Primitives/Violet/5** — [мастер 5861:39](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5861-39), слой `5861:39`, свойство `fills`.
202. **[Deprecated]/Brand/Social/VK** — [мастер 5861:39](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5861-39), слой `I5861:22;1087:10;16654:5052`, свойство `region0`.
203. **[Deprecated]/Brand/Social/Facebook** — [мастер 5861:39](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5861-39), слой `I5861:23;1088:8110;2615:1922`, свойство `region0`.
204. **Primitives/Blueberry/Primary** — [мастер 5861:39](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5861-39), слой `I5865:32110;5636:31463;5337:1017`, свойство `region0`.
205. **Primitives/Grey/Medium** — [мастер 6687:40012](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6687-40012), слой `6687:40012`, свойство `strokes`.
206. **Primitives/Black/78** — [мастер 6687:40012](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6687-40012), слой `6687:40022`, свойство `fills`.
207. **Primitives/Grey/Sidebar** — [мастер 6687:40007](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6687-40007), слой `6687:40007`, свойство `fills`.
208. **Primitives/Black/78** — [мастер 6687:40007](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6687-40007), слой `6687:40010`, свойство `fills`.
209. **Primitives/Grey/Medium** — [мастер 6687:39732](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6687-39732), слой `6687:39732`, свойство `strokes`.
210. **Primitives/Black/78** — [мастер 6687:39732](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6687-39732), слой `6687:39845`, свойство `fills`.
211. **Primitives/Grey/Sidebar** — [мастер 6687:39731](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6687-39731), слой `6687:39731`, свойство `fills`.
212. **Primitives/Black/78** — [мастер 6687:39731](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6687-39731), слой `6687:39723`, свойство `fills`.
213. **Primitives/Grey/Primary** — [мастер 9385:71121](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9385-71121), слой `9383:71329`, свойство `fills`.
214. **НЕ используем/Sticker Content/Offer** — [мастер 9385:71121](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9385-71121), слой `9385:71114`, свойство `fills`.
215. **Blueberry / Primary** — [мастер 9385:71121](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9385-71121), слой `I9385:71116;2774:5`, свойство `region0`.
216. **Primitives/Grey/Primary** — [мастер 9385:71142](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9385-71142), слой `9385:71127`, свойство `fills`.
217. **НЕ используем/Sticker Content/Offer** — [мастер 9385:71142](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9385-71142), слой `9385:71131`, свойство `fills`.
218. **Blueberry / Primary** — [мастер 9385:71142](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9385-71142), слой `I9385:71132;2774:5`, свойство `region0`.
219. **Primitives/Blueberry/Dark blueberry 100** — [мастер 9736:75216](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9736-75216), слой `9736:75215`, свойство `region0`.
220. **Primitives/Blueberry/Dark blueberry 100** — [мастер 9736:75216](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9736-75216), слой `9736:75215`, свойство `region1`.
221. **Primitives/Blueberry/Dark blueberry 100** — [мастер 9736:75216](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9736-75216), слой `9736:75215`, свойство `region2`.
222. **Primitives/Blueberry/Dark blueberry 100** — [мастер 9733:75200](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9733-75200), слой `I9736:75271;9736:75215`, свойство `region0`.
223. **Primitives/Blueberry/Dark blueberry 100** — [мастер 9733:75200](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9733-75200), слой `I9736:75271;9736:75215`, свойство `region1`.
224. **Primitives/Blueberry/Dark blueberry 100** — [мастер 9733:75200](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9733-75200), слой `I9736:75271;9736:75215`, свойство `region2`.
225. **Primitives/Black/Primary** — [мастер 9733:75200](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9733-75200), слой `9733:75183`, свойство `fills`.
226. **Primitives/Black/Primary** — [мастер 9733:75200](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9733-75200), слой `9733:75184`, свойство `fills`.
227. **Primitives/Blueberry/Dark blueberry 100** — [мастер 9736:75593](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9736-75593), слой `I9736:75595;9736:75215`, свойство `region0`.
228. **Primitives/Blueberry/Dark blueberry 100** — [мастер 9736:75593](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9736-75593), слой `I9736:75595;9736:75215`, свойство `region1`.
229. **Primitives/Blueberry/Dark blueberry 100** — [мастер 9736:75593](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9736-75593), слой `I9736:75595;9736:75215`, свойство `region2`.
230. **Primitives/Black/Primary** — [мастер 9736:75593](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9736-75593), слой `9736:75447`, свойство `fills`.
231. **Primitives/Black/Primary** — [мастер 9736:75593](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9736-75593), слой `9736:75448`, свойство `fills`.
232. **Primitives/Blueberry/Dark blueberry 100** — [мастер 9736:75428](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9736-75428), слой `I9736:75286;9736:75271;9736:75215`, свойство `region0`.
233. **Primitives/Blueberry/Dark blueberry 100** — [мастер 9736:75428](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9736-75428), слой `I9736:75286;9736:75271;9736:75215`, свойство `region1`.
234. **Primitives/Blueberry/Dark blueberry 100** — [мастер 9736:75428](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9736-75428), слой `I9736:75286;9736:75271;9736:75215`, свойство `region2`.
235. **Primitives/Black/Primary** — [мастер 9736:75428](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9736-75428), слой `I9736:75286;9733:75183`, свойство `fills`.
236. **Primitives/Black/Primary** — [мастер 9736:75428](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9736-75428), слой `I9736:75286;9733:75184`, свойство `fills`.
237. **Primitives/Black/Primary** — [мастер 9736:75428](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9736-75428), слой `I9736:75308;9733:75183`, свойство `fills`.
238. **Primitives/Black/Primary** — [мастер 9736:75428](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9736-75428), слой `I9736:75308;9733:75184`, свойство `fills`.
239. **Primitives/Black/Primary** — [мастер 9736:75428](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9736-75428), слой `I9736:75362;9733:75183`, свойство `fills`.
240. **Primitives/Black/Primary** — [мастер 9736:75428](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9736-75428), слой `I9736:75362;9733:75184`, свойство `fills`.
241. **Primitives/Black/Primary** — [мастер 9736:75428](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9736-75428), слой `I9736:75410;9733:75183`, свойство `fills`.
242. **Primitives/Black/Primary** — [мастер 9736:75428](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9736-75428), слой `I9736:75410;9733:75184`, свойство `fills`.
243. **Primitives/Black/Primary** — [мастер 9736:75428](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9736-75428), слой `9736:75792`, свойство `fills`.
244. **Primitives/Blueberry/Dark blueberry 100** — [мастер 9736:75807](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9736-75807), слой `I9736:75610;9736:75595;9736:75215`, свойство `region0`.
245. **Primitives/Blueberry/Dark blueberry 100** — [мастер 9736:75807](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9736-75807), слой `I9736:75610;9736:75595;9736:75215`, свойство `region1`.
246. **Primitives/Blueberry/Dark blueberry 100** — [мастер 9736:75807](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9736-75807), слой `I9736:75610;9736:75595;9736:75215`, свойство `region2`.
247. **Primitives/Black/Primary** — [мастер 9736:75807](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9736-75807), слой `I9736:75610;9736:75447`, свойство `fills`.
248. **Primitives/Black/Primary** — [мастер 9736:75807](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9736-75807), слой `I9736:75610;9736:75448`, свойство `fills`.
249. **Primitives/Black/Primary** — [мастер 9736:75807](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9736-75807), слой `I9736:75629;9736:75447`, свойство `fills`.
250. **Primitives/Black/Primary** — [мастер 9736:75807](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9736-75807), слой `I9736:75629;9736:75448`, свойство `fills`.
251. **Primitives/Black/Primary** — [мастер 9736:75807](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9736-75807), слой `I9736:75683;9736:75447`, свойство `fills`.
252. **Primitives/Black/Primary** — [мастер 9736:75807](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9736-75807), слой `I9736:75683;9736:75448`, свойство `fills`.
253. **Primitives/Black/Primary** — [мастер 9736:75807](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9736-75807), слой `I9736:75723;9736:75447`, свойство `fills`.
254. **Primitives/Black/Primary** — [мастер 9736:75807](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9736-75807), слой `I9736:75723;9736:75448`, свойство `fills`.
255. **Primitives/Black/Primary** — [мастер 9736:75807](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9736-75807), слой `9736:75800`, свойство `fills`.
256. **Primitives/Violet/Primary** — [мастер 10520:85045](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=10520-85045), слой `10520:85018`, свойство `fills`.
257. **Primitives/Blueberry/15** — [мастер 10520:85045](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=10520-85045), слой `10520:85019`, свойство `strokes`.
258. **[Deprecated]/Brand/Partners/Sber** — [мастер 10520:85045](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=10520-85045), слой `I10520:85022;7680:48592`, свойство `fills`.
259. **Primitives/Grey/Medium** — [мастер 10520:85045](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=10520-85045), слой `10520:85028`, свойство `fills`.
260. **Primitives/Grey/Light** — [мастер 10520:85119](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=10520-85119), слой `10520:85063`, свойство `fills`.
261. **Primitives/Grey/Primary** — [мастер 10520:85119](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=10520-85119), слой `10520:85068`, свойство `fills`.
262. **Primitives/Grey/Light** — [мастер 10520:85119](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=10520-85119), слой `10520:85070`, свойство `strokes`.
263. **Black / Primary** — [мастер 10520:85119](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=10520-85119), слой `I10520:85071;2089:12`, свойство `region0`.
264. **[Deprecated]/Brand/Partners/Sber** — [мастер 10520:85119](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=10520-85119), слой `I10520:85076;7680:48592`, свойство `fills`.
265. **Primitives/Grey/Medium** — [мастер 10520:85119](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=10520-85119), слой `10520:85082`, свойство `fills`.
266. **[Deprecated]/Background/Decorative/Primary** — [мастер 10520:86054](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=10520-86054), слой `I10520:85248;5299:31118`, свойство `fills`.
267. **Primitives/Black/Primary** — [мастер 10520:86054](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=10520-86054), слой `I10520:85248;5299:31121`, свойство `fills`.
268. **Fill/Solid/AccentB** — [мастер 10520:86054](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=10520-86054), слой `I10520:85254;6022:33204`, свойство `fills`.
269. **Fill/Solid/AccentB** — [мастер 10520:86054](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=10520-86054), слой `I10520:85255;6022:33602`, свойство `fills`.
270. **Primitives/Blueberry/15** — [мастер 10520:86054](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=10520-86054), слой `I10520:85255;6022:33602`, свойство `strokes`.
271. **Primitives/Black/Primary** — [мастер 1633:37](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=1633-37), слой `I15374:175870;15374:174461;3644:1176`, свойство `region0`.
272. **[Deprecated]/Fill/Decorative/Midnight** — [мастер 16179:175769](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16179-175769), слой `16179:175966`, свойство `fills`.
273. **[Deprecated]/Fill/Decorative/Dark Violet** — [мастер 16179:175769](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16179-175769), слой `16179:175935`, свойство `fills`.
274. **[Deprecated]/Text & icon/on Dark/Secondary** — [мастер 16713:185931](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16713-185931), слой `I16512:178476;16498:177838;5105:30460`, свойство `fills`.
275. **Primitives/Black/Primary** — [мастер 16713:185931](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16713-185931), слой `I16512:178476;16498:177838;5105:30461`, свойство `fills`.
276. **[Deprecated]/Brand/Social/VK** — [мастер 16713:185931](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16713-185931), слой `I16512:178476;16498:177841;1088:8178;1087:10;16654:5052`, свойство `region0`.
277. **[Deprecated]/Brand/Social/Facebook** — [мастер 16713:185931](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16713-185931), слой `I16512:178476;16498:177841;1088:8173;1088:8110;2615:1922`, свойство `region0`.
278. **[Deprecated]/Text & icon/on Dark/Secondary** — [мастер 16498:177832](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16498-177832), слой `I16498:177838;5105:30460`, свойство `fills`.
279. **Primitives/Black/Primary** — [мастер 16498:177832](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16498-177832), слой `I16498:177838;5105:30461`, свойство `fills`.
280. **[Deprecated]/Brand/Social/VK** — [мастер 16498:177832](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16498-177832), слой `I16498:177841;1088:8178;1087:10;16654:5052`, свойство `region0`.
281. **[Deprecated]/Brand/Social/Facebook** — [мастер 16498:177832](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16498-177832), слой `I16498:177841;1088:8173;1088:8110;2615:1922`, свойство `region0`.
282. **Primitives/Black/Primary** — [мастер 16498:177851](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16498-177851), слой `I16498:177858;5105:30461`, свойство `fills`.
283. **Primitives/Black/Primary** — [мастер 16498:177872](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16498-177872), слой `I16498:177879;5105:30461`, свойство `fills`.
284. **Primitives/Black/Primary** — [мастер 16498:177887](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16498-177887), слой `I16498:177894;5105:30461`, свойство `fills`.
285. **[Deprecated]/Text & icon/on Dark/Secondary** — [мастер 16713:186123](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16713-186123), слой `I16713:186092;5105:30460`, свойство `fills`.
286. **Primitives/Black/Primary** — [мастер 16713:186123](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16713-186123), слой `I16713:186092;5105:30461`, свойство `fills`.
287. **[Deprecated]/Brand/Social/VK** — [мастер 16713:186123](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16713-186123), слой `I16713:186095;1091:144;1087:10;16654:5052`, свойство `region0`.
288. **[Deprecated]/Brand/Social/Facebook** — [мастер 16713:186123](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16713-186123), слой `I16713:186095;1091:139;1088:8110;2615:1922`, свойство `region0`.
289. **Primitives/Black/Primary** — [мастер 16713:186166](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16713-186166), слой `I16713:186133;15508:173358;5105:30470`, свойство `fills`.
290. **[Deprecated]/Brand/Social/VK** — [мастер 16713:186166](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16713-186166), слой `I16713:186136;1091:144;1087:10;16654:5052`, свойство `region0`.
291. **[Deprecated]/Brand/Social/Facebook** — [мастер 16713:186166](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16713-186166), слой `I16713:186136;1091:139;1088:8110;2615:1922`, свойство `region0`.
292. **Primitives/Black/Primary** — [мастер 16713:186166](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16713-186166), слой `I16713:186136;1091:140;1087:31;3841:1130`, свойство `region0`.
293. **Primitives/Black/Primary** — [мастер 16713:186166](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16713-186166), слой `I16713:186136;1091:140;1087:31;3841:1130`, свойство `region1`.
294. **Primitives/Black/Primary** — [мастер 16713:186166](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16713-186166), слой `I16713:186136;1091:140;1087:31;3841:1130`, свойство `region2`.
295. **Primitives/Black/Primary** — [мастер 16498:177925](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16498-177925), слой `I16498:177933;5105:30544`, свойство `fills`.
296. **Primitives/Black/Primary** — [мастер 16498:177951](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16498-177951), слой `I16498:177958;5105:30544`, свойство `fills`.
297. **Primitives/Black/Primary** — [мастер 16498:177972](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16498-177972), слой `I16498:177979;5105:30544`, свойство `fills`.
298. **[Deprecated]/Text & icon/on Dark/Secondary** — [мастер 16498:177985](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16498-177985), слой `I16498:177992;5105:30543`, свойство `fills`.
299. **Primitives/Black/Primary** — [мастер 16498:177985](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16498-177985), слой `I16498:177992;5105:30544`, свойство `fills`.
300. **[Deprecated]/Brand/Social/VK** — [мастер 16498:177985](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16498-177985), слой `I16498:177995;1091:144;1087:10;16654:5052`, свойство `region0`.
301. **[Deprecated]/Brand/Social/Facebook** — [мастер 16498:177985](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16498-177985), слой `I16498:177995;1091:139;1088:8110;2615:1922`, свойство `region0`.
302. **Primitives/Grey/Primary** — [мастер 19355:299853](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=19355-299853), слой `19355:299858`, свойство `fills`.
303. **Primitives/Black/78** — [мастер 19355:299853](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=19355-299853), слой `19355:299863`, свойство `fillRange`.
304. **Primitives/Black/90** — [мастер 19355:299853](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=19355-299853), слой `19355:299863`, свойство `fillRange`.
305. **Primitives/Black/78** — [мастер 19355:299853](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=19355-299853), слой `19355:299863`, свойство `fillRange`.
306. **Primitives/Grey/50** — [мастер 19355:299853](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=19355-299853), слой `19355:299867`, свойство `fills`.
307. **Primitives/Black/78** — [мастер 19355:299853](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=19355-299853), слой `19355:299869`, свойство `fills`.
308. **Primitives/Black/Primary** — [мастер 1105:2](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=1105-2), слой `I22380:327125;5105:30461`, свойство `fills`.

