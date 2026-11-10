# Кнопки (адаптивные): замена цветов

Дата: 20 октября 2026. [Страница «Кнопки (адаптивные)»](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6037-35991).

Обновлены **233 уникальных слоёв**. Проверены все **113 мастера** с вложениями и скрытыми слоями. Полный обход страницы: **1141 узел**, включая саму страницу и оформление.

Выполнены 222 прямые операции по согласованной таблице, 10 операций у красных индикаторов снижения коэффициентов и 1 у скрытой стрелки снижения в OSD. Дополнительно один текстовый слой на зелёном Sber-фоне получил существующий static white; этот слой уже учтён среди остальных изменений.

Обновлены Glassy Third, Primary/Secondary/Third/Accent/Positive/Negative текста и иконок, декоративный Button, Fill Inverse, Border Glassy, Fill Positive. Красные Primitives/Red/Light у индикаторов снижения заменены на color/text-icon/negative. Розовый Path 5 Copy в OSD также переведён на negative: проверено, что это скрытый направленный вниз треугольник, а не видимая зелёная стрелка увеличения.

## Что осталось в обрабатываемых мастерах

**34 ссылки на старые paint-стили**: 33 фирменных цвета соцсетей и 1 сплошной Sber.

| Источник | Применений | Причина |
|---|---:|---|
| Brand/Social/VK | 10 | В текущих color/gradient токенах Head Library нет соответствующего фирменного VK. |
| Social / VK New / Primary | 3 | Актуальный токен цвета VK Connect не найден. |
| Brand/Social/Facebook | 10 | Актуальный фирменный color-токен не найден. |
| Brand/Social/Odnoklassniki | 5 | Актуальный фирменный color-токен не найден. |
| Brand/Social/Twitter | 5 | Актуальный фирменный color-токен не найден. |
| Brand/Partners/Sber | 1 | По договорённости сплошной Sber пока не менять. |

Проверены живые списки цветовых переменных и paint-стилей Head Library с префиксами color/gradient. Подходящих фирменных токенов соцсетей не найдено. Подмена фирменного синего общим accent/информационным цветом изменила бы смысл и цвет бренда, поэтому не выполнялась. Новые токены не создавались.

### [Deprecated]/Brand/Social/VK

- [Дополнительные → Ячейка / Социальные сети / ВК → I1087:10;16654:5052](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I1087-10%3B16654%3A5052)
- [Дополнительные → Социальные сети / Desktop / Раскрыты → I1088:8144;1087:10;16654:5052](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I1088-8144%3B1087%3A10%3B16654%3A5052)
- [Дополнительные → Социальные сети / Mobile / Раскрыты → I1091:116;1087:10;16654:5052](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I1091-116%3B1087%3A10%3B16654%3A5052)
- [Дополнительные → Социальные сети / Mobile / Скрыты → I1091:144;1087:10;16654:5052](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I1091-144%3B1087%3A10%3B16654%3A5052)
- [Дополнительные → Социальные сети /  Desktop / Скрыты → I1088:8178;1087:10;16654:5052](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I1088-8178%3B1087%3A10%3B16654%3A5052)
- [Поделиться → Разрешение=1720+ → 6811:43501](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6811-43501)
- [Поделиться → Разрешение=1440 → 11125:107615](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=11125-107615)
- [Поделиться → Разрешение=768 → 11125:107630](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=11125-107630)
- [Поделиться → Разрешение=375 → 6811:43511](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6811-43511)
- [Поделиться → Разрешение=320 → 11125:107646](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=11125-107646)

### Social / VK New / Primary

- [Дополнительные → Ячейка / Социальные сети / VK Connect → I8104:55425;6561:3495](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I8104-55425%3B6561%3A3495)
- [Дополнительные → Ячейка / Социальные сети / VK Connect мобильная → I8332:6;8104:55425;6561:3495](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I8332-6%3B8104%3A55425%3B6561%3A3495)
- [Дополнительные → Ячейка / Социальные сети / VK Connect мобильная специальная → I8333:6;8104:55425;6561:3495](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I8333-6%3B8104%3A55425%3B6561%3A3495)

### [Deprecated]/Brand/Social/Facebook

