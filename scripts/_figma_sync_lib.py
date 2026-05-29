#!/usr/bin/env python3
"""
Парсинг JSON-выгрузок Figma и генерация markdown-файлов для design-system/.
Вызывается из scripts/figma-sync-head-library.sh.

Usage:
    python3 _figma_sync_lib.py colors|icons|illustrations <cache_dir> <out_md>
"""
import json, re, sys, os, subprocess
from collections import defaultdict, Counter

FILE_KEY = "HYB1u9ysALVWtVWKoagiDH"


# ============================================================
# COLORS
# ============================================================

RAMP_ORDER = ['black', 'white', 'gray', 'red', 'yellow', 'green', 'brown',
              'blue', 'cobalt', 'purple', 'pink', 'violet', 'electric']

def hex_color(c):
    return '#%02X%02X%02X' % (round(c['r']*255), round(c['g']*255), round(c['b']*255))

def gradient_stops(fill):
    """Возвращает список (hex_with_alpha, position%) для GRADIENT_*."""
    stops = []
    for s in fill.get('gradientStops', []):
        col = s['color']
        hx = hex_color(col)
        a = col.get('a', 1.0)
        if a < 1.0:
            hx += f' a{a:.2f}'
        stops.append((hx, s['position']*100))
    return stops

def first_solid(node):
    for f in (node.get('fills') or []):
        if f.get('type') == 'SOLID' and f.get('visible', True):
            a = f.get('opacity', 1)
            hx = hex_color(f['color'])
            return hx, a
    return None, None

def get_text(node, label):
    """Найти первый TEXT с именем == label (рекурсивно)."""
    if node['type'] == 'TEXT' and node.get('name') == label:
        return node.get('characters', '')
    for c in node.get('children', []):
        r = get_text(c, label)
        if r is not None:
            return r
    return None


def extract_primitives(palette_json):
    """Из ноды 32102:23344 → Primitives и External по 'Color cell' INSTANCE."""
    doc = list(palette_json['nodes'].values())[0]['document']
    cells = []
    def walk(n):
        if n.get('name') == 'Color cell' and n['type'] == 'INSTANCE':
            hx, _ = first_solid(n)
            nm = get_text(n, 'Color name')
            cells.append((nm, hx))
            return
        for c in n.get('children', []):
            walk(c)
    # Primitives = doc.children[0]; External — отдельная подгруппа
    # (структура: Primitives -> Frame237 -> Frame345/Frame249 -> ...)
    walk(doc['children'][0])  # Primitives только
    seen = {}
    for nm, hx in cells:
        if nm and nm not in seen:
            seen[nm] = hx
    # делим на primitives.* и Primitives/External/* по имени
    prim, ext = {}, {}
    for nm, hx in seen.items():
        if nm.startswith('primitives.'):
            prim[nm[len('primitives.'):]] = hx  # gray1200, electric1300, …
        else:
            # 'gray1000' и т.п. без префикса — это тоже primitives (так в либе)
            # external = epl1, sber1, yandex1, … (короткие без числа на конце через 4 цифры)
            if re.match(r'^(epl|sber|yandex|vk|winline|ok|facebook|twitter|viber)\d+$', nm):
                ext[nm] = hx
            else:
                prim[nm] = hx
    return prim, ext


def fetch_style_nodes(file_key, node_ids):
    """Через scripts/figma-api.sh запросить ноды стилей пачкой."""
    ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ids_arg = ','.join(node_ids)
    result = subprocess.run(
        ['bash', os.path.join(ROOT, 'scripts/figma-api.sh'),
         f"/v1/files/{file_key}/nodes?ids={ids_arg}"],
        capture_output=True, text=True, check=True
    )
    return json.loads(result.stdout)


def extract_styles(styles_json, cache_dir):
    """Из /styles → не-deprecated FILL стили с их градиентами/solid."""
    metas = styles_json['meta']['styles']
    fills = [s for s in metas
             if s['style_type'] == 'FILL' and not s['name'].startswith('[Deprecated]')]
    # запросить ноды чтобы достать fills/gradientStops
    nodes = fetch_style_nodes(FILE_KEY, [s['node_id'] for s in fills])
    # сохранить кэш
    with open(os.path.join(cache_dir, 'style-nodes.json'), 'w') as f:
        json.dump(nodes, f)
    out = []
    for s in fills:
        nid = s['node_id']
        nd = nodes['nodes'].get(nid)
        if not nd: continue
        doc = nd['document']
        for fill in (doc.get('fills') or []):
            t = fill.get('type', '')
            if t == 'SOLID':
                hx = hex_color(fill['color']); a = fill.get('opacity', 1)
                out.append({'name': s['name'], 'kind': 'solid',
                            'value': hx + ('' if a >= 1 else f' a{a:.2f}')})
            elif 'GRADIENT' in t:
                stops = gradient_stops(fill)
                out.append({'name': s['name'], 'kind': t,
                            'stops': stops})
            break
    return out


