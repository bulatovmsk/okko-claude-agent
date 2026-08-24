# Иконки — Main Pack (Okko Head Library)
> Источник: file **Okko Head Library** (`HYB1u9ysALVWtVWKoagiDH`), секция **Main pack** — node `29361:322`. Только Main Pack (другие паки в базу не вносятся).

**493 компонентов-иконок** в **16 категориях**. Все — фреймы **24×24px** (единый размер кадра; оптический размер глифа внутри меньше).

## Конвенция именования

`Категория / Имя_Модификатор` — напр. `Menu / Bookmark_Solid_Bold`, `Actions / Cross`.

| Модификатор | Значение |
|---|---|
| *(без суффикса)* | базовый контурный (Regular, тонкая обводка) |
| `_Bold` | контурный с утолщённой обводкой |
| `_Solid` | залитый (filled) |
| `_Solid_Bold` | залитый + утолщённый |
| `_Light` | облегчённый (тоньше базового) |
| `_Indicator` | вариант с бейджем-индикатором (точка уведомления, отдельный VECTOR с цветовой переменной) |
| `_Color` | многоцветная иконка (фикс. цвета, напр. логотипы, карточки футбола) |

**Стиль = вес обводки/заливка.** Один глиф обычно есть в нескольких вариантах (например `Magnifier`, `Magnifier_Bold`, `Magnifier_Solid`, `Magnifier_Solid_Bold`). Контурные используются в покое, `_Solid`/`_Bold` — в активном/выбранном состоянии.

## Анатомия

- Кадр **24×24px**. Глиф — `BOOLEAN_OPERATION` (Union/Subtract) или `VECTOR` внутри.
- Цвет глифа задаётся при применении (наследуется от контекста), монохром.
- У `_Indicator` — отдельный слой бейджа (`Badge`, ~6–7px), привязан к цветовой переменной (акцент/негатив).
- `_Color`/логотипы — фиксированные цвета, перекрашивать нельзя.

## Правила построения

Источник правил — фрейм **«Создание иконки»** в Okko Head Library, node `5859:1`.

### Размер и масштабирование

- Исходный компонент иконки создаётся в кадре **24×24px**.
- В макете иконку можно только **пропорционально** увеличивать или уменьшать.
- Предпочтительные размеры применения кратны 4: **8, 12, 16, 20, 24, 28, 32px** и т.д.
- Размеров, кратных 5, по возможности избегать: **15, 25, 35px** и т.д.
- Исторические иконки, которые не соответствуют правилам, не использовать как образец для новых. Их отклонения фиксируются при аудите отдельно и исправляются без изменения смысла знака.

### Keyline-сетка 24×24

Нельзя растягивать глиф до всех границ кадра 24×24. Для одинакового оптического веса и совместимости иконок используется сетка, близкая к Material Design. Перед построением её копируют и приводят к размеру 24×24px.

Основные направляющие сетки:

| Элемент сетки | Размер в кадре 24×24 | Отступ от края |
|---|---:|---:|
| Вертикальные и горизонтальные оси | `8 / 12 / 16px` | — |
| Круглая keyline | `20×20px` | `2px` |
| Квадратная keyline | `18×18px` | `3px` |
| Горизонтальная keyline | `20×16px` | `2px` по горизонтали, `4px` по вертикали |
| Вертикальная keyline | `16×20px` | `4px` по горизонтали, `2px` по вертикали |
| Центральная круглая keyline | `10×10px` | `7px` |

Keyline задаёт ориентир, а не требование механически коснуться каждого края. Выбирай контур, соответствующий силуэту знака, и проверяй итоговый оптический вес рядом с другими иконками того же размера и модификатора.

### Оптическое выравнивание

- Визуальный центр важнее геометрического центра bounding box.
- Для асимметричных форм допустима оптическая компенсация. Например, треугольник `Play` внутри круга или кнопки не должен иметь математически одинаковые отступы слева и справа, если визуально он выглядит смещённым.
- Проверяй выравнивание не только изолированно, но и в строке с соседними иконками и внутри целевого компонента.

