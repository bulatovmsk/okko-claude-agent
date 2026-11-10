/**
 * Okko Doc Builder — перенос черновиков документации Select · Web в Figma.
 *
 * ВАЖНО, что делает и чего не делает:
 *   - дополняет ТОЛЬКО выбранный фрейм `Guide · Select · Web` или `Passport · Select · Web`;
 *   - только добавляет новые секции в конец, существующие ноды не трогает;
 *   - идемпотентен: секция с таким именем уже есть — пропускается;
 *   - оформление снимает с живого файла (шрифты, размеры, цвета берёт из существующих
 *     текстов выбранного фрейма), а не подставляет выдуманные значения;
 *   - ничего не отсоединяет и не меняет исходный компонент Select.
 *
 * Контент встроен из черновиков output/select-web-docs/.
 */

const CONTENT = {
  "guide": {
    "sections": [
      {
        "title": "1. Шапка",
        "blocks": [
          {
            "type": "p",
            "text": "Select · Web"
          },
          {
            "type": "p",
            "text": "Компактный контрол-фильтр: показывает уже применённый выбор и открывает список опций. В отличие от Chips, прячет варианты за одним контролом — для длинных списков."
          },
          {
            "type": "bullets",
            "items": [
              "Размеры: Small и Default, три брейкпоинта — 320+, 600+, 1720+",
              "Состояния: Desktop и Tablet — Rest / Hover / Focus / Pressed / Disabled; Mobile — без Focus",
              "Устойчивый выбор Selected — отдельная ось, не то же самое, что Pressed",
              "Счётчик выбранного через Show Counter + Count",
              "Работает в общей группе с Chips — см. Раздел 15"
            ]
          },
          {
            "type": "p",
            "text": "Якоря-чипы: [Назначение] [Когда использовать] [Анатомия] [Настройки] [Размеры] [Состояния] [Selected] [Зоны нажатия] [Do/Don't] [Каталог] [Ссылка на паспорт]"
          },
          {
            "type": "note",
            "text": "❓ Иллюстрации в контексте для шапки не подобраны: production-скриншотов с Select Web нет."
          }
        ]
      },
      {
        "title": "2. Когда использовать",
        "blocks": [
          {
            "type": "bullets",
            "items": [
              "Длинный список опций, который не помещается на экран россыпью тегов",
              "Множественный выбор с подсчётом: «Жанры · 3», «Страны · 5»",
              "Единичный выбор из списка",
              "Экономия места: один контрол вместо набора Chips"
            ]
          },
          {
            "type": "p",
            "text": "Поведение ✅: Selected=False — вся площадь открывает список. Selected=True — основная часть открывает список, правая зона сбрасывает выбор."
          },
          {
            "type": "note",
            "text": "❓ Иллюстрации в контексте: нужны реальные экраны Окко с Select. Не подбирать синтетические без пометки «схема»."
          }
        ]
      },
      {
        "title": "3. Когда НЕ использовать",
        "blocks": [
          {
            "type": "table",
            "rows": [
              [
                "Сценарий",
                "Вместо"
              ],
              [
                "Короткий список, все варианты помещаются в строку",
                "Chips — раскрывают короткие варианты прямо в строке"
              ],
              [
                "Десктопный список, раскрывающийся без шторки",
                "Dropdown — связанный компонент, не вложенная часть Select"
              ]
            ]
          },
          {
            "type": "p",
            "text": "⚠️ Выбор между Select и Dropdown требует решения: у Dropdown брейкпоинты 1720/1320, у Select — 1720+/600+/320+. Формального соответствия нет."
          }
        ]
      },
      {
        "title": "4. Анатомия компонента",
        "blocks": [
          {
            "type": "p",
            "text": "Публично управляемые части:"
          },
          {
            "type": "p",
            "text": "1. Корень (контейнер) — auto layout, несёт высоту, радиус и левый отступ по осям Size и Breakpoint 2. Лейбл — свойство Text, стиль Button Small или Button Default по размеру 3. Ведущая иконка — по Show Icon (Boolean) и Icon (instance swap); только вместе с текстом 4. Счётчик — Count (TEXT), виден при Selected=True и Show Counter=true 5. Трейлинг-зона — Selected=False: стрелка вниз; Selected=True: Actions / Cross_Small_Bold 6. Слой рамки фокуса — _Select - Border, отдельная белая обводка 1 px, opacity 56%, отступ 2 px, радиус корня + 2"
          },
          {
            "type": "p",
            "text": "Легенда выносок (фиолетовые номера, конец выноски точно на часть):"
          },
          {
            "type": "bullets",
            "items": [
              "↗ Корень — control/{small|default}/height/{phone|tablet|desktop}, .../radius/...",
              "→ Лейбл — стиль Button Small / Button Default",
              "↘ Ведущая иконка — Show Icon + Icon",
              "↙ Счётчик — Show Counter + Count",
              "← Трейлинг — стрелка / Actions / Cross_Small_Bold",
              "↖ Focus-рамка — _Select - Border, только Desktop и Tablet"
            ]
          },
          {
            "type": "note",
            "text": "⚠️ Выносок должно быть по числу значимых частей, а не «сколько влезло». Для иллюстрации брать связанный инстанс, на котором видны и счётчик, и крестик (Selected=True, Show Counter=true)."
          }
        ]
      },
      {
        "title": "5. Настройки компонента",
        "blocks": [
          {
            "type": "p",
            "text": "Публичные свойства, доступные дизайнеру в правой панели:"
          },
          {
            "type": "table",
            "rows": [
              [
                "Свойство",
                "Тип",
                "Что делает"
              ],
              [
                "Text",
                "text",
                "подпись контрола"
              ],
              [
                "Show Icon",
                "boolean",
                "показывает/скрывает ведущую иконку"
              ],
              [
                "Icon",
                "instance swap",
                "подмена ведущей иконки"
              ],
              [
                "Show Counter",
                "boolean",
                "показывает счётчик"
              ],
              [
                "Count",
                "text",
                "значение счётчика; виден при Selected=True и Show Counter=true"
              ]
            ]
          },
          {
            "type": "note",
            "text": "⚠️ Таблица — схема, не снимок панели Figma. Для гайда нужен реальный скриншот панели свойств с подписями-выносками."
          }
        ]
      },
      {
        "title": "6. Варианты",
        "blocks": [
          {
            "type": "p",
            "text": "Оси:"
          },
          {
            "type": "table",
            "rows": [
              [
                "Ось",
                "Значения"
              ],
              [
                "Size",
                "Small / Default"
              ],
              [
                "Breakpoint",
                "320+ / 600+ / 1720+"
              ],
              [
                "Selected",
                "False / True"
              ],
              [
                "состояния",
                "Rest / Hover / Focus / Pressed / Disabled — набор зависит от брейкпоинта"
              ]
            ]
          },
          {
            "type": "p",
            "text": "28 вариантов на каждый размер, всего 56. Два Overview (46767:1861, 46767:2468) содержат по 28 связанных инстансов с подписями, дублей нет."
          },
          {
            "type": "p",
            "text": "✅ В текущей версии удалён Kids; осей Theme и свойства Background больше нет — не восстанавливать их из старой версии."
          },
          {
            "type": "note",
            "text": "⚠️ Overview — проверочный стенд покрытия, а не пользовательский гайд. Правила применения и Do/Don't из него не выводим."
          }
        ]
      },
      {
        "title": "7. Размеры",
        "blocks": [
          {
            "type": "table",
            "rows": [
              [
                "Параметр: Mobile / Tablet / Desktop",
                "Small",
                "Default"
              ],
              [
                "Высота",
                "36 / 40 / 42",
                "48 / 52 / 58"
              ],
              [
                "Левый отступ",
                "14 / 16 / 18",
                "18 / 20 / 22"
              ],
              [
                "Gap",
                "6 / 8 / 8",
                "8 / 10 / 10"
              ],
              [
                "Radius",
                "8 / 10 / 12",
                "10 / 12 / 14"
              ]
            ]
          },
          {
            "type": "note",
            "text": "❓ Ширина в источниках не зафиксирована. Считать ли её «по содержимому» — требует проверки на живом компоненте; не публиковать утверждение без подтверждения."
          }
        ]
      },
      {
        "title": "8. Состояния",
        "blocks": [
          {
            "type": "table",
            "rows": [
              [
                "Состояние",
                "Desktop (1720+)",
                "Tablet (600+)",
                "Mobile (320+)"
              ],
              [
                "Rest",
                "да",
                "да",
                "да"
              ],
              [
                "Hover",
                "да",
                "да",
                "да"
              ],
              [
                "Focus",
                "да",
                "да",
                "нет"
              ],
              [
                "Pressed",
                "да",
                "да",
                "да"
              ],
              [
                "Disabled",
                "да",
                "да",
                "да"
              ]
            ]
          },
          {
            "type": "p",
            "text": "Четыре пустые ячейки Mobile Focus — допустимые отсутствующие сочетания, а не пропуск в матрице. Не переносить на Select отсутствие Mobile Hover из Chips: здесь Hover на Mobile есть."
          },
          {
            "type": "p",
            "text": "Правила отображения ✅:"
          },
          {
            "type": "bullets",
            "items": [
              "Hover и Focus для glassy/third используют опубликованный Paint Style"
            ]
          },
          {
            "type": "p",
            "text": "color/fill/glassy/hover-focus/third того же уровня, с привязанными градиентами Step_1 / Step_2. Не оставлять Rest-заливку и не подменять её другим уровнем."
          },
          {
            "type": "bullets",
            "items": [
              "Focus — отдельная белая обводка 1 px, opacity 56%, отступ 2 px. Слой называется _Select - Border;"
            ]
          },
          {
            "type": "p",
            "text": "это не связанный инстанс _Button - Border."
          }
        ]
      },
      {
        "title": "9. Состояние выбора (Selected)",
        "blocks": [
          {
            "type": "p",
            "text": "Selected — устойчивый выбор, отдельная ось от Pressed. Не смешивать «список открыт», Selected и Pressed."
          },
          {
            "type": "bullets",
            "items": [
              "Selected=True использует color/fill/solid/inverse",
              "Опционально показывается счётчик: Show Counter=true + Count",
              "Трейлинг-иконка меняется на Actions / Cross_Small_Bold — правая зона сбрасывает выбор"
            ]
          },
          {
            "type": "note",
            "text": "⚠️ Отдельного hover-токена для inverse при проверке не найдено — не выдумывать его. ❓ Утверждение «Selected переключается только при открытии» требует подтверждённого источника: в iOS-гайде формулировка противоречива, а прототипные события и API кода не проверены."
          }
        ]
      },
      {
        "title": "10. Иконки",
        "blocks": [
          {
            "type": "bullets",
            "items": [
              "Ведущая иконка управляется Show Icon (boolean) и Icon (instance swap)",
              "Трейлинг при Selected=True — Actions / Cross_Small_Bold",
              "Правая иконка лежит в Trailing Icon: горизонтальный auto layout, Hug по ширине, Fill по высоте,"
            ]
          },
          {
            "type": "p",
            "text": "центрирование по вертикали. Правый padding корня — 0, правый padding контейнера привязан к control/small/filter-icon/padding-horizontal/{device} для обоих размеров"
          },
          {
            "type": "bullets",
            "items": [
              "Слева по решению пользователя: фиксированные 14 px Mobile / 18 px Tablet; справа 18 / 22 px,"
            ]
          },
          {
            "type": "p",
            "text": "без привязки ширины и высоты к компонентным токенам — это осознанное решение, не ошибка"
          },
          {
            "type": "note",
            "text": "⚠️ Desktop не нормализовать молча. Последний снимок: слева 20 px, справа обычно 24 px, в отдельных вариантах иные размеры и привязка control/default/text-icon/icon-size/desktop. Текущую неоднородность нельзя выдавать за согласованное правило — нужно решение команды."
          }
        ]
      },
      {
        "title": "11. Текст",
        "blocks": [
          {
            "type": "bullets",
            "items": [
              "Стиль подписи: Button Small или Button Default — по оси Size, с вариантами"
            ]
          },
          {
            "type": "p",
            "text": "Mobile 0+ / Tablet 600+ / Desktop 1720+"
          },
          {
            "type": "bullets",
            "items": [
              "Text есть во всех вариантах"
            ]
          },
          {
            "type": "note",
            "text": "❓ Лимит символов, многоточие и перенос не подтверждены. Не публиковать правило обрезки, пока оно не проверено на живом компоненте."
          }
        ]
      },
      {
        "title": "12. Отступы",
        "blocks": [
          {
            "type": "table",
            "rows": [
              [
                "Параметр: Mobile / Tablet / Desktop",
                "Small",
                "Default"
              ],
              [
                "Левый отступ",
                "14 / 16 / 18",
                "18 / 20 / 22"
              ],
              [
                "Gap",
                "6 / 8 / 8",
                "8 / 10 / 10"
              ],
              [
                "Правый padding корня",
                "0",
                "0"
              ],
              [
                "Правый padding контейнера",
                "control/small/filter-icon/padding-horizontal/{device} — для обоих размеров",
                "—"
              ]
            ]
          },
          {
            "type": "note",
            "text": "⚠️ Привязку правого padding и значение для Desktop сверить в живых слоях: пользователь менял Desktop-значение. Не заменять этот токен обычным отступом text-icon."
          }
        ]
      },
      {
        "title": "13. Область нажатия",
        "blocks": [
          {
            "type": "table",
            "rows": [
              [
                "Состояние",
                "Зоны"
              ],
              [
                "Selected=False",
                "вся площадь открывает список опций"
              ],
              [
                "Selected=True",
                "две зоны: основная часть открывает список, правая зона с крестиком сбрасывает выбор"
              ]
            ]
          }
        ]
      },
      {
        "title": "14. Как использовать (Do / Don't)",
        "blocks": [
          {
            "type": "p",
            "text": "Черновик на подтверждённых сценариях — формулировки требуют ревью дизайнера."
          },
          {
            "type": "p",
            "text": "Пара 1 — выбор компонента"
          },
          {
            "type": "bullets",
            "items": [
              "✅ Do: длинный список жанров — Select со счётчиком «Жанры · 3».",
              "❌ Don't: три жанра, помещающиеся в строку — Select вместо Chips. Лишний тап и скрытое состояние."
            ]
          },
          {
            "type": "p",
            "text": "Пара 2 — различение выбора и нажатия"
          },
          {
            "type": "bullets",
            "items": [
              "✅ Do: Selected=True показывает применённый фильтр и остаётся после закрытия списка.",
              "❌ Don't: считать Pressed подтверждённым выбором. Момент нажатия ≠ применённый фильтр."
            ]
          },
          {
            "type": "p",
            "text": "Пара 3 — сброс"
          },
          {
            "type": "bullets",
            "items": [
              "✅ Do: при Selected=True сброс — правой зоной с Cross_Small_Bold.",
              "❌ Don't: оставлять весь контрол одной зоной открытия, когда выбор уже применён: пользователь"
            ]
          },
          {
            "type": "p",
            "text": "не сможет сбросить фильтр одним действием."
          },
          {
            "type": "p",
            "text": "Пара 4 — группа с Chips"
          },
          {
            "type": "bullets",
            "items": [
              "✅ Do: Chips и Select стоят вместе над выдачей — короткие варианты раскрыты, длинные спрятаны.",
              "❌ Don't: разносить их по разным местам экрана: пользователь не понимает, что это одна группа фильтров."
            ]
          },
          {
            "type": "note",
            "text": "❓ Не выдумывать антипаттерны, которых в продукте Окко не бывает. Пары 3 и 4 требуют подтверждения у дизайнера."
          }
        ]
      },
      {
        "title": "15. Схема каталога Chips + Select",
        "blocks": [
          {
            "type": "p",
            "text": "Подтверждено пользователем: Select используется в каталоге в общей группе с Chips, гайд должен показывать их вместе над выдачей."
          },
          {
            "type": "bullets",
            "items": [
              "Chips раскрывают короткие и быстрые варианты прямо в строке",
              "Select открывает список",
              "За компоновку группы и выдачу отвечает Filters Catalog (27582:114073), а не сам Select"
            ]
          },
          {
            "type": "note",
            "text": "⚠️ Схема каталога — не production-скриншот. Подписать это явно в гайде."
          }
        ]
      },
      {
        "title": "16. Связь с Dropdown",
        "blocks": [
          {
            "type": "p",
            "text": "Dropdown (22080:330029) — связанный десктопный список, а не вложенная часть Select."
          },
          {
            "type": "note",
            "text": "❓ У Dropdown значения брейкпоинтов 1720/1320, у Select — 1720+/600+/320+. Соответствие и мобильный способ раскрытия требуют решения. Не описывать Dropdown как «шторку Select»."
          }
        ]
      },
      {
        "title": "17. Связанные компоненты",
        "blocks": [
          {
            "type": "table",
            "rows": [
              [
                "Компонент",
                "Связь"
              ],
              [
                "Chips",
                "та же группа в каталоге; для коротких списков, раскрываются в строке"
              ],
              [
                "Dropdown",
                "связанный десктопный список; не вложен в Select"
              ],
              [
                "Filters Catalog",
                "компоновка группы и выдачи"
              ],
              [
                "Actions / Cross_Small_Bold",
                "сброс применённого выбора"
              ],
              [
                "BottomSheet",
                "⚠️ для Web не подтверждён как механизм раскрытия списка Select"
              ]
            ]
          }
        ]
      }
    ]
  },
  "passport": {
    "sections": [
      {
        "title": "1. Идентификация и достоверность",
        "blocks": [
          {
            "type": "table",
            "rows": [
              [
                "Параметр",
                "Значение"
              ],
              [
                "Компонент",
                "Select · Web"
              ],
              [
                "Файл",
                "Lib-Web e72TWMOh7ibwauqgKwLnC9"
              ],
              [
                "COMPONENT_SET",
                "21983:326646"
              ],
              [
                "Гайд",
                "46763:2394"
              ],
              [
                "Паспорт",
                "46763:2575"
              ],
              [
                "Overview",
                "46767:1861 (Default), 46767:2468 (Small)"
              ],
              [
                "Дата снимка контекста",
                "2026-10-09"
              ],
              [
                "Снимок Figma",
                "✅ есть; живое чтение узлов ⚠️ не выполнено в текущей сессии"
              ]
            ]
          },
          {
            "type": "p",
            "text": "Статус достоверности: документ описывает снимок задачи, а не опубликованное состояние библиотеки. Production-ready не присваивать. Клавиатура, лимит и обрезка подписи, применение множественного выбора и кодовая интеграция не проверены."
          }
        ]
      },
      {
        "title": "2. Публичные свойства Figma",
        "blocks": [
          {
            "type": "table",
            "rows": [
              [
                "Свойство",
                "Тип Figma",
                "Назначение",
                "Условие"
              ],
              [
                "Text",
                "TEXT",
                "подпись контрола",
                "есть во всех вариантах"
              ],
              [
                "Show Icon",
                "BOOLEAN",
                "видимость ведущей иконки",
                "—"
              ],
              [
                "Icon",
                "INSTANCE_SWAP",
                "подмена ведущей иконки",
                "вместе с Show Icon"
              ],
              [
                "Show Counter",
                "BOOLEAN",
                "видимость счётчика",
                "—"
              ],
              [
                "Count",
                "TEXT",
                "значение счётчика",
                "виден при Selected=True и Show Counter=true"
              ]
            ]
          },
          {
            "type": "p",
            "text": "Оси вариантов: Size (Default / Small), Breakpoint (1720+ / 600+ / 320+), Selected (False / True), плюс состояния в пределах брейкпоинта."
          }
        ]
      },
      {
        "title": "3. Допустимые сочетания",
        "blocks": [
          {
            "type": "bullets",
            "items": [
              "28 вариантов на каждый размер, всего 56. Два Overview содержат по 28 связанных инстансов, дублей нет.",
              "4 пустые ячейки Mobile Focus — намеренно отсутствующие сочетания. Presence варианта"
            ]
          },
          {
            "type": "p",
            "text": "Focus на Desktop/Tablet не означает, что он есть на Mobile."
          },
          {
            "type": "bullets",
            "items": [
              "Selected и Pressed — разные оси: устойчивый выбор и момент взаимодействия. Не сворачивать в одну.",
              "✅ Из текущей версии удалён Kids; осей Theme и свойства Background нет. Не восстанавливать из старой версии."
            ]
          }
        ]
      },
      {
        "title": "4. Переменные геометрии и места использования",
        "blocks": [
          {
            "type": "p",
            "text": "Корень использует существующие компонентные токены с суффиксом устройства:"
          },
          {
            "type": "table",
            "rows": [
              [
                "Место",
                "Токен"
              ],
              [
                "Высота корня",
                "control/{small|default}/height/{phone|tablet|desktop}"
              ],
              [
                "Радиус корня",
                "control/{small|default}/radius/{phone|tablet|desktop}"
              ],
              [
                "Левый отступ текста/иконки",
                "control/{small|default}/text-icon/padding-horizontal/{device}"
              ],
              [
                "Gap между частями",
                "control/{small|default}/text-icon/gap-horizontal/{device}"
              ],
              [
                "Правый padding контейнера (крестик)",
                "control/small/filter-icon/padding-horizontal/{device} — для обоих размеров"
              ],
              [
                "Размер ведущей иконки (Desktop, часть вариантов)",
                "control/default/text-icon/icon-size/desktop ⚠️"
              ]
            ]
          },
          {
            "type": "p",
            "text": "Размеры по осям:"
          },
          {
            "type": "table",
            "rows": [
              [
                "Параметр: Mobile / Tablet / Desktop",
                "Small",
                "Default"
              ],
              [
                "Высота",
                "36 / 40 / 42",
                "48 / 52 / 58"
              ],
              [
                "Левый отступ",
                "14 / 16 / 18",
                "18 / 20 / 22"
              ],
              [
                "Gap",
                "6 / 8 / 8",
                "8 / 10 / 10"
              ],
              [
                "Radius",
                "8 / 10 / 12",
                "10 / 12 / 14"
              ]
            ]
          },
          {
            "type": "p",
            "text": "⚠️ Иконки намеренно не привязаны к токенам по ширине и высоте (решение пользователя): слева фиксированные 14 px Mobile / 18 px Tablet, справа 18 / 22 px. Для Desktop последний снимок — слева 20 px, справа обычно 24 px, в отдельных вариантах иные размеры и привязка к control/default/text-icon/icon-size/desktop. Не нормализовать Desktop молча."
          },
          {
            "type": "p",
            "text": "⚠️ Правый padding корня — 0. Правый padding контейнера привязан к control/small/filter-icon/padding-horizontal/{device} для обоих размеров. Desktop-значение пользователь менял — сверить живую привязку. Не заменять этот токен обычным отступом text-icon."
          }
        ]
      },
      {
        "title": "5. Цвета и стили",
        "blocks": [
          {
            "type": "table",
            "rows": [
              [
                "Место",
                "Значение"
              ],
              [
                "Базовая заливка (Rest)",
                "color/fill/glassy/third"
              ],
              [
                "Hover и Focus",
                "опубликованный Paint Style color/fill/glassy/hover-focus/third того же уровня, с привязанными градиентами Step_1 / Step_2"
              ],
              [
                "Selected=True",
                "color/fill/solid/inverse"
              ],
              [
                "Focus-рамка",
                "отдельная белая обводка 1 px, opacity 56%, отступ 2 px, радиус корня + 2; слой _Select - Border"
              ]
            ]
          },
          {
            "type": "p",
            "text": "Ограничения:"
          },
          {
            "type": "bullets",
            "items": [
              "Для Hover/Focus не оставлять Rest-заливку и не подменять её другим уровнем glassy.",
              "⚠️ Отдельного hover-токена для inverse при проверке не найдено — не выдумывать его.",
              "⚠️ _Select - Border — не связанный инстанс _Button - Border. Проверять растяжение при"
            ]
          },
          {
            "type": "p",
            "text": "смене текста и видимости счётчика."
          }
        ]
      },
      {
        "title": "6. Текстовые стили",
        "blocks": [
          {
            "type": "table",
            "rows": [
              [
                "Размер",
                "Стиль",
                "Варианты"
              ],
              [
                "Small",
                "Button Small",
                "Mobile 0+ / Tablet 600+ / Desktop 1720+"
              ],
              [
                "Default",
                "Button Default",
                "Mobile 0+ / Tablet 600+ / Desktop 1720+"
              ]
            ]
          }
        ]
      },
      {
        "title": "7. Зависимости",
        "blocks": [
          {
            "type": "table",
            "rows": [
              [
                "Зависимость",
                "Роль",
                "Тип связи"
              ],
              [
                "Actions / Cross_Small_Bold",
                "иконка сброса при Selected=True",
                "instance swap"
              ],
              [
                "Chips",
                "общая группа в каталоге",
                "продуктовая, не вложенность"
              ],
              [
                "Dropdown (22080:330029)",
                "связанный десктопный список",
                "не вложенная часть Select"
              ],
              [
                "Filters Catalog (27582:114073)",
                "компоновка группы и выдачи",
                "внешний контейнер"
              ]
            ]
          }
        ]
      },
      {
        "title": "8. Контракт реализации и ограничения",
        "blocks": [
          {
            "type": "p",
            "text": "Подтверждено ✅:"
          },
          {
            "type": "bullets",
            "items": [
              "Selected=False — вся площадь контрола открывает список опций.",
              "Selected=True — две зоны: основная открывает список, правая сбрасывает выбор.",
              "Selected отражает уже применённый выбор."
            ]
          },
          {
            "type": "p",
            "text": "Не подтверждено ❓ — не публиковать как контракт:"
          },
          {
            "type": "bullets",
            "items": [
              "Клавиатура: Enter / Space, Tab, порядок фокуса, доступная семантика (роль, aria-expanded, объявление счётчика).",
              "Переключение Selected «только при открытии»: в iOS-гайде формулировка противоречива, прототипные события не проверены.",
              "Поведение при переполнении подписи: лимит символов, многоточие, перенос.",
              "Применение множественного выбора, интеграция в коде, события.",
              "Маппинг брейкпоинтов на Dropdown (1720/1320 против 1720+/600+/320+) и мобильный способ раскрытия списка."
            ]
          }
        ]
      },
      {
        "title": "9. Предлагаемый API — ❌ НЕ ПОДТВЕРЖДЁН",
        "blocks": [
          {
            "type": "p",
            "text": "Ниже — предложение для обсуждения, а не контракт реализации. Взято из продуктового смысла компонента; код и события не проверялись."
          },
          {
            "type": "code",
            "text": "type SelectProps = {\n  label: string;            // Text\n  selected?: boolean;       // Selected\n  showIcon?: boolean;       // Show Icon\n  icon?: ReactNode;         // Icon\n  showCounter?: boolean;    // Show Counter\n  count?: string;           // Count\n  onOpen?: () => void;      // открытие списка (вся площадь / основная зона)\n  onClear?: () => void;     // сброс выбора (правая зона при Selected=true)\n};"
          },
          {
            "type": "p",
            "text": "Открытые вопросы к API: как передаётся множественный выбор, кто управляет состоянием selected (контролируемый или нет), как объявляется счётчик для скринридера."
          }
        ]
      },
      {
        "title": "10. Обслуживание: клонирование вариантов",
        "blocks": [
          {
            "type": "p",
            "text": "Грабли, подтверждённые на этом компоненте: при клонировании вариантов определения свойств остаются, а привязки слоёв (componentPropertyReferences) теряются. Наличие свойства в панели не означает, что оно работает."
          },
          {
            "type": "p",
            "text": "При добавлении или клонировании вариантов проверять фактическое поведение: смену Text, переключение Show Icon и Show Counter, подмену Icon. Проверять инстансы, а не только наличие поля в панели свойств."
          }
        ]
      }
    ]
  }
};

