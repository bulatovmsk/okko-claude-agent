# Bet Button

## Назначение

Партнёрская кнопка букмекера для перехода к ставке или показа коэффициентов
в спортивном сценарии. Сохраняет фирменный логотип партнёра и специальную
структуру betting-данных.

## Когда использовать

- В одобренной интеграции с партнёром-букмекером.
- Для CTA с логотипом партнёра и текстом действия — `Type=Icon+Text`.
- Для строки коэффициентов исходов — `Type=Odds`.
- Для компактного выбранного исхода с направлением изменения коэффициента —
  `Type=Odds(Alt)`.

### Типы

| Type | Содержимое |
|---|---|
| `Icon+Text` | мини-логотип букмекера и текст действия |
| `Odds` | мини-логотип и набор исходов с коэффициентами |
| `Odds(Alt)` | обозначение исхода, индикатор направления и коэффициент |

## Когда НЕ использовать

- Для обычного действия без betting-контекста — использовать [Button](button.md).
- Для самостоятельного логотипа партнёра без действия или коэффициентов.
- Не заменять `Odds` произвольной строкой: структура исходов и коэффициентов
  является частью компонента.
- Не использовать вне согласованного партнёрского сценария.

## Платформенные особенности iOS

| Size | Phone | Pad |
|---|---:|---:|
| `Small` | 36 | 40 |
| `Default` | 48 | 52 |

- В Figma названия платформенных вариантов — `Phone` и `Pad`.
- Ширина зависит от типа: `Odds` шире, чем `Icon+Text` и `Odds(Alt)`.
- В живом наборе нет отдельных осей состояния; не достраивать `Disabled`,
  `Loading` или `Touch` вручную без согласованного расширения компонента.
- Для VoiceOver формировать осмысленное имя из партнёра, действия или исхода и
  коэффициента; не полагаться только на логотип или стрелку направления.

## Связанные компоненты

- [Button](button.md) — обычное действие без партнёрских betting-данных.
- `Bet Logo(Mini)` — мини-логотип партнёра; в живом контексте опубликован
  `Partner=Placeholder`.
- `.BetArrow` — индикатор направления в `Odds(Alt)`; в живом контексте найден
  `Status=Positive`.

<!-- FIGMA_SYNC:START -->
## Актуальные данные Figma

> Последняя проверка: `2026-08-21T15:30:16Z` · структура `ad45c60e25cc` · статус `unknown`.

### Свойства из компонента

| Свойство | Тип | Значение по умолчанию | Варианты |
|---|---|---|---|
| `Device` | `variant` | `—` | Pad / Phone |
| `Size` | `variant` | `—` | Default / Small |
| `Type` | `variant` | `—` | Icon+Text / Odds / Odds(Alt) |

### Варианты и размеры

| Ось | Значения |
|---|---|
| `Device` | Pad / Phone |
| `Size` | Default / Small |
| `Type` | Icon+Text / Odds / Odds(Alt) |

Комбинаций в COMPONENT_SET: **12**.

| Размер | Количество вариантов | Примеры |
|---|---:|---|
| `147.0×36.0` | 1 | Device=Phone, Type=Odds(Alt), Size=Small |
| `151.0×40.0` | 1 | Device=Pad, Type=Odds(Alt), Size=Small |
| `153.0×36.0` | 1 | Device=Phone, Type=Icon+Text, Size=Small |
| `174.0×40.0` | 1 | Device=Pad, Type=Icon+Text, Size=Small |
| `175.0×48.0` | 1 | Device=Phone, Type=Odds(Alt), Size=Default |
| `177.0×52.0` | 1 | Device=Pad, Type=Odds(Alt), Size=Default |
| `181.0×48.0` | 1 | Device=Phone, Type=Icon+Text, Size=Default |
| `193.0×36.0` | 1 | Device=Phone, Type=Odds, Size=Small |
| `201.0×52.0` | 1 | Device=Pad, Type=Icon+Text, Size=Default |
| `214.0×40.0` | 1 | Device=Pad, Type=Odds, Size=Small |
| `226.0×48.0` | 1 | Device=Phone, Type=Odds, Size=Default |
| `248.0×52.0` | 1 | Device=Pad, Type=Odds, Size=Default |

### Зависимости

- `.BetArrow` — node `dependency:bet-arrow`
- `Bet Logo(Mini)` — node `dependency:bet-logo`

### Источник

- [Bet Button](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=22908-9507&t=6NQra4uE9oLKkthr-4) — fileKey `rMcDm5qGp4CXkXXddEbcMh`, API key `rMcDm5qGp4CXkXXddEbcMh`, node `22908:9507`, type `COMPONENT_SET`.
<!-- FIGMA_SYNC:END -->
