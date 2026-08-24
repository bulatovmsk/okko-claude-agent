# Featured - Meta

## Назначение

Крупный featured-блок для акцентного контента. Объединяет фоновое
изображение или трейлер, бейджи, метаданные, постраничную индикацию
и опциональную offer-кнопку. Поддерживает кино, медиа, события, музыку,
спортивные программы и команды в одном адаптивном шаблоне.

## Когда использовать

- Для главного акцента экрана или карусели, где один объект контента
  должен получить высокий визуальный приоритет.
- Выбирайте `Content` по типу сущности, а `Device` — по ориентации и классу
  устройства.
- Включайте `Offer Button` только когда у featured-объекта есть отдельное
  целевое действие.

## Когда НЕ использовать

- Для повторяющегося ряда карточек используйте подходящий шаблон из
  [семейства Rail](rail-family.md), а не Featured - Meta.
- Не используйте `Trailer=True` для `Media`, `Event` и `Music`: таких
  комбинаций в мастере нет.
- Не собирайте блок вручную из `_Fade` и `_PageIndicator Item`: это
  внутренние запчасти.

## Платформенные особенности iOS

- Доступны три раскладки: `iPhone` — `440×478`, `iPad Portrait` —
  `1031×585`, `iPad Landscape` — `1130×400`.
- Матрица вариантов неполная: `Trailer=True` есть только у `Movie`,
  `Sport Program` и `Sport Teams`; `Trailer=False` есть у всех шести типов
  контента. Всего 27 комбинаций, а не 36.
- При автовоспроизведении трейлера сохраняйте доступное управление
  звуком через `Sound off` и не стартуйте звук без действия пользователя.
- Для VoiceOver объединяйте название, бейджи и ключевые метаданны в
  осмысленное описание; декоративный фон отдельно не озвучивайте.
- Значения визуальных токенов проверяются отдельно в Tokens Studio source of truth.

## Связанные компоненты

- [Button](button.md) — вложенное целевое действие, управляемое `Offer Button`.
- [Label : Large](label-large.md), `Label Rich` и `Labels / Broadcast_Bold` — текстовые
  и эфирные метки.
- `Meta`, `PageIndicator`, `Sound off` и `Spasibo Badge` — публичные зависимости,
  пока не зарегистрированные как отдельные рабочие карточки.
- `_Fade` и `_PageIndicator Item` — внутренние запчасти; отдельно в память не
  добавляются.

<!-- FIGMA_SYNC:START -->
## Актуальные данные Figma

> Последняя проверка: `2026-08-24T08:27:22Z` · структура `3b22c4255321` · статус `ready` · публикация Figma `CURRENT`.

### Свойства из компонента

| Свойство | Тип | Значение по умолчанию | Варианты |
|---|---|---|---|
| `Content` | `variant` | `Movie` | Event / Media / Movie / Music / Sport Program / Sport Teams |
| `Device` | `variant` | `iPhone` | iPad Landscape / iPad Portrait / iPhone |
| `Offer Button` | `boolean` | `false` | — |
| `Trailer` | `variant` | `True` | False / True |

### Варианты и размеры

| Ось | Значения |
|---|---|
| `Content` | Event / Media / Movie / Music / Sport Program / Sport Teams |
| `Device` | iPad Landscape / iPad Portrait / iPhone |
| `Trailer` | False / True |

Комбинаций в COMPONENT_SET: **27**.

| Размер | Количество вариантов | Примеры |
|---|---:|---|
| `440.0×478.0` | 9 | Device=iPhone, Content=Movie, Trailer=True; Device=iPhone, Content=Movie, Trailer=False; Device=iPhone, Content=Media, Trailer=False |
| `1031.0×585.0` | 9 | Device=iPad Portrait, Content=Movie, Trailer=True; Device=iPad Portrait, Content=Movie, Trailer=False; Device=iPad Portrait, Content=Media, Trailer=False |
| `1130.0×400.0` | 9 | Device=iPad Landscape, Content=Movie, Trailer=True; Device=iPad Landscape, Content=Movie, Trailer=False; Device=iPad Landscape, Content=Media, Trailer=False |

### Зависимости

- `_Fade` — node `40337:52769`
- `_PageIndicator Item` — node `30525:4`
- `Button` — node `31182:4417`
- `Label : Large` — node `12185:97166`
- `Label Rich` — node `19510:17417`
- `Labels / Broadcast_Bold` — node `39522:39358`
- `Meta` — node `40306:75165`
- `PageIndicator` — node `30525:8`
- `Sound off` — node `39215:62603`
- `Spasibo Badge` — node `39215:69835`

### Источник

- [Featured - Meta](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=40306-47681&t=6NQra4uE9oLKkthr-4) — fileKey `rMcDm5qGp4CXkXXddEbcMh`, API key `rMcDm5qGp4CXkXXddEbcMh`, node `40306:47681`, type `COMPONENT_SET`.
<!-- FIGMA_SYNC:END -->
