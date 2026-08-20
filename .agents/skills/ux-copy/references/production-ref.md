# production-ref

Looks up existing UX-copy strings in the Okko production reference.

## When to use

Need to verify consistency with existing strings or find
stylistic precedents in Okko's live interface copy.

## Source files

| File | Purpose |
|---|---|
| `references/production-reference/ID.tokens.json` | Token keys and metadata (no human-readable text) |
| `references/production-reference/RU.tokens.json` | Russian string values currently in production |

## Structure

Both files share the same JSON structure:

```
{
  "<Domain>": {              // e.g. "Глобальные ошибки", "Детское", "Универсальное"
    "<Feature>": {           // e.g. "Нет интернета", "Таймер"
      "<Component>": {       // e.g. "Модальная", "Шторка"
        "<Element>": {       // e.g. "Заголовок", "Главное действие"
          "$type": "string",
          "$value": "...",   // In RU: the Russian text. In ID: the token key
          "$description": "…" // Optional: search hint
        }
      }
    }
  }
}
```

Path segments map to the UI hierarchy: **Domain → Feature → ... → Component → Element**.

## How to look up

### By token key (if you have an ID)

1. Search `ID.tokens.json` for the `$value` matching the token key.
2. Follow the same JSON path in `RU.tokens.json` to get the Russian value.

### By semantic area (if you have a concept)

1. In `RU.tokens.json`, navigate to the relevant **Domain** (e.g. "Детское" for kids-related copy).
2. Drill down to the **Feature** and **Component**.
3. Read `$value` fields for the actual strings.

### By keyword search

1. Search `RU.tokens.json` `$value` and `$description` fields for the keyword.
2. Also search `ID.tokens.json` `$description` fields — they contain English hints.

### Cross-referencing with `{…}` references

Some `$value` fields contain references like `{Универсальное.Действие.Понятно}`.
Resolve these by following the dot-path from the root of `RU.tokens.json`.

## Output format for agents

When citing production examples, return:

```
<Russian text> | variable в Фигме [<Domain>/<Feature>/<Component>/<Element>]
```

Example:
```
Попробовать снова | variable в Фигме [Универсальное/Действие/Повторная попытка]
```
