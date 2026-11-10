# Подписки — миграция цветов

[Страница в Figma](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9821-75490)

## Результат

- Проверены **43 мастера**, **1345 слоёв** в мастерах и вложениях. Полный аудит страницы охватил **1464 узла**, включая примеры и контейнеры вне мастеров.
- Обновлены **170 уникальных слоёв**. Счётчик учитывает прямые изменения один раз; наследующие инстансы не увеличивают его.
- Число применений известных старых PAINT-стилей в мастерах и их вложениях уменьшилось с **565 до 64**. Часть применений исчезла через наследование после изменения базовых слоёв.
- Согласованные замены выполнены для текста, иконок, обводок, акционных цветов и заливок. Старых привязок в смешанных текстовых диапазонах не найдено.
- **22 слоя** с текстом/иконками на цветных фонах переведены на **static white/black** с сохранением видимой прозрачности. Эти 22 слоя частично пересекаются с основными заменами.
- **10 чёрных масок** карточек моно-подписки привязаны к существующему **color.static.solid.black**. RGB, прозрачность, видимость и режим смешивания проверены и сохранены; маски и геометрия не изменялись.
- Итоговая повторная проверка не нашла дополнительных кандидатов на static в обработанных контекстах. Ошибок чтения/записи и недоступных стилей нет. Один мастер карточки проверен визуально после изменений; ручной проверки Selection colors в интерфейсе не было.

## Остатки для согласования

В рабочей области осталось **64 применения старых PAINT-стилей**, пять групп:

| Старый стиль | Применений | Где | Существующие кандидаты / причина |
|---|---:|---|---|
| Primitives/Violet/Primary | 7 | Фон основных кнопок. [Пример мастера](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=1985-11184) | color.fill.solid.accent либо градиент color.component.button. Не подтверждено, нужно ли сохранить сплошную заливку или перейти на градиент. |
| Pink / Light | 14 | Метка «Первые 7 дней бесплатно». [Пример мастера](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=1985-11184) | color.fill.solid.accent либо один из существующих color.component.label.*. Нужен выбор семантики промометки; замена Pink/Light на negative здесь не соответствует роли. |
| Fill/Solid/AccentB | 23 | Базовые кнопки во вложениях. [Пример мастера](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=4583-27574) | color.fill.solid.accent либо color.component.button. Случаи радио/переключателя и loader из прошлых страниц на эти кнопки не распространяются. |
| [Deprecated]/Background/Decorative/Primary | 10 | BG карточки подписки. [Пример мастера](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9868-76023) | color.fill.solid.accent либо color.background.solid.* после выбора роли и уровня поверхности. Старый декоративный фон привязан к primitives/electric1100, точное соответствие не согласовано. |
| Primitives/Violet/Dark | 10 | BG карточки моно-подписки. [Пример мастера](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=10365-82856) | color.fill.solid.accent либо color.background.solid.*. Требуется решить, сохраняем ли фиолетовый декоративный фон; точный существующий токен для этого оттенка не подтверждён. |

У десяти BG с Background/Decorative/Primary сохранились десять привязок **primitives/electric1100** внутри того же стиля. Это те же десять заливок, а не дополнительные десять слоёв или отдельные применения поверх счётчика 64.

Существующие **color.fill.solid.positive**, **color.text-icon.primary** и **color.text-icon.secondary** из импортированной коллекции 41700 сверены по ключам с актуальными ресурсами и не считаются устаревшими из-за идентификатора коллекции.

## Вне рабочей области

Вне мастеров осталось **19 старых привязок**: фоновые контейнеры, заголовки/пояснения, примеры кнопок и отметки «Не пошли в работу». Они учтены отдельно от 64 и не редактировались напрямую. Исключённых Light/Kids-контекстов при проверке этой страницы не выявлено.

Новые токены, переменные и коллекции не создавались. Цвета без токена сохранены. Текст, геометрия, структура и свойства вариантов не менялись. Инстансы не отсоединялись и не сбрасывались; цветовые привязки во вложениях обновлялись адресно.

## Все 64 оставшихся применения

