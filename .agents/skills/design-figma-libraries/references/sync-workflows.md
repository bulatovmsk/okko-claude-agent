# Синхронизация Figma → design-system

## Выбор команды

| Данные | Команда |
|---|---|
| Цвета | `bash scripts/sync-from-figma.sh head colors --variables-dir <dump-dir>` |
| Иконки | `bash scripts/sync-from-figma.sh head icons` |
| Иллюстрации | `bash scripts/sync-from-figma.sh head illustrations` |
| Всё из Head Library | `bash scripts/sync-from-figma.sh head all --variables-dir <dump-dir>` |
| Mobile/Web typography | `bash scripts/sync-from-figma.sh tokens typography` |
| Mobile/Web spacing | `bash scripts/sync-from-figma.sh tokens spacing --variables-dir <dump-dir>` |
| Mobile/Web corner radius | `bash scripts/sync-from-figma.sh tokens corner-radius --variables-dir <dump-dir>` |
| Все Mobile/Web токены | `bash scripts/sync-from-figma.sh tokens all-mw --variables-dir <dump-dir>` |
| TV typography | `bash scripts/sync-from-figma.sh tokens typography-tv` |
| TV spacing | `bash scripts/sync-from-figma.sh tokens spacing-tv --variables-dir <dump-dir>` |
| TV corner radius | `bash scripts/sync-from-figma.sh tokens corner-radius-tv --variables-dir <dump-dir>` |
| Все TV-токены | `bash scripts/sync-from-figma.sh tokens all-tv --variables-dir <dump-dir>` |
| Все токены | `bash scripts/sync-from-figma.sh tokens all --variables-dir <dump-dir>` |

REST-маршрутам нужен `.env` с `FIGMA_TOKEN`. Number-only targets (`spacing`, `corner-radius` и TV-варианты) могут работать без токена, если передан Figma MCP dump. Перед запуском проверяй только наличие секрета и никогда не печатай его значение.

`sync-from-figma.sh` выполняет шаги в staged-копии и переносит их в рабочие файлы только после успешного разрешения aliases и валидации. Отчёт запуска находится в `.figma-cache/reports/` или по пути из `--report`.

## Источники

| Набор | fileKey |
|---|---|
| Okko Head Library | `HYB1u9ysALVWtVWKoagiDH` |
| Tokens mobile & web | `vztN8doGwBZOCbpDf2PhKR` |
| Tokens TV | `Zn2JrOHhSURjCuUEp6JcI8` |

Точные nodeId перечислены в [libraries-map.md](libraries-map.md).

## Variable dump и aliases

Генераторы создают маркеры только внутри staged-копии:

- `VARDEFS_FROM_MCP` в цветах;
- `VARDEFS_FROM_PLUGIN_API` в spacing и corner-radius.

Сначала команда пробует явно переданный JSON, затем Variables REST API. REST `/variables/local` может вернуть 403 без нужного Enterprise scope; в этом случае не повторяй запрос и получи dump через Figma MCP.

Для Figma MCP используй минимальный target. `get_variable_defs` подходит, если нужная node содержит все применяемые variables и возвращает resolved-значения. Иначе после загрузки обязательного Figma-use skill прочитай локальные collections через Plugin API.

1. Открой нужный файл по fileKey.
2. Для цветов выбери `COLOR` variables с префиксами `color/` и `brand/`, а также все variables, на которые они ссылаются; mode — `Dark`.
3. Для spacing/corner-radius выбери `FLOAT` variables с префиксами `spacing/`, `screen-padding/` и `corner-radius/`, а также alias dependencies; mode — `Web&Mobile` или `TV`.
4. Сохрани JSON под именем `{fileKey}.json`, `head.json`, `mobile-web.json` или `tv.json`. Допустимы:
   - сырой ответ Variables API;
   - `collections` + `variables` из Plugin API;
   - плоский объект `resolvedValues` с уже разрешёнными значениями.
5. Запусти минимальную команду с `--variables-dir`. Локальный resolver разрешит alias chains, обнаружит missing references и циклы и сформирует таблицы.

Получение dump — read-only. Не создавай временную ноду, если инструмент может вернуть отфильтрованный JSON напрямую. Не изменяй collections, modes или компоненты Figma.

## Завершение

Полный запуск:

```bash
bash scripts/sync-from-figma.sh tokens spacing --variables-dir <dump-dir>
```

Команда сама обновит `design-system/`, пересоберёт references, провалидирует skills и создаст Markdown-отчёт. Покажи пользователю статус и run-specific diff из отчёта. Коммит, push и публикация требуют отдельного запроса.
