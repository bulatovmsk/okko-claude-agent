# Лояльность: замена цветов

Дата: 20 октября 2026. [Страница «Лояльность»](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=24837-340094).

Обновлены **295 уникальных слоёв**. Выполнены 293 прямые замены старых стилей и 15 операций static white/black; часть слоёв участвовала в обоих этапах. Ещё 2 кандидата static обновились по наследованию.

Проверены все **130 мастеров** со вложениями и скрытыми слоями. Полный обход страницы: **1197 узлов**, включая саму страницу и контейнеры. Из 130 мастеров 30 старых вариантов /True оставлены как возможные Light; причина ниже.

Обновлены Solid Primary/Accent/Third, Primary/Secondary/Third/Fourth текста и иконок, Skeleton. Старые привязки electric900 исчезли из обработанных вариантов Switch; существующие актуальные переменные с другими локальными ID коллекций сохранены по их библиотечным ключам. Белые подписи на цветных фонах получили существующие static-токены. Цвета без токенов и изображения оставлены.

## Технически отложены 24 региона в четырёх логотипах

Четыре вложенных **Sber / Full Spasibo**, Color=White, содержат смешанные регионы: шесть серых регионов старого Text & icon/on Dark/Forth и восемь зелёных регионов Sber в каждом векторе.

Цель серых регионов известна: **color/text-icon/fourth**. Зелёные регионы должны остаться по договорённости.

- [🟡 Widget Spasibo → Breakponts=1720+, State=Dissable, Skeleton=False](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=32352-977)
- [🟡 Widget Spasibo → Breakponts=960+, State=Dissable, Skeleton=False](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=38496-1796)
- [🟡 Widget Spasibo → Breakponts=600+, State=Dissable, Skeleton=False](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=32352-982)
- [🟡 Widget Spasibo → Breakponts=320+, State=Dissable, Skeleton=False](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=32352-987)

Общая заливка этих векторов смешанная. Обычная замена fills была пропущена с четырьмя ошибками mixed paints до изменения узлов. Запись отдельных регионов требует vector network; Figma не допускает такую запись внутри инстансов. Полный перекрас уничтожил бы зелёные регионы, поэтому не выполнялся.

