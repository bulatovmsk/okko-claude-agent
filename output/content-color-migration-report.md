# Контент — миграция цветов

[Figma: страница Контент](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9821-75487)

## Результат

- Проверены все **986 мастеров**, **82 921 слой** в мастерах и вложениях. Отдельно проверены **11 538 узлов** вне мастеров; всего **94 459**.
- Изменены **4054 уникальных слоя**. Это прямые изменения; автоматически обновившиеся через наследование инстансы не увеличивают число.
- В **62 текстовых слоях** заменены **120 диапазонов** со смешанными цветами.
- В **192 слоях** применены статические белые/чёрные токены поверх цветных фонов; видимая прозрачность сохранена.
- У иконок «Лайв» в программе канала подтверждена роль прямого эфира: использован существующий **color.fill.solid.live**. Прямо изменены **63 слоя**, остальные наследуют обновление.
- Итоговые аудиты заливок, обводок, текстовых диапазонов, градиентных стопов, эффектов и регионов векторов завершились без ошибок чтения. Проверка программная; ручная проверка Selection colors в интерфейсе не выполнялась.

## Что осталось в рабочей области

**1204 применения старых PAINT-стилей**, перечисленных ниже. Это число ссылок на стиль в свойствах/текстовых диапазонах/регионах, а не уникальных цветов или слоёв. Дополнительно остались **12 привязок brand/partners/sber**, которые ранее решено пока не менять.

Числа в таблице охватывают все применения соответствующего ключа в рабочей области. Ссылка ведёт на пример мастера; исходный слой и свойство указаны рядом. Примеры и данные аудита по восьми частям страницы сохранены в соседнем JSON. Общую замену спорных Primitives без выбора роли не выполнял.

