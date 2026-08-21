# AI Button

## Назначение

Кнопка для вызова ИИ-ассистента.

## Когда использовать

- Для явного запуска или открытия ИИ-ассистента.
- Для действия, которое должно визуально отличаться от обычных продуктовых CTA
  и однозначно восприниматься как AI-функция.
- В компактном или стандартном размере в зависимости от плотности интерфейса.

## Когда НЕ использовать

- Для обычных действий, не связанных с ИИ, — использовать стандартный `Button`.
- Как декоративную плашку без действия: компонент визуально и семантически
  является кнопкой.
- Не оставлять демонстрационную подпись «Нажать кнопку» в продуктовом интерфейсе;
  текст должен называть конкретное действие ассистента.

## Платформенные особенности iOS

- `Device`: `iPhone` / `iPad`.
- `Size`: `Default` / `Small`.
- `State`: `Rest` / `Touch`.
- `Show icon`: показывает или скрывает фирменную AI-иконку.
- `Text`: задаёт подпись действия.

### Размеры

| Device | Default | Small |
|---|---:|---:|
| iPhone | 179×48 | 151×36 |
| iPad | 201×52 | 176×40 |

Внешний вид — тёмная кнопка с фиолетовым свечением/обводкой, белым текстом и
AI-иконкой слева. Ширина приведена для демонстрационной строки и меняется вместе
с текстом.

В опубликованном компоненте сейчас нет `Disabled` и `Loading`; не предполагать
их наличие при проектировании. Для VoiceOver подпись должна описывать действие,
а не повторять техническое название `AI Button`.

## Связанные компоненты

- `Objects / AI Kinobi` — встроенная фирменная иконка AI.
- `Button` — стандартные действия, не относящиеся к ИИ-ассистенту.

<!-- FIGMA_SYNC:START -->
## Актуальные данные Figma

> Последняя проверка: `2026-08-21T15:17:25Z` · структура `f35bec40e2bd` · статус `unknown`.

### Свойства из компонента

| Свойство | Тип | Значение по умолчанию | Варианты |
|---|---|---|---|
| `Device` | `variant` | `—` | iPad / iPhone |
| `Show icon` | `boolean` | `—` | — |
| `Size` | `variant` | `—` | Default / Small |
| `State` | `variant` | `—` | Rest / Touch |
| `Text` | `text` | `—` | — |

### Варианты и размеры

| Ось | Значения |
|---|---|
| `Device` | iPad / iPhone |
| `Size` | Default / Small |
| `State` | Rest / Touch |

Комбинаций в COMPONENT_SET: **8**.

| Размер | Количество вариантов | Примеры |
|---|---:|---|
| `151.0×36.0` | 2 | Device=iPhone, Size=Small, State=Rest; Device=iPhone, Size=Small, State=Touch |
| `176.0×40.0` | 2 | Device=iPad, Size=Small, State=Rest; Device=iPad, Size=Small, State=Touch |
| `179.0×48.0` | 2 | Device=iPhone, Size=Default, State=Rest; Device=iPhone, Size=Default, State=Touch |
| `201.0×52.0` | 2 | Device=iPad, Size=Default, State=Rest; Device=iPad, Size=Default, State=Touch |

### Состояния

- `State`: Rest / Touch

### Зависимости

В Figma-ответе внешние component dependencies не найдены.

### Источник

- [AI Button](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=30946-883&t=6NQra4uE9oLKkthr-4) — fileKey `rMcDm5qGp4CXkXXddEbcMh`, API key `rMcDm5qGp4CXkXXddEbcMh`, node `30946:883`, type `COMPONENT_SET`.
<!-- FIGMA_SYNC:END -->
