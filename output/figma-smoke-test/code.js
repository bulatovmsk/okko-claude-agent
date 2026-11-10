/**
 * Okko DS Smoke Test — development plugin for Figma.
 *
 * Создаёт на текущей странице один тестовый фрейм и ничего больше не меняет:
 * существующие ноды, инстансы и variables не затрагиваются.
 *
 * Значения взяты из source of truth проекта (design-system/tokens/):
 *   color.background.solid.primary  #000000
 *   color.fill.solid.secondary      #1B1A1D
 *   color.fill.solid.third          #2C2B2F
 *   color.fill.solid.accent         #4137DF
 *   color.fill.solid.positive       #12B77C
 *   color.text-icon.primary         #FFFFFFF5
 *   color.text-icon.secondary       #FFFFFFC7
 *   color.text-icon.third           #FFFFFF8F
 *   spacing.350 = 24, spacing.250 = 16, spacing.200 = 12, spacing.100 = 4
 *   corner-radius.700 = 16, corner-radius.400 = 8, corner-radius.round = 9999
 *   H3 = 20/26 · 600, Body 3 = 13/18 · 400 · ls 0.13
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
  spacing100: 4,
  radius700: 16,
  radius400: 8,
  radiusRound: 9999,
  h3: { size: 20, lineHeight: 26, weight: 'semibold' },
  body3: { size: 13, lineHeight: 18, letterSpacing: 0.13, weight: 'regular' },
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
  const r = parseInt(raw.slice(0, 2), 16) / 255;
  const g = parseInt(raw.slice(2, 4), 16) / 255;
  const b = parseInt(raw.slice(4, 6), 16) / 255;
  const paint = { type: 'SOLID', color: { r, g, b } };
  if (raw.length === 8) {
    paint.opacity = parseInt(raw.slice(6, 8), 16) / 255;
  }
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
  throw new Error('Не удалось загрузить ни один шрифт. Пробовали: ' + tried.join(', '));
}

function makeText(characters, font, spec, colorHex) {
  const text = figma.createText();
  // fontName принимает строго { family, style } — лишние поля ломают присвоение.
  text.fontName = { family: font.family, style: font.style };
  text.characters = characters;
  text.fontSize = spec.size;
  text.lineHeight = { unit: 'PIXELS', value: spec.lineHeight };
  if (spec.letterSpacing) {
    text.letterSpacing = { unit: 'PIXELS', value: spec.letterSpacing };
  }
  text.fills = [hexToPaint(colorHex)];
  return text;
}

function makeSwatch(size, radius, colorHex) {
  const rect = figma.createRectangle();
  rect.resize(size, size);
  rect.cornerRadius = Math.min(radius, size / 2);
  rect.fills = [hexToPaint(colorHex)];
  return rect;
}

/**
 * Позиция для нового фрейма — не в (0,0).
 * При documentAccess: dynamic-page children текущей страницы доступны, но
 * подстраховываемся центром вьюпорта, чтобы плагин не падал на пустом файле.
 */
function freePositionOnPage(width, height) {
  try {
    const children = figma.currentPage.children;
    if (children.length) {
      let maxRight = -Infinity;
      for (const node of children) {
        maxRight = Math.max(maxRight, node.x + node.width);
      }
      if (Number.isFinite(maxRight)) return { x: maxRight + 200, y: 0 };
    }
  } catch (error) {
    // dynamic-page: синхронный доступ к children недоступен — используем вьюпорт
  }
  const center = figma.viewport.center;
  return {
    x: Math.round(center.x - width / 2),
    y: Math.round(center.y - height / 2),
  };
}

(async () => {
  const createdNodeIds = [];
  const notes = [];

  try {
    // Идемпотентность: убираем результат прошлого запуска, чтобы повторный
    // прогон не плодил копии. Удаляем только свои ноды — фрейм с нашим именем
    // и осиротевшие тексты, оставшиеся от прерванного прогона.
    try {
      const stale = figma.currentPage.children.filter((node) => {
        if (node.type === 'FRAME') return node.name === 'DS smoke test · Okko';
        if (node.type === 'TEXT') {
          return (
            node.name.indexOf('Проверка связи с Figma') === 0 ||
            node.name.indexOf('spacing.350') === 0
          );
        }
        return false;
      });
      for (const node of stale) node.remove();
      if (stale.length) notes.push('Удалён прошлый прогон: ' + stale.length);
    } catch (cleanupError) {
      notes.push('Прошлый прогон не удалён: ' + cleanupError.message);
    }

    const fontSemibold = await loadFirstFont(FONT_CANDIDATES.semibold);
    const fontRegular = await loadFirstFont(FONT_CANDIDATES.regular);
    notes.push('Шрифт заголовка: ' + fontSemibold.family + ' ' + fontSemibold.style);
    if (fontSemibold.family !== 'Suisse Int\'l') {
      notes.push('Suisse Int\'l недоступен — использован фолбэк, размеры токенов сохранены.');
    }

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
    frame.clipsContent = false;
    createdNodeIds.push(frame.id);

    const title = makeText(
      'Дизайн-система Okko',
      fontSemibold,
      TOKENS.h3,
      TOKENS.textPrimary
    );
    frame.appendChild(title);
    createdNodeIds.push(title.id);

    const subtitle = makeText(
      'Проверка связи с Figma: Plugin API, токены, auto-layout и текст.',
      fontRegular,
      TOKENS.body3,
      TOKENS.textSecondary
    );
    // Сначала добавить в auto-layout родителя, только потом ставить FILL:
    // до appendChild нода ещё не ребёнок auto-layout фрейма, и сеттер падает.
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

    const swatches = [
      ['fill.solid.accent', TOKENS.accent, TOKENS.radius400],
      ['fill.solid.third', TOKENS.surfaceThird, TOKENS.radius400],
      ['fill.solid.positive', TOKENS.positive, TOKENS.radiusRound],
    ];
    for (const [, colorHex, radius] of swatches) {
      const swatch = makeSwatch(32, radius, colorHex);
      row.appendChild(swatch);
      createdNodeIds.push(swatch.id);
    }

    const footnote = makeText(
      'spacing.350 · corner-radius.700 · Body 3 · H3',
      fontRegular,
      TOKENS.body3,
      TOKENS.textThird
    );
    frame.appendChild(footnote);
    createdNodeIds.push(footnote.id);

    const position = freePositionOnPage(frame.width, frame.height);
    frame.x = position.x;
    frame.y = position.y;

    figma.currentPage.selection = [frame];
    figma.viewport.scrollAndZoomIntoView([frame]);

    const summary = {
      createdNodeIds,
      rootNodeId: frame.id,
      count: createdNodeIds.length,
      notes,
    };
    console.log(JSON.stringify(summary, null, 2));
    figma.notify('DS smoke test создан: ' + createdNodeIds.length + ' нод');
    figma.closePlugin();
  } catch (error) {
    figma.notify('Ошибка: ' + error.message, { error: true });
    figma.closePlugin('Ошибка: ' + error.message);
  }
})().catch((error) => {
  // Страховка: ошибка вне try/catch не должна превращаться в общий баннер
  // «An error occurred while loading the plugin environment».
  const message = error && error.message ? error.message : String(error);
  figma.closePlugin('Критическая ошибка: ' + message);
});
