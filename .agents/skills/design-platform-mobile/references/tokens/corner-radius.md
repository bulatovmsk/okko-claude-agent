# Corner-radius — Tokens [mobile & web]
> Источник: file **🦖 Tokens [mobile & web]** (`vztN8doGwBZOCbpDf2PhKR`), страница **Corner-radius** — node `2287:157374`. Токены — NUMBER variables Figma (REST не отдаёт значений, забираются через Plugin API).

Токены скруглений углов компонентов и контейнеров. Это **NUMBER variables** Figma.

## Токены

Базовая шкала `corner-radius/100..1000` — для скруглений компонентов.

| Токен | Значение | Типовое применение |
|---|---|---|
| `corner-radius.100` | 2 | минимальный, hairline |
| `corner-radius.200` | 4 | мелкие чипы |
| `corner-radius.300` | 6 |  |
| `corner-radius.400` | 8 | мелкие чипы / теги |
| `corner-radius.450` | 10 |  |
| `corner-radius.500` | 12 | кнопки (small) |
| `corner-radius.600` | 14 |  |
| `corner-radius.700` | 16 | кнопки (medium), мелкие карточки |
| `corner-radius.800` | 20 | карточки контента, постеры |
| `corner-radius.900` | 24 | большие шторки, sheets |
| `corner-radius.1000` | 28 | крупные модальные блоки |

### Специальный

| Токен | Значение | Применение |
|---|---|---|
| `corner-radius.round` | 9999 | полностью круглый (avatars, icon buttons, indicator dots) |

---

## Правила выбора

| Контекст | Токен |
|---|---|
| Маленькие чипсы, теги | `radius.s` (≈ 8) |
| Кнопки (мелкая / средняя) | `radius.m` (≈ 12) |
| Карточки контента, постеры | `radius.l` (≈ 16) |
| Большие сабшиты, шторки | `radius.xl` (≈ 20–24) |
| Полностью круглые (avatars, icon buttons) | `radius.full` / 9999 |

Значения отличаются по платформе — см. колонки таблицы выше.

---

## Обновление

```bash
bash scripts/sync-from-figma.sh tokens corner-radius --variables-dir <dump-dir>
```

Workflow принимает Variables REST API или Figma MCP dump, разрешает alias chains, обновляет source и references и формирует отчёт.
Раздел «Правила выбора» сохраняется при пересборе.
