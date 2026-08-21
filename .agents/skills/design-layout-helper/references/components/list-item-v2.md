# 🟡 List Item V2

## Назначение

Универсальная строка списка iOS с заголовком, опциональной подписью, ведущей
иконкой и правой зоной. Поддерживает действие, выбор, статическую информацию,
переключатель и сохранённую платёжную карту. В Figma набор помечен `🟡`, поэтому
его текущий статус — `work-in-progress`.

## Когда использовать

- `Variant=🔴Action` — строка, запускающая действие или переход; правую часть
  можно собрать из текста, изображения и `Action Icon`.
- `Variant=🟢Select` — выбор элемента списка с опциональным `Select Icon`.
- `Variant=🔴Static` — информационная строка без состояния нажатия.
- `Variant=🔴Switch` — бинарная настройка со встроенным [Switch](switch.md).
- `Variant=🔴Pay Card` — сохранённый платёжный инструмент с номером карты,
  платёжной системой и опциональным логотипом Сбера.
- `Style=Ghost` используйте без фоновой поверхности, `Style=Filled` — для
  выделенной строки на собственной поверхности.
- `Type=Negative` предназначен для отрицательного действия и опубликован только
  в комбинации `Action + Filled`.
- `Title` задаёт основной текст; `Subtitle`, `Text Right`, `Icon`, `Image Right`,
  `Action Icon`, `Select Icon` и `Sber Logo` управляют дополнительными зонами.

## Когда НЕ использовать

- Для самостоятельного действия вне списка используйте [Button](button.md).
- Для отдельного бинарного контроля без строки используйте [Switch](switch.md).
- Для явного множественного или одиночного выбора вне паттерна строки используйте
  [Checkbox](checkbox.md) или [Radio button](radio-button.md).
- Не собирайте отсутствующие комбинации. `Loading` есть только у
  `Action + Filled + Neutral`; `Negative` — только у `Action + Filled`;
  `Static` не имеет `Touch`; `Filled` отсутствует у `Select`, `Static` и
  `Pay Card`.
- Не считайте красные/зелёные маркеры частью пользовательского текста: они
  входят в точные имена вариантов Figma и отражают внутреннюю маркировку набора.

## Платформенные особенности iOS

- Все 32 варианта iPhone имеют размер 344×52 pt; 32 варианта iPad —
  384×58 pt. Всего в наборе 64 комбинации.
- `Rest` — базовое состояние, `Touch` — кратковременная обратная связь на
  касание, `Disabled` — недоступность, `Loading` — выполнение действия,
  `Skeleton` — загрузка содержимого строки.
- Не используйте `Skeleton` как синоним `Disabled`: первое скрывает ещё не
  загруженный контент, второе сохраняет контент и запрещает взаимодействие.
- Для интерактивных вариантов вся строка должна иметь понятную touch area и
  VoiceOver label, собранный из заголовка, подписи и значения справа.
- В `Switch`-строке не создавайте два конкурирующих accessibility-действия,
  если нажатие по строке и по переключателю меняет одну настройку. Если действия
  различаются, разделите их семантически и явно озвучьте.
- Для `Select` передавайте выбранность через accessibility state, для
  `Negative` называйте конкретное последствие, а во время `Loading` блокируйте
  повторный запуск того же действия.
- Из-за статуса `work-in-progress` перед новым продуктовым применением нужно
  повторно проверить сохранённую Figma-ссылку и актуальность матрицы.

## Связанные компоненты

- [Switch](switch.md) — встроенный бинарный контроль варианта `🔴Switch`.
- [Button](button.md) — самостоятельная альтернатива для действия.
- [Checkbox](checkbox.md), [Radio button](radio-button.md) — альтернативные
  паттерны выбора.
- `Mark / Star`, `Profile logo`, `Arrows / Arrow_Right_Small_Bold` — ведущая
  и правая зоны обычных строк.
- `_Card`, `Logo / SberPay`, `Sber / Sber Pay` — сборка `🔴Pay Card`.
- `_itemList / loading gradient`, `_itemList / skeletonLoading` — состояния
  загрузки.
