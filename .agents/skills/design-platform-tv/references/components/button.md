# Button

## Назначение

Универсальная кнопка для основных, вторичных, опасных и брендированных действий на iPhone и iPad.

## Когда использовать

- Для основного или дополнительного действия пользователя.
- Для запуска операции, подтверждения, продолжения или отмены сценария.
- Для компактных icon-only действий и действий с подписью рядом или снизу.

### Стили

| Style | Назначение |
|---|---|
| `Primary` | главное действие в текущем контексте |
| `Secondary` | альтернативное или менее приоритетное действие |
| `Ghost` | действие с минимальным визуальным акцентом |
| `Danger` | опасное или разрушительное действие |
| `SberPay` | действие оплаты через SberPay |
| `Sber` | брендированное действие Сбера |

## Когда НЕ использовать

- Для запуска ИИ-ассистента — использовать `AI Button`.
- Для партнёрского betting-действия или коэффициентов — использовать
  [Bet Button](bet-button.md).
- Для выбора фильтра или тега — использовать `Chips`/`Select`.
- Для переключения разделов — использовать соответствующую навигацию, а не Button.
- Не применять `Sber` или `SberPay` вне соответствующего брендированного сценария.

## Платформенные особенности iOS

### Формы

- `Rectangle` — стандартная кнопка-контейнер.
- `Circle →` — круглая кнопка, подпись располагается справа.
- `Circle ↓` — круглая кнопка, подпись располагается снизу.
- `Text=False` — icon-only вариант; `Icon` включает иконку, а
  `↳ Icon Instance` позволяет заменить её.

### Размеры

| Size | iPhone | iPad | Ограничение |
|---|---:|---:|---|
| `ExtraSmall` | 28 | 32 | опубликован только для части Rectangle/Circle-вариантов |
| `Small` | 36 | 40 | стандартный компактный размер |
| `Default` | 48 | 52 | основной размер |
| `Large` | 58 | 76 | опубликован для части круглых вариантов |

Размер выше — базовая высота/диаметр. Итоговая ширина зависит от формы, текста
и брендированного стиля; например, `SberPay` шире обычной Rectangle-кнопки.

### Состояния

`Rest`, `Touch`, `Disabled`, `Loading`, `Progress`.

Набор содержит **412 опубликованных комбинаций**, но значения свойств нельзя
комбинировать произвольно: некоторые состояния, размеры и брендированные стили
существуют только для части форм. При сборке выбирать реальный опубликованный
вариант, а не достраивать отсутствующую комбинацию вручную.

## Связанные компоненты

- `AI Button` — специализированное действие ИИ-ассистента.
- [Bet Button](bet-button.md) — партнёрское действие букмекера и коэффициенты.
- `Mark / Star_Bold` — демонстрационная иконка в icon slot.
- `.x / loading shape` — индикатор состояния `Loading`.
- `Logotypes / Sberbank` — логотип для стиля `Sber`.
- `Банки / Sber Pay / Без обводки(alt)` — знак стиля `SberPay`.
- `_compensation` — внутренний служебный компонент выравнивания.

<!-- FIGMA_SYNC:START -->
## Актуальные данные Figma

> Последняя проверка: `2026-08-21T15:22:52Z` · структура `6dd72c6fcadb` · статус `unknown`.

### Свойства из компонента

| Свойство | Тип | Значение по умолчанию | Варианты |
|---|---|---|---|
| `Device` | `variant` | `—` | iPad / iPhone |
| `Icon` | `boolean` | `—` | — |
| `Shape` | `variant` | `—` | Circle → / Circle ↓ / Rectangle |
| `Size` | `variant` | `—` | Default / ExtraSmall / Large / Small |
| `State` | `variant` | `—` | Disabled / Loading / Progress / Rest / Touch |
| `String Text` | `text` | `—` | — |
| `Style` | `variant` | `—` | Danger / Ghost / Primary / Sber / SberPay / Secondary |
| `Text` | `variant` | `—` | False / True |
| `↳ Icon Instance` | `instance_swap` | `—` | — |