1. **Primitives/Violet/Primary** — [мастер 1985:11184](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=1985-11184), слой `1984:11187`, свойство `fills`.
2. **Pink / Light** — [мастер 1985:11184](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=1985-11184), слой `1984:11395`, свойство `fills`.
3. **Pink / Light** — [мастер 2075:81](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=2075-81), слой `2075:71`, свойство `fills`.
4. **Fill/Solid/AccentB** — [мастер 4583:27574](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=4583-27574), слой `I4583:27568;4496:35918`, свойство `fills`.
5. **Fill/Solid/AccentB** — [мастер 4583:27599](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=4583-27599), слой `I4583:31845;4496:35918`, свойство `fills`.
6. **Fill/Solid/AccentB** — [мастер 4595:26552](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=4595-26552), слой `I4595:26567;4496:35918`, свойство `fills`.
7. **Fill/Solid/AccentB** — [мастер 5944:33122](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5944-33122), слой `I5944:33127;4583:27242;4583:27568;4496:35918`, свойство `fills`.
8. **Fill/Solid/AccentB** — [мастер 5944:33122](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5944-33122), слой `I6674:40512;4583:31845;4496:35918`, свойство `fills`.
9. **Fill/Solid/AccentB** — [мастер 5944:33122](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5944-33122), слой `I6674:40514;4583:27568;4496:35918`, свойство `fills`.
10. **Fill/Solid/AccentB** — [мастер 5944:33122](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5944-33122), слой `I6674:40513;4583:27568;4496:35918`, свойство `fills`.
11. **Fill/Solid/AccentB** — [мастер 5944:33122](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5944-33122), слой `I6674:40515;4583:27568;4496:35918`, свойство `fills`.
12. **Fill/Solid/AccentB** — [мастер 5945:32734](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5945-32734), слой `I6674:40652;4595:26567;4496:35918`, свойство `fills`.
13. **Fill/Solid/AccentB** — [мастер 5945:32734](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5945-32734), слой `I6674:40654;4595:26567;4496:35918`, свойство `fills`.
14. **Fill/Solid/AccentB** — [мастер 5945:32734](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5945-32734), слой `I6674:40653;4595:26567;4496:35918`, свойство `fills`.
15. **Fill/Solid/AccentB** — [мастер 5945:32734](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5945-32734), слой `I6674:40655;4595:26567;4496:35918`, свойство `fills`.
16. **Pink / Light** — [мастер 2075:211](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=2075-211), слой `I2075:82;2075:71`, свойство `fills`.
17. **Pink / Light** — [мастер 2075:211](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=2075-211), слой `I2075:93;2075:71`, свойство `fills`.
18. **Pink / Light** — [мастер 2075:211](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=2075-211), слой `I2075:105;2075:71`, свойство `fills`.
19. **Pink / Light** — [мастер 2075:211](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=2075-211), слой `I2075:116;2075:71`, свойство `fills`.
20. **Pink / Light** — [мастер 2075:211](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=2075-211), слой `I2075:127;2075:71`, свойство `fills`.
21. **Pink / Light** — [мастер 2075:211](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=2075-211), слой `I2075:138;2075:71`, свойство `fills`.
22. **Primitives/Violet/Primary** — [мастер 1986:11250](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=1986-11250), слой `I1985:11217;1984:11187`, свойство `fills`.
23. **Pink / Light** — [мастер 1986:11250](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=1986-11250), слой `I1985:11217;1984:11395`, свойство `fills`.
24. **Primitives/Violet/Primary** — [мастер 1986:11250](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=1986-11250), слой `I1985:11218;1984:11187`, свойство `fills`.
25. **Pink / Light** — [мастер 1986:11250](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=1986-11250), слой `I1985:11218;1984:11395`, свойство `fills`.
26. **Primitives/Violet/Primary** — [мастер 1986:11250](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=1986-11250), слой `I1985:11219;1984:11187`, свойство `fills`.
27. **Pink / Light** — [мастер 1986:11250](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=1986-11250), слой `I1985:11219;1984:11395`, свойство `fills`.
28. **Primitives/Violet/Primary** — [мастер 1986:11250](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=1986-11250), слой `I1985:11220;1984:11187`, свойство `fills`.
29. **Pink / Light** — [мастер 1986:11250](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=1986-11250), слой `I1985:11220;1984:11395`, свойство `fills`.
30. **Primitives/Violet/Primary** — [мастер 1986:11250](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=1986-11250), слой `I1985:11221;1984:11187`, свойство `fills`.
31. **Pink / Light** — [мастер 1986:11250](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=1986-11250), слой `I1985:11221;1984:11395`, свойство `fills`.
32. **Primitives/Violet/Primary** — [мастер 1986:11250](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=1986-11250), слой `I1986:11237;1984:11187`, свойство `fills`.
33. **Pink / Light** — [мастер 1986:11250](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=1986-11250), слой `I1986:11237;1984:11395`, свойство `fills`.
34. **Fill/Solid/AccentB** — [мастер 4583:27495](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=4583-27495), слой `I4583:27420;4583:31845;4496:35918`, свойство `fills`.
35. **Fill/Solid/AccentB** — [мастер 4583:27495](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=4583-27495), слой `I4583:31886;4583:27568;4496:35918`, свойство `fills`.
36. **Fill/Solid/AccentB** — [мастер 4583:27495](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=4583-27495), слой `I4583:31911;4583:27568;4496:35918`, свойство `fills`.
37. **Fill/Solid/AccentB** — [мастер 4607:295](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=4607-295), слой `I4607:205;4595:26567;4496:35918`, свойство `fills`.
38. **Fill/Solid/AccentB** — [мастер 4607:295](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=4607-295), слой `I4607:207;4595:26567;4496:35918`, свойство `fills`.
39. **[Deprecated]/Background/Decorative/Primary** — [мастер 9868:76023](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9868-76023), слой `9868:76026`, свойство `fills`.
40. **[Deprecated]/Background/Decorative/Primary** — [мастер 9868:76044](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9868-76044), слой `9868:76048`, свойство `fills`.
41. **Fill/Solid/AccentB** — [мастер 9868:76044](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9868-76044), слой `I9868:76066;6022:33388`, свойство `fills`.
42. **[Deprecated]/Background/Decorative/Primary** — [мастер 9868:76067](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9868-76067), слой `9868:76070`, свойство `fills`.
43. **[Deprecated]/Background/Decorative/Primary** — [мастер 9868:76086](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9868-76086), слой `9868:76090`, свойство `fills`.
44. **[Deprecated]/Background/Decorative/Primary** — [мастер 9868:76097](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9868-76097), слой `9868:76101`, свойство `fills`.
45. **Fill/Solid/AccentB** — [мастер 9868:76097](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9868-76097), слой `I9868:76102;6022:33388`, свойство `fills`.
46. **[Deprecated]/Background/Decorative/Primary** — [мастер 9868:76109](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9868-76109), слой `9868:76113`, свойство `fills`.
47. **[Deprecated]/Background/Decorative/Primary** — [мастер 9868:76120](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9868-76120), слой `9868:76124`, свойство `fills`.
48. **[Deprecated]/Background/Decorative/Primary** — [мастер 9868:76131](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9868-76131), слой `9868:76135`, свойство `fills`.
49. **[Deprecated]/Background/Decorative/Primary** — [мастер 9868:76142](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9868-76142), слой `9868:76146`, свойство `fills`.
50. **[Deprecated]/Background/Decorative/Primary** — [мастер 9868:76153](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9868-76153), слой `9868:76157`, свойство `fills`.
51. **Fill/Solid/AccentB** — [мастер 9868:76153](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9868-76153), слой `I9868:76158;6022:33388`, свойство `fills`.
52. **Primitives/Violet/Dark** — [мастер 10365:82856](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=10365-82856), слой `10365:82861`, свойство `fills`.
53. **Primitives/Violet/Dark** — [мастер 10365:82868](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=10365-82868), слой `10365:82873`, свойство `fills`.
54. **Primitives/Violet/Dark** — [мастер 10365:82882](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=10365-82882), слой `10365:82887`, свойство `fills`.
55. **Fill/Solid/AccentB** — [мастер 10365:82882](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=10365-82882), слой `I10365:82888;6022:33388`, свойство `fills`.
56. **Primitives/Violet/Dark** — [мастер 10365:82897](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=10365-82897), слой `10365:82902`, свойство `fills`.
57. **Primitives/Violet/Dark** — [мастер 10365:82911](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=10365-82911), слой `10365:82916`, свойство `fills`.
58. **Primitives/Violet/Dark** — [мастер 10365:82925](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=10365-82925), слой `10365:82930`, свойство `fills`.
59. **Primitives/Violet/Dark** — [мастер 10365:82939](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=10365-82939), слой `10365:82944`, свойство `fills`.
60. **Primitives/Violet/Dark** — [мастер 10365:82953](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=10365-82953), слой `10365:82958`, свойство `fills`.
61. **Primitives/Violet/Dark** — [мастер 10365:82967](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=10365-82967), слой `10365:82972`, свойство `fills`.
62. **Fill/Solid/AccentB** — [мастер 10365:82967](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=10365-82967), слой `I10365:82981;6022:33382`, свойство `fills`.
63. **Primitives/Violet/Dark** — [мастер 10365:82982](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=10365-82982), слой `10365:82987`, свойство `fills`.
64. **Fill/Solid/AccentB** — [мастер 10365:82982](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=10365-82982), слой `I10365:82988;6022:33388`, свойство `fills`.

