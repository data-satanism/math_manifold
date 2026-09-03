---
id: mathematics-integration-map
title: "Интеграция математических направлений и ИИ"
aliases: ["Карта междисциплинарных связей", "Cross-domain mathematics map"]
type: map
status: canonical
publish: true
areas: [knowledge-engineering, applied-mathematics, functional-analysis, linear-algebra, numerical-analysis, kernel-methods, random-matrix-theory, harmonic-analysis, geometric-deep-learning, statistical-learning, information-geometry, operator-learning, stochastic-dynamics, topological-data-analysis, tensor-methods]
concepts: [knowledge-graph, mathematical-invariant, source-integration]
prerequisites: [content-integration-policy]
ai_domains: [scientific-machine-learning, kernels, representation-learning, optimization, neural-operators, graph-ml]
source_refs:
  - id: myshkis-applied-mathematics-engineers-2006
    pages: "11-671"
    role: primary
  - id: hofmann-scholkopf-smola-kernel-methods-2006
    pages: "1-53"
    role: primary
  - id: boss-linear-algebra-2005
    pages: "10-215"
    role: primary
level: advanced
created: 2026-07-16
updated: 2026-09-03
---

# Интеграция математических направлений и ИИ

## Зачем нужна эта карта

Новые источники не образуют три независимых курса. Они усиливают уже существующий граф: прикладная математика добавляет физические модели и вариационные механизмы, линейная алгебра уточняет конечномерные структуры, функциональный анализ даёт бесконечномерные основания, численный анализ превращает утверждения в алгоритмы, а теория случайных матриц описывает высокоразмерный режим.

## Основные линии переноса