### Варианты и размеры

| Ось | Значения |
|---|---|
| `Device` | iPad / iPhone |
| `Shape` | Circle → / Circle ↓ / Rectangle |
| `Size` | Default / ExtraSmall / Large / Small |
| `State` | Disabled / Loading / Progress / Rest / Touch |
| `Style` | Danger / Ghost / Primary / Sber / SberPay / Secondary |
| `Text` | False / True |

Комбинаций в COMPONENT_SET: **412**.

| Размер | Количество вариантов | Примеры |
|---|---:|---|
| `28.0×28.0` | 8 | Device=iPhone, Shape=Circle ↓, Style=Secondary, Size=ExtraSmall, State=Rest, Text=False; Device=iPhone, Shape=Circle ↓, Style=Danger, Size=ExtraSmall, State=Rest, Text=False; Device=iPhone, Shape=Circle ↓, Style=Secondary, Size=ExtraSmall, State=Touch, Text=False |
| `32.0×32.0` | 8 | Device=iPad, Shape=Circle ↓, Style=Secondary, Size=ExtraSmall, State=Rest, Text=False; Device=iPad, Shape=Circle ↓, Style=Danger, Size=ExtraSmall, State=Rest, Text=False; Device=iPad, Shape=Circle ↓, Style=Secondary, Size=ExtraSmall, State=Touch, Text=False |
| `36.0×36.0` | 35 | Device=iPhone, Shape=Rectangle, Style=Secondary, Size=Small, State=Rest, Text=False; Device=iPhone, Shape=Rectangle, Style=Danger, Size=Small, State=Rest, Text=False; Device=iPhone, Shape=Rectangle, Style=Sber, Size=Small, State=Rest, Text=False |
| `36.0×38.0` | 2 | Device=iPhone, Shape=Circle ↓, Style=Ghost, Size=Small, State=Rest, Text=True; Device=iPhone, Shape=Circle ↓, Style=Ghost, Size=Small, State=Disabled, Text=True |
| `40.0×40.0` | 34 | Device=iPad, Shape=Rectangle, Style=Secondary, Size=Small, State=Rest, Text=False; Device=iPad, Shape=Rectangle, Style=Danger, Size=Small, State=Rest, Text=False; Device=iPad, Shape=Rectangle, Style=Sber, Size=Small, State=Rest, Text=False |
| `40.0×44.0` | 3 | Device=iPad, Shape=Circle ↓, Style=Ghost, Size=Small, State=Rest, Text=True; Device=iPad, Shape=Circle ↓, Style=Ghost, Size=Small, State=Disabled, Text=True; Device=iPad, Shape=Circle ↓, Style=Ghost, Size=Small, State=Touch, Text=True |
| `48.0×44.0` | 3 | Device=iPhone, Shape=Circle ↓, Style=Ghost, Size=Default, State=Rest, Text=True; Device=iPhone, Shape=Circle ↓, Style=Ghost, Size=Default, State=Disabled, Text=True; Device=iPhone, Shape=Circle ↓, Style=Ghost, Size=Default, State=Touch, Text=True |
| `48.0×48.0` | 34 | Device=iPhone, Shape=Rectangle, Style=Primary, Size=Default, State=Rest, Text=False; Device=iPhone, Shape=Rectangle, Style=Primary, Size=Default, State=Loading, Text=False; Device=iPhone, Shape=Rectangle, Style=Primary, Size=Default, State=Progress, Text=False |
| `52.0×50.0` | 3 | Device=iPad, Shape=Circle ↓, Style=Ghost, Size=Default, State=Rest, Text=True; Device=iPad, Shape=Circle ↓, Style=Ghost, Size=Default, State=Disabled, Text=True; Device=iPad, Shape=Circle ↓, Style=Ghost, Size=Default, State=Touch, Text=True |
| `52.0×52.0` | 34 | Device=iPad, Shape=Rectangle, Style=Secondary, Size=Default, State=Rest, Text=False; Device=iPad, Shape=Rectangle, Style=Danger, Size=Default, State=Rest, Text=False; Device=iPad, Shape=Rectangle, Style=Sber, Size=Default, State=Rest, Text=False |
| `58.0×58.0` | 15 | Device=iPhone, Shape=Circle ↓, Style=Secondary, Size=Large, State=Rest, Text=False; Device=iPhone, Shape=Circle ↓, Style=Danger, Size=Large, State=Rest, Text=False; Device=iPhone, Shape=Circle ↓, Style=Primary, Size=Large, State=Rest, Text=False |
| `76.0×76.0` | 15 | Device=iPad, Shape=Circle ↓, Style=Secondary, Size=Large, State=Rest, Text=False; Device=iPad, Shape=Circle ↓, Style=Danger, Size=Large, State=Rest, Text=False; Device=iPad, Shape=Circle ↓, Style=Primary, Size=Large, State=Rest, Text=False |
| `90.0×56.0` | 12 | Device=iPhone, Shape=Circle ↓, Style=Secondary, Size=Small, State=Rest, Text=True; Device=iPhone, Shape=Circle ↓, Style=Danger, Size=Small, State=Rest, Text=True; Device=iPhone, Shape=Circle ↓, Style=Primary, Size=Small, State=Rest, Text=True |
| `90.0×70.0` | 12 | Device=iPhone, Shape=Circle ↓, Style=Secondary, Size=Default, State=Rest, Text=True; Device=iPhone, Shape=Circle ↓, Style=Danger, Size=Default, State=Rest, Text=True; Device=iPhone, Shape=Circle ↓, Style=Primary, Size=Default, State=Rest, Text=True |
| `102.0×66.0` | 12 | Device=iPad, Shape=Circle ↓, Style=Secondary, Size=Small, State=Rest, Text=True; Device=iPad, Shape=Circle ↓, Style=Danger, Size=Small, State=Rest, Text=True; Device=iPad, Shape=Circle ↓, Style=Primary, Size=Small, State=Rest, Text=True |
| `102.0×80.0` | 12 | Device=iPad, Shape=Circle ↓, Style=Secondary, Size=Default, State=Rest, Text=True; Device=iPad, Shape=Circle ↓, Style=Danger, Size=Default, State=Rest, Text=True; Device=iPad, Shape=Circle ↓, Style=Primary, Size=Default, State=Rest, Text=True |
| `120.0×28.0` | 5 | Device=iPhone, Shape=Rectangle, Style=Secondary, Size=ExtraSmall, State=Rest, Text=True; Device=iPhone, Shape=Rectangle, Style=Secondary, Size=ExtraSmall, State=Loading, Text=True; Device=iPhone, Shape=Rectangle, Style=Secondary, Size=ExtraSmall, State=Progress, Text=True |
| `141.0×36.0` | 12 | Device=iPhone, Shape=Circle →, Style=Secondary, Size=Small, State=Rest, Text=True; Device=iPhone, Shape=Circle →, Style=Danger, Size=Small, State=Rest, Text=True; Device=iPhone, Shape=Circle →, Style=Primary, Size=Small, State=Rest, Text=True |
| `145.0×32.0` | 5 | Device=iPad, Shape=Rectangle, Style=Secondary, Size=ExtraSmall, State=Rest, Text=True; Device=iPad, Shape=Rectangle, Style=Secondary, Size=ExtraSmall, State=Loading, Text=True; Device=iPad, Shape=Rectangle, Style=Secondary, Size=ExtraSmall, State=Progress, Text=True |
| `151.0×36.0` | 24 | Device=iPhone, Shape=Rectangle, Style=Secondary, Size=Small, State=Rest, Text=True; Device=iPhone, Shape=Rectangle, Style=Danger, Size=Small, State=Rest, Text=True; Device=iPhone, Shape=Rectangle, Style=Secondary, Size=Small, State=Loading, Text=True |
| `162.0×40.0` | 12 | Device=iPad, Shape=Circle →, Style=Secondary, Size=Small, State=Rest, Text=True; Device=iPad, Shape=Circle →, Style=Danger, Size=Small, State=Rest, Text=True; Device=iPad, Shape=Circle →, Style=Primary, Size=Small, State=Rest, Text=True |
| `169.0×48.0` | 12 | Device=iPhone, Shape=Circle →, Style=Secondary, Size=Default, State=Rest, Text=True; Device=iPhone, Shape=Circle →, Style=Danger, Size=Default, State=Rest, Text=True; Device=iPhone, Shape=Circle →, Style=Primary, Size=Default, State=Rest, Text=True |
| `176.0×40.0` | 24 | Device=iPad, Shape=Rectangle, Style=Secondary, Size=Small, State=Rest, Text=True; Device=iPad, Shape=Rectangle, Style=Danger, Size=Small, State=Rest, Text=True; Device=iPad, Shape=Rectangle, Style=Secondary, Size=Small, State=Loading, Text=True |
| `179.0×48.0` | 24 | Device=iPhone, Shape=Rectangle, Style=Primary, Size=Default, State=Rest, Text=True; Device=iPhone, Shape=Rectangle, Style=Sber, Size=Default, State=Rest, Text=True; Device=iPhone, Shape=Rectangle, Style=Primary, Size=Default, State=Loading, Text=True |
| `183.0×36.0` | 4 | Device=iPhone, Shape=Rectangle, Style=SberPay, Size=Small, State=Rest, Text=True; Device=iPhone, Shape=Rectangle, Style=SberPay, Size=Small, State=Loading, Text=True; Device=iPhone, Shape=Rectangle, Style=SberPay, Size=Small, State=Disabled, Text=True |
| `189.0×52.0` | 12 | Device=iPad, Shape=Circle →, Style=Secondary, Size=Default, State=Rest, Text=True; Device=iPad, Shape=Circle →, Style=Danger, Size=Default, State=Rest, Text=True; Device=iPad, Shape=Circle →, Style=Primary, Size=Default, State=Rest, Text=True |
| `201.0×52.0` | 24 | Device=iPad, Shape=Rectangle, Style=Secondary, Size=Default, State=Rest, Text=True; Device=iPad, Shape=Rectangle, Style=Danger, Size=Default, State=Rest, Text=True; Device=iPad, Shape=Rectangle, Style=Secondary, Size=Default, State=Loading, Text=True |
| `210.0×40.0` | 4 | Device=iPad, Shape=Rectangle, Style=SberPay, Size=Small, State=Rest, Text=True; Device=iPad, Shape=Rectangle, Style=SberPay, Size=Small, State=Loading, Text=True; Device=iPad, Shape=Rectangle, Style=SberPay, Size=Small, State=Disabled, Text=True |
| `218.0×48.0` | 4 | Device=iPhone, Shape=Rectangle, Style=SberPay, Size=Default, State=Rest, Text=True; Device=iPhone, Shape=Rectangle, Style=SberPay, Size=Default, State=Loading, Text=True; Device=iPhone, Shape=Rectangle, Style=SberPay, Size=Default, State=Disabled, Text=True |
| `243.0×52.0` | 4 | Device=iPad, Shape=Rectangle, Style=SberPay, Size=Default, State=Rest, Text=True; Device=iPad, Shape=Rectangle, Style=SberPay, Size=Default, State=Loading, Text=True; Device=iPad, Shape=Rectangle, Style=SberPay, Size=Default, State=Disabled, Text=True |

### Состояния

- `State`: Disabled / Loading / Progress / Rest / Touch

### Зависимости

В Figma-ответе внешние component dependencies не найдены.

### Источник

- [Button](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=31182-4417&t=6NQra4uE9oLKkthr-4) — fileKey `rMcDm5qGp4CXkXXddEbcMh`, API key `rMcDm5qGp4CXkXXddEbcMh`, node `31182:4417`, type `COMPONENT_SET`.
- [Component guide_Button](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=31214-29705) — `guide`, node `31214:29705`.
<!-- FIGMA_SYNC:END -->