def write_colors_md(prim, ext, styles, out_path):
    lines = []
    lines.append("# Цвета — Okko Head Library\n")
    lines.append("> Источник: file **Okko Head Library** (`HYB1u9ysALVWtVWKoagiDH`), страница `Color Tokens` (`32102:23149`). "
                 "Тема — **Dark** (основная и единственная активная в библиотеке).\n")
    lines.append("\nЦвета устроены как **переменные** (variables) и **стили** (опубликованные FILL-стили Figma):\n")
    lines.append("\n- **Variables** — применяются программно (Code Connect, токены) и через bound variables в Figma. Это и сырая палитра (`primitives.*`), и семантика (`color.*`), и `brand.*`.")
    lines.append("\n- **Styles** — опубликованные FILL-стили; **только для градиентов и многостоповых fade**, которые нельзя выразить одной переменной.\n")
    lines.append("\nСинхронизация: `bash scripts/figma-sync-head-library.sh colors` (см. раздел «Обновление» внизу).\n")
    lines.append("\n---\n")

    # ───────── Часть A — Variables ─────────
    lines.append("\n## A. Variables (переменные)\n")
    lines.append("### A.1. Primitives — сырая палитра\n")
    lines.append("Не использовать напрямую в макетах. Шкала: `100` (светлый) … `1300` (тёмный).\n")

    # group ramps
    ramps = defaultdict(list)
    for name, hx in prim.items():
        m = re.match(r'^([a-z]+)(\d+)?$', name)
        if not m: continue
        ramp = m.group(1)
        ramps[ramp].append((name, hx, int(m.group(2)) if m.group(2) else 0))

    # black/white
    lines.append("\n**Чёрный/белый:**\n\n| Токен | HEX |\n|---|---|\n")
    for nm in ('black', 'white'):
        if nm in prim:
            lines.append(f"| `primitives.{nm}` | `{prim[nm].upper()}` |\n")

    for ramp in RAMP_ORDER:
        if ramp in ('black', 'white'): continue
        if ramp not in ramps: continue
        items = sorted(ramps[ramp], key=lambda t: t[2])
        if not items: continue
        lines.append(f"\n**{ramp}**\n\n| Тон | HEX |\n|---|---|\n")
        for name, hx, _ in items:
            lines.append(f"| `{name}` | `{hx.upper()}` |\n")

    # External primitives
    lines.append("\n### A.2. External primitives — фирменные/партнёрские (сырые)\n\n| Токен | HEX |\n|---|---|\n")
    for nm, hx in ext.items():
        lines.append(f"| `{nm}` | `{hx.upper()}` |\n")

    # Semantic
    lines.append("\n### A.3. Semantic-токены — `color.*` (применять в макетах)\n")
    lines.append("> ⚙️ Значения resolved-hex для semantic-токенов добираются через MCP "
                 "`get_variable_defs(nodeId='32102:23149', fileKey='HYB1u9ysALVWtVWKoagiDH')` "
                 "и подставляются в маркер ниже. REST `/variables/local` отдаёт 403 без Enterprise scope.\n")
    lines.append("\n<!-- VARDEFS_FROM_MCP:semantic — заполнить через MCP get_variable_defs -->\n")

    # Brand
    lines.append("\n### A.4. Brand / партнёры / соцсети\n")
    lines.append("<!-- VARDEFS_FROM_MCP:brand — заполнить через MCP get_variable_defs -->\n")

    # ───────── Часть B — Styles ─────────
    lines.append("\n---\n")
    lines.append("\n## B. Styles (опубликованные FILL-стили Figma)\n")
    lines.append(f"\n**{len(styles)} не-deprecated стилей.** Применять как «стиль» в Figma (для градиентов и многостоповых fade).\n")

    # сгруппировать по неймспейсу color/<group>/...
    groups = defaultdict(list)
    for s in styles:
        path = s['name']
        parts = path.split('/')
        # color/border/decorative/* → group="border/decorative"
        if parts[0] == 'color':
            grp = '/'.join(parts[1:-1]) if len(parts) > 2 else parts[1]
        else:
            grp = parts[0]
        groups[grp].append(s)

    group_order = ['border/decorative', 'component', 'component/label',
                   'fill/fade/top', 'fill/fade/right', 'fill/fade/bottom', 'fill/fade/left',
                   'fill/glassy/hover-focus', 'fill/solid/hover-focus',
                   'fill/technical', 'partners']

    def render_style(s):
        nm = s['name']
        if s['kind'] == 'solid':
            return f"| `{nm}` | solid | `{s['value']}` |\n"
        # gradient — компактно: для fade (16 стопов) → первый/последний, иначе все
        stops = s.get('stops', [])
        if len(stops) > 4:
            disp = f"`{stops[0][0]}` 0% … `{stops[-1][0]}` 100% ({len(stops)} стопов)"
        else:
            disp = ', '.join(f"`{h}` {p:.0f}%" for h, p in stops)
        kind = s['kind'].replace('GRADIENT_', '').lower()
        return f"| `{nm}` | {kind} | {disp} |\n"

    rendered = set()
    for grp in group_order:
        if grp not in groups: continue
        lines.append(f"\n### `color/{grp}/…`\n\n| Стиль | Тип | Значение |\n|---|---|---|\n")
        for s in sorted(groups[grp], key=lambda x: x['name']):
            lines.append(render_style(s))
            rendered.add(s['name'])

    # остальные группы (если что-то не покрыто order)
    other = [s for s in styles if s['name'] not in rendered]
    if other:
        lines.append("\n### Прочие\n\n| Стиль | Тип | Значение |\n|---|---|---|\n")
        for s in sorted(other, key=lambda x: x['name']):
            lines.append(render_style(s))

    # Связь styles ↔ variables
    lines.append("\n### Связь со semantic-токенами\n")
    lines.append("Большинство FILL-стилей продублированы как semantic-переменные с тем же путём "
                 "(стиль `color/fill/fade/top/primary` ↔ переменная `color.fill.fade.top.primary`). "
                 "Это сделано, чтобы один и тот же градиент можно было применить и как «стиль» в Figma, "
                 "и через bound variable в коде.\n")

    # ───────── Правила ─────────
    lines.append("\n---\n")
    lines.append("\n## Правила: что когда брать\n")
    lines.append("\n| Когда | Брать |\n|---|---|\n")
    lines.append("| Solid-цвет (один тон, без градиента) | **переменную** (`color.*`) — программно или через bound variable |\n")
    lines.append("| Градиент / многостоповая fade-рампа | **опубликованный стиль** Figma (`color/...`) — невозможно одной переменной |\n")
    lines.append("| Hover/focus 2-стоповые состояния | **стиль** (анимация между двумя точками) |\n")
    lines.append("| Цвет фирменного партнёра (Сбер, EPL, …) | `Primitives/External/*` (сырьё) или `brand.partners.*` (применяемый) |\n")
    lines.append("| Цвета, не зависящие от темы | `color.static.*` — единственные не меняющиеся между Dark/Light |\n")
    lines.append("\n**Не использовать:** все `[Deprecated]/*` стили (в `/styles` их большинство — 181 из 220).\n")
    lines.append("**Прозрачность:** кодируется 8-значным HEX (`#RRGGBBAA`); напр. `#FFFFFFF5` = white α=0.96.\n")

    # ───────── Обновление ─────────
    lines.append("\n---\n")
    lines.append("\n## Обновление\n")
    lines.append("\n```bash\nbash scripts/figma-sync-head-library.sh colors\n```\n")
    lines.append("\nСкрипт перепишет этот файл из актуальной Figma. Resolved-hex semantic-токенов "
                 "далее заполняются скилом `design-figma-libraries` через MCP `get_variable_defs` "
                 "(см. маркеры `VARDEFS_FROM_MCP` выше).\n")

    with open(out_path, 'w') as f:
        f.write(''.join(lines))


