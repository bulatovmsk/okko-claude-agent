# Календарь: замена цветов

Дата: 20 октября 2026. [Страница «Календарь»](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=36332-517).

Обновлены **1928 уникальных слоёв**. Проверены все **35 мастеров**, **15 929 слоёв в их деревьях** и **8 узлов вне мастеров**. Полный охват: **15 937 узлов**, включая саму страницу и контейнеры.

Обновлены Primary/Secondary/Third/Fourth текста и иконок, Fill Primary/Secondary/Live, Border Contour и Glassy Secondary. Изменения базовых мастеров наследуются их вложениями; оставшиеся переопределения заменены адресно. Из 3404 первоначальных ссылок на старые paint-стили в мастерах удалены 2917, осталось 487.

Дополнительных однозначных замен на static-токены не найдено.

## Оставшиеся 487 применений в мастерах

| Где | Старый стиль | Количество | Причина / варианты |
|---|---|---:|---|
| Слои Photo | Fill/Solid: hover & focus/Third, key 7190d7e2… | 437 | Старый радиальный фон. Возможны существующий color/fill/technical/placeholder по роли заглушки фотографии или актуальный color/fill/solid/hover-focus/third, который линейный. Варианты меняют вид по-разному; выбор оставлен пользователю. |
| Bet Logo, region0 | Color/fill/solid/hover-focus/Third, тот же key 7190d7e2… | 25 | Старый радиальный градиент. Актуальный hover-focus/third линейный; для части логотипа возможен inverse. Неоднозначно. |
| Bet Logo, region1 | Fill/Solid/Primary, key 974f85fc… | 25 | По исходной библиотеке это Inverse → color/fill/solid/inverse. Источник Bet Logo исправлен ранее, но старые локальные версии/переопределения сохраняют регионы. Figma не разрешает запись vector network внутри инстанса; требуется обновление библиотечной версии и проверка переопределений. |

У Photo и Bet один старый библиотечный ключ, но разные роли. Замена для Photo должна применяться к соответствующим слоям, а выбор для Bet рассматриваться отдельно.

Пример Photo: [вложение в Calendar item, Announcement](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=36332-6433); ID одного из слоёв: I36332:6443;789:298118. Пример Bet: [Tournament Header, Size=1720+](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=36332-6925).

### Все мастера с остатками

В столбце Bet указано число ссылок на регионы: по две на каждый из 25 логотипов.

| Мастер | Photo | Bet |
|---|---:|---:|
| [Calendar item → Size=1720+, State=Announcement](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=36332-6433) | 2 | 0 |
| [Calendar item → Size=1720+, State=Live](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=36332-6464) | 2 | 0 |
| [Calendar item → Size=1720+, State=Ended](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=36332-6497) | 2 | 0 |
| [Calendar item → Size=1320+, State=Announcement](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=36332-6530) | 2 | 0 |
| [Calendar item → Size=1320+, State=Ended](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=36332-6561) | 2 | 0 |
| [Calendar item → Size=1320+, State=Live](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=36332-6594) | 2 | 0 |
| [Calendar item → Size=600+, State=Announcement](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=36332-6627) | 2 | 0 |
| [Calendar item → Size=600+, State=Ended](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=36332-6658) | 2 | 0 |
| [Calendar item → Size=600+, State=Live](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=36332-6691) | 2 | 0 |
| [Calendar item → Size=375+, State=Announcement](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=36332-6725) | 2 | 0 |
| [Calendar item → Size=375+, State=Ended](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=36332-6756) | 2 | 0 |
| [Calendar item → Size=320+, State=Ended](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=36332-6789) | 2 | 0 |
| [Calendar item → Size=375+, State=Live](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=36332-6823) | 2 | 0 |
| [Calendar item → Size=320+, State=Announcement](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=36332-6857) | 2 | 0 |
| [Calendar item → Size=320+, State=Live](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=36332-6889) | 2 | 0 |
| [.Tournament Header → Size=1720+](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=36332-6925) | 0 | 2 |
| [.Tournament Header → Size=1320+](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=36332-6932) | 0 | 2 |
| [.Tournament Header → Size=600+](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=36332-6939) | 0 | 2 |
| [.Tournament Header → Size=375+](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=36332-6947) | 0 | 2 |
| [.Tournament Header → Size=320+](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=36332-6954) | 0 | 2 |
| [Widget (with Label) → Виджет календаря 1320+](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=36332-6152) | 116 | 6 |
| [Widget (with Label) → Виджет календаря / 1720+](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=36332-7043) | 33 | 4 |
| [Widget (with Label) → Виджет календаря / 600+](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=36332-7071) | 43 | 8 |
| [Widget (with Label) → Виджет календаря / 960+](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=36332-7253) | 59 | 6 |
| [Widget (with Label) → Виджет календаря / 320+](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=36332-7445) | 78 | 8 |
| [Widget (with Label) → Виджет календаря / 375+](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=36332-7617) | 78 | 8 |

Полный список 487 записей, включая ID слоя, свойство/номер региона, исходный стиль и ID вложенного инстанса, записан в JSON-аудите.

## Вне мастеров

Сохранена одна старая заливка Background/Solid/Primary у [секции Widget (with Label)](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=36332-6150). Это оформление холста вне мастер-компонентов; оно не редактировалось.

Light/Kids-контекстов со старыми цветами на этой странице не найдено. Сырые цвета без токена и изображения сохранены. Новые дизайн-переменные, aliases, коллекции и стили не создавались. Использованы существующие библиотечные ресурсы. Геометрия, тексты, типографика, свойства вариантов и прочие переопределения не менялись. Инстансы не отсоединялись, не заменялись и не сбрасывались.

## Проверка

Полный программный обход по мастерам и остальным узлам: fills/strokes, регионы векторов, градиентные остановки, текстовые диапазоны, эффекты и скрытые вложения. Каждый мастер входит ровно в одну из семи проверенных групп. Ошибок записи и финального аудита, неразрешённых ссылок нет. Панель Selection colors вручную не проверялась.

При выборе всей страницы ещё будут видны перечисленные 487 применений старых стилей и одна заливка секции. Отчёт не означает, что страница полностью очищена от старых цветов.

