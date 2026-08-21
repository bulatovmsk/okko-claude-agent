# Onboarding Bubble

## Назначение

Короткая контекстная подсказка онбординга, визуально привязанная указателем
(`Beak`) к элементу интерфейса. Содержит основной и опциональный дополнительный
текст.

## Когда использовать

- Чтобы впервые объяснить новую или неочевидную функцию рядом с её элементом.
- Для короткого пояснения, которое можно понять без перехода на отдельный экран.
- Когда направление указателя позволяет однозначно связать подсказку с целью.

### Направление указателя

- `Left` — цель слева от bubble.
- `Right` — цель справа.
- `Top` — цель над bubble.
- `Bottom` — цель под bubble.

## Когда НЕ использовать

- Для постоянной инструкции или обязательного текста — размещать пояснение прямо
  в интерфейсе.
- Для ошибки, предупреждения или подтверждения действия.
- Для длинного многошагового обучения с изображениями и действиями: компонент
  не содержит кнопок, счётчика шагов или встроенного закрытия.
- Не показывать несколько bubble одновременно и не перекрывать ими целевой элемент.

## Платформенные особенности iOS

| Device | Размер |
|---|---:|
| `iPhone` | 158×56 |
| `iPad` | 185×68 |

- `Secondary Text` управляет видимостью дополнительной строки.
- Тексты задаются свойствами `String / Primary Text` и
  `String / Secondary Text`.
- `Text Alignment=Centre` опубликован только для `Beak=Top` и `Beak=Bottom`.
  Для `Left` и `Right` использовать только `Text Alignment=Left`.
- В COMPONENT_SET нет состояний появления, закрытия или прогресса. Правила
  показа, повторного показа и dismiss определяются продуктовым сценарием.
- Для VoiceOver связывать подсказку с целевым элементом и озвучивать текст при
  появлении; смысл не должен зависеть только от направления указателя.

## Связанные компоненты

- Живая нода не содержит внешних component dependencies.
- Целевой элемент не входит в компонент: bubble позиционируется относительно
  него на уровне экрана или onboarding-сценария.

<!-- FIGMA_SYNC:START -->
## Актуальные данные Figma

> Последняя проверка: `2026-08-21T15:46:56Z` · структура `a0c02430ac12` · статус `unknown`.

### Свойства из компонента

| Свойство | Тип | Значение по умолчанию | Варианты |
|---|---|---|---|
| `Beak` | `variant` | `—` | Bottom / Left / Right / Top |
| `Device` | `variant` | `—` | iPad / iPhone |
| `Secondary Text` | `boolean` | `—` | — |
| `String / Primary Text` | `text` | `—` | — |
| `String / Secondary Text` | `text` | `—` | — |
| `Text Alignment` | `variant` | `—` | Centre / Left |

### Варианты и размеры

| Ось | Значения |
|---|---|
| `Beak` | Bottom / Left / Right / Top |
| `Device` | iPad / iPhone |
| `Text Alignment` | Centre / Left |

Комбинаций в COMPONENT_SET: **12**.

| Размер | Количество вариантов | Примеры |
|---|---:|---|
| `158.0×56.0` | 6 | Device=iPhone, Beak=Left, Text Alignment=Left; Device=iPhone, Beak=Bottom, Text Alignment=Left; Device=iPhone, Beak=Bottom, Text Alignment=Centre |
| `185.0×68.0` | 6 | Device=iPad, Beak=Left, Text Alignment=Left; Device=iPad, Beak=Bottom, Text Alignment=Left; Device=iPad, Beak=Bottom, Text Alignment=Centre |

### Зависимости

В Figma-ответе внешние component dependencies не найдены.

### Источник

- [Onboarding Bubble](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=32634-7164&t=6NQra4uE9oLKkthr-4) — fileKey `rMcDm5qGp4CXkXXddEbcMh`, API key `rMcDm5qGp4CXkXXddEbcMh`, node `32634:7164`, type `COMPONENT_SET`.
<!-- FIGMA_SYNC:END -->
