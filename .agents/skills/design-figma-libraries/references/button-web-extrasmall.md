# Button · Web · ExtraSmall — проверка геометрии

Сохранено 2026-10-14 по работе в Figma 2026-10-12. Это снимок конкретной задачи; перед записью перечитай живые узлы. Актуальные токены проверяй через DS Librarian. Публикация и реализация в коде не проверялись.

## Источники и область

Работа выполнена в [Extra Small button](https://www.figma.com/design/8HSaM3phwMCpOf118T9mOz/Extra-Small-button?node-id=26093-350409): fileKey `8HSaM3phwMCpOf118T9mOz`, страница `26086:343528`, Button COMPONENT_SET `26093:350409`.

Добавлено 35 вариантов `Size=ExtraSmall` **только для Rectangle Secondary**; рабочий набор увеличился с 882 до 917. Более поздний [контекст основной Lib-Web](buttons-web.md) также фиксирует 917 вариантов и ExtraSmall. Не считай совпадение nodeId доказательством идентичности файлов: текущий источник и связи проверяй по актуальной ссылке пользователя.

iOS-референс: fileKey `rMcDm5qGp4CXkXXddEbcMh`, Button `31182:4417`; ExtraSmall Rectangle Secondary Rest — iPhone `35550:13165`, iPad `35550:13138`.

| Breakpoint | Text=true | Text=false | Всего |
|---|---|---|---:|
| Mobile 320+ | Rest, Pressed, Disabled, Loading, Progress | Rest, Pressed, Disabled, Loading | 9 |
| Tablet 600+ | Rest, Hover, Pressed, Focus, Disabled, Loading, Progress | Rest, Hover, Pressed, Focus, Disabled, Loading | 13 |
| Desktop 1720+ | Rest, Hover, Pressed, Focus, Disabled, Loading, Progress | Rest, Hover, Pressed, Focus, Disabled, Loading | 13 |

## Геометрия, проверенная в Main

| Параметр, px | Mobile | Tablet | Desktop |
|---|---:|---:|---:|
| Высота | 28 | 32 | 32 |
| Радиус кнопки | 6 | 8 | 8 |
| Боковые отступы с текстом | 8 | 10 | 10 |
| Gap между иконкой и текстовой группой | 4 | 6 | 6 |
| Иконка с текстом | 12 | 16 | 16 |
| Иконка без текста | 16 | 18 | 18 |
| Подпись: font size / line height | 11 / 12 | 13 / 14 | 13 / 14 |

Использованы существующие привязки `control/extra-small/…/phone` и `…/tablet`. Для Desktop в этой задаче приняты параметры Tablet: это локальное решение, не универсальное правило платформы. В прочитанном Figma-наборе не было полного отдельного комплекта Desktop ExtraSmall; при этом `icon-only/padding-horizontal/desktop` существовал. Meta/Kids отдельно не проверялись.

Mobile-подпись использует импортированный iOS-стиль с key `a4e53eb7c1985cd5e252b8ce285fa53b198fe8e0`; Tablet/Desktop — существующий Web-стиль `d80fb5d55be97fe2b68e44bec27bc8bac0b96eb5`. Интерлиньяж Tablet/Desktop 14 отличается от iPad-референса 16.

## Исправления и проверка

- У 12 внешних `_Button - Border` для Hover/Pressed/Focus на Tablet/Desktop радиус исправлен с унаследованных 12–14 на **10 px**: радиус кнопки 8 плюс внешний отступ 2. Использована существующая привязка `corner-radius/450`.
- Обводка: `x=y=-2`, ширина и высота равны размеру кнопки плюс 4, constraints STRETCH по обеим осям. Устранён лишний выступ справа. На короткой и длинной подписях с выключенной иконкой отступ сохранился по 2 px со всех сторон.
- В девяти Loading/Progress `_loading gradient` занимает всю высоту, начинается с `y=0`; у кнопки включён `clipsContent`, чтобы обрезать градиент по скруглению. Сохранена прозрачность: Loading 0,5, Progress 1.
- После клонирования восстановлены потерянные `componentPropertyReferences` по соответствующим слоям Small: Text, Icon, instance swap, Tooltip. Реальная смена подписи и скрытие иконки проверены на экземплярах.
- Все 35 вариантов проверены визуально. Временные экземпляры удалены. В этой задаче постоянный Overview не создавался; более поздний Overview основной Lib-Web описан в контексте кнопок.

Примеры в рабочем файле: Mobile Rest `46845:18145`, Tablet Rest `46845:18283`, Desktop Rest `46845:18199`, Desktop Hover `46845:18229`, Pressed `46845:18238`, Focus `46845:18246`.
