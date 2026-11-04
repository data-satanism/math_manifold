---
id: source-cap-principles
title: Общие вычислительные принципы — источники и границы доказательств
aliases: []
type: source
status: canonical
publish: true
areas:
- numerical-linear-algebra
concepts: []
prerequisites: []
ai_domains:
- compression
- scientific-ml
source_refs: []
level: advanced
created: '2026-11-04'
updated: '2026-11-04'
---

# Основания второго цикла

1. Ортогональные координаты и SVD — матричная теория, подробно выведенная в [[30_mathematics/computational-algebra-principles/modules/cap-p01-isometric-core]]. Тензорный перенос основан на Oseledets 2011, §§2–3, см. [[60_sources/source-cap-tensor-research]].
2. N. Halko, P. G. Martinsson, J. A. Tropp. Finding Structure with Randomness. SIAM Review 53(2), 2011, 217–288. [Авторская версия arXiv:0909.4061](https://arxiv.org/abs/0909.4061). Для [[30_mathematics/computational-algebra-principles/modules/cap-p02-random-subspace]] изучены детерминированное ядро, спектральные блоки и теорема 10.5. Формула ожидания обратного Уишарта импортирована явно. Средняя ошибка не подменяется гарантией отдельного запуска.
3. Структура разрезов и локальные блоки — собственные матричные выводы и первичные TT-результаты. [[30_mathematics/computational-algebra-principles/modules/cap-p03-structure-locality]] не приписывает одной схеме представления универсальную оптимальность.
4. Обусловленность, фильтрация Тихонова и SPD-преобразования — прямые выводы из SVD и порядка положительно определённых матриц. Формулы полностью доказаны в [[30_mathematics/computational-algebra-principles/modules/cap-p04-conditioning]].
5. Сертификат Фробениуса по независимым гауссовым произведениям в [[30_mathematics/computational-algebra-principles/modules/cap-p05-certificates]] доказан через вторую и четвёртую гауссовы моменты и неравенство Чебышёва. Это собственная учебная версия, а не цитата точной концентрационной константы HMT.

Численные проверки и графики — [[70_labs/computational-algebra-principles/cap-full-plan-lab]]. Вторая серия принципов сводит результаты разных модулей в проверяемые правила выбора алгоритма.