| Сохраняемая структура | Источники и разделы | Существующий узел | Перенос в ИИ и машинное обучение |
|---|---|---|---|
| Внутреннее произведение и положительность | Босс; обзор ядерных методов | [[20_concepts/hilbert-space|Гильбертово пространство]], [[50_bridges/hilbert-rkhs|RKHS и ядра]] | допустимые ядра, матрицы Грама, гауссовские процессы |
| Спектр и инвариантные подпространства | Босс; Тыртышников; RMT | [[30_mathematics/functional-analysis/modules/10-spectral-theory|Спектральная теория]], [[50_bridges/operators-spectrum|операторы и спектр]] | PCA, устойчивость представлений, спектральная диагностика |
| Вариационный принцип | Мышкис; функциональный и численный анализ | [[30_mathematics/functional-analysis/modules/11-nonlinear-frechet|производная Фреше]], [[30_mathematics/numerical-analysis/modules/23-operator-equations-fem-galerkin|слабые решения и Галёркин]] | неявные слои, физически информированные модели, нейронные операторы |
| Свёртка и преобразования | Мышкис; функциональный анализ | [[30_mathematics/functional-analysis/modules/08-distributions-convolution|обобщённые функции и свёртка]], [[50_bridges/fft-convolution-structured-layers|БПФ и свёрточные слои]] | CNN, спектральные слои, фильтрация временных рядов |
| Частотно-временная локализация и масштабы | Тао; Малла; Добеши; Бруна—Малла | [[30_mathematics/harmonic-analysis-wavelets/harmonic-analysis-wavelets-map|гармонический анализ и вейвлеты]], [[50_bridges/harmonic-localization-ai|локализация и архитектуры ИИ]] | многомасштабные признаки, рассеяние, устойчивость к деформациям, перенос между разрешениями |
| Положительный конус и монотонность | Босс; функциональный анализ | [[30_mathematics/functional-analysis/modules/12-positive-operators|положительные операторы]] | марковские модели, монотонные сети, устойчивые динамические слои |
| Низкоранговая и ядерная структура | обзор ядерных методов; Тыртышников; RMT | [[50_bridges/hierarchical-matrices-kernel-attention|иерархические матрицы, ядра и внимание]] | приближения Нюстрёма, случайные признаки, быстрое внимание |
| Резольвента и интегральное уравнение | Мышкис; функциональный анализ; RMT | [[30_mathematics/functional-analysis/modules/09-operator-equations|операторные уравнения]], [[50_bridges/operator-equations|обратные задачи]] | регуляризация, операторное обучение, спектральные детерминированные эквиваленты |
| Отступ и сложность класса | обзор ядерных методов | [[30_mathematics/kernel-methods/modules/02-support-vector-estimation|методы опорных векторов]], [[30_mathematics/kernel-methods/modules/03-margin-uniform-convergence|равномерная сходимость]], [[50_bridges/generalization-complexity-ai|связь с ИИ]] | классификация, честный выбор моделей, диагностика представлений, оценки обобщения |
| Нормировка, моменты и ковариация | обзор ядерных методов, раздел 5.1 | [[30_mathematics/kernel-methods/theorems/log-partition-moment-geometry|логарифмическая статистическая сумма]], [[30_mathematics/kernel-methods/methods/conditional-exponential-rkhs-model|условная модель RKHS]], [[50_bridges/log-partition-kernels-energy-models|связь с ИИ]] | мягкое максимальное преобразование, условные случайные поля, энергетические модели, классификация гауссовскими процессами |
| Кликовая локальность и древесная ширина | обзор ядерных методов, раздел 5.2 | [[30_mathematics/kernel-methods/theorems/hammersley-clifford-factorization|факторизация]], [[30_mathematics/kernel-methods/theorems/graph-compatible-kernel-decomposition|графическое ядро]], [[50_bridges/graphical-kernels-structured-inference|связь с ИИ]] | разметка последовательностей, условные случайные поля, структурные методы опорных векторов, вероятностный вывод |
| Центрирование, перекрёстная ковариация и средние вложения | обзор ядерных методов, раздел 6; линейная алгебра; RMT | [[30_mathematics/kernel-methods/methods/kernel-pca-centered-gram|ядерный PCA]], [[30_mathematics/kernel-methods/theorems/rkhs-cross-covariance-independence|HSIC]], [[30_mathematics/kernel-methods/theorems/kernel-mean-embedding-mmd|MMD]], [[50_bridges/kernel-independence-representation-learning|связь с ИИ]] | согласование модальностей, диагностика представлений, двухвыборочные критерии, мониторинг сдвига |
| Групповое действие и эквивариантность | Кириллов; Галлье; геометрическое глубокое обучение | [[30_mathematics/lie-groups-differential-geometry/lie-groups-differential-geometry-map|группы Ли, представления и геометрия]], [[50_bridges/lie-symmetry-geometry-ai|геометрия и эквивариантные архитектуры]] | групповые свёртки, типы признаков, калибровочно-эквивариантные сети, модели физических полей |
| Сложность класса и информация | вероятность; статистическое обучение; теория информации | [[30_mathematics/statistical-learning-information-theory/modules/slt-04-symmetrization-double-sampling|симметризация]], [[50_bridges/complexity-information-generalization|аудит обобщения]] | выбор модели, повторное использование проверочной выборки, информационные оценки |
| Метрика Фишера и дивергенции | информационная геометрия; выпуклый анализ | [[30_mathematics/information-geometry/modules/ig-02-fisher-rao-metric|метрика Фишера—Рао]], [[50_bridges/information-geometry-optimization-inference|геометрия оптимизации и вывода]] | естественный градиент, вариационный вывод, вероятностная калибровка |
| Оператор решения, слабая форма и энергия | функциональный анализ; численный анализ; классическая теория PDE; вариационное исчисление | [[30_mathematics/classical-pde-variational/classical-pde-variational-map|классические PDE и вариационные методы]], [[30_mathematics/operator-learning/modules/opl-02-weak-variational-formulations|слабые формулировки]], [[50_bridges/pde-inverse-neural-operators|PDE и нейронные операторы]] | DeepONet, FNO, обратные задачи, перенос между сетками, независимая проверка решателя |
| Генератор и эволюция плотности | вероятность; динамические системы; стохастический анализ | [[30_mathematics/stochastic-dynamics/modules/dyn-05-generator-fokker-planck|генератор и уравнение Фоккера—Планка]], [[50_bridges/sde-diffusion-state-space|SDE и диффузионные модели]] | модели на основе скор-функции, фильтрация, модели состояния |
| Гомология и устойчивость фильтраций | топология; вычислительная линейная алгебра | [[30_mathematics/topological-data-analysis/modules/tda-05-stability-bottleneck|устойчивость персистентности]], [[50_bridges/topology-representation-diagnostics|топология представлений]] | диагностика скрытых представлений, графов и многообразий данных |
| Многолинейный ранг и тензорные сети | линейная и численная алгебра; RMT | [[30_mathematics/tensor-methods/modules/ten-03-tucker-hosvd|Tucker и HOSVD]], [[50_bridges/tensor-low-rank-ai|тензорные методы в ИИ]] | сжатие, адаптация моделей, восстановление и научные вычисления |

## Очередь интеграции

1. Устранить шаблонные повторения и углубить теоремный слой семи курсов, опубликованных 12 августа 2026 года.
2. Нормализовать словари `concepts`, `prerequisites` и `ai_domains`, не превращая тематические теги в ложные ссылки на заметки.
3. Провести пользовательское ревью готового курса гармонического анализа и вейвлетов: 12 модулей, 9 теорем и 22 визуализации.
4. Провести пользовательское ревью курса групп Ли, теории представлений и дифференциальной геометрии: 12 модулей, 11 новых теорем и 24 визуализации.
5. Провести пользовательское ревью курса классических PDE и вариационных методов: 12 модулей, 11 новых теорем, расширенные общие узлы и 24 визуализации.

Решение по каждому пересекающемуся разделу хранится в `90_admin/content_overlap_registry.csv`. Правила выбора описаны в административной заметке `90_admin/content-integration-policy.md`.

> [!note] Редакционный статус
> Эта версия карты утверждена владельцем 3 сентября 2026 года в составе полного редакционного пакета.
