# Navbar

## Назначение

Верхняя навигационная оболочка экрана iOS. Показывает бренд Okko или Okko Kids,
заголовок раздела, состояние профиля или входа, кнопку возврата либо закрытия —
в зависимости от типа экрана. Компонент включает системную строку состояния и
имеет отдельные сборки для iPhone и iPad.

## Когда использовать

- `Type=Logo` — на верхнем уровне приложения с основным брендингом Okko.
- `Type=Logo Kids` — на верхнем уровне детского профиля.
- `Type=Title` — когда основным ориентиром экрана служит текстовый заголовок из
  свойства `Title`.
- `Type=Secondary screen` — на вложенном экране с возвратом назад.
- `Type=Content Card` — над карточкой контента или поверхностью, которую нужно
  закрыть.
- `Scrolled=False` — для развёрнутого состояния в начале прокрутки;
  `Scrolled=True` — для компактной закреплённой панели после прокрутки.

## Когда НЕ использовать

- Для переключения основных разделов снизу: используйте `Tabbar - Main`.
- В качестве заголовка нативной шторки: используйте заголовок
  [Bottom Sheet Native](bottom-sheet-native.md).
- Не собирайте произвольные комбинации свойств, которых нет среди 24
  опубликованных вариантов. В частности, `Unauthorized=True` доступен только
  для непрокрученных `Logo` и `Title` на обоих устройствах.

## Платформенные особенности iOS

- `Device=iPhone`: ширина эталонной сборки 393 pt; высота `Logo` — 160/98 pt,
  `Title` — 150/98 pt для развёрнутого/компактного состояния, `Content Card` —
  114 pt, `Secondary screen` — 98 pt.
- `Device=iPad`: ширина эталонной сборки 1024 pt; развёрнутые `Logo`,
  `Logo Kids` и `Title` — 120 pt; компактный `Logo` — 72 pt; компактные
  `Logo Kids` и `Title`, а также `Secondary screen` — 68 pt; `Content Card` —
  88 pt.
- Свойство `Statusbar` управляет присутствием `Status Bar`; не добавляйте
  системную строку поверх Navbar второй раз.
- `Unauthorized` меняет профильную область на сценарий входа. Авторизованное
  состояние собирается через `_Avatar`, `Profile logo` и при необходимости
  `Sber / Mini Spasibo`.
- Для VoiceOver сохраняйте логичный порядок: навигационное действие, заголовок
  или логотип, профильное действие. Кнопкам назад и закрытия нужны осмысленные
  accessibility labels, а заголовок должен сохранять семантику при сворачивании.

## Связанные компоненты

- [Tabbar - Meta](tabbar-meta.md) — нижняя навигация верхнего уровня.
- [Error - Fulscreen](error-fullscreen.md) — использует Navbar в верхней
  оболочке полноэкранной ошибки.
- [Button](button.md) — основа круглого действия в варианте `Content Card`.
- `Status Bar` — системная область сверху.
- `_Avatar`, `Menu / Avatar_Bold`, `Profile logo`, `Sber / Mini Spasibo` —
  профильная область и состояния авторизации.
- `Arrows / Arrow_Left` — возврат в `Secondary screen`.
- `Actions / Trash`, `Mark / Star_Bold` — действия, встречающиеся в живой
  структуре компонента.

<!-- FIGMA_SYNC:START -->
## Актуальные данные Figma

> Последняя проверка: `2026-08-21T15:50:49Z` · структура `b6d954947a45` · статус `unknown`.

### Свойства из компонента

| Свойство | Тип | Значение по умолчанию | Варианты |
|---|---|---|---|
| `Device` | `variant` | `—` | iPad / iPhone |
| `Scrolled` | `variant` | `—` | False / True |
| `Statusbar` | `boolean` | `—` | — |
| `Title` | `text` | `—` | — |
| `Type` | `variant` | `—` | Content Card / Logo / Logo Kids / Secondary screen / Title |
| `Unauthorized` | `variant` | `—` | False / True |

### Варианты и размеры

| Ось | Значения |
|---|---|
| `Device` | iPad / iPhone |
| `Scrolled` | False / True |
| `Type` | Content Card / Logo / Logo Kids / Secondary screen / Title |
| `Unauthorized` | False / True |

Комбинаций в COMPONENT_SET: **24**.

| Размер | Количество вариантов | Примеры |
|---|---:|---|
| `393.0×98.0` | 5 | Device=iPhone, Type=Logo, Scrolled=True, Unauthorized=False; Device=iPhone, Type=Logo Kids, Scrolled=True, Unauthorized=False; Device=iPhone, Type=Title, Scrolled=True, Unauthorized=False |
| `393.0×114.0` | 2 | Device=iPhone, Type=Content Card, Scrolled=False, Unauthorized=False; Device=iPhone, Type=Content Card, Scrolled=True, Unauthorized=False |
| `393.0×150.0` | 2 | Device=iPhone, Type=Title, Scrolled=False, Unauthorized=False; Device=iPhone, Type=Title, Scrolled=False, Unauthorized=True |
| `393.0×160.0` | 3 | Device=iPhone, Type=Logo, Scrolled=False, Unauthorized=False; Device=iPhone, Type=Logo, Scrolled=False, Unauthorized=True; Device=iPhone, Type=Logo Kids, Scrolled=False, Unauthorized=False |
| `1024.0×68.0` | 4 | Device=iPad, Type=Logo Kids, Scrolled=True, Unauthorized=False; Device=iPad, Type=Title, Scrolled=True, Unauthorized=False; Device=iPad, Type=Secondary screen, Scrolled=False, Unauthorized=False |
| `1024.0×72.0` | 1 | Device=iPad, Type=Logo, Scrolled=True, Unauthorized=False |
| `1024.0×88.0` | 2 | Device=iPad, Type=Content Card, Scrolled=False, Unauthorized=False; Device=iPad, Type=Content Card, Scrolled=True, Unauthorized=False |
| `1024.0×120.0` | 5 | Device=iPad, Type=Logo, Scrolled=False, Unauthorized=False; Device=iPad, Type=Logo, Scrolled=False, Unauthorized=True; Device=iPad, Type=Title, Scrolled=False, Unauthorized=False |

### Зависимости

- `_Avatar` — node `dependency:avatar`
- `Actions / Trash` — node `dependency:trash`
- `Arrows / Arrow_Left` — node `dependency:arrow-left`
- `Button` — node `dependency:button`
- `Mark / Star_Bold` — node `dependency:star`
- `Menu / Avatar_Bold` — node `dependency:avatar-icon`
- `Profile logo` — node `dependency:profile-logo`
- `Sber / Mini Spasibo` — node `dependency:sber-spasibo`
- `Status Bar` — node `dependency:status-bar`

### Источник

- [Navbar](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=12978-100799&t=6NQra4uE9oLKkthr-4) — fileKey `rMcDm5qGp4CXkXXddEbcMh`, API key `rMcDm5qGp4CXkXXddEbcMh`, node `12978:100799`, type `COMPONENT_SET`.
<!-- FIGMA_SYNC:END -->
