# Списки — миграция цветов

[Страница в Figma](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=9821-75491)

## Результат

- Проверен **91 мастер** в старых и адаптивных списках, включая обычные ячейки, чекбоксы, радио, свитчи, выпадающие списки и список аккаунтов.
- В мастерах и вложениях проверены **6253 слоя**. Итоговый аудит всей страницы охватил **7810 узлов**, включая примеры и контейнеры вне мастеров.
- Обновлены **178 уникальных слоёв**. Прямые изменения базовых слоёв автоматически обновили множество наследующих инстансов; эти наследующие слои отдельно к числу прямых изменений не добавлялись.
- Число известных старых PAINT-привязок в рабочей области уменьшилось с **3498 до 29**.
- В **3 слоях** иконок на цветных контролах применён static white с сохранением видимой прозрачности. Эти изменения частично пересекаются со стандартными заменами.
- В финальном аудите нет ошибок чтения/записи и недоступных стилей. Проверены заливки, обводки, текстовые диапазоны, градиентные стопы, регионы векторов, эффекты и переменные.
- Ячейка списка аккаунтов проверена визуально после изменений. Selection colors вручную в интерфейсе не проверялся.

## Остатки для решения

**29 применений старых PAINT-стилей** сосредоточены в мастерах [Ячейка / Список аккаунтов](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5324-566) и [Список аккаунтов](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5336-31523). Скрытые вложенные слои тоже включены в аудит.

| Старый стиль | Применений | Где | Причина / варианты |
|---|---:|---|---|
| Primitives/Grey/Primary | 6 | Текст «Иван Иванов» в старой ячейке аккаунта и её инстансах. [Пример мастера](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5324-566) | color.text-icon.secondary либо color.text-icon.third. Требуется определить иерархию/контраст старого вспомогательного текста. |
| Primitives/Blueberry/15 | 6 | Лоадинг → Ellipse 30. [Пример мастера](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5324-566) | Нужно согласовать цвет и альфу лоадера: один существующий color-токен с прозрачностью фазы либо разные семантические уровни. Прямого соответствия Blueberry/15 не подтверждено. |
| Primitives/Blueberry/32 | 6 | Лоадинг → Ellipse 31. [Пример мастера](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5324-566) | Та же тройка фаз лоадера. Прозрачность и назначение не позволяют безопасно назначить произвольный UI-цвет по одному оттенку. |
| Primitives/Blueberry/60 | 6 | Лоадинг → Ellipse 32. [Пример мастера](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5324-566) | Та же тройка фаз лоадера. Требуется выбрать существующий color-токен и согласовать альфу для третьей фазы. |
| [Deprecated]/Brand/Partners/Sber | 3 | Сбер и фоновые слои старых банковских/социальных логотипов. [Пример мастера](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5336-31523) | Solid Sber ранее решено пока не менять. Для нестандартных применений в фонах социальных логотипов также требуется отдельное решение. |
| [Deprecated]/Brand/Social/Facebook | 1 | Facebook в списке аккаунтов. [Пример мастера](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5336-31523) | Подходящий актуальный токен фирменного Facebook в изученном наборе color не найден. Общий UI-accent не назначался; новый токен не создавался. |
| [Deprecated]/Brand/Social/VK | 1 | VK в списке аккаунтов. [Пример мастера](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5336-31523) | Подходящий актуальный токен фирменного VK в изученном наборе color не найден. Общий UI-accent не назначался; новый токен не создавался. |

Три оттенка Blueberry — **лоадер**, а не аватар: путь `Списки (Old) → Ячейка / Список аккаунтов → Данные справа → Лоадинг`. У него 3 фазы в 6 контекстах, всего 18 оставшихся заливок.

Дополнительно сохранены **6 привязок brand/partners/sber** в исходных элементах логотипов, согласно прежней договорённости. Это отдельные привязки, они не включены в счётчик 29 PAINT-стилей.

## Исключённые области и актуальные переменные

- В Light осталось **87 применений известных старых стилей**, отдельно от 29 рабочих. Прямые изменения в Light-вариантах не выполнялись; общие вложенные ресурсы могут наследовать обновление своих Dark-мастеров.
- В Light также сохранены 2 привязки primitives/electric900 внутри тех же старых Accent-заливок. Они не добавляются повторно к числу PAINT-применений.
- Вне мастеров осталось **15 старых привязок**: контейнеры, заголовки, примеры и служебные фреймы. Они учтены отдельно и напрямую не редактировались.
- color.fill.solid.inverse и color.fill.solid.accent из импортированной коллекции 41700 актуальны по ключам; идентификатор коллекции сам по себе не делает их устаревшими.
- Цвета без токенов сохранены. Новые переменные, токены и коллекции не создавались. Геометрия, структура, тексты и свойства вариантов не менялись. Инстансы не отсоединялись и не сбрасывались; цветовые привязки во вложениях обновлялись адресно.

