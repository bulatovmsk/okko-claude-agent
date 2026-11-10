/**
 * Okko Doc Builder — перенос черновиков документации Select · Web в Figma.
 *
 * ВАЖНО, что делает и чего не делает:
 *   - дополняет ТОЛЬКО выбранный фрейм `Guide · Select · Web` или `Passport · Select · Web`;
 *   - только добавляет новые секции в конец, существующие ноды не трогает;
 *   - идемпотентен: секция с таким именем уже есть — пропускается;
 *   - оформление снимает с живого файла (шрифты, размеры, цвета берёт из существующих
 *     текстов выбранного фрейма), а не подставляет выдуманные значения;
 *   - ничего не отсоединяет и не меняет исходный компонент Select.
 *
 * Контент встроен из черновиков output/select-web-docs/.
 */

const CONTENT = __CONTENT_JSON__;

const FALLBACK = {
  fonts: {
    title: { family: "Suisse Int'l", style: 'Medium' },
    body: { family: "Suisse Int'l", style: 'Regular' },
  },
  colors: {
    text: '#FFFFFFF5',
    text2: '#FFFFFFC7',
    text3: '#FFFFFF8F',
    surface: '#1B1A1D',
    surface2: '#2C2B2F',
    accent: '#616CFB',
    do: '#12B77C',
    dont: '#F25857',
  },
  sizes: { title: 24, h3: 18, body: 14, code: 12 },
  gap: { section: 48, block: 12, pad: 24, radius: 16 },
};

function hexToPaint(hex) {
  const raw = String(hex).replace('#', '');
  const paint = {
    type: 'SOLID',
    color: {
      r: parseInt(raw.slice(0, 2), 16) / 255,
      g: parseInt(raw.slice(2, 4), 16) / 255,
      b: parseInt(raw.slice(4, 6), 16) / 255,
    },
  };
  if (raw.length === 8) paint.opacity = parseInt(raw.slice(6, 8), 16) / 255;
  return paint;
}

function solidPaint(fills) {
  if (!fills || fills === figma.mixed || !fills.length) return null;
  for (const f of fills) {
    if (f && f.type === 'SOLID' && f.visible !== false) {
      const paint = { type: 'SOLID', color: { r: f.color.r, g: f.color.g, b: f.color.b } };
      if (typeof f.opacity === 'number') paint.opacity = f.opacity;
      return paint;
    }
  }
  return null;
}

async function loadFont(candidates) {
  const tried = [];
  for (const [family, style] of candidates) {
    try {
      await figma.loadFontAsync({ family, style });
      return { family, style };
    } catch (e) {
      tried.push(family + ' ' + style);
    }
  }
  throw new Error('Не удалось загрузить шрифт. Пробовали: ' + tried.join(', '));
}

function pickTarget() {
  const sel = figma.currentPage.selection;
  if (sel.length !== 1) {
    return { error: 'Выберите ровно один фрейм: Guide · Select · Web или Passport · Select · Web.' };
  }
  const node = sel[0];
  if (node.type !== 'FRAME' && node.type !== 'SECTION') {
    return { error: 'Выбранная нода — ' + node.type + ', а нужен фрейм или секция.' };
  }
  const isPassport = /passport/i.test(node.name);
  const isGuide = /guide/i.test(node.name);
  if (!isPassport && !isGuide) {
    return { error: 'В имени фрейма нет «Guide» или «Passport»: «' + node.name + '». Остановлено, чтобы не писать не туда.' };
  }
  return { target: node, doc: isPassport ? 'passport' : 'guide' };
}

