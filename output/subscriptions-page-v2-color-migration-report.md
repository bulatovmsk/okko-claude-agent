# Миграция цветов: Подписки (14176:164159)

Дата: 20.10.2026. [Страница в Figma](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=14176-164159).

Проверены **116 мастеров**, 8652 слоя со скрытыми вложениями. Итоговый аудит всей страницы охватил 8786 узлов. Полное чтение ранее задерживалось; выполнен обход по индексу мастеров, чтение однородных векторов по заливке и смешанных — по отдельным областям.

## Выполнено

Обновлены **1713 уникальных слоёв**. Журналы содержат 1570 обычных замен свойств и 172 замены диапазонов в 86 текстовых слоях. В 91 слое передний план на цветной подложке привязан к static white/black с сохранением эффективной непрозрачности. Эти числа пересекаются; 1713 — объединение IDs, а не сумма операций.

Заменены согласованные токены текста, цен/офферов, заливок и границ. Новые переменные, коллекции, aliases и стили не создавались. Нетокенизированные цвета оставлены, в том числе 18 найденных передних планов на цветных подложках. Light исключён, прежние актуальные привязки светлых вложений сохранены. Структура, геометрия, текст и свойства вариантов сохранены.

## Осталось в мастерах — 56 применений

Из них **47 требуют выбора**, **9 однотонных Sber отложены по вашему указанию**.

### Primitives/Black/Primary — 22

Rectangle 288 внутри Замок / Compare Table Status.

Маленькая чёрная часть графики замка, isMask=false. Нужно определить, является ли она фиксированной частью рисунка/вырезом либо нейтральным знаком невыбранного состояния; по RGB семантику не назначал.

Кандидаты из существующих токенов: `color/static/solid/black`, `color/text-icon/fourth`. Это варианты для решения, не утверждённое соответствие.

Расположение:

- [Breakpoint=Tablet 1024+, Type=Compare](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=15028-173221) — `I18493:299964;18493:299107;18493:298816;10043:3579`, fills.
- [Breakpoint=Tablet 1024+, Type=Compare](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=15028-173221) — `I18493:299964;18493:299206;18493:298816;10043:3579`, fills.
- [Breakpoint=Tablet 1024+, Type=Compare](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=15028-173221) — `I18493:299964;31088:12699;18493:298816;10043:3579`, fills.
- [Breakpoint=Tablet 1024+, Type=Compare](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=15028-173221) — `I18493:299964;18493:299329;18493:298816;10043:3579`, fills.
- [Breakpoint=Tablet 1024+, Type=Compare](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=15028-173221) — `I18493:300001;18493:299329;18493:298816;10043:3579`, fills.
- [Breakpoint=Tablet 1024+, Type=Upgrade](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=27709-17313) — `I27709:17315;31088:13131;18493:298816;10043:3579`, fills.
- [Breakpoint=Tablet 1024+, Type=Upgrade](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=27709-17313) — `I27709:17315;22624:328864;18493:298816;10043:3579`, fills.
- [Breakpoint=Tablet 1024+, Type=Upgrade](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=27709-17313) — `I27709:17316;31088:12699;18493:298816;10043:3579`, fills.
- [Breakpoint=Tablet 1024+, Type=Upgrade](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=27709-17313) — `I27709:17317;18493:299329;18493:298816;10043:3579`, fills.
- [Breakpoint=Tablet 1024+, Type=Upgrade](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=27709-17313) — `I35441:9335;31088:13131;18493:298816;10043:3579`, fills.
- [Breakpoint=Tablet 1024+, Type=Upgrade](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=27709-17313) — `I35441:9335;22624:328864;18493:298816;10043:3579`, fills.
- [Breakpoint=Tablet 1024+, Type=Upgrade](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=27709-17313) — `I35441:9336;31088:12699;18493:298816;10043:3579`, fills.
- [Breakpoint=Tablet 1024+, Type=Upgrade](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=27709-17313) — `I35441:9337;18493:299329;18493:298816;10043:3579`, fills.
- [Type=Unpurchased, Breakpoint=Tablet 1024+](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=14419-170122) — `I18493:299107;18493:298816;10043:3579`, fills.
- [Type=Unpurchased, Breakpoint=Tablet 1024+](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=14419-170122) — `I18493:299206;18493:298816;10043:3579`, fills.
- [Type=Unpurchased, Breakpoint=Tablet 1024+](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=14419-170122) — `I31088:12699;18493:298816;10043:3579`, fills.
- [Type=Unpurchased, Breakpoint=Tablet 1024+](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=14419-170122) — `I18493:299329;18493:298816;10043:3579`, fills.
- [Type=My, Breakpoint=Tablet 1024+](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=14419-170421) — `I22624:328862;18493:298816;10043:3579`, fills.
- [Type=My, Breakpoint=Tablet 1024+](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=14419-170421) — `I22624:328863;18493:298816;10043:3579`, fills.
- [Type=My, Breakpoint=Tablet 1024+](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=14419-170421) — `I31088:13131;18493:298816;10043:3579`, fills.
- [Type=My, Breakpoint=Tablet 1024+](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=14419-170421) — `I22624:328864;18493:298816;10043:3579`, fills.
- [Включено=False, Размер=1024+](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=18493-298815) — `I18493:298816;10043:3579`, fills.

### Fill/Decorative/Sky — 21

Widget Upsale & Upgrade / текстовые знаки +.

Исходная заливка — голубой радиальный градиент. Подтверждённого актуального декоративного соответствия нет; переход на семантический текстовый цвет требует выбора роли.

Кандидаты из существующих токенов: `color/text-icon/primary`, `color/text-icon/accent`. Это варианты для решения, не утверждённое соответствие.

Расположение:

