# Android — платформенные правила

Контекст: нативное приложение для Android-смартфонов и планшетов. Compose / View system.

## Базовая сетка

- TODO: брейкпоинты (compact / medium / expanded)
- TODO: margins по умолчанию
- TODO: правила для планшетов и foldable

## Типографика

- Системная гарнитура Roboto / кастомная — TODO
- Шкала: см. `tokens/typography.md` → секция android
- Поддержка system font scaling: TODO

## Hit-area

- **Минимум 48×48dp** (Material Design)
- Touch slop: 8dp

## Жесты

- Back gesture (свайп от края) — поддерживать корректно
- Pull-to-refresh — где уместно
- Long-press для контекстных меню

## Состояния

- Ripple на нажатие — обязательно для material-like компонентов
- Disabled — opacity по токену `state.disabled.opacity`
- Selected — выделение через bg или underline

## Material Design

- TODO: какую версию Material используем (M2, M3)
- TODO: что берём из Material, а что переопределяем

## Тёмная тема

- Основной режим — тёмный
- Светлый: TODO

## Доступность

- TalkBack labels для всех интерактивных элементов
- Поддержка font scale 0.85x – 1.3x минимум
- Контраст AA минимум

## Что НЕ типично для Android

- iOS-стиль pill-buttons с тенью — заменить на material-варианты
- Tab bar внизу как на iOS — на Android либо bottom navigation (≤5 пунктов), либо navigation drawer

## Тонкие моменты

- TODO: edge-to-edge — используем ли
- TODO: predictive back animation на Android 14+
- TODO: foldable adaptive layout