/** Снимает оформление с живого фрейма: шрифты, размеры и цвета существующих текстов. */
function sampleStyle(target) {
  const style = {
    fonts: {
      title: { family: FALLBACK.fonts.title.family, style: FALLBACK.fonts.title.style },
      body: { family: FALLBACK.fonts.body.family, style: FALLBACK.fonts.body.style },
    },
    colors: {
      text: hexToPaint(FALLBACK.colors.text),
      text2: hexToPaint(FALLBACK.colors.text2),
      text3: hexToPaint(FALLBACK.colors.text3),
      surface: hexToPaint(FALLBACK.colors.surface),
      surface2: hexToPaint(FALLBACK.colors.surface2),
      accent: hexToPaint(FALLBACK.colors.accent),
    },
    sizes: {
      title: FALLBACK.sizes.title,
      h3: FALLBACK.sizes.h3,
      body: FALLBACK.sizes.body,
      code: FALLBACK.sizes.code,
    },
    contentWidth: 1200,
    sampled: false,
  };

  try {
    const texts = target.findAll((n) => n.type === 'TEXT');
    const info = [];
    for (const t of texts) {
      if (typeof t.fontSize !== 'number') continue;
      if (!t.fontName || t.fontName === figma.mixed) continue;
      info.push({ size: t.fontSize, font: t.fontName, fills: t.fills });
    }
    if (info.length) {
      info.sort((a, b) => b.size - a.size);
      const title = info[0];
      style.sizes.title = Math.min(Math.max(title.size, 18), 32);
      style.fonts.title = { family: title.font.family, style: title.font.style };
      const titlePaint = solidPaint(title.fills);
      if (titlePaint) style.colors.text = titlePaint;

      const counts = {};
      for (const it of info) {
        if (it.size < title.size) counts[it.size] = (counts[it.size] || 0) + 1;
      }
      let bodySize = null;
      let best = 0;
      for (const key in counts) {
        if (counts[key] > best) {
          best = counts[key];
          bodySize = Number(key);
        }
      }
      if (bodySize) {
        style.sizes.body = Math.min(Math.max(bodySize, 11), 18);
        const sample = info.find((it) => it.size === bodySize);
        if (sample) {
          style.fonts.body = { family: sample.font.family, style: sample.font.style };
          const bodyPaint = solidPaint(sample.fills);
          if (bodyPaint) style.colors.text2 = bodyPaint;
        }
      }
      style.sizes.h3 = Math.max(style.sizes.body + 2, Math.round(style.sizes.body * 1.25));
      style.sizes.code = Math.max(10, style.sizes.body - 2);
      style.sampled = true;
    }
  } catch (e) {
    // остаёмся на значениях токенов ДС
  }

  try {
    if (target.layoutMode && target.layoutMode !== 'NONE') {
      style.contentWidth =
        target.width - (target.paddingLeft || 0) - (target.paddingRight || 0);
    } else {
      // У фрейма без auto-layout ширину контентной колонки задаёт самый широкий ребёнок.
      let widest = 0;
      for (const child of target.children) widest = Math.max(widest, child.width);
      style.contentWidth = widest || target.width;
    }
  } catch (e) {
    style.contentWidth = 1200;
  }
  if (!style.contentWidth || style.contentWidth < 240) style.contentWidth = 1200;
  return style;
}

function makeText(value, font, size, paint, lineHeight) {
  const node = figma.createText();
  // fontName принимает строго { family, style }
  node.fontName = { family: font.family, style: font.style };
  node.characters = value;
  node.fontSize = size;
  node.lineHeight = { unit: 'PIXELS', value: Math.round(lineHeight) };
  node.fills = [paint];
  return node;
}

function vstack(name) {
  const frame = figma.createFrame();
  frame.name = name;
  frame.layoutMode = 'VERTICAL';
  frame.primaryAxisSizingMode = 'AUTO';
  frame.counterAxisSizingMode = 'FIXED';
  frame.itemSpacing = FALLBACK.gap.block;
  frame.fills = [];
  frame.clipsContent = false;
  return frame;
}

const created = [];
function track(node) {
  created.push(node.id);
  return node;
}