### Критерии аудита иконки

Иконка проходит аудит, если выполнены все применимые пункты:

- [ ] Корневой кадр компонента — ровно **24×24px**, глиф не обрезан.
- [ ] Геометрия построена с опорой на keyline-сетку; глиф не растянут до границ кадра без оптической причины.
- [ ] Масштабирование пропорциональное, без деформации по одной оси.
- [ ] Оптический вес сопоставим с соседними иконками того же размера и модификатора.
- [ ] Асимметричные формы выровнены визуально, а не только математически.
- [ ] Варианты одного глифа сохраняют силуэт, пропорции и воспринимаемый размер.
- [ ] Base, `_Bold`, `_Solid`, `_Solid_Bold` и `_Light` соответствуют заявленному типу обводки или заливки.
- [ ] У `_Indicator` бейдж является отдельным слоем и использует цветовую переменную.
- [ ] `_Color` и логотипы сохраняют утверждённые цвета; остальные варианты остаются монохромными и получают цвет из контекста.
- [ ] Имя соответствует схеме `Категория / Имя_Модификатор`, не содержит пробелов в начале или конце и совпадает с именем ассета в синхронизированных репозиториях.
- [ ] После публикации компонент имеет уникальный стабильный Figma key; переименование и замена key согласованы с владельцами платформенных репозиториев.

### Do / Don't

- **Do:** начинай с кадра 24×24 и подходящей keyline; **Don't:** рисуй глиф произвольного размера и затем растягивай его до краёв.
- **Do:** сравнивай иконку с соседними знаками того же веса; **Don't:** оценивай размер и толщину только изолированно.
- **Do:** центрируй `Play` и другие асимметричные формы оптически; **Don't:** полагайся только на равные числовые отступы.
- **Do:** сохраняй полное имя и стабильный key при синхронизации; **Don't:** переименовывай опубликованную иконку без проверки платформенных репозиториев.

### Референсы из Figma

