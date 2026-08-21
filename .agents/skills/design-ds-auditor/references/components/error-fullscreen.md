# Error - Fulscreen

## Назначение

Готовая полноэкранная сборка блокирующей ошибки внутри основного app shell:
системные области, верхняя навигация, [Error - View](error-view.md) и нижняя
навигация адаптированы под конкретные размеры iPhone и iPad.

> В Figma исходное имя содержит опечатку: `Error - Fulscreen`. Устойчивый slug
> карточки — `error-fullscreen`, чтобы компонент находился по слову fullscreen.

## Когда использовать

- Когда ошибка блокирует основной контент экрана, но пользователь должен видеть
  и сохранять доступ к основному app shell.
- Для готового device-пресета с Navbar, Tabbar и safe-area элементами.
- Когда требуется единая полноэкранная адаптация Error View для поддерживаемых
  размеров iPhone и iPad.

## Когда НЕ использовать

- Для переиспользуемого содержимого ошибки без оболочки — использовать
  [Error - View](error-view.md).
- Для ошибки поверх текущего контекста — использовать [Error - Sheet](error-sheet.md).
- Для локальной ошибки поля, блока или короткого неблокирующего уведомления.
- Не растягивать ближайший пресет на произвольный viewport без проверки
  responsive-поведения и safe area.

## Платформенные особенности iOS

| Device | Размер |
|---|---:|
| `iPhone 15` | 393×852 |
| `iPhone 17 Pro Max` | 440×956 |
| `iPad 10 Portrait` | 820×1180 |
| `iPad 10 Landscape` | 1180×820 |
| `iPad Pro 13 Portrait` | 1032×1376 |
| `iPad Pro 13 Landscape` | 1376×1032 |

- Верхний COMPONENT_SET публикует только `Device`. Управление изображением,
  текстами, кнопками и support widget находится во вложенном Error View.
- На iPhone действия расположены столбцом, на iPad — рядом.
- В landscape Error View использует горизонтальную композицию: основной текст и
  действия находятся отдельно от изображения.
- `Navbar`, `Status Bar`, `Tabbar - Main` и `Home Indicator` являются частью
  полноэкранной сборки, а не содержимого Error View.
- При появлении ошибки переводить VoiceOver к заголовку ошибки, сохраняя доступ
  к восстановительным действиям и навигации выхода из проблемного раздела.

## Связанные компоненты

- [Error - View](error-view.md) — содержимое полноэкранной ошибки.
- [Error - Sheet](error-sheet.md) — модальная ошибка поверх текущего контекста.
- [Navbar](navbar.md), `Status Bar` — верхняя оболочка экрана.
- `Tabbar - Main`, `Home Indicator` — нижняя навигация и системная область.
- [Button](button.md), `Image Placeholder`, `_Error - Support Widget` —
  транзитивные зависимости Error View.
- `_Avatar`, `Profile logo`, `Sber / Mini Spasibo` — зависимости Navbar.
- `_Tabbar Item` и иконки `Menu / …` — зависимости Tabbar.

<!-- FIGMA_SYNC:START -->
## Актуальные данные Figma

> Последняя проверка: `2026-08-21T15:44:33Z` · структура `82634fbfb4e0` · статус `unknown`.

### Свойства из компонента

| Свойство | Тип | Значение по умолчанию | Варианты |
|---|---|---|---|
| `Device` | `variant` | `—` | iPad 10 Landscape / iPad 10 Portrait / iPad Pro 13 Landscape / iPad Pro 13 Portrait / iPhone 15 / iPhone 17 Pro Max |

### Варианты и размеры

| Ось | Значения |
|---|---|
| `Device` | iPad 10 Landscape / iPad 10 Portrait / iPad Pro 13 Landscape / iPad Pro 13 Portrait / iPhone 15 / iPhone 17 Pro Max |

Комбинаций в COMPONENT_SET: **6**.

| Размер | Количество вариантов | Примеры |
|---|---:|---|
| `393.0×852.0` | 1 | Device=iPhone 15 |
| `440.0×956.0` | 1 | Device=iPhone 17 Pro Max |
| `820.0×1180.0` | 1 | Device=iPad 10 Portrait |
| `1032.0×1376.0` | 1 | Device=iPad Pro 13 Portrait |
| `1180.0×820.0` | 1 | Device=iPad 10 Landscape |
| `1376.0×1032.0` | 1 | Device=iPad Pro 13 Landscape |

### Зависимости

- `_Avatar` — node `dependency:avatar`
- `_compensation` — node `dependency:compensation`
- `_Error - Support Widget` — node `dependency:support-widget`
- `_Materials/Mode Options` — node `dependency:mode-options`
- `_Tabbar Item` — node `dependency:tabbar-item`
- `Actions / Copy_Bold` — node `dependency:copy`
- `Button` — node `dependency:button`
- `Error - View` — node `dependency:error-view`
- `Home Indicator` — node `dependency:home-indicator`
- `Image Placeholder` — node `dependency:image-placeholder`
- `Mark / Star_Bold` — node `dependency:star`
- `Menu / Ball` — node `dependency:ball`
- `Menu / Ball_Solid` — node `dependency:ball-solid`
- `Menu / Bookmark` — node `dependency:bookmark`
- `Menu / Bookmark_Solid` — node `dependency:bookmark-solid`
- `Menu / House_Solid` — node `dependency:house-solid`
- `Menu / Magnifier` — node `dependency:magnifier`
- `Menu / Magnifier_Solid` — node `dependency:magnifier-solid`
- `Menu / TV_Old` — node `dependency:tv`
- `Menu / TV_Old_Solid` — node `dependency:tv-solid`
- `Navbar` — node `dependency:navbar`
- `Profile logo` — node `dependency:profile-logo`
- `Sber / Mini Spasibo` — node `dependency:sber-spasibo`
- `Status Bar` — node `dependency:status-bar`
- `Tabbar - Main` — node `dependency:tabbar`

### Источник

- [Error - Fulscreen](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=40967-4323&t=6NQra4uE9oLKkthr-4) — fileKey `rMcDm5qGp4CXkXXddEbcMh`, API key `rMcDm5qGp4CXkXXddEbcMh`, node `40967:4323`, type `COMPONENT_SET`.
<!-- FIGMA_SYNC:END -->
