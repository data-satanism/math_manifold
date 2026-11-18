---
id: random-matrix-theory-map
title: "Теория случайных матриц для машинного обучения"
aliases: ["RMT MOC", "Карта RMT", "Random Matrix Theory for ML"]
type: map
status: canonical
publish: true
areas: [random-matrix-theory, high-dimensional-statistics]
concepts: [empirical-spectral-distribution, resolvent-stieltjes-transform, marchenko-pastur-law, spiked-covariance-transition]
prerequisites: [probability, linear-algebra, complex-analysis]
ai_domains: [statistical-learning, kernels, neural-networks, graph-ml, optimization, model-compression, tensor-learning]
source_refs:
  - id: rmt4ml-2022
    pages: "7-410"
    role: primary
  - id: louart2018randomnn
    pages: "1-19"
    role: primary
  - id: goulart2022randomtensors
    pages: "7-19"
    role: primary
  - id: seddik2022randomtensors
    pages: "2-25"
    role: primary
  - id: lebeau2025tensor
    pages: "9-24"
    role: primary
level: advanced
created: 2026-07-10
updated: 2026-11-18
---

# Теория случайных матриц для машинного обучения

Теория случайных матриц изучает не отдельные случайные коэффициенты, а устойчивые коллективные закономерности спектра при одновременном росте числа объектов и размерности. Для машинного обучения это язык, который отличает спектральную структуру сигнала от структуры, неизбежно создаваемой шумом и конечной выборкой.

## Маршрут

## Маршрут от шумовой модели к выводу

1. [[30_mathematics/random-matrix-theory/theorems/marchenko-pastur-law|Закон Марченко—Пастура]]. Повторите вывод скалярного уравнения и вычислите края при $c=1/4$. Для гауссовой модели переход от меры к верхнему краю использует [[30_mathematics/random-matrix-theory/theorems/gaussian-sample-covariance-operator-bound|оценку сингулярного числа]].
2. [[30_mathematics/random-matrix-theory/theorems/sample-covariance-spectral-support|Носитель и точное разделение]]. Из знака $x'(v)$ получите зазор для двух популяционных уровней и порог, который определяет число значений по обе стороны.
3. [[30_mathematics/random-matrix-theory/theorems/spiked-covariance-transition|Один спайк]]. Проверьте допустимость алгебраического корня и вычислите согласование направления. Докритическое поведение выборочного собственного вектора опирается на теорему Пола.
4. [[30_mathematics/random-matrix-theory/theorems/population-covariance-contour|Популяционный вывод]] и [[30_mathematics/random-matrix-theory/modules/04-random-kernel-matrices|два масштаба ядра]]. В первом случае вычислите поправку к моменту, во втором выведите дисперсию предельного полукруга из масштаба элементов.

[[70_labs/rmt/01-marchenko-pastur-finite-size|Лаборатория шума]] и [[70_labs/rmt/stage-4/rmt-stage-4-diagnostics|лаборатория спектральных проверок]] дают первые расчёты. В [[30_mathematics/random-matrix-theory/rmt-source-map|карте источников]] указаны места, где нужны внешние вероятностные теоремы.

1. [[30_mathematics/random-matrix-theory/modules/01-high-dimensional-spectra|Спектральное мышление в высокой размерности]].
2. [[30_mathematics/random-matrix-theory/modules/02-resolvents-deterministic-equivalents|Резольвентный метод и детерминированные эквиваленты]].
3. [[30_mathematics/random-matrix-theory/modules/03-covariance-inference-linear-models|Оценивание ковариации и линейные модели]].
4. [[30_mathematics/random-matrix-theory/modules/04-random-kernel-matrices|Случайные ядровые матрицы]].
5. [[30_mathematics/random-matrix-theory/modules/05-random-neural-networks|Случайные нейронные сети]] и [[50_bridges/rmt-random-feature-networks|строгий мост к однослойным сетям случайных признаков]].
6. [[30_mathematics/random-matrix-theory/modules/06-high-dimensional-convex-classifiers|Выпуклые классификаторы большой размерности]].
7. [[30_mathematics/random-matrix-theory/modules/07-graph-spectra-community-detection|Спектры графов и обнаружение сообществ]].
8. [[30_mathematics/random-matrix-theory/modules/08-universality-real-data|Универсальность и реальные данные]].
9. [[30_mathematics/random-matrix-theory/modules/09-random-tensors|Случайные тензоры через матричные окна]] — свёртки, развёртки и пороги восстановления.

