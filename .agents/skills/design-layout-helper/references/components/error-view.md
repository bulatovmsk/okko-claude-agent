# Error - View

## Назначение

Составное представление ошибки для ситуации, когда основной контент экрана
нельзя показать. Объясняет проблему, предлагает восстановительное действие и
при необходимости даёт данные для обращения в поддержку.

## Когда использовать

- Для блокирующей ошибки загрузки или выполнения сценария, которая заменяет
  основное содержимое области или экрана.
- Когда пользователю нужны заголовок, пояснение и одно или два действия:
  повторить, вернуться или выбрать альтернативный путь.
- Когда вместе с ошибкой нужно показать код, Session ID, Trace ID и действие
  обращения в поддержку.

### Управляемое содержимое

- `Image`, `Heading`, `Body text`, `Caption`, `Timer` — видимость отдельных блоков.
- `↳ Heading Content`, `↳ Body Content`, `↳ Caption Content`, `↳ Timer Content` —
  текст соответствующих блоков.
- `Button Box` — видимость зоны действий.
- `↳ Secondary Btn` — видимость второй кнопки.

## Когда НЕ использовать

- Для ошибки конкретного поля формы — показывать локальную ошибку рядом с полем.
- Для краткого неблокирующего сообщения — использовать компактное уведомление,
  а не заменять им содержимое экрана.
- Для штатного отсутствия данных — использовать Empty State, если он
  предусмотрен библиотекой.
- Не показывать технические идентификаторы без понятного пользовательского
  объяснения и доступного следующего шага.

## Платформенные особенности iOS

| Device | Размер варианта | Компоновка |
|---|---:|---|
| `iPhone` | 375×543.5 | вертикальная, кнопки друг под другом |
| `iPad Portrait` | 452×616 | вертикальная, действия рядом |
| `iPad Landscape` | 747×380 | текст и действия слева, изображение справа |

- Единственное опубликованное значение `Orientation` — `Vertical`; ориентацию
  устройства задаёт `Device`, включая `iPad Landscape`.
- `Image Placeholder` использует пропорции 2:1 или 3:4 в зависимости от варианта.
- Основное и вторичное действия собираются компонентом [Button](button.md).
- Для VoiceOver сохранять порядок: заголовок, описание, дополнительные данные,
  действия и блок поддержки. Кнопка копирования должна иметь осмысленное имя.
- Таймер не должен создавать чрезмерно частые объявления; важное изменение
  состояния сообщать отдельно.

## Связанные компоненты

- [Error - Fulscreen](error-fullscreen.md) — полноэкранная device-сборка с навигацией.
- [Error - Sheet](error-sheet.md) — Error View внутри нативной модальной шторки.
- [Button](button.md) — основное и вторичное восстановительные действия.
- `Image Placeholder` — слот иллюстрации ошибки.
- `_Error - Support Widget` — обращение в поддержку и технические идентификаторы.
- `Actions / Copy_Bold` — действие копирования данных ошибки.
- `Mark / Star_Bold`, `_compensation` — внутренние зависимости Button.

<!-- FIGMA_SYNC:START -->
## Актуальные данные Figma

> Последняя проверка: `2026-08-21T15:38:37Z` · структура `6e094f021dc0` · статус `unknown`.

### Свойства из компонента

| Свойство | Тип | Значение по умолчанию | Варианты |
|---|---|---|---|
| `Body text` | `boolean` | `—` | — |
| `Button Box` | `boolean` | `—` | — |
| `Caption` | `boolean` | `—` | — |
| `Device` | `variant` | `—` | iPad Landscape / iPad Portrait / iPhone |
| `Heading` | `boolean` | `—` | — |
| `Image` | `boolean` | `—` | — |
| `Orientation` | `variant` | `—` | Vertical |
| `Timer` | `boolean` | `—` | — |
| `↳ Body Content` | `text` | `—` | — |
| `↳ Caption Content` | `text` | `—` | — |
| `↳ Heading Content` | `text` | `—` | — |
| `↳ Secondary Btn` | `boolean` | `—` | — |
| `↳ Timer Content` | `text` | `—` | — |

### Варианты и размеры

| Ось | Значения |
|---|---|
| `Device` | iPad Landscape / iPad Portrait / iPhone |
| `Orientation` | Vertical |

Комбинаций в COMPONENT_SET: **3**.

| Размер | Количество вариантов | Примеры |
|---|---:|---|
| `375.0×543.5` | 1 | Device=iPhone, Orientation=Vertical |
| `452.0×616.0` | 1 | Device=iPad Portrait, Orientation=Vertical |
| `747.0×380.0` | 1 | Device=iPad Landscape, Orientation=Vertical |

### Зависимости

- `_compensation` — node `dependency:compensation`
- `_Error - Support Widget` — node `dependency:support-widget`
- `Actions / Copy_Bold` — node `dependency:copy`
- `Button` — node `dependency:button`
- `Image Placeholder` — node `dependency:image-placeholder`
- `Mark / Star_Bold` — node `dependency:star`

### Источник

- [Error - View](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=22536-7360&t=6NQra4uE9oLKkthr-4) — fileKey `rMcDm5qGp4CXkXXddEbcMh`, API key `rMcDm5qGp4CXkXXddEbcMh`, node `22536:7360`, type `COMPONENT_SET`.
<!-- FIGMA_SYNC:END -->