const FALLBACK = {
  fonts: {
    title: { family: "Suisse Int'l", style: 'Medium' },
    body: { family: "Suisse Int'l", style: 'Regular' },
  },
  colors: {
    text: '#FFFFFFF5',
    text2: '#FFFFFFC7',
    text3: '#FFFFFF8F',
    surface: '#1B1A1D',
    surface2: '#2C2B2F',
    accent: '#616CFB',
    do: '#12B77C',
    dont: '#F25857',
  },
  sizes: { title: 24, h3: 18, body: 14, code: 12 },
  gap: { section: 48, block: 12, pad: 24, radius: 16 },
};

function hexToPaint(hex) {
  const raw = String(hex).replace('#', '');
  const paint = {
    type: 'SOLID',
    color: {
      r: parseInt(raw.slice(0, 2), 16) / 255,
      g: parseInt(raw.slice(2, 4), 16) / 255,
      b: parseInt(raw.slice(4, 6), 16) / 255,
    },
  };
  if (raw.length === 8) paint.opacity = parseInt(raw.slice(6, 8), 16) / 255;
  return paint;
}

function solidPaint(fills) {
  if (!fills || fills === figma.mixed || !fills.length) return null;
  for (const f of fills) {
    if (f && f.type === 'SOLID' && f.visible !== false) {
      const paint = { type: 'SOLID', color: { r: f.color.r, g: f.color.g, b: f.color.b } };
      if (typeof f.opacity === 'number') paint.opacity = f.opacity;
      return paint;
    }
  }
  return null;
}

