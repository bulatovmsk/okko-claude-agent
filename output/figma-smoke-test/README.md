# Okko DS Smoke Test — проверка работы в Figma

Тестовый артефакт для файла **[Untitled · VPksdlfxRuYt1N0UlBK27n](https://www.figma.com/design/VPksdlfxRuYt1N0UlBK27n/Untitled?node-id=0-1)**.

## Зачем два файла

| Файл | Когда использовать | Нужна авторизация Figma MCP |
|---|---|---|
| `manifest.json` + `code.js` | прямо сейчас, вручную через Figma Desktop | нет |
| `use_figma-script.js` | когда коннектор Figma MCP авторизован (`use_figma`) | да |

Причина разделения: создавать и редактировать ноды в Figma умеет только Plugin API. В моей
сессии инструмент `use_figma` недоступен (коннектор `mcp.figma.com` отдаёт 401, плагин Figma
не включён), поэтому запись из агента сейчас невозможна. Оба файла написаны так, чтобы
результат был одинаковым.

## Как запустить development-плагин (30 секунд)

1. Откройте файл `VPksdlfxRuYt1N0UlBK27n` в Figma Desktop.
2. Меню **Plugins → Development → Import plugin from manifest…**
3. Выберите `output/figma-smoke-test/manifest.json`.
4. Запустите **Plugins → Development → Okko DS Smoke Test**.
5. Плагин создаст один фрейм и покажет нотификацию с числом созданных нод.

### Если Figma показывает «Manifest error»

Манифест обязан содержать ровно это:

| Поле | Значение | Почему |
|---|---|---|
| `networkAccess.allowedDomains` | `["none"]` | пустой массив `[]` невалиден: Figma требует именно `["none"]` для полного запрета сети |
| `documentAccess` | `"dynamic-page"` | обязательно для всех новых плагинов, иначе импорт отклоняется |
| `id` | не задаём | для локального development-плагина ID Figma не нужен |

После правки манифеста импорт нужно повторить: **Plugins → Development → Import plugin from manifest…**
Если в списке осталась запись от неудачного импорта с подписью «Locate missing manifest» —
удалите её правым кликом → **Remove**.

## Что появится на странице

Фрейм `DS smoke test · Okko` (360 px, тёмная поверхность, auto-layout):

```text
DS smoke test · Okko                ← fill: color.background.solid.primary #000000
│  padding 24 (spacing.350), gap 16 (spacing.250), radius 16 (corner-radius.700)
├─ «Дизайн-система Okko»            ← H3 = 20/26 · 600, color.text-icon.primary #FFFFFFF5
├─ «Проверка связи с Figma: …»      ← Body 3 = 13/18 · 400 · ls 0.13, text-icon.secondary
├─ Tokens / swatches                ← fill: color.fill.solid.secondary #1B1A1D
│  ├─ 32×32 radius 8                ← color.fill.solid.accent #4137DF
│  ├─ 32×32 radius 8                ← color.fill.solid.third #2C2B2F
│  └─ 32×32 radius 9999             ← color.fill.solid.positive #12B77C
└─ «spacing.350 · corner-radius.700 · Body 3 · H3»   ← color.text-icon.third #FFFFFF8F
```

Фрейм ставится справа от крайней правой ноды страницы, а не в `(0,0)`.

## Источники значений

Все размеры и цвета взяты из source of truth проекта, ничего не выдумано:

- `design-system/tokens/colors.md` — `color.background.solid.primary`, `color.fill.solid.*`, `color.text-icon.*`
- `design-system/tokens/spacing.md` — `spacing.350`, `spacing.250`, `spacing.200`
- `design-system/tokens/corner-radius.md` — `corner-radius.700`, `corner-radius.400`, `corner-radius.round`
- `design-system/tokens/typography.md` — `H3` (20/26 · 600), `Body 3` (13/18 · 400 · ls 0.13)

Скрипт **не привязывает** значения к Figma variables: в файле `Untitled` нет подключённых
библиотек токенов. Если файл подключить к `Tokens [mobile & web]` (`vztN8doGwBZOCbpDf2PhKR`),
следующий шаг — заменить raw-значения на `setBoundVariable`.

## Что требует ручной проверки

- **Шрифт.** В токенах указан `Suisse Int'l`. Плагин пробует `Suisse Int'l SemiBold/Medium`,
  затем `Inter Semi Bold/Medium`, и сообщает в нотификации, какой шрифт загрузился. Если
  использован `Inter` — это фолбэк среды, а не решение дизайн-системы.
- **Размеры.** Ширина фрейма 360 px задана как тестовая, а не как платформенный брейкпоинт.
- Ничего, кроме созданных нод, плагин не изменяет: существующие инстансы и variables не
  затрагиваются, компоненты не отсоединяются.

## Если запускать через `use_figma`

Сначала загрузите навык `figma-use` (он обязателен перед каждым вызовом `use_figma`), затем
отправьте содержимое `use_figma-script.js` одним вызовом. Скрипт следует правилам навыка:
top-level `await`, вывод только через `return`, без `figma.notify()` и `figma.closePlugin()`,
возвращает все созданные node id.

## Проверка результата

После запуска результат можно подтвердить чтением через Figma Dev Mode MCP — без прав записи:

```bash
# вывести структуру страницы с созданным фреймом
curl -s -X POST http://127.0.0.1:3845/mcp \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json, text/event-stream' \
  -H "Mcp-Session-Id: $SID" \
  -d '{"jsonrpc":"2.0","id":2,"method":"tools/call",
       "params":{"name":"get_metadata","arguments":{"nodeId":"0:1","clientLanguages":"swift","clientFrameworks":"unknown"}}}'
```