- [Размер=Desktop 1720+](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=14176-171211) — `14372:170172`, fills.
- [Размер=Tablet 600+](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=14425-171020) — `18698:299173`, fills.
- [Размер=Mobile 320+](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=14295-169250) — `14372:170258`, fills.
- [Тип=Мой, Размер=1720+, Оффер=False](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=14315-169330) — `14315:169338`, fills.
- [Тип=Новый, Размер=1720+, Оффер=False](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=14315-169346) — `14315:169348`, fills.
- [Тип=Новый, Размер=1720+, Оффер=True](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=17472-253991) — `17472:253995`, fills.
- [Тип=Новый, Размер=1440, Оффер=False](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=14400-170133) — `14400:170153`, fills.
- [Тип=Новый, Размер=1440, Оффер=True](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=17472-254005) — `17472:254012`, fills.
- [Тип=Новый, Размер=1024, Оффер=False](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=14424-170945) — `14424:170965`, fills.
- [Тип=Новый, Размер=1024, Оффер=True](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=17472-254019) — `17472:254026`, fills.
- [Тип=Новый, Размер=768, Оффер=False](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=14444-171543) — `14444:171545`, fills.
- [Тип=Новый, Размер=768, Оффер=True](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=17472-254033) — `17472:254040`, fills.
- [Тип=Мой, Размер=1440, Оффер=False](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=14400-170203) — `14400:170205`, fills.
- [Тип=Мой, Размер=1024, Оффер=False](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=14424-170999) — `14424:171017`, fills.
- [Тип=Мой, Размер=768, Оффер=False](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=14444-171592) — `14444:171607`, fills.
- [Тип=Новый, Размер=375, Оффер=False](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=14313-169496) — `14313:169407`, fills.
- [Тип=Новый, Размер=375, Оффер=True](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=17472-254085) — `17472:254088`, fills.
- [Тип=Новый, Размер=320, Оффер=False](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=14452-172483) — `14453:172389`, fills.
- [Тип=Новый, Размер=320, Оффер=True](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=17472-254102) — `17472:254106`, fills.
- [Тип=Мой, Размер=375, Оффер=False](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=14313-169518) — `17472:253772`, fills.
- [Тип=Мой, Размер=320, Оффер=False](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=14453-172424) — `17472:253782`, fills.

### Elevation New/Solid/04 — 2

Период подписки / Тип=Мой, Размер=375 и 320 / strokes.

Старый уровень Elevation применяется как обводка. Нужен выбор между обычным разделением и выделением выбранного периода.

Кандидаты из существующих токенов: `color/border/solid`, `color/border/active`. Это варианты для решения, не утверждённое соответствие.

Расположение:

- [Тип=Мой, Размер=375, Оффер=False](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=14313-169518) — `14313:169518`, strokes.
- [Тип=Мой, Размер=320, Оффер=False](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=14453-172424) — `14453:172424`, strokes.

### Fill/Solid/AccentB — 2

Баннер апсейла / Размер=375 и 320 / базовая кнопка.

Однотонная заливка базовой кнопки; соответствие компонентному градиенту не подтверждено.

Кандидаты из существующих токенов: `color/fill/solid/accent`, `color/component/button`. Это варианты для решения, не утверждённое соответствие.

Расположение:

- [Размер=375](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=14296-169358) — `I14295:169334;6022:33388`, fills.
- [Размер=320](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=14451-177095) — `I14451:176969;6022:33388`, fills.

### [Deprecated]/Brand/Partners/Sber — 9

Sber Authorisation и Виджет авторизации Сбер ID / Button.

Оставлено по прямому указанию пользователя: однотонный Brand/Partners/Sber пока не менять.

Расположение:

- [Authorised=False, Breakpoints=Desktop 1720+](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=19356-299323) — `19470:304631`, fills.
- [Authorised=False, Breakpoints=Tablet 600+](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=21798-323594) — `21798:323598`, fills.
- [Authorised=False, Breakpoints=Mobile 320+](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=19367-299356) — `19470:304646`, fills.
- [Размер=1720+](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16991-213572) — `19469:307557`, fills.
- [Размер=1440](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16998-213435) — `19469:307581`, fills.
- [Размер=1024](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16998-213599) — `19469:307598`, fills.
- [Размер=768](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16999-213613) — `19469:307605`, fills.
- [Размер=375](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16995-213597) — `19469:307612`, fills.
- [Размер=320](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=17001-213492) — `19469:307625`, fills.

## Вне мастеров

Ещё **27 применений** старых стилей оставлены в секциях, подписи об обновлении, примерах инстансов и подписях состояний. Они не относятся к мастерам. Всего по странице — **83 применения 13 старых стилей**, из них в мастерах 56 применений 5 стилей.

## Проверка и ограничения

После обычной и диапазонной миграции повторно прочитаны заливки, обводки, диапазоны текста, эффекты, цвета точек градиента и смешанные векторные области. Ошибок записи и итогового чтения нет; старых смешанных текстовых диапазонов не осталось. Имена трёх незнакомых стилей уточнены непосредственно в Figma: Sky, Elevation New/Solid/04 и Grey/Medium.

Действующая переменная label/lighthouse из коллекции 41700 проверена по имени и ключу и сохранена. Внутренние привязки существующих градиентов Sber и color/component/button сохранены по известным ключам; в выгрузке для части этих внутренних переменных имя помечено UNRESOLVED, потому что оно отсутствует в загруженном каталоге. Эти записи не прибавляются к остаткам старых стилей. Отдельный неизвестный ключ цвета у внешней подписи находится вне области миграции и оставлен.

Аудит программный; ручная проверка Selection colors не заявляется. Полный список 1713 изменённых IDs и 56 остаточных применений сохранён в audit.json.