async function loadFont(candidates) {
  const tried = [];
  for (const [family, style] of candidates) {
    try {
      await figma.loadFontAsync({ family, style });
      return { family, style };
    } catch (e) {
      tried.push(family + ' ' + style);
    }
  }
  throw new Error('Не удалось загрузить шрифт. Пробовали: ' + tried.join(', '));
}

function pickTarget() {
  const sel = figma.currentPage.selection;
  if (sel.length !== 1) {
    return { error: 'Выберите ровно один фрейм: Guide · Select · Web или Passport · Select · Web.' };
  }
  const node = sel[0];
  if (node.type !== 'FRAME' && node.type !== 'SECTION') {
    return { error: 'Выбранная нода — ' + node.type + ', а нужен фрейм или секция.' };
  }
  const isPassport = /passport/i.test(node.name);
  const isGuide = /guide/i.test(node.name);
  if (!isPassport && !isGuide) {
    return { error: 'В имени фрейма нет «Guide» или «Passport»: «' + node.name + '». Остановлено, чтобы не писать не туда.' };
  }
  return { target: node, doc: isPassport ? 'passport' : 'guide' };
}

/** Снимает оформление с живого фрейма: шрифты, размеры и цвета существующих текстов. */
function sampleStyle(target) {
  const style = {
    fonts: {
      title: { family: FALLBACK.fonts.title.family, style: FALLBACK.fonts.title.style },
      body: { family: FALLBACK.fonts.body.family, style: FALLBACK.fonts.body.style },
    },
    colors: {
      text: hexToPaint(FALLBACK.colors.text),
      text2: hexToPaint(FALLBACK.colors.text2),
      text3: hexToPaint(FALLBACK.colors.text3),
      surface: hexToPaint(FALLBACK.colors.surface),
      surface2: hexToPaint(FALLBACK.colors.surface2),
      accent: hexToPaint(FALLBACK.colors.accent),
    },
    sizes: {
      title: FALLBACK.sizes.title,
      h3: FALLBACK.sizes.h3,
      body: FALLBACK.sizes.body,
      code: FALLBACK.sizes.code,
    },
    contentWidth: 1200,
    sampled: false,
  };

  try {
    const texts = target.findAll((n) => n.type === 'TEXT');
    const info = [];
    for (const t of texts) {
      if (typeof t.fontSize !== 'number') continue;
      if (!t.fontName || t.fontName === figma.mixed) continue;
      info.push({ size: t.fontSize, font: t.fontName, fills: t.fills });
    }
    if (info.length) {
      info.sort((a, b) => b.size - a.size);
      const title = info[0];
      style.sizes.title = Math.min(Math.max(title.size, 18), 32);
      style.fonts.title = { family: title.font.family, style: title.font.style };
      const titlePaint = solidPaint(title.fills);
      if (titlePaint) style.colors.text = titlePaint;

      const counts = {};
      for (const it of info) {
        if (it.size < title.size) counts[it.size] = (counts[it.size] || 0) + 1;
      }
      let bodySize = null;
      let best = 0;
      for (const key in counts) {
        if (counts[key] > best) {
          best = counts[key];
          bodySize = Number(key);
        }
      }
      if (bodySize) {
        style.sizes.body = Math.min(Math.max(bodySize, 11), 18);
        const sample = info.find((it) => it.size === bodySize);
        if (sample) {
          style.fonts.body = { family: sample.font.family, style: sample.font.style };
          const bodyPaint = solidPaint(sample.fills);
          if (bodyPaint) style.colors.text2 = bodyPaint;
        }
      }
      style.sizes.h3 = Math.max(style.sizes.body + 2, Math.round(style.sizes.body * 1.25));
      style.sizes.code = Math.max(10, style.sizes.body - 2);
      style.sampled = true;
    }
  } catch (e) {
    // остаёмся на значениях токенов ДС
  }

  try {
    if (target.layoutMode && target.layoutMode !== 'NONE') {
      style.contentWidth =
        target.width - (target.paddingLeft || 0) - (target.paddingRight || 0);
    } else {
      // У фрейма без auto-layout ширину контентной колонки задаёт самый широкий ребёнок.
      let widest = 0;
      for (const child of target.children) widest = Math.max(widest, child.width);
      style.contentWidth = widest || target.width;
    }
  } catch (e) {
    style.contentWidth = 1200;
  }
  if (!style.contentWidth || style.contentWidth < 240) style.contentWidth = 1200;
  return style;
}