## Опорные узлы курса

- [[20_concepts/empirical-spectral-distribution|Эмпирическое спектральное распределение]] превращает спектр матрицы в вероятностную меру.
- [[20_concepts/resolvent-stieltjes-transform|Резольвента и преобразование Штильтьеса]] дают гладкий аналитический интерфейс к спектру.
- [[30_mathematics/random-matrix-theory/theorems/marchenko-pastur-law|Закон Марченко—Пастура]] описывает шумовой спектральный массив выборочной ковариации.
- [[30_mathematics/random-matrix-theory/theorems/spiked-covariance-transition|Спайковый переход]] показывает, когда низкоранговый сигнал отделяется от шума.
- [[30_mathematics/random-matrix-theory/theorems/sample-covariance-deterministic-equivalent|Детерминированный эквивалент выборочной ковариации]] заменяет случайную резольвенту самосогласованной моделью.
- [[30_mathematics/random-matrix-theory/theorems/trace-covariance-distance-correction|Поправка к следовому расстоянию между ковариациями]] отделяет истинную геометрию от высокоразмерного смещения.
- [[30_mathematics/random-matrix-theory/theorems/distance-kernel-low-rank-equivalent|Низкоранговый эквивалент дистанционного ядра]] объясняет информативные спектральные направления.
- [[30_mathematics/random-matrix-theory/theorems/random-feature-gram-deterministic-equivalent|Эквивалент грамовой матрицы случайных признаков]] связывает активацию с эффективным ядром.
- [[30_mathematics/random-matrix-theory/theorems/generalized-linear-classifier-asymptotics|Асимптотика обобщённого линейного классификатора]] описывает направление и ошибку в пропорциональном режиме.
- [[30_mathematics/random-matrix-theory/theorems/dense-sbm-spectral-transition|Спектральный переход в плотной блочной модели]] задаёт порог обнаружения сообщества.
- [[30_mathematics/random-matrix-theory/theorems/lipschitz-image-concentration|Сохранение концентрации липшицевым отображением]] формулирует границу универсальности.
- [[50_bridges/rmt-spectral-diagnostics|Спектральная диагностика средствами теории случайных матриц]] переводит результаты в проверяемый исследовательский протокол.
- [[50_bridges/rmt-random-feature-networks|RMT для однослойных сетей случайных признаков]] отделяет доказанный результат от переноса на глубокие сети.
- [[30_mathematics/random-matrix-theory/modules/09-random-tensors|Случайные тензоры]] показывают, как матричные развёртки и свёртки открывают разные стороны тензорного сигнала.

## Связи с существующим каталогом

- [[30_mathematics/functional-analysis/modules/10-spectral-theory|Спектральная теория]] даёт операторный язык.
- [[50_bridges/operators-spectrum|Операторы и спектр в ИИ]] предупреждает, что спектры весов, ковариаций, гессианов и якобианов не взаимозаменяемы.
- [[50_bridges/hilbert-rkhs|Гильбертовы пространства и RKHS]] подводит к случайным ядровым матрицам.
- [[50_bridges/lp-risk|Мера и статистический риск]] связывает спектральные пределы с вероятностными утверждениями.

## Источники и статус

Основной источник — [[60_sources/rmt4ml-couillet-liao|Couillet и Liao, RMT4ML]]. Новые первичные источники уточняют два направления: [[60_sources/louart-liao-couillet-random-neural-networks|случайные признаки]] и [[60_sources/goulart-couillet-comon-random-tensors|случайные тензоры]] вместе с работами [[60_sources/seddik-guillaud-couillet-random-tensors|об асимметричных тензорах]] и [[60_sources/lebeau-chatelain-couillet-tensor-approximation|низкомноголинейном приближении]]. Полное покрытие оглавлений и локальных конспектов хранится в [[30_mathematics/random-matrix-theory/rmt-source-map]]. Все девять модулей курса утверждены и имеют статус `canonical`.