def cmd_colors(cache_dir, out_path):
    palette = json.load(open(os.path.join(cache_dir, 'palette.json')))
    styles_meta = json.load(open(os.path.join(cache_dir, 'styles.json')))
    prim, ext = extract_primitives(palette)
    styles = extract_styles(styles_meta, cache_dir)
    write_colors_md(prim, ext, styles, out_path)


# ============================================================
# ICONS — Main Pack
# ============================================================

CAT_ORDER = ['Menu', 'Navigation', 'Categories', 'Arrows', 'Mark', 'Labels',
             'Notification', 'Objects', 'Actions', 'Devices', 'Player',
             'Logotypes', 'Sports', 'Football', 'Settings', 'Helpdesk']

CAT_DESC = {
    'Menu': 'таб-бар и разделы приложения',
    'Navigation': 'списки, сетки, выход',
    'Categories': 'жанры и категории контента',
    'Arrows': 'стрелки и направления',
    'Mark': 'оценки (звёзды, лайки)',
    'Labels': 'метки (рубль, подарок, замок)',
    'Notification': 'колокольчик, галочки прочтения',
    'Objects': 'предметы и сущности (карты, документы, фильтры)',
    'Actions': 'действия (добавить, удалить, поделиться)',
    'Devices': 'устройства (TV, телефон, пульт)',
    'Player': 'управление плеером',
    'Logotypes': 'логотипы Окко, партнёров, соцсетей',
    'Sports': 'виды спорта',
    'Football': 'события матча (голы, карточки)',
    'Settings': 'настройки',
    'Helpdesk': 'поддержка (вложение, отправка)',
}