function makeText(value, font, size, paint, lineHeight) {
  const node = figma.createText();
  // fontName принимает строго { family, style }
  node.fontName = { family: font.family, style: font.style };
  node.characters = value;
  node.fontSize = size;
  node.lineHeight = { unit: 'PIXELS', value: Math.round(lineHeight) };
  node.fills = [paint];
  return node;
}

function vstack(name) {
  const frame = figma.createFrame();
  frame.name = name;
  frame.layoutMode = 'VERTICAL';
  frame.primaryAxisSizingMode = 'AUTO';
  frame.counterAxisSizingMode = 'FIXED';
  frame.itemSpacing = FALLBACK.gap.block;
  frame.fills = [];
  frame.clipsContent = false;
  return frame;
}

const created = [];
function track(node) {
  created.push(node.id);
  return node;
}

function renderTable(rows, style, width) {
  const cols = Math.max.apply(
    null,
    rows.map((r) => r.length)
  );
  const firstShare = cols > 2 ? 1.6 : 1;
  const totalShare = firstShare + (cols - 1);
  const widths = [];
  for (let c = 0; c < cols; c++) {
    widths.push(Math.round((width * (c === 0 ? firstShare : 1)) / totalShare));
  }

  const table = vstack('table');
  table.itemSpacing = 2;
  table.counterAxisSizingMode = 'FIXED';
  table.resize(width, 40);

  rows.forEach((cells, rowIndex) => {
    const row = figma.createFrame();
    row.name = 'row';
    row.layoutMode = 'HORIZONTAL';
    row.primaryAxisSizingMode = 'FIXED';
    row.counterAxisSizingMode = 'AUTO';
    row.itemSpacing = 2;
    row.fills = [];
    row.clipsContent = false;
    table.appendChild(row);
    row.resize(width, 24);
    track(row);
    const cellsInRow = [];

    for (let c = 0; c < cols; c++) {
      const cell = figma.createFrame();
      cell.name = 'cell';
      cell.layoutMode = 'VERTICAL';
      cell.primaryAxisSizingMode = 'AUTO';
      cell.counterAxisSizingMode = 'FIXED';
      cell.paddingTop = 8;
      cell.paddingBottom = 8;
      cell.paddingLeft = 12;
      cell.paddingRight = 12;
      cell.cornerRadius = 6;
      cell.fills = rowIndex === 0 ? [style.colors.surface2] : [style.colors.surface];
      cell.clipsContent = false;
      row.appendChild(cell);
      cell.resize(widths[c], 24);
      track(cell);
      cellsInRow.push(cell);

      const value = cells[c] === undefined ? '' : cells[c];
      const text = makeText(
        value,
        style.fonts.body,
        rowIndex === 0 ? style.sizes.body : style.sizes.body,
        rowIndex === 0 ? style.colors.text : style.colors.text2,
        style.sizes.body * 1.4
      );
      cell.appendChild(text);
      text.layoutSizingHorizontal = 'FILL';
      track(text);
    }

    // Высоту строки фиксируем по самой высокой ячейке и только потом растягиваем
    // остальные: если растянуть все ячейки сразу, hug-строка схлопывается.
    let maxHeight = 24;
    for (const c of cellsInRow) maxHeight = Math.max(maxHeight, c.height);
    row.counterAxisSizingMode = 'FIXED';
    row.resize(width, maxHeight);
    for (const c of cellsInRow) c.layoutSizingVertical = 'FILL';
  });

  return table;
}

