# iOS — платформенные правила

Контекст: нативное приложение для iPhone и iPad. SwiftUI / UIKit.

## Базовая сетка

- TODO: безопасные зоны (safe area top/bottom)
- TODO: margins по умолчанию для разных типов экранов
- TODO: правила для iPad (split view, multi-column)

## Типографика

- Системная гарнитура SF Pro по умолчанию (или кастомная — TODO)
- Динамический тип: TODO стратегия
- Шкала: см. `tokens/typography.md` → секция ios

## Hit-area

- **Минимум 44×44pt** (Apple HIG)
- При меньшем визуальном размере — расширять hit-target невидимо

## Жесты

- Swipe-back для возврата с детального экрана — обязателен
- Long-press для контекстных меню — где уместно
- Pull-to-refresh — на ленточных экранах
- Pinch-to-zoom — только в плеере и галереях

## Состояния

- Highlighted (нажатие) — обязательно для всех таппабельных элементов
- Disabled — opacity по токену `state.disabled.opacity`
- Selected — для табов, сегмент-контролов

## Тёмная тема

- Основной режим — тёмный
- Светлый режим: TODO поддерживается ли, и как переключается

## Доступность

- VoiceOver labels для всех интерактивных элементов
- Dynamic Type: TODO поддерживаемые размеры
- Контраст AA минимум

## Что НЕ типично для iOS

- Hamburger menu (≡) — использовать tab bar или sidebar для iPad
- Android-стиль FAB (Floating Action Button) — не использовать
- Material ripple — не использовать

## Тонкие моменты

- TODO: правила для iPad (когда дублируем iPhone, когда делаем split view)
- TODO: tvOS — это отдельная платформа, см. `tv.md`?
- TODO: haptics — где применяем