def render_icons_section(icons_json):
    """Сборка ВСЕГО кроме раздела «Правила выбора модификатора»."""
    doc = list(icons_json['nodes'].values())[0]['document']
    comps = [c for c in doc.get('children', []) if c['type'] == 'COMPONENT']
    cats = defaultdict(list)
    for c in comps:
        cat, _, icon = c['name'].partition(' / ')
        cats[cat].append(icon)

    L = []
    L.append("# Иконки — Main Pack (Okko Head Library)\n")
    L.append("> Источник: file **Okko Head Library** (`HYB1u9ysALVWtVWKoagiDH`), секция **Main pack** — node `29361:322`. "
             "Только Main Pack (другие паки в базу не вносятся).\n")
    L.append(f"\n**{len(comps)} компонентов-иконок** в **{len(cats)} категориях**. "
             "Все — фреймы **24×24px** (единый размер кадра; оптический размер глифа внутри меньше).\n")

    L.append("""
## Конвенция именования

`Категория / Имя_Модификатор` — напр. `Menu / Bookmark_Solid_Bold`, `Actions / Cross`.

| Модификатор | Значение |
|---|---|
| *(без суффикса)* | базовый контурный (Regular, тонкая обводка) |
| `_Bold` | контурный с утолщённой обводкой |
| `_Solid` | залитый (filled) |
| `_Solid_Bold` | залитый + утолщённый |
| `_Light` | облегчённый (тоньше базового) |
| `_Indicator` | вариант с бейджем-индикатором (точка уведомления, отдельный VECTOR с цветовой переменной) |
| `_Color` | многоцветная иконка (фикс. цвета, напр. логотипы, карточки футбола) |

**Стиль = вес обводки/заливка.** Один глиф обычно есть в нескольких вариантах (например `Magnifier`, `Magnifier_Bold`, `Magnifier_Solid`, `Magnifier_Solid_Bold`). Контурные используются в покое, `_Solid`/`_Bold` — в активном/выбранном состоянии.

## Анатомия

- Кадр **24×24px**. Глиф — `BOOLEAN_OPERATION` (Union/Subtract) или `VECTOR` внутри.
- Цвет глифа задаётся при применении (наследуется от контекста), монохром.
- У `_Indicator` — отдельный слой бейджа (`Badge`, ~6–7px), привязан к цветовой переменной (акцент/негатив).
- `_Color`/логотипы — фиксированные цвета, перекрашивать нельзя.

## Применение

- Базовый размер кадра 24×24; масштабировать пропорционально.
- В компонентах (Chips, Button и т.д.) иконка вставляется через слот `Icon Instance` (swap).
- Не использовать `_Color`/логотипы как обычные монохромные иконки.
- Логотипы партнёров/соцсетей — только в санкционированных контекстах (авторизация, партнёрские блоки).
""")

    # Категории
    L.append("\n## Категории\n\n| Категория | Кол-во | Назначение |\n|---|---|---|\n")
    for cat in CAT_ORDER:
        if cat in cats:
            L.append(f"| {cat} | {len(cats[cat])} | {CAT_DESC.get(cat, '')} |\n")

    # Полный список
    L.append("\n## Полный список (по категориям)\n")
    L.append("\n<details><summary>Развернуть все иконки</summary>\n")
    for cat in CAT_ORDER:
        if cat not in cats: continue
        items = sorted(set(cats[cat]))
        L.append(f"\n**{cat}** ({len(cats[cat])}): " + ', '.join(f'`{i}`' for i in items) + "\n")
    L.append("\n</details>\n")

    # Источник + обновление
    L.append("\n## Источник\n\n- Figma `HYB1u9ysALVWtVWKoagiDH` node `29361:322` (секция Main pack).\n")
    L.append("\n## Обновление\n\n```bash\nbash scripts/figma-sync-head-library.sh icons\n```\n")
    L.append("\nСкрипт перепишет всё, **кроме раздела «Правила выбора модификатора»** "
             "(он редактируется вручную и сохраняется при синке).\n")
    return ''.join(L)


def cmd_icons(cache_dir, out_path):
    icons_json = json.load(open(os.path.join(cache_dir, 'icons.json')))
    new_main = render_icons_section(icons_json)

    # сохранить вручную-секцию «Правила выбора модификатора», если есть
    rules_block = ''
    if os.path.exists(out_path):
        old = open(out_path).read()
        m = re.search(r'(## Правила выбора модификатора\n.*?)(?=\n## (?!Правила выбора)|\Z)', old, re.S)
        if m:
            rules_block = '\n' + m.group(1).rstrip() + '\n'

    # вставить rules_block перед «## Источник»
    if rules_block:
        new_main = new_main.replace("\n## Источник\n", rules_block + "\n## Источник\n", 1)

    with open(out_path, 'w') as f:
        f.write(new_main)


# ============================================================
# ILLUSTRATIONS — Static / Product / Bobokko
# ============================================================

def collect_textnode_chars(n, out):
    if n['type'] == 'TEXT' and n.get('characters','').strip():
        out.append(n['characters'])
    for c in n.get('children', []):
        collect_textnode_chars(c, out)