| Старый стиль | Применений | Где | Причина / существующие кандидаты |
|---|---:|---|---|
| Purple / Primary | 4 | Новинка. [Мастер 200:4433](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=200-4433) → Web / 24 / Новинка (fills) | color.fill.solid.accent или color.component.label.continuum; сплошной цвет и градиент дают разный результат. |
| Primitives/White/64 | 208 | Тексты и иконки, метаданные, баннеры. [Мастер 200:4433](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=200-4433) → Текст (fills) | color.text-icon.secondary для обычного текста либо color.static.solid.white с сохранением альфы для контекста поверх изображения. Одной замены для всех применений нет. |
| Primitives/Grey/Primary | 253 | Подписи и второстепенные строки. [Мастер 200:4433](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=200-4433) → Хан Соло: (fills) | color.text-icon.secondary либо color.text-icon.third: требуется выбрать иерархию и контраст. |
| Primitives/Grey/50 | 2 | Обводка второстепенной кнопки. [Мастер 200:4433](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=200-4433) → Второстепенная / Текст / Нормальная (strokes) | color.border.glassy либо color.border.solid; различаются прозрачность и поведение темы. |
| НЕ используем/Clickable/Button 30 | 10 | Фоны второстепенных кнопок. [Мастер 3674:29105](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=3674-29105) → Иконка / Второстепенная на тёмном (fills) | color.fill.glassy.primary/secondary: нужно согласовать уровень прозрачности. |
| Primitives/Blueberry/Dark blueberry 100 | 247 | Фоны, задние карточки, Фичерд. [Мастер 3674:29280](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=3674-29280) → Задняя (fills) | color.background.solid.primary либо color.fill.solid.secondary в зависимости от уровня поверхности. Нельзя закрепить одно соответствие по оттенку. |
| Primitives/Violet/Primary | 7 | Основные кнопки. [Мастер 3674:29105](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=3674-29105) → Текст / Основная (fills) | color.fill.solid.accent либо существующий градиент color.component.button. |
| Sticker Content / DTO | 2 | Стикер DTO на цветном фоне. [Мастер 3674:29105](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=3674-29105) → Web / 26 / На цветном (fills) | Нужно выбрать семантику метки: существующие color.component.label.* либо color.fill.solid.accent. Прямого DTO-токена в изученном актуальном наборе нет. |
| Primitives/Black/50 | 141 | bg внутри каверов. [Мастер 1335:14449](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=1335-14449) → bg (fills) | color.background.glassy.primary/secondary либо color.static.solid.black с альфой 50%; требуется решить, должен ли слой зависеть от темы. |
| Primitives/Blueberry/Primary | 2 | Иконка рубля внутри стикера. [Мастер 250:1128](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=250-1128) → Vector (region0) | color.text-icon.inverse.primary либо статический тёмный цвет с сохранением контраста. Цвет находится в регионе вложенного вектора; единая перекраска затронет остальные регионы. |
| Primitives/Black/Primary | 46 | Затемнение холодного старта и маски аватаров. [Мастер 13806:163398](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=13806-163398) → Затемнение (fills) | color.static.solid.black либо color.background.solid.primary; проверить назначение затемнения. Часть применений — регионы векторов. |
| НЕ используем/Elevation/01 | 7 | Подложки блоков подписки. [Мастер 1624:14202](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=1624-14202) → Подложка (fills) | color.background.solid.secondary либо color.fill.solid.secondary: требуется определить уровень поверхности. |
| Fill/Solid/AccentB | 10 | Базовые кнопки. [Мастер 1624:14202](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=1624-14202) → .Базовая кнопка (fills) | color.fill.solid.accent либо color.component.button. Прежнее исключение для фиолетового loader не распространяется на эти кнопки. |
| НЕ используем/Elevation/03 | 2 | Тумблер СберПрайм. [Мастер 2314:13670](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=2314-13670) → х / СберПрайм / Desktop / Тумблер (fills) | color.background.solid.secondary либо color.fill.solid.secondary; отдельного соответствия Elevation/03 не согласовано. |
| НЕ используем/Elevation/05 | 2 | Аддон СберПрайм. [Мастер 7510:48662](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=7510-48662) → х / СберПрайм / Desktop / Аддон (fills) | color.background.solid.secondary либо color.fill.solid.secondary; отдельного соответствия Elevation/05 не согласовано. |
| Pink / Light | 2 | Rectangle 222, Матч дня. [Мастер 2511:1880](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=2511-1880) → Rectangle 222 (fills) | У прямоугольника не подтверждена роль ошибки/статуса. Нужен выбор семантической группы; исключение для стрелки вниз здесь неприменимо. |
| Fade Gradient / Linear 0% to BG | 37 | Затемнение фона Фичерд/Спорт. [Мастер 10257:81333](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=10257-81333) → Затемнение (fills) | Один из существующих color.fill.fade.*; нужно выбрать направление и интенсивность. Старое название не определяет точную замену. |
| Primitives/White/20 / White / 20 | 42 | Разделители, обводки, детали контента. [Мастер 10903:111017](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=10903-111017) → Rectangle 1283 (fills) | Для обводок color.border.glassy, для заливок color.fill.glassy.*; нужен выбор по роли и прозрачности. |
| Color/fill/solid/hover-focus/Third | 52 | Регионы Bet Logo. [Мастер 11743:113466](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=11743-113466) → Vector (region0) | Старый градиент радиальный, актуальный color.fill.solid.hover-focus.third — линейный. Требуется согласовать изменение градиента и обновить исходный вектор, сохранив остальные регионы. |
| Fill/Solid/Primary | 45 | Регионы Bet Logo. [Мастер 11743:113466](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=11743-113466) → Vector (region1) | Целевой color.fill.solid.inverse известен по ключу Head Library, несмотря на локальное имя Primary. Остатки находятся в смешанных векторах инстансов: менять весь fills нельзя, запись vectorNetwork в инстанс недоступна. Нужна синхронизация исходного логотипа. |
| [Deprecated]/Brand/Social/Odnoklassniki | 20 | Служебные Safe Zone баннеров. [Мастер 12286:118037](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=12286-118037) → Safe Zone (fills) | Применение брендового цвета в служебной разметке. Подходящий технический color-токен для этой роли не найден. Не заменять на произвольный UI-токен. |
| Primitives/Green/Light/48 | 34 | Служебные Safe Zone баннеров. [Мастер 12286:118037](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=12286-118037) → Safe Zone (fills) | Нужен существующий технический токен для направляющих; это не подтверждённый позитивный статус. Подходящий не найден. |
| Primitives/Red/48 | 20 | Служебные Safe Zone баннеров. [Мастер 12286:118037](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=12286-118037) → Safe Zone (fills) | Нужен существующий технический токен для направляющих; это не подтверждённая ошибка. Подходящий не найден. |
| Primitives/White/15 | 8 | Rectangle 1360 в списках каналов. [Мастер 14148:167331](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=14148-167331) → Rectangle 1360 (fills) | color.fill.glassy.* либо color.border.glassy: требуется уточнить роль разделителя и прозрачность. |
| Primitives/Violet/15 | 1 | Фон прошедшей программы 375. [Мастер 14148:169874](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=14148-169874) → Ячейка Программы / Базовая / 375 (fills) | color.fill.glassy.* либо color.fill.solid.hover-focus.*: требуется уточнить смысл состояния. |

Sber: [х / СберПрайм / Desktop / Тумблер](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=2314-13670) и вложенные логотипы; существующая договорённость — оставить solid Sber. Градиент Sber не относится к этому исключению.

## Исключённые области

- В мастерах осталось **1301 применение старых стилей в Light** и **11 в детских вариантах**.
- Вне мастеров осталось **791 применение старых стилей**: 28 в Light и 763 в остальных примерах, контейнерах и служебных элементах. Они не входят в 1204 выше и не редактировались напрямую.
- Остались старые библиотечные переменные внутри Light: Lighthouse и primitives/electric*. Они учтены отдельно от PAINT-стилей в JSON, без удвоения счётчика 1204.
- Ранее согласованные исключения применялись: on Light Primary/Secondary/Third/Forth → inverse и детский декоративный градиент → progress-bar. Поэтому утверждение «Light и детские компоненты вообще не затронуты» было бы неточным.
- При проверке обнаружено нестандартное свойство **Детский=True**. Пяти фоновым полосам прогресса 8446:20010, 8446:20013, 8446:20016, 8446:20019, 8446:20022 возвращена старая привязка **[Deprecated]/Text & icon/on Dark/Forth**; в итоговые 4054 изменения эти пять слоёв не включены. В восьми детских полосах сохранена только заранее согласованная замена градиента progress-bar.

Новые токены, переменные, коллекции и дубликаты не создавались. Цвета без привязки к стилю/переменной сохранены. Геометрия, текст, свойства вариантов и структура компонентов не изменялись. Существующие цветовые переопределения во вложениях обновлялись адресно; инстансы не отсоединялись и не сбрасывались.