function renderBullets(items, style) {
  const text = makeText(
    items.map((i) => '—  ' + i).join('\n'),
    style.fonts.body,
    style.sizes.body,
    style.colors.text2,
    style.sizes.body * 1.6
  );
  return text;
}

function renderBlock(block, style, width) {
  if (block.type === 'h3') {
    return makeText(block.text, style.fonts.title, style.sizes.h3, style.colors.text, style.sizes.h3 * 1.3);
  }
  if (block.type === 'p') {
    return makeText(block.text, style.fonts.body, style.sizes.body, style.colors.text2, style.sizes.body * 1.55);
  }
  if (block.type === 'bullets') {
    return renderBullets(block.items, style);
  }
  if (block.type === 'note') {
    const frame = vstack('note');
    frame.counterAxisSizingMode = 'FIXED';
    frame.resize(width, 20);
    frame.paddingTop = 10;
    frame.paddingBottom = 10;
    frame.paddingLeft = 14;
    frame.paddingRight = 14;
    frame.cornerRadius = 8;
    frame.fills = [style.colors.surface];
    const text = makeText(block.text, style.fonts.body, style.sizes.body, style.colors.text3, style.sizes.body * 1.5);
    frame.appendChild(text);
    text.layoutSizingHorizontal = 'FILL';
    track(text);
    return frame;
  }
  if (block.type === 'code') {
    const frame = vstack('code');
    frame.counterAxisSizingMode = 'FIXED';
    frame.resize(width, 20);
    frame.paddingTop = 12;
    frame.paddingBottom = 12;
    frame.paddingLeft = 14;
    frame.paddingRight = 14;
    frame.cornerRadius = 8;
    frame.fills = [style.colors.surface];
    const text = makeText(block.text, style.fonts.body, style.sizes.code, style.colors.text2, style.sizes.code * 1.5);
    frame.appendChild(text);
    text.layoutSizingHorizontal = 'FILL';
    track(text);
    return frame;
  }
  if (block.type === 'table') {
    return renderTable(block.rows, style, width);
  }
  return null;
}

