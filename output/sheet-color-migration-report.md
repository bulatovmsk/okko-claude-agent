# Миграция цветов Sheet

20 октября 2026.

[Страница Sheet](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=28937-684).

Изменено 1180 уникальных слоёв страницы; выполнено 1200 прямых замен привязок. Дополнительно обновлены четыре исходных мастера Label - Small / Continuum на странице Label. Проверены все 5994 слоя и 130 мастеров Sheet, включая скрытые вложенные слои, стили и переменные, градиенты и векторные регионы.

## Выполнено

- 65 замен в собственных слоях мастеров.
- 1082 замены согласованных старых привязок вложенных слоёв. В том числе старые Forth и Fade/Bottom/Third из ранних наборов переведены на существующие семантически соответствующие current-токены.
- 33 старых Brand/Okko/Accent в метках переведены на color/component/label/continuum. Вариант Continuum проверен через componentProperties и main component каждого типа метки.
- Четыре исходных Label - Small / Continuum переведены со старой переменной color/component/label/continuum (59adfaa…) на актуальный существующий одноимённый стиль. Это исправило по наследованию ещё 12 таких заливок внутри Sheet. ID источников: [21066:306462](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=21066-306462), [16627:178723](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16627-178723), [16627:178726](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16627-178726), [16627:178729](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=16627-178729).
- 20 заливок белого текста на цветных фонах переведены на static/solid/white с сохранением цвета и эффективной прозрачности. Итоговая проверка: 173 подходящих заливки уже static, новых подходящих замен нет. 45 raw-заливок на цветных фонах сохранены.

## Осталось в Bet Logo

В 23 вложенных векторах Bet Logo(Full/Mini) осталось 59 старых применений цветовых стилей. API не позволяет менять vector-data внутри экземпляра; отсоединения и замены экземпляров не выполнялись.

- 23 региона Fill/Solid/Primary с key 974f85…: в источнике этот ключ соответствует старому Fill/Solid/Inverse. Замена на color/fill/solid/inverse согласована; исходные Full и Mini ранее исправлены. Для этих экземпляров требуется выпуск и применение библиотечного обновления; возможны локальные переопределения региона.
- 36 регионов Color/fill/solid/hover-focus/Third с key 7190d7…: старый радиальный градиент. Название выглядит актуальным, ключ устаревший. Текущий hover-focus/third — линейный градиент, а исходные мастера логотипа используют inverse. Выбор замены для переопределённых регионов неоднозначен; оставлено для решения. Кандидаты: color/fill/solid/hover-focus/third или color/fill/solid/inverse.

