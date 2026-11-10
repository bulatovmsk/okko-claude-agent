# Grid: замена цветов

Дата: 20 октября 2026. [UI Type → Grid](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=17529-266815).

Обновлены **90 уникальных слоёв**: 6 собственных слоёв мастеров, 83 слоя вложенных инстансов и 1 исходный вложенный Label с Continuum.

Проверены все **76 мастеров**, 36 886 слоёв в их деревьях и 13 901 узел вне мастеров. Полный охват страницы: **50 787 узлов**, включая саму страницу и контейнеры.

Заменены старые Fill/Solid/Secondary → color/fill/solid/secondary, Background/Solid/Primary → color/background/solid/primary и Border/Contour → color/border/contour. У Label с подтверждённой Theme=Continuum устаревшая переменная color/component/label/continuum из старой коллекции заменена существующим актуальным одноимённым градиентным стилем. Изменение одного Label [в Cover 1920](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=39756-152082) обновило 27 его применений в мастерах.

Проверка текста и иконок на цветном фоне не выявила дополнительных однозначных замен на static-токены. Цвета без стиля/переменной сохранены.

## Остатки в доступных темах

В мастерах осталось **54 применения старых paint-стилей** — по два региона в 27 вложенных векторах Bet Logo. Других старых paint-стилей и старых цветовых переменных в доступных темах не обнаружено.

| Стиль | Применений | Решение |
|---|---:|---|
| Color/fill/solid/hover-focus/Third, key 7190d7e2… | 27 | Старый радиальный градиент; текущий одноимённый hover-focus/third — линейный. По роли возможен inverse. Оставлен как неоднозначный. |
| Fill/Solid/Primary, key 974f85fc… | 27 | В исходной библиотеке это старый Inverse; цель color/fill/solid/inverse известна. Исходный Bet Logo обновлён ранее, но локальные старые версии/переопределения сохраняют старые регионы. Figma запрещает запись vector network внутри инстанса. Требуется обновить библиотечную версию и проверить переопределения. Detach, swap и сбросы не выполнялись. |

### Мастера с остатками Bet Logo

- [mainGrid → breakpoint=1920, theme=Dark](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=17529-291786)
- [mainGrid → breakpoint=1792(🔴Deprecated), theme=Dark](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=17529-291788)
- [mainGrid → breakpoint=1440(🔴Deprecated), theme=Dark](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=17529-291790)
- [mainGrid → breakpoint=1440, theme=Dark](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=17529-291792)
- [mainGrid → breakpoint=1024, theme=Dark](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=17529-291794)
- [mainGrid → breakpoint=768, theme=Dark](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=17529-291796)
- [mainGrid → breakpoint=375, theme=Dark](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=17529-291798)
- [mainGrid → breakpoint=320, theme=Dark](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=17529-291800)
- [squareGrid → breakpoint=1920, theme=Dark](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=17580-311176)
- [squareGrid → breakpoint=1792(🔴Deprecated), theme=Dark](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=17580-311178)
- [squareGrid → breakpoint=1440, theme=Dark](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=17580-311180)
- [squareGrid → breakpoint=1024, theme=Dark](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=17580-311184)
- [squareGrid → breakpoint=768, theme=Dark](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=17580-311186)
- [squareGrid → breakpoint=375, theme=Dark](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=17580-311188)
- [squareGrid → breakpoint=320, theme=Dark](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=17580-311190)
- [🟡personGrid → Breakpoint=1720+, Theme=Dark](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=30925-94043)
- [🟡personGrid → Breakpoint=1320+, Theme=Dark](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=30925-94066)
- [🟡personGrid → Breakpoint=960+, Theme=Dark](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=30925-94089)
- [🟡personGrid → Breakpoint=600+, Theme=Dark](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=30925-94112)
- [🟡personGrid → Breakpoint=375+, Theme=Dark](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=30925-94135)
- [🟡personGrid → Breakpoint=320+, Theme=Dark](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=30925-94168)
- [ticketGrid → breakpoint=1920](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=39759-158150)
- [ticketGrid → breakpoint=1440](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=39701-138648)
- [ticketGrid → breakpoint=1024](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=39701-138650)
- [ticketGrid → breakpoint=768](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=39701-138652)
- [ticketGrid → breakpoint=375](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=39704-134791)
- [ticketGrid → breakpoint=320](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=39701-138656)

Полные ID вложенных векторов, номера регионов и родительских инстансов записаны в JSON-аудите.

## Исключения и внешние примеры

- В мастерах в контекстах Light осталось **555 применений** старых paint-стилей.
- Вне мастеров осталось **467 применений**: 338 в обычном внешнем контексте, 125 в Light и 4 в Kids.
- Устаревшая переменная Lighthouse осталась только в исключённых контекстах Light: 158 применений внутри мастеров и 148 во внешних примерах. Это привязки переменных; они не прибавлены к числам paint-стилей выше.

Light/Kids напрямую не редактировались. Общие компоненты без свойства Theme обновлялись в собственных мастерах; такие изменения наследуются их инстансами, включая использование в Light. Именно наследование уменьшило число старых Background/Primary в Light на 72; отдельные Light-переопределения не создавались и не сбрасывались. Внешние примеры напрямую не редактировались.

Новые переменные, aliases, коллекции и стили не создавались. Применены существующие библиотечные ресурсы. Геометрия, текст и свойства вариантов не менялись.

## Проверка

Программный обход всех мастеров и остальных узлов страницы, включая скрытые вложения, fills/strokes, регионы векторов, градиентные остановки, текстовые диапазоны и эффекты. Ошибок итогового аудита и неразрешённых ссылок нет. Панель Selection colors вручную не проверялась.

В Selection colors всей страницы старые цвета ещё могут быть видны из перечисленных 54 применений Bet Logo, Light/Kids и внешних примеров. Отчёт не означает, что на всей странице отсутствуют Deprecated.