- [Material Design icons](https://material.io/design/iconography/system-icons.html) — принцип keyline-сетки.
- [Оптическое выравнивание элементов](https://habr.com/ru/company/badoo/blog/333992/) — визуальный центр и компенсации.
- [Подробный гайд по иконкам](https://paper.dropbox.com/doc/--BIfU2ydV1NCg36KSUVERl1VEAQ-nWX04fSSIK5pPjxqSbPYJ) — дополнительный материал, указанный в библиотеке.

## Применение

- Базовый размер кадра 24×24; масштабировать пропорционально.
- В компонентах (Chips, Button и т.д.) иконка вставляется через слот `Icon Instance` (swap).
- Не использовать `_Color`/логотипы как обычные монохромные иконки.
- Логотипы партнёров/соцсетей — только в санкционированных контекстах (авторизация, партнёрские блоки).

## Категории

| Категория | Кол-во | Назначение |
|---|---|---|
| Menu | 69 | таб-бар и разделы приложения |
| Navigation | 14 | списки, сетки, выход |
| Categories | 44 | жанры и категории контента |
| Arrows | 30 | стрелки и направления |
| Mark | 15 | оценки (звёзды, лайки) |
| Labels | 12 | метки (рубль, подарок, замок) |
| Notification | 11 | колокольчик, галочки прочтения |
| Objects | 54 | предметы и сущности (карты, документы, фильтры) |
| Actions | 54 | действия (добавить, удалить, поделиться) |
| Devices | 16 | устройства (TV, телефон, пульт) |
| Player | 89 | управление плеером |
| Logotypes | 32 | логотипы Окко, партнёров, соцсетей |
| Sports | 36 | виды спорта |
| Football | 11 | события матча (голы, карточки) |
| Settings | 4 | настройки |
| Helpdesk | 2 | поддержка (вложение, отправка) |

## Полный список (по категориям)

<details><summary>Развернуть все иконки</summary>

**Menu** (69): `Avatar`, `Avatar_Bold`, `Avatar_Solid`, `Avatar_Solid_Bold`, `Bag`, `Bag_Bold`, `Bag_Solid`, `Bag_Solid_Bold`, `Ball`, `Ball_Bold`, `Ball_Solid`, `Ball_Solid_Bold`, `Bear`, `Bear_Bold`, `Bear_Solid`, `Bear_Solid_Bold`, `Bookmark`, `Bookmark_Bold`, `Bookmark_Bold_Indicator`, `Bookmark_Indicator`, `Bookmark_Solid`, `Bookmark_Solid_Bold`, `Bookmark_Solid_Bold_Indicator`, `Bookmark_Solid_Indicator`, `Game`, `Game_Bold`, `Game_Solid`, `Game_Solid_Bold`, `Gear`, `Gear_Bold`, `Gear_Solid`, `Gear_Solid_Bold`, `House`, `House_Bold`, `House_Solid`, `House_Solid_Bold`, `Magnifier`, `Magnifier_Bold`, `Magnifier_Solid`, `Magnifier_Solid_Bold`, `Megaphone`, `Megaphone_Bold`, `Megaphone_Solid`, `Megaphone_Solid_Bold`, `Moments`, `Moments_Bold`, `Moments_Solid`, `Play_Catalog`, `Play_Catalog_Bold`, `Play_Catalog_Solid`, `Play_Catalog_Solid_Bold`, `Stack`, `Stack_Bold`, `Stack_Solid`, `Stack_Solid_Bold`, `Subscription`, `Subscription_Bold`, `Subscription_Solid`, `Subscription_Solid_Bold`, `TV_Old`, `TV_Old_Bold`, `TV_Old_Solid`, `TV_Old_Solid_Bold`, `Timer`, `Timer_Bold`, `Timer_Indicator`, `Timer_Indicator_Bold`, `Timer_Solid`, `Timer_Solid_Bold`

**Navigation** (14): `Circle_Grid`, `Dots_Horizontal`, `Dots_Vertical`, `Exit`, `Exit_Bold`, `Exit_Optic_Balance`, `Exit_Optic_Balance_Bold`, `Horizontal_Lines`, `Horizontal_Lines_Bold`, `List_Bulleted`, `List_Bulleted_Bold`, `Playlist`, `Playlist_Bold`, `Square_Grid`

**Categories** (44): `Binoculars`, `Binoculars_Bold`, `Christmas_Tree`, `Christmas_Tree_Bold`, `Clapperboard`, `Clapperboard_Bold`, `Cube`, `Cube_Bold`, `Curtains`, `Curtains_Bold`, `Cutlery`, `Cutlery_Bold`, `Disco_Ball`, `Disco_Ball_Bold`, `Flag`, `Flag_Bold`, `Hat_Academic`, `Hat_Academic_Bold`, `Karaoke`, `Karaoke_Bold`, `Newspaper`, `Newspaper_Bold`, `Note_Musicial`, `Note_Musicial_Bold`, `Particles`, `Particles_Bold`, `Pencil_Writing`, `Pencil_Writing_Bold`, `People`, `People_Bold`, `Picture`, `Picture_Bold`, `Play_Circled`, `Play_Circled_Bold`, `Pulse`, `Pulse_Bold`, `Rotation`, `Rotation_Bold`, `Smile`, `Smile_Bold`, `Suitcase`, `Suitcase_Bold`, `Trees`, `Trees_Bold`

**Arrows** (30): `Arrow_Curved`, `Arrow_Curved_Bold`, `Arrow_Down`, `Arrow_Down_Bold`, `Arrow_Down_Small`, `Arrow_Down_Small_Bold`, `Arrow_Down_Tail`, `Arrow_Down_Tail_Bold`, `Arrow_Left`, `Arrow_Left_Bold`, `Arrow_Left_Small`, `Arrow_Left_Small_Bold`, `Arrow_Left_Solid`, `Arrow_Left_Tail`, `Arrow_Left_Tail_Bold`, `Arrow_Right`, `Arrow_Right_Bold`, `Arrow_Right_Small`, `Arrow_Right_Small_Bold`, `Arrow_Right_Solid`, `Arrow_Right_Tail`, `Arrow_Right_Tail_Bold`, `Arrow_Up`, `Arrow_Up_Bold`, `Arrow_Up_Small`, `Arrow_Up_Small_Bold`, `Arrow_Up_Tail`, `Arrow_Up_Tail_Bold`, `Download_Prohibited`, `Download_Prohibited_Bold`

**Mark** (15): `Playing_Status`, `Playing_Status_Bold`, `Star`, `Star_Bold`, `Star_Solid`, `Thumbs_Down_Rounded`, `Thumbs_Down_Rounded_Bold`, `Thumbs_Down_Rounded_Solid_Bold`, `Thumbs_Down_Solid`, `Thumbs_Down_Tilted_Solid`, `Thumbs_Up_Rounded`, `Thumbs_Up_Rounded_Bold`, `Thumbs_Up_Rounded_Solid_Bold`, `Thumbs_Up_Solid`, `Thumbs_Up_Tilted_Solid`

**Labels** (12): `Broadcast`, `Broadcast_Bold`, `Gift`, `Gift_Bold`, `Gift_Solid`, `Gift_Solid_Bold`, `Lock`, `Lock_Bold`, `Lock_Solid_Bold`, `Ruble`, `Ruble_Bold`, `Thumbs_Up_Color`

**Notification** (11): `Bell`, `Bell_Bold`, `Bell_Tilted_Solid`, `Bell_Tilted_Solid_Bold`, `Check_Mark_Double`, `Check_Mark_Double_Bold`, `Check_Mark_Single`, `Check_Mark_Single_Bold`, `Check_Mark_Small`, `Check_Mark_Small_Bold`, `Check_Mark_Solid_Bold`

**Objects** (54): `AI Kinobi`, `Bank`, `Bank_Bold`, `Call`, `Call_Bold`, `Card_Back`, `Card_Back_Bold`, `Card_Back_CVV`, `Card_Back_CVV_Bold`, `Card_Back_CVV_Light`, `Card_Back_Light`, `Card_Back_Solid`, `Card_Back_Solid_Bold`, `Card_Face`, `Card_Face_Bold`, `Card_Face_Light`, `Chat`, `Chat_Solid_Bold`, `Clock`, `Clock_Bold`, `Document`, `Document_Bold`, `Document_Solid`, `Document_Solid_Bold`, `Documents`, `Email`, `Email_Bold`, `Equalizer_Not_Played`, `Equalizer_Not_Played_Bold`, `Equalizer_Played`, `Equalizer_Played_Bold`, `Filters`, `Filters_Bold`, `Filters_Indicator`, `Filters_Indicator_Bold`, `Focus`, `Focus_Bold`, `Geo`, `Globe`, `Globe_Bold`, `Magic_Solid`, `Moon_Solid`, `Picker`, `Privacy`, `Qr_Code`, `Qr_Code_Bold`, `Shield_Solid`, `Shield_Solid_Bold`, `Stack`, `Ticket_Solid`, `Top`, `Top_Bold`, `Wallet`, `Wallet_Bold`

**Actions** (54): `Bubokko`, `Calendar`, `Calendar_Add`, `Calendar_Bold`, `Circle_Crossed`, `Circle_Crossed_Bold`, `Clear`, `Clear_Bold`, `Copy`, `Copy_Bold`, `Cross`, `Cross_Bold`, `Cross_Small`, `Cross_Small_Bold`, `Cross_Solid`, `Download`, `Eye`, `Eye_Bold`, `Eye_Crossed`, `Eye_Crossed_Bold`, `Info_Symbol`, `Info_Symbol_Bold`, `KeyboardAbove_Solid`, `KeyboardAbove_Solid_Bold`, `Keyboard_Bold`, `Keyboard_Solid_Bold`, `Medal`, `Medal_Bold`, `Minus`, `Minus_Bold`, `Move`, `Move_Bold`, `Pencil`, `Pencil_Bold`, `Pencil_NEW`, `Play`, `Play_Bold`, `Plus`, `Plus_Bold`, `Plus_Circled`, `Plus_Circled_Bold`, `Plus_Circled_Light`, `Plus_Small`, `Plus_Small_Bold`, `Prime`, `Share`, `Share_Bold`, `Trash`, `Trash_Bold`, `Trash_Detailed`, `Trash_Detailed_Bold`, `Upper_Case_Bold`, `Upper_Case_Long_Solid`, `Upper_Case_On_One_Solid`

**Devices** (16): `Computer`, `Computer_Bold`, `Connected_Devices`, `Connected_Devices_Bold`, `Phone`, `Phone_Bold`, `Remote`, `Remote_Bold`, `Remote_Rotated`, `Remote_Rotated_Bold`, `TV`, `TV_Bold`, `TV_Box`, `TV_Box_Bold`, `Tablet`, `Tablet_Bold`

**Player** (89): `18+`, `18+_Bold`, `Air_Play`, `Air_Play_Bold`, `Arrow_Reload`, `Arrow_Reload_Bold`, `Arrow_Return`, `Arrow_Return_Bold`, `Attention`, `Attention_Bold`, `Attention_Solid_Bold`, `Audio_Subtitles`, `Bad_Signal`, `Bad_Signal_Bold`, `Brightness`, `Brightness_Bold`, `Camera`, `Camera_Bold`, `Camera_Old`, `Camera_Old_Bold`, `Cards`, `Cards_Bold`, `Cards_Inversed_Solid`, `Cards_Inversed_Solid_Bold`, `Cards_Solid`, `Cards_Solid_Bold`, `Chromecast`, `Chromecast_Solid`, `Dialog`, `Dialog_Bold`, `Episode_Next_Solid`, `Episode_Previous_Solid`, `Explicit`, `Explicit_Bold`, `Explicit_Indicator_Solid`, `Explicit_Solid`, `Fifteen_Back`, `Fifteen_Back_Bold`, `Fifteen_Forward`, `Fifteen_Forward_Bold`, `Fullscreen`, `Fullscreen_Bold`, `Fullscreen_Inversed`, `Fullscreen_Inversed_Bold`, `Heart`, `Heart_Bold`, `Heart_Solid`, `Inoagent`, `Inoagent_Bold`, `Link_External`, `Link_External_Bold`, `Microphone`, `Microphone_Bold`, `Mood_Tuner`, `Mood_Tuner_Selected`, `Pause_Solid`, `Play_Partial`, `Play_Partial_Bold`, `Play_Solid`, `Repeat`, `RepeatTrack_Indicator`, `Repeat_Bold`, `Repeat_Indicator`, `Repeat_Indicator_Bold`, `Repeat_Track_Indicator_Bold`, `Rewind_Back_Solid`, `Rewind_Forward_Solid`, `Rotate_Device`, `Rotate_Device_Bold`, `Screen`, `Screen_Bold`, `Screen_Constriction`, `Screen_Constriction_Bold`, `Screen_Stretch`, `Screen_Stretch_Bold`, `Shuffle`, `Shuffle_Bold`, `Shuffle_Indicator`, `Shuffle_Indicator_Bold`, `Speaker`, `Speaker_Bold`, `Speaker_Crossed`, `Speaker_Crossed_Bold`, `Ten_Back`, `Ten_Back_Bold`, `Ten_Forward`, `Ten_Forward_Bold`, `Text`, `Text_Bold`

**Logotypes** (32): `Android`, `Apl`, `Apl_Solid`, `Apple`, `Bundesliga`, `Facebook`, `Google_Color`, `Instagram`, `Live`, `MAX`, `Mls`, `Odnoklassniki`, `Okko`, `Okko_Afisha`, `Pushkin_Card`, `Pushkin_Card_Solid`, `RUTUBE`, `Reward`, `Rpl_Color`, `Saf`, `Salut`, `Sber_Spasibo`, `Sberbank`, `Telegram`, `Twitter`, `Vk1`, `Vk2`, `Whatsapp`, `Yandex`, `Youtube`, `Zvuk`, `Zvuk_Solid`

**Sports** (36): `3x3 `, `3x3_Bold `, `Athletics`, `Athletics_Bold`, `Basketball`, `Basketball_Bold`, `Basketball_Solid`, `Biathlon`, `Biathlon_Bold`, `Boat-racing`, `Boat-racing_Bold`, `Cyber`, `Cyber_Bold`, `Cycling`, `Cycling_Bold`, `Football`, `Football_Bold`, `Football_Solid`, `Hockey`, `Hockey_Bold`, `Iceskating`, `Iceskating_Bold`, `Mma`, `Mma_Bold`, `Phygital`, `Phygital_Bold`, `Rugby`, `Rugby_Bold`, `Rugby_Solid`, `Short-track`, `Short-track_Bold`, `Tennis`, `Tennis_Bold`, `Tennis_Solid`, `Volleyball`, `Volleyball_Bold`

**Football** (11): `Check_Color`, `Cross_Color`, `Goal_Color`, `No_penalty_Color`, `Own_Goal_Color`, `Penalty_Color`, `Red_Card_Color`, `Sub_Color`, `Var`, `Whistle`, `Yellow_Card_Color`

**Settings** (4): `Headphones`, `History`, `Match_Score`, `Share`

**Helpdesk** (2): `Attachment`, `Send`

</details>

## Правила выбора модификатора

Какой суффикс брать в каком контексте — это редактируемый раздел, `sync` его **не перезаписывает**.

| Контекст | Модификатор | Почему |
|---|---|---|
| Таб-бар: активная вкладка | `_Solid_Bold` (или `_Bold` если нет Solid) | максимальная заметность, контраст с inactive |
| Таб-бар: неактивная вкладка | base (без суффикса), реже `_Light` | приглушённое состояние, экономия акцента |
| Иконка в Chips / Select / Button (контурная) | base или `_Bold` (в зависимости от размера компонента) | гармонирует с тонкой обводкой компонента |
| Иконка в filled-кнопке (Primary, Action) | `_Solid` | заливка под заливку, не «дырявит» кнопку |
| Иконка с уведомлением (точка-бейдж) | `_Indicator` (тот же глиф + `Badge`) | бейдж — отдельный VECTOR, цвет через переменную (акцент / негатив) |
| Иконка для выбранного состояния (Chips=Selected, Tab=active) | `_Solid_Bold` или `_Bold` (если в покое — base) | визуально отличает выбранное от обычного |
| Логотипы (Okko, партнёры, соцсети) | `_Color` или просто из категории `Logotypes/*` | фиксированные фирменные цвета, нельзя перекрашивать |
| Многоцветные смысловые (Football/Cards, Mark/Thumbs_Up_Color) | `_Color` | многоцветность — часть знака |
| Контекст с очень тонкой графикой / 16pt-иконка | `_Light` | тоньше базового, не «выпирает» в плотных макетах |

**Парные варианты:** один глиф (например `Magnifier`) есть в base/`_Bold`/`_Solid`/`_Solid_Bold`. В одном экране **придерживайся одного веса** — не смешивай base и Bold в одной строке.

**Цвет:** монохромные модификаторы (всё, кроме `_Color`) перекрашиваются цветом контекста. Применяй переменную `color.text-icon.*` (см. [`design-system/tokens/colors.md`](../tokens/colors.md#a3-semantic-токены--color-применять-в-макетах)) — `primary` для активного состояния, `secondary` для приглушённого, `accent` для акцентных action-иконок.

## Источник

- Figma `HYB1u9ysALVWtVWKoagiDH` node `29361:322` (секция Main pack).
- Правила построения: Figma `HYB1u9ysALVWtVWKoagiDH` node `5859:1` (фрейм «Создание иконки»).

## Обновление

```bash
bash scripts/figma-sync-head-library.sh icons
```

Скрипт перепишет всё, **кроме раздела «Правила выбора модификатора»** (он редактируется вручную и сохраняется при синке).