- `Notification / Check_Mark_Single_Bold` — индикатор выбора.

<!-- FIGMA_SYNC:START -->
## Актуальные данные Figma

> Последняя проверка: `2026-08-21T16:04:40Z` · структура `196efa8fa300` · статус `work-in-progress`.

### Свойства из компонента

| Свойство | Тип | Значение по умолчанию | Варианты |
|---|---|---|---|
| `Action Icon` | `boolean` | `—` | — |
| `Device` | `variant` | `—` | iPad / iPhone |
| `Icon` | `boolean` | `—` | — |
| `Image Right` | `boolean` | `—` | — |
| `Sber Logo` | `boolean` | `—` | — |
| `Select Icon` | `boolean` | `—` | — |
| `State` | `variant` | `—` | Disabled / Loading / Rest / Skeleton / Touch |
| `Style` | `variant` | `—` | Filled / Ghost |
| `Subtitle` | `boolean` | `—` | — |
| `Text Right` | `boolean` | `—` | — |
| `Title` | `text` | `—` | — |
| `Type` | `variant` | `—` | Negative / Neutral |
| `Variant` | `variant` | `—` | 🔴Action / 🔴Pay Card / 🔴Static / 🔴Switch / 🟢Select |
| `↳ Action Icon` | `instance_swap` | `—` | — |
| `↳ Card Number` | `text` | `—` | — |
| `↳ Icon` | `instance_swap` | `—` | — |
| `↳ Pay System` | `text` | `—` | — |
| `↳ Sber Logo` | `instance_swap` | `—` | — |
| `↳ Subtitle` | `text` | `—` | — |
| `↳ Text Right` | `text` | `—` | — |

### Варианты и размеры

| Ось | Значения |
|---|---|
| `Device` | iPad / iPhone |
| `State` | Disabled / Loading / Rest / Skeleton / Touch |
| `Style` | Filled / Ghost |
| `Type` | Negative / Neutral |
| `Variant` | 🔴Action / 🔴Pay Card / 🔴Static / 🔴Switch / 🟢Select |

Комбинаций в COMPONENT_SET: **64**.

| Размер | Количество вариантов | Примеры |
|---|---:|---|
| `344.0×52.0` | 32 | Device=iPhone, Variant=🔴Action, Style=Ghost, Type=Neutral, State=Rest; Device=iPhone, Variant=🔴Action, Style=Ghost, Type=Neutral, State=Touch; Device=iPhone, Variant=🔴Action, Style=Ghost, Type=Neutral, State=Disabled |
| `384.0×58.0` | 32 | Device=iPad, Variant=🔴Action, Style=Ghost, Type=Neutral, State=Rest; Device=iPad, Variant=🔴Action, Style=Ghost, Type=Neutral, State=Touch; Device=iPad, Variant=🔴Action, Style=Ghost, Type=Neutral, State=Disabled |

### Состояния

- `State`: Disabled / Loading / Rest / Skeleton / Touch

### Зависимости

- `_Card` — node `dependency:card`
- `_itemList / loading gradient` — node `dependency:list-loading-gradient`
- `_itemList / skeletonLoading` — node `dependency:list-skeleton-loading`
- `Arrows / Arrow_Right_Small_Bold` — node `dependency:arrow-right-small-bold`
- `Logo / SberPay` — node `dependency:logo-sberpay`
- `Mark / Star` — node `dependency:mark-star`
- `Notification / Check_Mark_Single_Bold` — node `dependency:check-mark-single-bold`
- `Profile logo` — node `dependency:profile-logo`
- `Sber / Sber Pay` — node `dependency:sber-pay`
- `Switch` — node `dependency:switch`

### Источник

- [🟡 List Item V2](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=36507-21672&t=6NQra4uE9oLKkthr-4) — fileKey `rMcDm5qGp4CXkXXddEbcMh`, API key `rMcDm5qGp4CXkXXddEbcMh`, node `36507:21672`, type `COMPONENT_SET`.
<!-- FIGMA_SYNC:END -->