def render_illustrations(j):
    nodes = j['nodes']
    static = nodes['39089:10560']['document']
    product = nodes['39101:215']['document']
    bobokko = nodes['39104:349']['document']

    L = []
    L.append("# Иллюстрации — Okko Head Library\n")
    L.append("""
> Источник: file **Okko Head Library** (`HYB1u9ysALVWtVWKoagiDH`). Три раздела:
> - **Static** — node `39089:10560`
> - **Product images** — node `39101:215`
> - **Bobokko** (маскот) — node `39104:349`

Иллюстрации Окко делятся на три группы: служебные (Static), продуктовые объекты-плейсхолдеры (Product images) и маскот-медведь **Bobokko**.

---

## 1. Static (служебные)

Системные иллюстрации для технических и навигационных состояний.

""")
    L.append("| Элемент | Тип | Размер | Назначение |\n|---|---|---|---|\n")
    static_meta = {
        'Loader': ('компонент', '300×300', 'анимация загрузки (есть `Loader Revers` — инстанс реверс)'),
        'Age Mark': ('component set', '2961×1024', 'возрастная маркировка: `0+`, `6+`, `12+`, `16+`, `18+`'),
        'Devices': ('frame', '3891×1264', 'изображения устройств: Стандартные / Мобильные / Все девайсы'),
        'Static splash': ('frame', '4932×1984', 'статичный сплэш-экран запуска'),
        'Menu promo Image': ('frame', '1632×1314', 'промо-картинка для меню'),
    }
    for ch in static.get('children', []):
        nm = ch['name']
        if nm in static_meta:
            tp, sz, dsc = static_meta[nm]
            L.append(f"| `{nm}` | {tp} | {sz} | {dsc} |\n")

    # Product images
    L.append("\n---\n\n## 2. Product images (продуктовые объекты)\n")
    L.append("Декоративные иллюстрации-плейсхолдеры (очки, мячи, попкорн и т.п.) — для пустых состояний, профилей, промо.\n")
    L.append("\n| Set | Вариантов | Состав |\n|---|---|---|\n")
    for ch in product.get('children', []):
        if ch['type'] != 'COMPONENT_SET': continue
        variants = [k['name'].split('=', 1)[-1] for k in ch.get('children', []) if k['type'] == 'COMPONENT']
        sample = ', '.join(variants[:8]) + (f' …+{len(variants)-8}' if len(variants) > 8 else '')
        L.append(f"| `{ch['name']}` | {len(variants)} | {sample} |\n")

    # Bobokko
    L.append("\n---\n\n## 3. Bobokko (маскот)\n")
    L.append("**Bobokko** — фирменный медведь-маскот Окко. Один component set `Bobokko` с переключателем поз через `Property 1`.\n")
    bob_set = next((c for c in bobokko.get('children', []) if c['type'] == 'COMPONENT_SET'), None)
    if bob_set:
        poses = [k['name'].split('=', 1)[-1] for k in bob_set.get('children', []) if k['type'] == 'COMPONENT']
        L.append(f"\n**{len(poses)} поз.** ")
        L.append("<details><summary>Все позы</summary>\n\n" + ' · '.join(poses) + "\n\n</details>\n")
    L.append("\n**Применение:** эмоциональные состояния, пустые экраны, онбординг, праздники, спорт. "
             "Поза подбирается по контексту (ошибка → «Обиделся»/«WTF», успех → «Палец вверх»/«ОК», ночь → «Спит…»).\n")

    L.append("""
---

## Правила применения

- **Static** — только по прямому назначению (загрузка, сплэш, возрастной знак). `Age Mark` обязателен по требованиям маркировки.
- **Product images** — декор и плейсхолдеры; не использовать как функциональные иконки (для иконок — [Main Pack](icons.md)).
- **Bobokko** — фирменный маскот, нельзя искажать/перекрашивать; позу выбирать по тону и контексту экрана.
- Все иллюстрации — общие для всех платформ (Web/iOS/Android/TV).

## Источник

- Static — Figma `HYB1u9ysALVWtVWKoagiDH` node `39089:10560`
- Product images — node `39101:215`
- Bobokko — node `39104:349`

## Обновление

```bash
bash scripts/figma-sync-head-library.sh illustrations
```
""")
    return ''.join(L)


def cmd_illustrations(cache_dir, out_path):
    j = json.load(open(os.path.join(cache_dir, 'illustrations.json')))
    with open(out_path, 'w') as f:
        f.write(render_illustrations(j))


# ============================================================
# TYPOGRAPHY — TEXT styles из vztN8doGwBZOCbpDf2PhKR
# ============================================================

TOKENS_FILE_KEY = "vztN8doGwBZOCbpDf2PhKR"

# Порядок колонок в сводной таблице — основные платформенные категории
TYPOGRAPHY_PLATFORM_ORDER = [
    'iPhone SE', 'iPhone', 'Android Mobile', 'Mobile 0+', 'Mobile 320+',
    '320+', '375+', 'Mobile',
    'iPad', 'Android Tablet', 'Tablet 600+', '600+', 'Tablet',
    '1320+', '1720+', 'Desktop 1720+', 'Desktop', 'Dektop 1720+',
    'Android Default',
]


