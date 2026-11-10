/**
 * Минимальная проверка окружения плагинов Figma.
 *
 * Намеренно НЕ использует: шрифты, async/await, auto-layout, текст, цвета из токенов.
 * Задача — отделить проблему окружения/манифеста от проблемы в основном коде.
 *
 * Если этот плагин создаёт квадрат — окружение в порядке, и причина в code.js.
 * Если он тоже падает — дело в манифесте или в самом Figma Desktop.
 */

const rect = figma.createRectangle();
rect.name = 'minimal check';
rect.resize(120, 120);
rect.cornerRadius = 12;
rect.fills = [{ type: 'SOLID', color: { r: 0.25, g: 0.22, b: 0.87 } }];

const center = figma.viewport.center;
rect.x = Math.round(center.x - rect.width / 2);
rect.y = Math.round(center.y - rect.height / 2);

figma.currentPage.selection = [rect];
figma.viewport.scrollAndZoomIntoView([rect]);

console.log('minimal check created: ' + rect.id);
figma.closePlugin('OK: квадрат создан, id ' + rect.id);
