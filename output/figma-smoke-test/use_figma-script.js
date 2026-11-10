/**
 * Эквивалент smoke-теста для инструмента `use_figma` (Plugin API через Figma MCP).
 *
 * Запускать только после загрузки навыка `figma-use` — он обязателен перед
 * каждым вызовом `use_figma`. Отправлять как единый скрипт в инструмент.
 *
 * Отличия от варианта для development-плагина (code.js):
 *   - нет `figma.closePlugin()` и `figma.notify()` (в use_figma они запрещены);
 *   - нет обёртки async IIFE — код выполняется в async-контексте;
 *   - результат отдаётся только через `return`;
 *   - возвращаются ВСЕ созданные node id (правило 15 навыка figma-use).
 */

const TOKENS = {
  bgPrimary: '#000000',
  surfaceSecondary: '#1B1A1D',
  surfaceThird: '#2C2B2F',
  accent: '#4137DF',
  positive: '#12B77C',
  textPrimary: '#FFFFFFF5',
  textSecondary: '#FFFFFFC7',
  textThird: '#FFFFFF8F',
  spacing350: 24,
  spacing250: 16,
  spacing200: 12,
  radius700: 16,
  radius400: 8,
  radiusRound: 9999,
};

const FONT_CANDIDATES = {
  semibold: [
    ['Suisse Int\'l', 'SemiBold'],
    ['Suisse Int\'l', 'Semibold'],
    ['Suisse Int\'l', 'Demi Bold'],
    ['Suisse Int\'l', 'Medium'],
    ['Inter', 'Semi Bold'],
    ['Inter', 'Medium'],
  ],
  regular: [
    ['Suisse Int\'l', 'Regular'],
    ['Inter', 'Regular'],
  ],
};

function hexToPaint(hex) {
  const raw = hex.replace('#', '');
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

async function loadFirstFont(candidates) {
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

const fontSemibold = await loadFirstFont(FONT_CANDIDATES.semibold);
const fontRegular = await loadFirstFont(FONT_CANDIDATES.regular);

const createdNodeIds = [];

const frame = figma.createFrame();
frame.name = 'DS smoke test · Okko';
frame.layoutMode = 'VERTICAL';
frame.primaryAxisSizingMode = 'AUTO';
frame.counterAxisSizingMode = 'FIXED';
frame.resize(360, 100);
frame.itemSpacing = TOKENS.spacing250;
frame.paddingTop = TOKENS.spacing350;
frame.paddingBottom = TOKENS.spacing350;
frame.paddingLeft = TOKENS.spacing350;
frame.paddingRight = TOKENS.spacing350;
frame.cornerRadius = TOKENS.radius700;
frame.fills = [hexToPaint(TOKENS.bgPrimary)];
createdNodeIds.push(frame.id);

const title = figma.createText();
title.fontName = fontSemibold;
title.characters = 'Дизайн-система Okko';
title.fontSize = 20;
title.lineHeight = { unit: 'PIXELS', value: 26 };
title.fills = [hexToPaint(TOKENS.textPrimary)];
frame.appendChild(title);
createdNodeIds.push(title.id);

const subtitle = figma.createText();
subtitle.fontName = fontRegular;
subtitle.characters = 'Проверка связи с Figma: Plugin API, токены, auto-layout и текст.';
subtitle.fontSize = 13;
subtitle.lineHeight = { unit: 'PIXELS', value: 18 };
subtitle.letterSpacing = { unit: 'PIXELS', value: 0.13 };
subtitle.fills = [hexToPaint(TOKENS.textSecondary)];
frame.appendChild(subtitle);
subtitle.layoutSizingHorizontal = 'FILL';
createdNodeIds.push(subtitle.id);

const row = figma.createFrame();
row.name = 'Tokens / swatches';
row.layoutMode = 'HORIZONTAL';
row.primaryAxisSizingMode = 'AUTO';
row.counterAxisSizingMode = 'AUTO';
row.itemSpacing = TOKENS.spacing200;
row.paddingTop = TOKENS.spacing200;
row.paddingBottom = TOKENS.spacing200;
row.paddingLeft = TOKENS.spacing200;
row.paddingRight = TOKENS.spacing200;
row.cornerRadius = TOKENS.radius400;
row.fills = [hexToPaint(TOKENS.surfaceSecondary)];
frame.appendChild(row);
createdNodeIds.push(row.id);

for (const [colorHex, radius] of [
  [TOKENS.accent, TOKENS.radius400],
  [TOKENS.surfaceThird, TOKENS.radius400],
  [TOKENS.positive, TOKENS.radiusRound],
]) {
  const swatch = figma.createRectangle();
  swatch.resize(32, 32);
  swatch.cornerRadius = Math.min(radius, 16);
  swatch.fills = [hexToPaint(colorHex)];
  row.appendChild(swatch);
  createdNodeIds.push(swatch.id);
}

const footnote = figma.createText();
footnote.fontName = fontRegular;
footnote.characters = 'spacing.350 · corner-radius.700 · Body 3 · H3';
footnote.fontSize = 13;
footnote.lineHeight = { unit: 'PIXELS', value: 18 };
footnote.letterSpacing = { unit: 'PIXELS', value: 0.13 };
footnote.fills = [hexToPaint(TOKENS.textThird)];
frame.appendChild(footnote);
createdNodeIds.push(footnote.id);

// Правило 13: новые top-level ноды не ставим в (0,0).
let maxRight = -Infinity;
for (const node of figma.currentPage.children) {
  if (node.id === frame.id) continue;
  maxRight = Math.max(maxRight, node.x + node.width);
}
frame.x = maxRight === -Infinity ? 0 : maxRight + 200;
frame.y = 0;

return {
  createdNodeIds,
  rootNodeId: frame.id,
  count: createdNodeIds.length,
  fontTitle: fontSemibold.family + ' ' + fontSemibold.style,
  fontBody: fontRegular.family + ' ' + fontRegular.style,
};
