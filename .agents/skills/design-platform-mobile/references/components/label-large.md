# Label : Large

## Назначение

Крупная компактная метка для категории, статуса или короткого продуктового
признака. Содержит текст и опциональный сменный логотип/значок; визуальная тема
задаёт характер акцента без изменения структуры компонента.

## Когда использовать

- Когда метке нужен более заметный размер: на карточке, обложке или рядом с
  важным названием.
- Текст задаётся свойством `text -->`; сохраняйте это точное имя при работе с
  экземпляром Figma.
- `Icon` включает значок, `Icon Instance` заменяет его. Базовая зависимость —
  `Logotypes / Live`; тема `SberSpasibo` использует партнёрский логотип.
- Выбирайте только опубликованные значения `theme`: `Lighthouse`, `Continuum`,
  `Red`, `Neutral`, `Black`, `Positive`, `Lemon`, `Offer`, `Outline`,
  `SberSpasibo`.
- `device=phone` используйте на iPhone, `device=tablet` — на iPad.

## Когда НЕ использовать

- В плотных строках и рядом с большим количеством метаданных используйте
  [Label : Small](label-small.md).
- Не используйте Label как кнопку: у компонента нет интерактивных состояний и
  гарантированной hit-area.
- Не создавайте произвольную цветовую тему или размер вне опубликованной
  матрицы. Актуальные значения токенов проверяйте отдельно в Tokens Studio.
- Не передавайте смысл только цветом или логотипом — короткий текст должен
  оставаться понятным сам по себе.

## Платформенные особенности iOS

- Большинство тем имеют размер 49×20 pt на `phone` и 59×24 pt на `tablet`.
- `SberSpasibo` шире из-за логотипа: 66×20 pt на `phone` и 80×24 pt на
  `tablet`.
- Всего опубликовано 20 вариантов: десять тем для каждого из двух устройств.
- Держите текст коротким: ширина компонента зависит от содержимого, но живые
  размеры подтверждены на строке `LABEL`.
- Если метка неинтерактивна, VoiceOver должен читать её как обычный текст;
  декоративный значок не должен дублировать произносимое название.
- Для интерактивного родительского элемента accessibility label должен
  объединять содержание метки с назначением этого элемента.

## Связанные компоненты

- [Label : Small](label-small.md) — компактный размер того же семейства.
- `Logotypes / Live` — базовый сменный значок.
- `Logotypes / Sber_Spasibo` — логотип темы `SberSpasibo`.

<!-- FIGMA_SYNC:START -->
## Актуальные данные Figma

> Последняя проверка: `2026-08-21T16:01:51Z` · структура `de13e1902456` · статус `unknown`.

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
| `49.0×20.0` | 9 | device=phone, theme=Lighthouse; device=phone, theme=Continuum; device=phone, theme=Red |
| `59.0×24.0` | 9 | device=tablet, theme=Lighthouse; device=tablet, theme=Continuum; device=tablet, theme=Red |
| `66.0×20.0` | 1 | device=phone, theme=SberSpasibo |
| `80.0×24.0` | 1 | device=tablet, theme=SberSpasibo |

### Зависимости

- `Logotypes / Live` — node `dependency:logotypes-live`
- `Logotypes / Sber_Spasibo` — node `dependency:logotypes-sber-spasibo`

### Источник

- [Label : Large](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=12185-97166&t=6NQra4uE9oLKkthr-4) — fileKey `rMcDm5qGp4CXkXXddEbcMh`, API key `rMcDm5qGp4CXkXXddEbcMh`, node `12185:97166`, type `COMPONENT_SET`.
<!-- FIGMA_SYNC:END -->