def fetch_style_nodes_chunked(file_key, node_ids, chunk_size=80):
    """Запросить style-ноды через scripts/figma-api.sh пачками."""
    ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    merged = {'nodes': {}}
    for i in range(0, len(node_ids), chunk_size):
        chunk = node_ids[i:i+chunk_size]
        ids_arg = ','.join(chunk)
        r = subprocess.run(
            ['bash', os.path.join(ROOT, 'scripts/figma-api.sh'),
             f"/v1/files/{file_key}/nodes?ids={ids_arg}"],
            capture_output=True, text=True, check=True
        )
        nd = json.loads(r.stdout)
        merged['nodes'].update(nd.get('nodes', {}))
    return merged


def cmd_typography_fetch(cache_dir):
    """Дозапрос всех TEXT-стилей по их node_id (для извлечения font properties)."""
    styles = json.load(open(os.path.join(cache_dir, 'styles.json')))
    fills = [s for s in styles['meta']['styles']
             if s['style_type'] == 'TEXT' and not s['name'].startswith('[Deprecated]')]
    ids = [s['node_id'] for s in fills]
    nodes = fetch_style_nodes_chunked(TOKENS_FILE_KEY, ids)
    with open(os.path.join(cache_dir, 'style-nodes.json'), 'w') as f:
        json.dump(nodes, f)


def is_okkolokino(style_meta):
    """Является ли стиль частью sub-brand Okkolokino (по description)."""
    desc = (style_meta.get('description') or '').lower()
    return 'окколокино' in desc or 'okkolokino' in desc


def classify_style(name, meta):
    """Вернёт ('main' | 'okkolokino' | 'other', logical_name, platform_suffix)."""
    if '/' in name:
        log, _, suf = name.rpartition('/')
    else:
        log, suf = name, ''
    # признак Okkolokino — по description
    if is_okkolokino(meta):
        return 'okkolokino', log, suf
    # эвристика по имени для прочих sub-brands
    first = log.split()[0] if log else ''
    if first in ('Godzilla', 'Spasibo', 'Meta'):
        return 'other', log, suf
    # Media — Okkolokino даже без description
    if first == 'Media':
        return 'okkolokino', log, suf
    return 'main', log, suf


def extract_typography_props(style_node):
    """Из COMPONENT/style ноды достать font properties."""
    doc = style_node['document']
    st = doc.get('style', {})
    return {
        'fontFamily': st.get('fontFamily'),
        'fontPostScriptName': st.get('fontPostScriptName'),
        'fontWeight': st.get('fontWeight'),
        'fontSize': st.get('fontSize'),
        'lineHeightPx': st.get('lineHeightPx'),
        'lineHeightPercent': st.get('lineHeightPercent'),
        'letterSpacing': st.get('letterSpacing'),
        'paragraphSpacing': st.get('paragraphSpacing'),
    }


def fmt_typography_cell(props):
    """Компактное представление: 22/26 · 600 (без шрифта в ячейке, шрифт — отдельной колонкой)."""
    if not props or not props.get('fontSize'):
        return '—'
    fs = int(round(props['fontSize']))
    lh = props.get('lineHeightPx')
    lh_s = str(int(round(lh))) if lh else '—'
    w = props.get('fontWeight')
    ls = props.get('letterSpacing')
    ls_s = ''
    if ls is not None and abs(ls) > 0.01:
        ls_s = f' · ls {ls:.2f}'
    return f"{fs}/{lh_s} · {w}{ls_s}"


def render_typography_section(rows, all_platforms):
    """rows: dict logical_name → dict suffix → props. Возвращает markdown-таблицу."""
    if not rows:
        return "_нет стилей_\n"
    # колонки — те платформы, что встречаются хоть в одной строке (в порядке TYPOGRAPHY_PLATFORM_ORDER)
    used = set()
    for cells in rows.values():
        used.update(cells.keys())
    cols = [p for p in TYPOGRAPHY_PLATFORM_ORDER if p in used]
    # плюс «прочие» в конце по алфавиту
    extras = sorted(used - set(cols))
    cols += extras

    # колонка «Шрифт» (если есть единый fontFamily) — для упрощения покажем основной
    head = "| Стиль |" + "|".join(f" {c} " for c in cols) + "|\n"
    sep = "|---|" + "|".join("---" for _ in cols) + "|\n"
    body = []
    for logical in sorted(rows.keys()):
        cells = rows[logical]
        cells_md = []
        for c in cols:
            cells_md.append(fmt_typography_cell(cells.get(c)))
        body.append(f"| **{logical}** | " + " | ".join(cells_md) + " |\n")
    return head + sep + ''.join(body)