function renderTable(rows, style, width) {
  const cols = Math.max.apply(
    null,
    rows.map((r) => r.length)
  );
  const firstShare = cols > 2 ? 1.6 : 1;
  const totalShare = firstShare + (cols - 1);
  const widths = [];
  for (let c = 0; c < cols; c++) {
    widths.push(Math.round((width * (c === 0 ? firstShare : 1)) / totalShare));
  }

  const table = vstack('table');
  table.itemSpacing = 2;
  table.counterAxisSizingMode = 'FIXED';
  table.resize(width, 40);

  rows.forEach((cells, rowIndex) => {
    const row = figma.createFrame();
    row.name = 'row';
    row.layoutMode = 'HORIZONTAL';
    row.primaryAxisSizingMode = 'FIXED';
    row.counterAxisSizingMode = 'AUTO';
    row.itemSpacing = 2;
    row.fills = [];
    row.clipsContent = false;
    table.appendChild(row);
    row.resize(width, 24);
    track(row);
    const cellsInRow = [];

    for (let c = 0; c < cols; c++) {
      const cell = figma.createFrame();
      cell.name = 'cell';
      cell.layoutMode = 'VERTICAL';
      cell.primaryAxisSizingMode = 'AUTO';
      cell.counterAxisSizingMode = 'FIXED';
      cell.paddingTop = 8;
      cell.paddingBottom = 8;
      cell.paddingLeft = 12;
      cell.paddingRight = 12;
      cell.cornerRadius = 6;
      cell.fills = rowIndex === 0 ? [style.colors.surface2] : [style.colors.surface];
      cell.clipsContent = false;
      row.appendChild(cell);
      cell.resize(widths[c], 24);
      track(cell);
      cellsInRow.push(cell);

      const value = cells[c] === undefined ? '' : cells[c];
      const text = makeText(
        value,
        style.fonts.body,
        rowIndex === 0 ? style.sizes.body : style.sizes.body,
        rowIndex === 0 ? style.colors.text : style.colors.text2,
        style.sizes.body * 1.4
      );
      cell.appendChild(text);
      text.layoutSizingHorizontal = 'FILL';
      track(text);
    }

    // Высоту строки фиксируем по самой высокой ячейке и только потом растягиваем
    // остальные: если растянуть все ячейки сразу, hug-строка схлопывается.
    let maxHeight = 24;
    for (const c of cellsInRow) maxHeight = Math.max(maxHeight, c.height);
    row.counterAxisSizingMode = 'FIXED';
    row.resize(width, maxHeight);
    for (const c of cellsInRow) c.layoutSizingVertical = 'FILL';
  });

  return table;
}

function renderBullets(items, style) {
  const text = makeText(
    items.map((i) => '—  ' + i).join('\n'),
    style.fonts.body,
    style.sizes.body,
    style.colors.text2,
    style.sizes.body * 1.6
  );
  return text;
}

function renderBlock(block, style, width) {
  if (block.type === 'h3') {
    return makeText(block.text, style.fonts.title, style.sizes.h3, style.colors.text, style.sizes.h3 * 1.3);
  }
  if (block.type === 'p') {
    return makeText(block.text, style.fonts.body, style.sizes.body, style.colors.text2, style.sizes.body * 1.55);
  }
  if (block.type === 'bullets') {
    return renderBullets(block.items, style);
  }
  if (block.type === 'note') {
    const frame = vstack('note');
    frame.counterAxisSizingMode = 'FIXED';
    frame.resize(width, 20);
    frame.paddingTop = 10;
    frame.paddingBottom = 10;
    frame.paddingLeft = 14;
    frame.paddingRight = 14;
    frame.cornerRadius = 8;
    frame.fills = [style.colors.surface];
    const text = makeText(block.text, style.fonts.body, style.sizes.body, style.colors.text3, style.sizes.body * 1.5);
    frame.appendChild(text);
    text.layoutSizingHorizontal = 'FILL';
    track(text);
    return frame;
  }
  if (block.type === 'code') {
    const frame = vstack('code');
    frame.counterAxisSizingMode = 'FIXED';
    frame.resize(width, 20);
    frame.paddingTop = 12;
    frame.paddingBottom = 12;
    frame.paddingLeft = 14;
    frame.paddingRight = 14;
    frame.cornerRadius = 8;
    frame.fills = [style.colors.surface];
    const text = makeText(block.text, style.fonts.body, style.sizes.code, style.colors.text2, style.sizes.code * 1.5);
    frame.appendChild(text);
    text.layoutSizingHorizontal = 'FILL';
    track(text);
    return frame;
  }
  if (block.type === 'table') {
    return renderTable(block.rows, style, width);
  }
  return null;
}