Проверен точный исходный мастер в Head Library: [Sber / Full Spasibo, Color=White](https://www.figma.com/design/HYB1u9ysALVWtVWKoagiDH/?node-id=26255-211), key 10a528c0a31439d76901c206e34bd043a3d5f867. Его соответствующие белые регионы — сырые цвета без токенов, а не старый Fourth. По правилу «цвета без токена не трогаем» исходник не изменялся. В текущих четырёх инстансах это отдельные серые переопределения. Для завершения нужна ручная замена именно этих регионов в Figma либо отдельное решение по устройству исходника.

Регионы в каждом из четырёх векторов: **0, 1, 2, 3, 4, 8**. Полные ID векторов и 24 записи сохранены в JSON.

## Согласованный пропуск Sber

Сохранены **13 применений Brand/Partners/Sber** у Partner Button и **32 привязки brand/partners/sber** в зелёных регионах четырёх логотипов. Это сплошной Sber, который пользователь просил пока не менять. Подписи на цветных кнопках закреплены static-токенами.

Итого в доступных темах осталось **37 старых paint-ссылок**: 24 региона Fourth и 13 Sber. Отдельные 32 привязки переменных Sber не прибавлены к числу paint-ссылок.

## Старые варианты /True: возможная светлая тема

В секции Deprecated есть 30 отдельных мастеров Tumbler/Bubble с окончанием /True. Явного свойства Theme у них больше нет. В обычных подписях таких Tumbler используются on Light Primary/Third; в соответствующих /False — on Dark. Это свидетельствует о возможной светлой теме, но точное имя прежнего булева свойства не восстановлено.

**Эти 30 мастеров и вложенные экземпляры с такими именами не редактировались**, включая ранее согласованные исключения для отдельных on Light-токенов. Это консервативное решение по правилу «если сомневаешься — оставить и перечислить». Нужно подтвердить назначение /True, если эти варианты следует включить в миграцию.

В этой группе осталось **83 применения старых paint-стилей** и 10 связанных привязок primitives/electric900. В итоговом JSON они помечены light + loyaltyDeferred; это отдельная группа исключений, а не доказанное актуальное свойство Theme.

- [_[Deprecated]🟡  Tumbler Spasibo/1720+/able/True](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=27269-28426)
- [_[Deprecated]🟡  Tumbler Spasibo/1720+/0 TVOD/True](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=27269-28446)
- [_[Deprecated]🟡  Tumbler Spasibo/1720+/another method/True](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=27269-28463)
- [_[Deprecated]🟡  Tumbler Spasibo/1720+/max discount/True](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=27269-28615)
- [_[Deprecated]🟡  Tumbler Spasibo/1320+/able/True](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=27269-28684)
- [_[Deprecated]🟡  Tumbler Spasibo/1320+/0 TVOD/True](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=27269-28690)
- [_[Deprecated]🟡  Tumbler Spasibo/1320+/another method/True](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=27269-28693)
- [_[Deprecated]🟡  Tumbler Spasibo/1320+/max discount/True](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=27269-28696)
- [_[Deprecated]🟡  Tumbler Spasibo/600+/able/True](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=27269-28790)
- [_[Deprecated]🟡  Tumbler Spasibo/600+/0 TVOD/True](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=27269-28796)
- [_[Deprecated]🟡  Tumbler Spasibo/600+/another method/True](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=27269-28799)
- [_[Deprecated]🟡  Tumbler Spasibo/600+/max discount/True](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=27269-28802)
- [_[Deprecated]🟡  Tumbler Spasibo/375+/able/True](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=27269-28896)
- [_[Deprecated]🟡  Tumbler Spasibo/375+/0 TVOD/True](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=27269-28902)
- [_[Deprecated]🟡  Tumbler Spasibo/375+/another method/True](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=27269-28905)
- [_[Deprecated]🟡  Tumbler Spasibo/375+/max discount/True](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=27269-28908)
- [_[Deprecated]🟡  Tumbler Spasibo/320+/able/True](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=27269-29026)
- [_[Deprecated]🟡  Tumbler Spasibo/320+/0 TVOD/True](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=27269-29032)
- [_[Deprecated]🟡  Tumbler Spasibo/320+/another method/True](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=27269-29035)
- [_[Deprecated]🟡  Tumbler Spasibo/320+/max discount/True](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=27269-29038)
- [_[Deprecated]🟡  Bubble Spasibo/1720+/Rest/True](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=27269-28541)
- [_[Deprecated]🟡  Bubble Spasibo/1720+/Disabled/True](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=27269-28545)
- [_[Deprecated]🟡  Bubble Spasibo/1320+/Rest/True](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=27269-28548)
- [_[Deprecated]🟡  Bubble Spasibo/1320+/Disabled/True](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=27269-28552)
- [_[Deprecated]🟡  Bubble Spasibo/600+/Rest/True](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=27269-28555)
- [_[Deprecated]🟡  Bubble Spasibo/600+/Disabled/True](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=27269-28559)
- [_[Deprecated]🟡  Bubble Spasibo/375+/Rest/True](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=27269-28562)
- [_[Deprecated]🟡  Bubble Spasibo/375+/Disabled/True](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=27269-28566)
- [_[Deprecated]🟡  Bubble Spasibo/320+/Rest/True](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=27269-28569)
- [_[Deprecated]🟡  Bubble Spasibo/320+/Disabled/True](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=27269-28573)

## Вне мастеров

Оставлены **6 ссылок на старые стили**: 2 у заголовков страницы и 4 у внешних Label Main (NEW SB Gradient и Main / White). Внешнее оформление и примеры напрямую не редактировались.

Новых дизайн-переменных, aliases, коллекций и стилей не создавал. Использованы существующие библиотечные ресурсы. Геометрия, тексты, свойства вариантов и прочие переопределения не менялись. В Head Library изменений не выполнялось.

## Проверка

Полный программный аудит fills/strokes, всех регионов векторов, градиентных остановок, текстовых диапазонов, эффектов и скрытых вложений. Ошибок финального чтения и неразрешённых ссылок нет. Четыре ограничения записи смешанных векторов учтены выше; они не означают успешную миграцию оставшихся регионов. Панель Selection colors вручную не проверялась.

При выборе всей страницы старые цвета останутся видны из перечисленных 24 регионов, Sber, 30 исключённых /True-мастеров и внешнего оформления.