- [Дополнительные → Ячейка / Социальные сети / Facebook → I1088:8110;2615:1922](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I1088-8110%3B2615%3A1922)
- [Дополнительные → Социальные сети / Desktop / Раскрыты → I1087:47;1088:8110;2615:1922](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I1087-47%3B1088%3A8110%3B2615%3A1922)
- [Дополнительные → Социальные сети / Mobile / Раскрыты → I1091:111;1088:8110;2615:1922](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I1091-111%3B1088%3A8110%3B2615%3A1922)
- [Дополнительные → Социальные сети / Mobile / Скрыты → I1091:139;1088:8110;2615:1922](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I1091-139%3B1088%3A8110%3B2615%3A1922)
- [Дополнительные → Социальные сети /  Desktop / Скрыты → I1088:8173;1088:8110;2615:1922](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I1088-8173%3B1088%3A8110%3B2615%3A1922)
- [Поделиться → Разрешение=1720+ → 6811:43492](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6811-43492)
- [Поделиться → Разрешение=1440 → 11125:107618](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=11125-107618)
- [Поделиться → Разрешение=768 → 11125:107633](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=11125-107633)
- [Поделиться → Разрешение=375 → 6811:43508](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6811-43508)
- [Поделиться → Разрешение=320 → 11125:107649](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=11125-107649)

### [Deprecated]/Brand/Partners/Sber

- [Дополнительные → Ячейка / Социальные сети / Сбер ID / зелёная → 7680:48592](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=7680-48592)

### [Deprecated]/Brand/Social/Odnoklassniki

- [Поделиться → Разрешение=1720+ → 6811:43495](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6811-43495)
- [Поделиться → Разрешение=1440 → 11125:107621](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=11125-107621)
- [Поделиться → Разрешение=768 → 11125:107636](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=11125-107636)
- [Поделиться → Разрешение=375 → 6811:43514](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6811-43514)
- [Поделиться → Разрешение=320 → 11125:107652](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=11125-107652)

### [Deprecated]/Brand/Social/Twitter

- [Поделиться → Разрешение=1720+ → 6811:43498](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6811-43498)
- [Поделиться → Разрешение=1440 → 11125:107624](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=11125-107624)
- [Поделиться → Разрешение=768 → 11125:107639](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=11125-107639)
- [Поделиться → Разрешение=375 → 6811:43517](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=6811-43517)
- [Поделиться → Разрешение=320 → 11125:107655](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=11125-107655)

Отдельно сохранены **4 привязки brand/partners/sber** в доступных темах и 12 таких привязок в Light. Эти ссылки на переменные не прибавлены к числу paint-стилей. Два зелёных вектора логотипа на цветном фоне не перекрашивались в static white/black: они относятся к сохранённому фирменному Sber.

Других старых paint-стилей и устаревших цветовых переменных в доступных мастерах не осталось.

## Light и внешние примеры

По всей странице осталось **75 применений старых paint-стилей в Light-контекстах** — это совместный счётчик мастеров и внешних примеров.

Ещё **90 применений находятся вне мастеров в остальных контекстах**: оформление, демонстрации focus/hover/disabled и прототипы. Внешние примеры напрямую не редактировались.

В Light распознавались свойства Theme=Light, Светлый фон=True и названия «На светлом»/«… / светлая», в том числе вложенные Sber-ячейки. Light/Kids исключены из обычной миграции. Ранее явно согласованное исключение для старых on Light Primary → color/text-icon/inverse/primary применено адресно; остальные светлые цвета оставлены. Цвет on Light Accent у светлых ссылок не менялся.

Сырые цвета без токена оставлены. Новые дизайн-переменные, aliases, коллекции и стили не создавались. Геометрия, тексты, свойства, состояния и прочие переопределения не менялись. Head Library проверялась только на чтение.

## Проверка

Программный полный обход: fills/strokes, регионы векторов, градиентные остановки, текстовые диапазоны, эффекты и скрытые вложения. Ошибок записи и итогового аудита, неразрешённых ссылок нет. OSD осмотрен для определения роли цветного индикатора. Панель Selection colors вручную не проверялась.

Selection colors всей страницы продолжит показывать перечисленные фирменные стили, исключённые Light-элементы и внешнее оформление.

