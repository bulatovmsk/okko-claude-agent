# Rail — семейство шаблонов

## Модель семейства

Rail — не одна карточка, а семейство готовых горизонтальных шаблонов. Общий
каркас задаёт [Rail - Base](rail-base.md): заголовок, левый слот и платформенную
раскладку. Каждый публичный `Rail - …` подставляет свой тип карточки и задаёт
состав, размеры и поведение ряда для поддерживаемых устройств.

Ноды, имена которых начинаются с `_`, — внутренние запчасти шаблонов: карточки,
обложки, прогресс, метаданные, цифры и колонки. Они не публикуются как
самостоятельные решения и отдельно в библиотеке знаний не регистрируются.

## Как выбирать шаблон

| Шаблон | Что находится в карточке | Статус | Устройства |
|---|---|---|---|
| [Rail - Announces](rail-announces.md) | анонс | ready | 5 вариантов iPhone/iPad |
| [Rail - Catalog](rail-catalog.md) | каталожная карточка | work-in-progress, нет в проде | 5 вариантов iPhone/iPad |
| [Rail - Background](rail-background.md) | контент на брендированном фоне | ready | 5 вариантов iPhone/iPad |
| [Rail - Circle](rail-circle.md) | круглая обложка с подписью | ready | 5 вариантов iPhone/iPad |
| [Rail - Continue](rail-continue.md) | продолжение просмотра с прогрессом | ready | 5 вариантов iPhone/iPad |
| [Rail - Highlights](rail-highlights.md) | крупный рейтинг, цифра и тег | ready | 5 вариантов iPhone/iPad |
| [Rail - Large](rail-large.md) | крупная горизонтальная карточка | ready | 5 вариантов iPhone/iPad |
| [Rail - Main](rail-main.md) | основная горизонтальная карточка | ready | 5 вариантов iPhone/iPad |
| [Rail - Marketing](rail-marketing.md) | крупный маркетинговый креатив | ready | 5 вариантов iPhone/iPad |
| [Rail - Medium](rail-medium.md) | средняя горизонтальная карточка | ready | 5 вариантов iPhone/iPad |
| [Rail - Person Horizontal](rail-person-horizontal.md) | персона или участник | ready | только iPhone, iPad 10, iPad Pro 13 |
| [Rail - Personal Widget](rail-personal-widget.md) | персональный виджет с метаданными | ready | 5 вариантов iPhone/iPad |
| [Rail - Square](rail-square.md) | квадратная обложка | ready | 5 вариантов iPhone/iPad |
| [Rail - SquareSmall1Story](rail-square-small-1-story.md) | компактная квадратная карточка, один ряд | ready | 5 вариантов iPhone/iPad |
| [Rail - SquareSmall2Story](rail-square-small-2-story.md) | компактная квадратная карточка, два ряда | ready | 5 вариантов iPhone/iPad |
| [Rail - Ticket](rail-ticket.md) | билет или специальное предложение | ready, есть deprecated-вариант | 4 актуальных + iPhone 320 deprecated |
| [Rail - Vertical](rail-vertical.md) | вертикальная обложка | ready | 5 вариантов iPhone/iPad |
| [Rail - Content](rail-content.md) | контентная карточка с прогрессом/метаданными | work-in-progress, нет в проде | iPhone 15 и 3 iPad-варианта |
| [Rail - Square Medium](rail-square-medium.md) | квадратная карточка среднего размера | work-in-progress | 5 вариантов iPhone/iPad |
| [Rail / Tracks](rail-tracks.md) | трек, название и длительность | ready | 5 вариантов iPhone/iPad |

Рейлы рейтингов `Rail / Top Titles`, `Rail / Top Collections` и
`Rail / Mixed Top` описаны отдельной группой и не входят в эту страницу
`UI Type Rail`.

## Общие правила

- Используйте мастер нужного `Rail`, а не собирайте ряд из `_…`-запчастей.
- Значение `Device`/`device` выбирайте по целевой платформенной раскладке; точное
  написание свойства сохраняйте таким, как оно задано в Figma.
- Карточки внутри ряда остаются отдельными интерактивными элементами. Сам рейл
  не должен превращаться в одну общую кнопку.
- В VoiceOver сохраняйте порядок карточек и полезное название каждой карточки;
  декоративные обложки, цифры и фон не озвучивайте отдельно.
- Значения цветов, отступов, радиусов и типографики не переносите из этой
  документации: актуальные токены проверяются в Tokens Studio source of truth.
- Шаблоны со статусом `work-in-progress` нельзя выбирать автоматически для
  продуктового макета до подтверждения готовности.

## Источник

- [Страница UI Type Rail](https://www.figma.com/design/rMcDm5qGp4CXkXXddEbcMh/Lib-iOS?node-id=6890-64101) — fileKey `rMcDm5qGp4CXkXXddEbcMh`, node `6890:64101`.