def cmd_typography(cache_dir, out_path):
    styles = json.load(open(os.path.join(cache_dir, 'styles.json')))
    nodes = json.load(open(os.path.join(cache_dir, 'style-nodes.json')))
    fills = [s for s in styles['meta']['styles']
             if s['style_type'] == 'TEXT' and not s['name'].startswith('[Deprecated]')]

    # сгруппировать
    by_cat = {'main': {}, 'okkolokino': {}, 'other': {}}
    family_counter = Counter()
    for s in fills:
        nid = s['node_id']
        node = nodes['nodes'].get(nid)
        if not node: continue
        cat, logical, suf = classify_style(s['name'], s)
        props = extract_typography_props(node)
        if props.get('fontFamily'):
            family_counter[props['fontFamily']] += 1
        by_cat[cat].setdefault(logical, {})[suf] = props

    # собрать markdown
    L = []
    L.append("# Типографика — Tokens [mobile & web]\n")
    L.append("> Источник: file **🦖 Tokens [mobile & web]** (`vztN8doGwBZOCbpDf2PhKR`), страница **Text Styles** — node `3:9`. "
             "Опубликованных TEXT-стилей — **{}**. Резолв: REST `/styles` + дозапрос `/nodes`.\n".format(len(fills)))
    L.append("\n**Формат ячейки:** `<size>/<line-height> · <weight>` (точно как в стиле Figma). "
             "Опциональная добавка `· ls 0.13` — letter-spacing.\n")
    L.append("\n**Шрифты в файле:** " + ', '.join(f"`{f}` ({n})" for f, n in family_counter.most_common(5)) + "\n")

    L.append("\n---\n\n## Основные стили\n")
    L.append(render_typography_section(by_cat['main'], TYPOGRAPHY_PLATFORM_ORDER))

    if by_cat['okkolokino']:
        L.append("\n---\n\n## Okkolokino (sub-brand)\n")
        L.append("Стили раздела Окколокино (помечены в описании стиля или по группе `Media/*`).\n\n")
        L.append(render_typography_section(by_cat['okkolokino'], TYPOGRAPHY_PLATFORM_ORDER))

    if by_cat['other']:
        L.append("\n---\n\n## Прочие\n")
        L.append("Спец-стили (`Godzilla`, `Spasibo`, `Meta` и т.п.) — для отдельных продуктовых контекстов.\n\n")
        L.append(render_typography_section(by_cat['other'], TYPOGRAPHY_PLATFORM_ORDER))

    L.append("""
---

## Правила выбора стиля

> Раздел редактируется вручную и **не перезаписывается** при `sync`.

| Контекст | Стиль |
|---|---|
| Заголовок раздела (mobile) | `Label Large/iPhone` (или платформенный аналог) |
| Заголовок раздела (tablet) | `Label Large/iPad` |
| Подзаголовок / описание | `Subtitles/...` |
| Текст параграфа | `Body 2/...` или `Body 3/...` в зависимости от плотности |
| Акцентный текст в карточке | `Body N Accent/...` |
| Caption / мелкие пояснения | `Label Small/...` или `Caption/...` |
| Кнопка | `Button Small/...` или `Button/...` |
| Меню (sidebar/dropdown) | `Menu Item/...` |
| Декоративный (промо, splash) | `Decorative/...` |
| Возрастные знаки | `Age Mark/...` |

**Правила парных платформ:** для одного экрана выбирай суффикс по таргет-устройству — на iPhone берём `/iPhone` или `/iPhone SE`, на iPad `/iPad`, на Web по брейкпоинту (`320+` / `600+` / `1320+` / `1720+` или семантические `Mobile 0+` / `Tablet 600+` / `Desktop 1720+`).

**Шрифты:** базовый шрифт интерфейса — `Suisse Int'l` (основной набор). Okkolokino sub-brand использует свой набор (см. колонки таблицы).

---

## Обновление

```bash
bash scripts/figma-sync-tokens.sh typography
```

Скрипт перепишет основной контент. Раздел «Правила выбора стиля» сохраняется.
""")

    # Сохранение ручного раздела при пересборе (если он уже есть)
    rules_block = ''
    if os.path.exists(out_path):
        old = open(out_path).read()
        m = re.search(r'(## Правила выбора стиля\n.*?)(?=\n## Обновление|\Z)', old, re.S)
        if m:
            rules_block = '\n' + m.group(1).rstrip() + '\n\n---\n\n'

    new_text = ''.join(L)
    if rules_block:
        # заменить дефолтный rules-блок на ручной
        new_text = re.sub(
            r'\n## Правила выбора стиля\n.*?\n\n---\n\n## Обновление\n',
            rules_block + '## Обновление\n',
            new_text, count=1, flags=re.S
        )

    with open(out_path, 'w') as f:
        f.write(new_text)


# ============================================================
# SPACING and CORNER-RADIUS — NUMBER variables (Plugin API)
# ============================================================

