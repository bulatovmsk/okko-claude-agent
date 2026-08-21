# Label : Small

## Назначение

Малая компактная метка для категории, статуса или короткого продуктового
признака в плотной композиции. Содержит текст и опциональный сменный
логотип/значок, сохраняя те же темы, что и крупная метка.

## Когда использовать

- В строках метаданных, плотных списках и небольших карточках, где крупная
  метка занимает слишком много места.
- Текст задаётся свойством `text -->`; сохраняйте точное имя свойства Figma.
- `Icon` включает значок, `Icon Instance` позволяет его заменить.
- Используйте одно из опубликованных значений `theme`: `Lighthouse`,
  `Continuum`, `Red`, `Neutral`, `Black`, `Positive`, `Lemon`, `Offer`,
  `Outline`, `SberSpasibo`.
- `device=phone` используйте на iPhone, `device=tablet` — на iPad.

## Когда НЕ использовать

- Когда метка должна быть заметнее или находится на крупной поверхности,
  используйте [Label : Large](label-large.md).
- Не используйте Label как самостоятельную кнопку или переключатель: в наборе
  нет состояний нажатия, выбора или фокуса.
- Не добавляйте неподтверждённые темы и не копируйте значения цветов из Figma;
  source of truth для токенов — Tokens Studio.
- Не полагайтесь только на цвет: текст должен передавать смысл темы.

## Платформенные особенности iOS

- Большинство тем имеют размер 37×14 pt на `phone` и 42×16 pt на `tablet`.
- `SberSpasibo` шире: 49×14 pt на `phone` и 57×16 pt на `tablet`.
- Всего опубликовано 20 вариантов: десять тем для каждого устройства.
- Компонент меньше минимальной touch target iOS и должен оставаться
  неинтерактивным либо входить в большую интерактивную область родителя.
- VoiceOver должен читать содержимое как текст. Декоративный значок скрывайте
  от отдельного озвучивания, если его смысл уже передан текстом.

## Связанные компоненты

- [Label : Large](label-large.md) — более заметный размер семейства.
- [Tabgroup - Item](tabgroup-item.md) — может показывать малую метку над
  текстовой вкладкой через свойство `Label`.
- `Logotypes / Live` — базовый сменный значок.
- `Logotypes / Sber_Spasibo` — логотип темы `SberSpasibo`.

<!-- FIGMA_SYNC:START -->
## Актуальные данные Figma

> Последняя проверка: `2026-08-21T16:01:52Z` · структура `8d78b6794c91` · статус `unknown`.

### Свойства из компонента

| Свойство | Тип | Значение по умолчанию | Варианты |
|---|---|---|---|
| `device` | `variant` | `—` | phone / tablet |
| `Icon` | `boolean` | `—` | — |
| `Icon Instance` | `instance_swap` | `—` | — |
| `text -->` | `text` | `—` | — |
| `theme` | `variant` | `—` | Black / Continuum / Lemon / Lighthouse / Neutral / Offer / Outline / Positive / Red / SberSpasibo |

### Варианты и размеры

| Ось | Значения |
|---|---|
| `device` | phone / tablet |
| `theme` | Black / Continuum / Lemon / Lighthouse / Neutral / Offer / Outline / Positive / Red / SberSpasibo |

Комбинаций в COMPONENT_SET: **20**.

| Размер | Количество вариантов | Примеры |
|---|---:|---|
| `37.0×14.0` | 9 | device=phone, theme=Lighthouse; device=phone, theme=Continuum; device=phone, theme=Red |
| `42.0×16.0` | 9 | device=tablet, theme=Lighthouse; device=tablet, theme=Continuum; device=tablet, theme=Red |
| `49.0×14.0` | 1 | device=phone, theme=SberSpasibo |
| `57.0×16.0` | 1 | device=tablet, theme=SberSpasibo |

### Зависимости

- `Logotypes / Live` — node `dependency:logotypes-live`
- `Logotypes / Sber_Spasibo` — node `dependency:logotypes-sber-spasibo`

### Источник

- [Label : Small](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=12185-97090&t=6NQra4uE9oLKkthr-4) — fileKey `rMcDm5qGp4CXkXXddEbcMh`, API key `rMcDm5qGp4CXkXXddEbcMh`, node `12185:97090`, type `COMPONENT_SET`.
<!-- FIGMA_SYNC:END -->
