# Имена и описания скилов для Figma

## Навигация по библиотекам

**Skill name:** `okko-library-navigator`

**Description:** Находит Figma-библиотеки Okko, страницы, компоненты, fileKey и nodeId и проверяет источник в живом файле. Использовать для навигации и поиска нод; не использовать для выбора UI-компонента по продуктовому сценарию.

**Instructions:** `library-navigator.md`

## Библиотекарь дизайн-системы

**Skill name:** `okko-ds-librarian`

**Description:** Помогает выбрать существующий компонент, токен или правило дизайн-системы Okko и проверяет lifecycle. Использовать для вопросов «что применить» и «есть ли решение в ДС»; не использовать для аудита целого экрана или создания макета.

**Instructions:** `ds-librarian.md`

## Аудит макета

**Skill name:** `okko-ds-auditor`

**Description:** Проверяет Figma-макет на соответствие компонентам, токенам и платформенным правилам Okko и предлагает конкретные исправления. Использовать для ревью готового экрана; не изменять макет без отдельного запроса.

**Instructions:** `ds-auditor.md`

## Компоновка экранов

**Skill name:** `okko-layout-helper`

**Description:** Собирает и адаптирует экраны из готовых компонентов Okko с учётом платформы, состояний и навигации. Использовать для компоновки экранов и флоу; изменять Figma только по явному запросу.

**Instructions:** `layout-helper.md`

## Overview вариантов компонента

**Skill name:** `okko-component-overview`

**Description:** Создаёт тестовый Overview всех существующих вариантов component set из связанных инстансов и проверяет покрытие. Использовать для variant matrix и regression board; не использовать вместо пользовательского гайда.

**Instructions:** `component-overview.md`

## Документация компонента

**Skill name:** `okko-component-doc-writer`

**Description:** Создаёт или обновляет гайдлайн компонента Okko в Figma: anatomy, properties, variants, states, Do/Don't и примеры. Использовать для документации компонента; итог требует дизайнерского ревью.

**Instructions:** `component-doc-writer.md`

## Оптимизация библиотеки

**Skill name:** `okko-library-optimizer`

**Description:** Проверяет структуру Figma-библиотеки Okko: порядок страниц и Assets, naming, lifecycle, descriptions и Sections. Использовать для аудита и согласованной оптимизации библиотеки; не менять внутреннее устройство компонентов без отдельного решения.

**Instructions:** `library-optimizer.md`