def cmd_spacing(cache_dir, out_path):
    """Создать скелет spacing.md с маркерами для Plugin API."""
    write_number_var_skeleton(
        out_path=out_path,
        title='Spacing',
        source_node='2280:155798',
        source_page='Spacing',
        intro=("Токены отступов: внутренние padding'и компонентов, gap'ы между элементами, "
               "размеры секций и грид-промежутки. Это **NUMBER variables** Figma."),
        marker='VARDEFS_FROM_PLUGIN_API:spacing',
        rules=DEFAULT_SPACING_RULES,
        target_arg='spacing',
    )


def cmd_corner_radius(cache_dir, out_path):
    write_number_var_skeleton(
        out_path=out_path,
        title='Corner-radius',
        source_node='2287:157374',
        source_page='Corner-radius',
        intro=("Токены скруглений углов компонентов и контейнеров. Это **NUMBER variables** Figma."),
        marker='VARDEFS_FROM_PLUGIN_API:corner-radius',
        rules=DEFAULT_CORNER_RADIUS_RULES,
        target_arg='corner-radius',
    )


DEFAULT_SPACING_RULES = """\
| Контекст | Токен |
|---|---|
| Внутренний padding кнопки/чипса (H/V) | `spacing.s` / `spacing.xs` (зависит от размера компонента) |
| Gap между элементами в строке (Chips, Tabs) | `spacing.s` |
| Внутренний padding карточек контента | `spacing.m` или `spacing.l` |
| Отступ между секциями экрана | `spacing.xl` или больше |
| Inset от безопасной зоны до контента | `spacing.l` (mobile) / `spacing.xl` (tablet) |

Конкретные значения см. в таблице выше. Между mobile и web/tablet token-имена общие — меняются **значения** под брейкпоинт через моды.
"""

DEFAULT_CORNER_RADIUS_RULES = """\
| Контекст | Токен |
|---|---|
| Маленькие чипсы, теги | `radius.s` (≈ 8) |
| Кнопки (мелкая / средняя) | `radius.m` (≈ 12) |
| Карточки контента, постеры | `radius.l` (≈ 16) |
| Большие сабшиты, шторки | `radius.xl` (≈ 20–24) |
| Полностью круглые (avatars, icon buttons) | `radius.full` / 9999 |

Значения отличаются по платформе — см. колонки таблицы выше.
"""


def write_number_var_skeleton(out_path, title, source_node, source_page, intro,
                              marker, rules, target_arg):
    """Каркас файла для NUMBER vars (заполняется потом из Plugin API)."""
    rules_block = ''
    if os.path.exists(out_path):
        old = open(out_path).read()
        m = re.search(r'(## Правила выбора\n.*?)(?=\n## Обновление|\Z)', old, re.S)
        if m:
            rules_block = m.group(1).rstrip() + '\n\n---\n\n'

    if not rules_block:
        rules_block = "## Правила выбора\n\n" + rules + "\n---\n\n"
    L = [
        f"# {title} — Tokens [mobile & web]\n",
        f"> Источник: file **🦖 Tokens [mobile & web]** (`{TOKENS_FILE_KEY}`), "
        f"страница **{source_page}** — node `{source_node}`. "
        f"Токены — NUMBER variables Figma (REST не отдаёт значений, забираются через Plugin API).\n\n",
        intro + "\n\n",
        "## Токены\n\n",
        f"<!-- {marker} — заполняется через use_figma + figma.variables.* -->\n\n",
        "_Если таблица пустая или содержит маркер выше — запусти команду из раздела «Обновление»; "
        "затем скил `design-figma-libraries` пройдётся через MCP `use_figma` Plugin API "
        "и впишет значения._\n\n",
        "---\n\n",
        rules_block,
        f"## Обновление\n\n```bash\nbash scripts/figma-sync-tokens.sh {target_arg}\n```\n\n",
        f"Скрипт обновит шапку и скелет. Resolved-значения NUMBER-переменных подставляет скил через "
        f"`use_figma` (figma.variables.getLocalVariableCollectionsAsync → фильтр FLOAT → temp TEXT-узел → REST).\n",
        "Раздел «Правила выбора» сохраняется при пересборе.\n",
    ]
    with open(out_path, 'w') as f:
        f.write(''.join(L))


# ============================================================
# main
# ============================================================

if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'colors':
        cmd_colors(sys.argv[2], sys.argv[3])
    elif cmd == 'icons':
        cmd_icons(sys.argv[2], sys.argv[3])
    elif cmd == 'illustrations':
        cmd_illustrations(sys.argv[2], sys.argv[3])
    elif cmd == 'typography_fetch':
        cmd_typography_fetch(sys.argv[2])
    elif cmd == 'typography':
        cmd_typography(sys.argv[2], sys.argv[3])
    elif cmd == 'spacing':
        cmd_spacing(sys.argv[2], sys.argv[3])
    elif cmd == 'corner_radius':
        cmd_corner_radius(sys.argv[2], sys.argv[3])
    else:
        print(f"unknown cmd: {cmd}", file=sys.stderr); sys.exit(2)
