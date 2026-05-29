# Spacing — Tokens [tv]
> Источник: file **🦍 Tokens [tv]** (`Zn2JrOHhSURjCuUEp6JcI8`), страница **Spacing** — node `857:2088`. Токены — NUMBER variables Figma (REST не отдаёт значений, забираются через Plugin API).

Токены отступов для TV-интерфейса (Smart TV / Android TV, 1920×1080). Базовый модуль — 8px. Это **NUMBER variables** Figma.

## Токены

| Токен | Значение (px) | Модули (×8) |
|---|---:|---:|
| `spacing/50` | 4 | 0.5m |
| `spacing/100` | 8 | 1m |
| `spacing/125` | 10 | 1.25m |
| `spacing/150` | 12 | 1.5m |
| `spacing/175` | 14 | 1.75m |
| `spacing/200` | 16 | 2m |
| `spacing/225` | 18 | 2.25m |
| `spacing/250` | 20 | 2.5m |
| `spacing/300` | 24 | 3m |
| `spacing/325` | 26 | 3.25m |
| `spacing/350` | 28 | 3.5m |
| `spacing/375` | 32 | 4m |
| `spacing/400` | 36 | 4.5m |
| `spacing/450` | 44 | 5.5m |
| `spacing/475` | 48 | 6m |
| `spacing/500` | 52 | 6.5m |
| `spacing/550` | 56 | 7m |
| `spacing/600` | 60 | 7.5m |
| `spacing/650` | 64 | 8m |
| `spacing/700` | 68 | 8.5m |
| `spacing/750` | 72 | 9m |
| `spacing/800` | 80 | 10m |
| `spacing/900` | 88 | 11m |
| `spacing/1000` | 104 | 13m |

### Screen-padding (для 1920×1080)

| Токен | Значение (px) |
|---|---:|
| `screen-padding/left` | 148 |
| `screen-padding/right` | 60 |

---

## Правила выбора

| Контекст | Токен (пример) |
|---|---|
| Базовый модуль | `spacing/100` = 8px |
| Мелкий gap (между иконкой и текстом) | `spacing/50`…`spacing/150` (4–12px) |
| Внутренний padding кнопки/чипса | `spacing/200`…`spacing/300` (16–24px) |
| Gap между элементами строки (chip-ряд, top-навигация) | `spacing/200`…`spacing/300` |
| Внутренний padding карточки контента / постера | `spacing/300`…`spacing/450` (24–44px) |
| Отступ между секциями экрана | `spacing/600`…`spacing/900` (60–88px) |
| Inset от края экрана до контента (1920×1080) | `screen-padding/left` = 148px / `screen-padding/right` = 60px |

**Safe-zone-правило** (из гайд-страницы Lib-TV `Grid & Safezones & Spacing`, 12902:105094): для разрешения 1920×1080 безопасные зоны слева 102px, справа 78px, сверху/снизу 60px. Отступы от края контейнера выбирай **кратными 8** (модулю), не равными значению safe-zone. Уже учтённые `screen-padding/*` сделаны кратными.

Подробное визуальное гайд-описание см. в Lib-TV: `Grid & Safezones & Spacing` (12902:105094). Конкретные значения токенов — в таблице выше.

---

## Обновление

```bash
bash scripts/figma-sync-tokens.sh spacing-tv
```

Скрипт обновит шапку и скелет. Resolved-значения NUMBER-переменных подставляет скил через `use_figma` (Plugin API, fileKey `Zn2JrOHhSURjCuUEp6JcI8`).
Раздел «Правила выбора» сохраняется при пересборе.