function alreadyPresent(target, name) {
  return target.children.some((child) => child.name === name);
}

async function main() {
  const picked = pickTarget();
  if (picked.error) {
    figma.closePlugin(picked.error);
    return;
  }
  const target = picked.target;
  const document = CONTENT[picked.doc];
  if (!document || !document.sections.length) {
    figma.closePlugin('Нет контента для документа «' + picked.doc + '».');
    return;
  }

  const style = sampleStyle(target);

  style.fonts.title = await loadFont([
    [style.fonts.title.family, style.fonts.title.style],
    ["Suisse Int'l", 'Medium'],
    ['Inter', 'Semi Bold'],
    ['Inter', 'Medium'],
  ]);
  style.fonts.body = await loadFont([
    [style.fonts.body.family, style.fonts.body.style],
    ["Suisse Int'l", 'Regular'],
    ['Inter', 'Regular'],
  ]);

  const isAutoLayout = target.layoutMode && target.layoutMode !== 'NONE';
  const width = Math.round(style.contentWidth);
  const notes = [];
  if (!style.sampled) {
    notes.push('Оформление не считано с файла — применены токены ДС.');
  }

  let bottom = 0;
  if (!isAutoLayout) {
    for (const child of target.children) {
      bottom = Math.max(bottom, child.y + child.height);
    }
  }

  let createdSections = 0;
  let skipped = 0;

  for (let i = 0; i < document.sections.length; i++) {
    const section = document.sections[i];
    const name = section.title;
    if (alreadyPresent(target, name)) {
      skipped++;
      continue;
    }

    const frame = vstack(name);
    frame.itemSpacing = FALLBACK.gap.block;
    frame.counterAxisSizingMode = 'FIXED';
    frame.resize(width, 80);

    const heading = makeText(name, style.fonts.title, style.sizes.title, style.colors.text, style.sizes.title * 1.25);
    frame.appendChild(heading);
    heading.layoutSizingHorizontal = 'FILL';
    track(heading);

    for (const block of section.blocks) {
      const node = renderBlock(block, style, width);
      if (!node) continue;
      frame.appendChild(node);
      if (node.type === 'TEXT') {
        node.layoutSizingHorizontal = 'FILL';
      } else if (node.type === 'FRAME') {
        node.layoutSizingHorizontal = 'FIXED';
      }
      track(node);
    }

    target.appendChild(frame);
    if (isAutoLayout) {
      frame.layoutSizingHorizontal = 'FILL';
    } else {
      frame.x = 0;
      frame.y = bottom + (bottom ? FALLBACK.gap.section : 0);
      bottom = frame.y + frame.height;
    }
    track(frame);
    createdSections++;
  }

  const summary = {
    document: picked.doc,
    targetName: target.name,
    targetId: target.id,
    createdSections,
    skippedExisting: skipped,
    createdNodes: created.length,
    sampledFromFile: style.sampled,
    notes,
  };
  console.log(JSON.stringify(summary, null, 2));
  figma.closePlugin(
    'Готово: секций ' +
      createdSections +
      ', пропущено уже существующих ' +
      skipped +
      ', создано нод ' +
      created.length
  );
}

main().catch((error) => {
  const message = error && error.message ? error.message : String(error);
  figma.closePlugin('Ошибка: ' + message);
});