| Вектор | Путь | Старых регионов |
|---|---|---:|
| [I30919:110019;24384:3936](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I30919-110019;24384-3936) | 🛠Parts/Sheet header > Breakpoint=1792+, Type=Primary > Text box > Bet Logo(Full) > Vector | 3 |
| [I30919:110044;24384:3936](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I30919-110044;24384-3936) | 🛠Parts/Sheet header > Breakpoint=960+, Type=Primary > Text box > Bet Logo(Full) > Vector | 3 |
| [I30919:110106;24384:3936](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I30919-110106;24384-3936) | 🛠Parts/Sheet header > Breakpoint=600+, Type=Primary > Text box > Bet Logo(Full) > Vector | 3 |
| [I30919:110136;24376:3562](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I30919-110136;24376-3562) | 🛠Parts/Sheet header > Breakpoint=320+, Type=Primary > Text box > Bet Logo(Mini) > Vector | 2 |
| [I30919:110125;24376:3562](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I30919-110125;24376-3562) | 🛠Parts/Sheet header > Breakpoint=375+, Type=Primary > Text box > Bet Logo(Mini) > Vector | 2 |
| [I30533:7087;30919:110019;24384:3936](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I30533-7087;30919-110019;24384-3936) | Sheet > Breakpoint=1792+ > Header+ItemBox > 🛠Parts/Sheet header > Text box > Bet Logo(Full) > Vector | 3 |
| [I30533:7095;30919:110044;24384:3936](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I30533-7095;30919-110044;24384-3936) | Sheet > Breakpoint=1320+ > Header+ItemBox > 🛠Parts/Sheet header > Text box > Bet Logo(Full) > Vector | 3 |
| [I30541:7142;30919:110044;24384:3936](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I30541-7142;30919-110044;24384-3936) | Sheet > Breakpoint=960+ > Header+ItemBox > 🛠Parts/Sheet header > Text box > Bet Logo(Full) > Vector | 3 |
| [I30541:7119;30919:110106;24384:3936](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I30541-7119;30919-110106;24384-3936) | Sheet > Breakpoint=600+ > Header+ItemBox > 🛠Parts/Sheet header > Text box > Bet Logo(Full) > Vector | 3 |
| [I30541:7111;30919:110125;24376:3562](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I30541-7111;30919-110125;24376-3562) | Sheet > Breakpoint=375+ > Header+ItemBox > 🛠Parts/Sheet header > Text box > Bet Logo(Mini) > Vector | 2 |
| [I30541:7103;30919:110136;24376:3562](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I30541-7103;30919-110136;24376-3562) | Sheet > Breakpoint=320+ > Header+ItemBox > 🛠Parts/Sheet header > Text box > Bet Logo(Mini) > Vector | 2 |
| [I30574:455486;24384:3936](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I30574-455486;24384-3936) | 🛠Parts/SheetItem > Content=Header, Breakpoint=1720+ > Bet Logo(Full) > Vector | 3 |
| [I30574:455495;24384:3936](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I30574-455495;24384-3936) | 🛠Parts/SheetItem > Content=Header, Breakpoint=600+ > Bet Logo(Full) > Vector | 3 |
| [I30574:455498;24384:3936](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I30574-455498;24384-3936) | 🛠Parts/SheetItem > Content=Header, Breakpoint=375+ > Bet Logo(Full) > Vector | 3 |
| [I30574:455501;24384:3936](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I30574-455501;24384-3936) | 🛠Parts/SheetItem > Content=Header, Breakpoint=320+ > Bet Logo(Full) > Vector | 3 |
| [I30574:455489;24384:3936](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I30574-455489;24384-3936) | 🛠Parts/SheetItem > Content=Header, Breakpoint=1320+ > Bet Logo(Full) > Vector | 3 |
| [I30574:455492;24384:3936](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I30574-455492;24384-3936) | 🛠Parts/SheetItem > Content=Header, Breakpoint=960+ > Bet Logo(Full) > Vector | 3 |
| [I30239:11542;17117:237854;16812:199380;30438:93108;24376:3562](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I30239-11542;17117-237854;16812-199380;30438-93108;24376-3562) | 🛠Parts/SheetItem > Content=Main rail, Breakpoint=1720+ > Rail / Main > baseRail > headingRail > text & logo > Bet Logo > Vector | 2 |
| [I30550:99551;17117:237862;16812:199432;30438:93114;24376:3562](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I30550-99551;17117-237862;16812-199432;30438-93114;24376-3562) | 🛠Parts/SheetItem > Content=Main rail, Breakpoint=600+ > Rail / Main > baseRail > headingRail > text & logo > Bet Logo > Vector | 2 |
| [I30550:101025;17117:237864;16812:199444;30438:93119;24376:3562](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I30550-101025;17117-237864;16812-199444;30438-93119;24376-3562) | 🛠Parts/SheetItem > Content=Main rail, Breakpoint=375+ > Rail / Main > baseRail > headingRail > text & logo > Bet Logo > Vector | 2 |
| [I30550:102451;17117:237866;16812:199456;30438:93117;24376:3562](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I30550-102451;17117-237866;16812-199456;30438-93117;24376-3562) | 🛠Parts/SheetItem > Content=Main rail, Breakpoint=320+ > Rail / Main > baseRail > headingRail > text & logo > Bet Logo > Vector | 2 |
| [I30550:95907;17117:237858;16812:199406;30438:93116;24376:3562](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I30550-95907;17117-237858;16812-199406;30438-93116;24376-3562) | 🛠Parts/SheetItem > Content=Main rail, Breakpoint=1320+ > Rail / Main > baseRail > headingRail > text & logo > Bet Logo > Vector | 2 |
| [I30550:98183;17117:237862;16812:199432;30438:93114;24376:3562](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=I30550-98183;17117-237862;16812-199432;30438-93114;24376-3562) | 🛠Parts/SheetItem > Content=Main rail, Breakpoint=960+ > Rail / Main > baseRail > headingRail > text & logo > Bet Logo > Vector | 2 |

## Исключения

Сохранено 51 применение старых PAINT-стилей внутри Light-вложений и 3 вне мастеров: два заголовка страницы и фон component set SheetItem. В Light также остались 27 привязок primitive/electric1100 и 12 переменных Lighthouse из старой Color-коллекции. Эти счётчики не являются уникальными слоями.

Итого Selection colors всей страницы продолжит показывать 113 применений известных старых PAINT-стилей: 59 Bet Logo, 51 Light, 3 вне мастеров. В собственных слоях обрабатываемых мастеров старых токенов нет. Других неоднозначных замен, кроме регионов логотипов, не найдено.

Новые дизайн-переменные, aliases и стили не создавались. Raw-цвета, геометрия, тексты, свойства вариантов и состав компонентов сохранены. Стили эффектов Blur не входят в счётчик старых цветовых стилей. Все напрямую изменённые ID и полные остатки внутри мастеров сохранены в sheet-color-migration-audit.json.
