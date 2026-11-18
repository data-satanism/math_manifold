---
id: atlas-content-review-2026-11-18
title: "Доработки математического атласа"
aliases: ["Ревизия атласа, ноябрь 2026"]
type: map
status: canonical
publish: true
areas: [mathematics, knowledge-engineering]
concepts: [learning-path, reproducibility]
prerequisites: []
ai_domains: [scientific-machine-learning, model-compression]
source_refs: []
level: foundation
created: 2026-11-18
updated: 2026-11-18
---

# Доработки математического атласа

Выпуск по итогам ревизии от 18 ноября 2026 года. В каждой теме ниже есть расчёт или предельный случай, с которого удобно начать проверку.

## Исправленные утверждения и рисунки

- [[30_mathematics/numerical-analysis/theorems/hermitian-qr-cubic-convergence|Кубическая сходимость QR]]. Проверьте спектральный зазор, условия на собственные векторы и один вычисленный шаг. Для общего случая см. [[30_mathematics/numerical-analysis/theorems/rayleigh-shift-quadratic-convergence|квадратичную оценку]].
- [[30_mathematics/functional-analysis/modules/07-hilbert-operators|Операторы в гильбертовом пространстве]]. Сравните тождественный оператор и диагональный оператор с коэффициентами $1/j$.
- [[30_mathematics/random-matrix-theory/theorems/trace-covariance-distance-correction|Обращение ковариации]]. Сравните известное и выборочное среднее при $p=n$.
- [[30_mathematics/stochastic-dynamics/modules/dyn-06-numerical-sde|Схема Эйлера — Маруямы]]. Вычислите локальный средний квадрат ошибки при мультипликативном шуме.
- [[30_mathematics/statistical-learning-information-theory/theorems/sauer-shelah-growth|Лемма Зауэра — Шелаха]]. Проследите базу индукции при $d=0$.
- [[30_mathematics/linear-algebra/modules/01-coordinate-geometry-invariants|Ортогональные координаты]], [[30_mathematics/numerical-analysis/methods/arnoldi-lanczos|Галёркин и GMRES]], [[30_mathematics/lie-groups-differential-geometry/modules/lg-01-smooth-manifolds-atlases|угловые карты и критические слои]], [[30_mathematics/classical-pde-variational/modules/pde-01-operator-data-well-posedness|Пуассон, тепло и волна]].
- [[30_mathematics/operator-learning/modules/opl-01-pde-solution-operators|Решение при вырождении коэрцитивности]], [[30_mathematics/harmonic-analysis-wavelets/modules/ha-01-harmonic-viewpoint-characters|сдвиг и свёртка]], [[30_mathematics/probability/modules/01-probability-refresher|закон статистики]], [[30_mathematics/real-analysis/modules/01-measures-radon-nikodym|разложение Жордана]], [[50_bridges/tyrtyshnikov-tensors-2023-2024/tga-ml-02-moe|замена эксперта при фиксированном маршруте]].
- [[10_maps/mathematics-integration-map|Входы по математической подготовке]], [[10_maps/ai-domain-navigation|входы по задаче ИИ]], [[index|главная карта]].

## Спектральный маршрут RMT

1. [[30_mathematics/random-matrix-theory/theorems/marchenko-pastur-law|Закон Марченко — Пастура]]. Выведите уравнение для следа резольвенты и выберите допустимый корень.
2. [[30_mathematics/random-matrix-theory/theorems/sample-covariance-spectral-support|Носитель и зазоры]]. Вычислите четыре границы двух полос и порог разделения.
3. [[30_mathematics/random-matrix-theory/theorems/spiked-covariance-transition|Один спайк]]. Сравните два выступа, дающие один алгебраический кандидат и разные пределы.
4. [[30_mathematics/random-matrix-theory/theorems/population-covariance-contour|Контурный вывод]] и [[30_mathematics/random-matrix-theory/modules/04-random-kernel-matrices|масштаб случайного ядра]]. Проверьте поправку второго момента и предельную дисперсию.