## Все 29 оставшихся применений стилей в рабочей области

1. **Primitives/Grey/Primary** — [мастер 5324:566](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5324-566), слой `5612:31544`, свойство `fills`.
2. **Primitives/Blueberry/15** — [мастер 5324:566](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5324-566), слой `I6206:36149;5743:1279`, свойство `fills`.
3. **Primitives/Blueberry/32** — [мастер 5324:566](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5324-566), слой `I6206:36149;5743:1280`, свойство `fills`.
4. **Primitives/Blueberry/60** — [мастер 5324:566](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5324-566), слой `I6206:36149;5743:1281`, свойство `fills`.
5. **Primitives/Grey/Primary** — [мастер 5336:31523](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5336-31523), слой `I5336:31434;5612:31544`, свойство `fills`.
6. **Primitives/Blueberry/15** — [мастер 5336:31523](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5336-31523), слой `I5336:31434;6206:36149;5743:1279`, свойство `fills`.
7. **Primitives/Blueberry/32** — [мастер 5336:31523](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5336-31523), слой `I5336:31434;6206:36149;5743:1280`, свойство `fills`.
8. **Primitives/Blueberry/60** — [мастер 5336:31523](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5336-31523), слой `I5336:31434;6206:36149;5743:1281`, свойство `fills`.
9. **[Deprecated]/Brand/Partners/Sber** — [мастер 5336:31523](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5336-31523), слой `I5336:31434;5611:31843;3022:13`, свойство `region0`.
10. **Primitives/Grey/Primary** — [мастер 5336:31523](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5336-31523), слой `I5336:31449;5612:31544`, свойство `fills`.
11. **Primitives/Blueberry/15** — [мастер 5336:31523](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5336-31523), слой `I5336:31449;6206:36149;5743:1279`, свойство `fills`.
12. **Primitives/Blueberry/32** — [мастер 5336:31523](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5336-31523), слой `I5336:31449;6206:36149;5743:1280`, свойство `fills`.
13. **Primitives/Blueberry/60** — [мастер 5336:31523](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5336-31523), слой `I5336:31449;6206:36149;5743:1281`, свойство `fills`.
14. **[Deprecated]/Brand/Partners/Sber** — [мастер 5336:31523](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5336-31523), слой `I5336:31449;5611:31843;23:1878`, свойство `fills`.
15. **[Deprecated]/Brand/Social/Facebook** — [мастер 5336:31523](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5336-31523), слой `I5336:31449;5611:31843;23:1879`, свойство `region0`.
16. **Primitives/Grey/Primary** — [мастер 5336:31523](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5336-31523), слой `I5336:31464;5612:31544`, свойство `fills`.
17. **Primitives/Blueberry/15** — [мастер 5336:31523](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5336-31523), слой `I5336:31464;6206:36149;5743:1279`, свойство `fills`.
18. **Primitives/Blueberry/32** — [мастер 5336:31523](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5336-31523), слой `I5336:31464;6206:36149;5743:1280`, свойство `fills`.
19. **Primitives/Blueberry/60** — [мастер 5336:31523](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5336-31523), слой `I5336:31464;6206:36149;5743:1281`, свойство `fills`.
20. **[Deprecated]/Brand/Partners/Sber** — [мастер 5336:31523](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5336-31523), слой `I5336:31464;5611:31843;23:1883`, свойство `fills`.
21. **[Deprecated]/Brand/Social/VK** — [мастер 5336:31523](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5336-31523), слой `I5336:31464;5611:31843;1741:1550`, свойство `region0`.
22. **Primitives/Grey/Primary** — [мастер 5336:31523](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5336-31523), слой `I5611:31935;5612:31544`, свойство `fills`.
23. **Primitives/Blueberry/15** — [мастер 5336:31523](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5336-31523), слой `I5611:31935;6206:36149;5743:1279`, свойство `fills`.
24. **Primitives/Blueberry/32** — [мастер 5336:31523](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5336-31523), слой `I5611:31935;6206:36149;5743:1280`, свойство `fills`.
25. **Primitives/Blueberry/60** — [мастер 5336:31523](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5336-31523), слой `I5611:31935;6206:36149;5743:1281`, свойство `fills`.
26. **Primitives/Grey/Primary** — [мастер 5336:31523](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5336-31523), слой `I5611:31945;5612:31544`, свойство `fills`.
27. **Primitives/Blueberry/15** — [мастер 5336:31523](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5336-31523), слой `I5611:31945;6206:36149;5743:1279`, свойство `fills`.
28. **Primitives/Blueberry/32** — [мастер 5336:31523](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5336-31523), слой `I5611:31945;6206:36149;5743:1280`, свойство `fills`.
29. **Primitives/Blueberry/60** — [мастер 5336:31523](https://www.figma.com/design/sb7SelAF2PBcYZsOxL092c/?node-id=5336-31523), слой `I5611:31945;6206:36149;5743:1281`, свойство `fills`.