function alreadyPresent(target, name) {
  return target.children.some((child) => child.name === name);
}

async function main() {
  const picked = pickTarget();
  if (picked.error) {
    figma.closePlugin(picked.error);
    return;
  }
  const target = picked.target;
  const document = CONTENT[picked.doc];
  if (!document || !document.sections.length) {
    figma.closePlugin('Нет контента для документа «' + picked.doc + '».');
    return;
  }

  const style = sampleStyle(target);

  style.fonts.title = await loadFont([
    [style.fonts.title.family, style.fonts.title.style],
    ["Suisse Int'l", 'Medium'],
    ['Inter', 'Semi Bold'],
    ['Inter', 'Medium'],
  ]);
  style.fonts.body = await loadFont([
    [style.fonts.body.family, style.fonts.body.style],
    ["Suisse Int'l", 'Regular'],
    ['Inter', 'Regular'],
  ]);

  const isAutoLayout = target.layoutMode && target.layoutMode !== 'NONE';
  const width = Math.round(style.contentWidth);
  const notes = [];
  if (!style.sampled) {
    notes.push('Оформление не считано с файла — применены токены ДС.');
  }

  let bottom = 0;
  if (!isAutoLayout) {
    for (const child of target.children) {
      bottom = Math.max(bottom, child.y + child.height);
    }
  }

  let createdSections = 0;
  let skipped = 0;

  for (let i = 0; i < document.sections.length; i++) {
    const section = document.sections[i];
    const name = section.title;
    if (alreadyPresent(target, name)) {
      skipped++;
      continue;
    }

    const frame = vstack(name);
    frame.itemSpacing = FALLBACK.gap.block;
    frame.counterAxisSizingMode = 'FIXED';
    frame.resize(width, 80);

    const heading = makeText(name, style.fonts.title, style.sizes.title, style.colors.text, style.sizes.title * 1.25);
    frame.appendChild(heading);
    heading.layoutSizingHorizontal = 'FILL';
    track(heading);

    for (const block of section.blocks) {
      const node = renderBlock(block, style, width);
      if (!node) continue;
      frame.appendChild(node);
      if (node.type === 'TEXT') {
        node.layoutSizingHorizontal = 'FILL';
      } else if (node.type === 'FRAME') {
        node.layoutSizingHorizontal = 'FIXED';
      }
      track(node);
    }

    target.appendChild(frame);
    if (isAutoLayout) {
      frame.layoutSizingHorizontal = 'FILL';
    } else {
      frame.x = 0;
      frame.y = bottom + (bottom ? FALLBACK.gap.section : 0);
      bottom = frame.y + frame.height;
    }
    track(frame);
    createdSections++;
  }

  const summary = {
    document: picked.doc,
    targetName: target.name,
    targetId: target.id,
    createdSections,
    skippedExisting: skipped,
    createdNodes: created.length,
    sampledFromFile: style.sampled,
    notes,
  };
  console.log(JSON.stringify(summary, null, 2));
  figma.closePlugin(
    'Готово: секций ' +
      createdSections +
      ', пропущено уже существующих ' +
      skipped +
      ', создано нод ' +
      created.length
  );
}

main().catch((error) => {
  const message = error && error.message ? error.message : String(error);
  figma.closePlugin('Ошибка: ' + message);
});