## Тензоры

Начните с [[30_mathematics/tensor-methods/modules/ten-01-multilinear-objects|развёртки массива 2 × 3 × 2]]. В [[30_mathematics/tensor-methods/modules/ten-formats-worked-example|общем примере CP, Таккера и TT]] определите ранги, повторите один шаг ALS и вычислите ошибку на входе слоя.

[[30_mathematics/tensor-methods/ten-map|Карта курса]] связывает пример с [[30_mathematics/tensor-methods/modules/ten-05-identifiability-degeneracy|вырождением CP]], [[30_mathematics/tyrtyshnikov-video-2026/lectures/tva-08-kruskal-proof|доказательством Крускала]] и [[30_mathematics/tyrtyshnikov-tensors-2023-2024/lectures/tga-10|лекцией об ALS]].

## Соседние курсы

- [[30_mathematics/classical-pde-variational/theorems/parabolic-galerkin-existence-theorem|Слабое параболическое решение]]. Проверьте оценку производной, формулу начального следа и расчёт для одной моды.
- [[30_mathematics/operator-learning/theorems/deeponet-universal-operator-approximation|Конечные датчики DeepONet]]. Две функции дают одну строку измерений и разные выходы.
- [[30_mathematics/harmonic-analysis-wavelets/modules/ha-06-sampling-dft-fft-aliasing|Наложение частот]] и [[30_mathematics/harmonic-analysis-wavelets/modules/ha-10-filter-banks-perfect-reconstruction|обращение банка Хаара]]. Сравните пять отсчётов и восстановите пару из среднего и детали.
- [[30_mathematics/information-geometry/theorems/fisher-reparameterization-invariance|Метрика Фишера]] и [[30_mathematics/information-geometry/modules/ig-07-natural-gradient|естественный градиент]]. Проверьте равенство квадратичных длин и пересчитайте конечный шаг Эйлера.

## Повторить вычисления

Для коротких проверок достаточно стандартного Python 3. В каждой указанной лаборатории есть входные данные, ожидаемый результат и допуск.

| Задача | Открыть лабораторию |
| --- | --- |
| Допустимость и принятие пробного шага | [[70_labs/matrix-manifolds-manopt/mda-geometry-lab|Кэли и Армихо]] |
| Монотонность среднего | [[70_labs/population-optimization-manifolds/pom-geometry-lab|Популяционная оптимизация]] |
| Края, ветвь и сглаживание спектра | [[70_labs/rmt/01-marchenko-pastur-finite-size|Марченко — Пастур]], [[70_labs/rmt/02-bbp-spiked-transition|спайк]], [[70_labs/rmt/03-resolvent-density-recovery|сглаженная плотность]] |
| Компоненты носителя и поправка момента | [[70_labs/rmt/stage-4/rmt-stage-4-diagnostics|Спектральные проверки RMT]] |
| Порядок осей, единственность и шаг ALS | [[70_labs/tensor-methods/stage-4/tensor-stage-4-diagnostics|Ранги и остаток]], [[70_labs/tyrtyshnikov-video-2026/tva-visual-lab|условие Крускала]], [[70_labs/tyrtyshnikov-tensors-2023-2024/tga-visual-lab|один шаг ALS]] |
| Выбор блока и уменьшение ранга | [[70_labs/computational-algebra-principles/cap-rank-spectrum-lab|Дополнение Шура]] |
| Потоковая цель и ядерная норма | [[70_labs/big-data-algorithms/stage-5/bda-stage-5-streaming-lab|Объединение пакетов]], [[70_labs/big-data-algorithms/stage-6/bda-stage-6-completion-lab|шаг мягкого порога]] |

Часть опытов запускается прямо в браузере. [[70_labs/rmt/06-rmt-interactives|Интерактивы RMT]] дают гистограмму, спайковый переход и спектральное сглаживание.
