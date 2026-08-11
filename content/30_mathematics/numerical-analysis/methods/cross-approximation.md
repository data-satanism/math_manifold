---
id: cross-approximation-method
title: "Метод крестовой аппроксимации"
aliases: ["Скелетное разложение", "Выбор опорных строк и столбцов"]
type: method
status: canonical
publish: true
areas: [numerical-analysis, numerical-linear-algebra]
concepts: [cross-approximation, max-volume, pivoting, low-rank-approximation]
prerequisites: [cross-approximation-max-volume-theorem]
ai_domains: [compression, kernel-methods, matrix-completion]
source_refs:
  - id: tyrtyshnikov-numerical-analysis
    pages: "271-273"
    role: primary
level: research
created: 2026-07-15
updated: 2026-07-27
---

# Метод крестовой аппроксимации

## Формула

Для наборов индексов $I,J$ размера $r$:

$$
\widetilde A=A_{:,J}A_{I,J}^{-1}A_{I,:}.
$$

Используются лишь $r$ строк и $r$ столбцов, то есть $O(r(m+n))$ элементов.

## Практический алгоритм

1. Выбрать начальный опорный элемент.
2. Чередовать поиск большого остатка в текущей строке и столбце.
3. Добавлять опорные индексы и обновлять малоранговое представление.
4. Остановиться по независимой оценке остатка.
5. При необходимости улучшить пересечение перестановками максимального объёма.

## Режимы отказа

Плохой опорный блок почти вырожден; выбор по обучающей подвыборке пропускает локальный выброс; поэлементная ошибка не всегда контролирует требуемую операторную норму.

## Визуализация

![Опорные строки и столбцы образуют устойчивый крест только при хорошем пересечении](80_assets/numerical-analysis/gpt-image-v5/nla-ch25-hierarchical-low-rank-insight.png)

## Источник

[[60_sources/tyrtyshnikov-numerical-analysis|Тыртышников]], §25.6, стр. 271–273.
