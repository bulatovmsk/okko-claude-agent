# Corner-radius — Tokens [tv]
> Источник: file **🦍 Tokens [tv]** (`Zn2JrOHhSURjCuUEp6JcI8`), страница **Corner-radius** — node `857:2089`. Токены — NUMBER variables Figma (REST не отдаёт значений, забираются через Plugin API).

Токены скруглений для TV-интерфейса. Включают **regular** (для самих компонентов, node `859:3226`) и **focus** (контур при наведении пультом, node `3143:465`) — это две разные сущности.

## Токены

| Токен | Значение (px) |
|---|---:|
| `corner-radius/100` | 4 |
| `corner-radius/200` | 6 |
| `corner-radius/300` | 8 |
| `corner-radius/400` | 10 |
| `corner-radius/450` | 12 |
| `corner-radius/475` | 14 |
| `corner-radius/500` | 16 |
| `corner-radius/550` | 18 |
| `corner-radius/600` | 20 |
| `corner-radius/650` | 22 |
| `corner-radius/700` | 24 |
| `corner-radius/750` | 26 |
| `corner-radius/800` | 28 |
| `corner-radius/900` | 32 |
| `corner-radius/1000` | 36 |
| `corner-radius/round` | 9999 |

### Focus-radius

| Токен | Значение (px) |
|---|---:|
| `corner-radius/focus/100` | 10 |
| `corner-radius/focus/200` | 12 |
| `corner-radius/focus/300` | 14 |
| `corner-radius/focus/400` | 16 |
| `corner-radius/focus/450` | 18 |
| `corner-radius/focus/475` | 20 |
| `corner-radius/focus/500` | 22 |
| `corner-radius/focus/550` | 24 |
| `corner-radius/focus/600` | 26 |
| `corner-radius/focus/650` | 28 |
| `corner-radius/focus/700` | 30 |
| `corner-radius/focus/750` | 32 |
| `corner-radius/focus/800` | 34 |
| `corner-radius/focus/900` | 38 |
| `corner-radius/focus/1000` | 42 |

_Применяется как радиус outline-контура вокруг компонента в состоянии focus (наведение пультом). Значение focus-радиуса = regular + 6px._

---

## Правила выбора

| Контекст | Regular (компонент) | Focus (outline вокруг) |
|---|---|---|
| Чипсы, теги | `corner-radius/100`…`corner-radius/300` (4–8px) | `corner-radius/focus/100`…`corner-radius/focus/300` (10–14px) |
| Кнопки | `corner-radius/300`…`corner-radius/500` (8–16px) | соответствующий `focus/*` (+6) |
| Карточки контента, постеры | `corner-radius/500`…`corner-radius/700` (16–24px) | соответствующий `focus/*` |
| Большие модалки / шторки | `corner-radius/700`…`corner-radius/1000` (24–36px) | соответствующий `focus/*` |
| Полностью круглые (avatars, icon buttons) | `corner-radius/round` (9999) | `corner-radius/round` |

**Правило соответствия:** focus-радиус всегда `regular + 6px` (компенсация толщины outline). Если для компонента есть `corner-radius/500` = 16px, то для outline вокруг него — `corner-radius/focus/500` = 22px.

**Focus-обводка** появляется при наведении пультом (Smart TV / Android TV) — это TV-специфика, на mobile/web не используется.

---

## Обновление

```bash
bash scripts/figma-sync-tokens.sh corner-radius-tv
```

Скрипт обновит шапку и скелет. Resolved-значения NUMBER-переменных подставляет скил через `use_figma` (Plugin API, fileKey `Zn2JrOHhSURjCuUEp6JcI8`).
Раздел «Правила выбора» сохраняется при пересборе.
