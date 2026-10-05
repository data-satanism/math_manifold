---
id: atlas-stage-4-review
title: "Пакет углубления: тензорные методы и RMT"
aliases: ["Атлас: этап 4", "Проверка тензоров и RMT"]
type: map
status: canonical
publish: true
areas: [tensor-methods, random-matrix-theory, mathematics-for-ai]
concepts: [learning-path, source-coverage, failure-analysis]
prerequisites: [ten-course-map, random-matrix-theory-map]
ai_domains: [model-compression, pca, covariance-estimation]
source_refs:
  - id: kolda-bader-tensors-2009
    pages: "PDF 13–16, 23–24"
    role: primary
  - id: oseledets-tensor-train-2011
    pages: "PDF 4–7"
    role: primary
  - id: de-lathauwer-multilinear-svd-2000
    pages: "PDF 15, 17"
    role: primary
  - id: davidson-szarek-gaussian-2001
    pages: "PDF 42–43"
    role: primary
  - id: paul-spiked-covariance-2007
    pages: "PDF 2–3, 6, 16–18"
    role: primary
level: advanced
created: 2026-10-02
updated: 2026-10-02
---

# Пакет углубления: тензорные методы и RMT

Маршрут объединяет локальные дополнения от 2 октября 2026 года. Существующие математические узлы расширены; центральные результаты не размножаются в параллельные конспекты. Новые заметки проходят проверку, опубликованный сайт обновляется отдельным действием.

## Тензорные методы

1. [[30_mathematics/tensor-methods/modules/ten-03-tucker-hosvd|Tucker, HOSVD и HOOI]]: алгоритм, стоимость, несовпадение отдельных подпространств с совместным оптимумом. Полное доказательство вынесено в [[30_mathematics/tensor-methods/theorems/hosvd-quasioptimality|существующую теорему квазиоптимальности]].
2. [[30_mathematics/tensor-methods/modules/ten-04-tensor-networks|TT-SVD]]: точные ранги, локальная энергия усечений, верхняя оценка через исходные хвосты, правило выбора рангов и зависимость от порядка осей.
3. [[30_mathematics/tensor-methods/modules/ten-05-identifiability-degeneracy|CP: идентифицируемость и вырождение]]: отдельные вопросы существования, единственности и устойчивости; явная последовательность ранга 2 к пределу ранга 3.
4. [[70_labs/tensor-methods/stage-4/tensor-stage-4-diagnostics|Вычислительная лаборатория]]: сохранённые результаты, отрицательные контроли и воспроизводимые графики.
5. [[50_bridges/tensor-low-rank-ai|Перенос в сжатие моделей]]: какие гарантии относятся к коэффициентам и одному линейному слою, а какие выводы требуют измерения качества всей сети.

Общее техническое доказательство условия Крускала, глобальная сходимость HOOI, округление готового TT и алгоритмы доступа к отдельным элементам не объявляются раскрытыми этим пакетом.

## Теория случайных матриц

1. [[30_mathematics/random-matrix-theory/theorems/gaussian-sample-covariance-operator-bound|Конечновыборочная операторная ошибка гауссовой ковариации]]: размерность, число наблюдений, вероятность, центрирование и пример отказа при зависимых столбцах.
2. [[30_mathematics/random-matrix-theory/theorems/spiked-covariance-transition|Спайковый переход]]: положение выброса, допустимая ветвь и согласование направления. Предпосылки для собственного значения и собственного вектора различаются.
3. [[30_mathematics/random-matrix-theory/modules/01-high-dimensional-spectra|Высокоразмерные спектры]] → [[30_mathematics/random-matrix-theory/modules/02-resolvents-deterministic-equivalents|резольвенты]] → [[30_mathematics/random-matrix-theory/modules/03-covariance-inference-linear-models|ковариационный вывод]]. Эти существующие модули связывают новые количественные результаты с учебным маршрутом.
4. [[70_labs/rmt/stage-4/rmt-stage-4-diagnostics|Вычислительная лаборатория RMT]]: тождества, контроль допустимой ветви, частоты нарушений с биномиальными интервалами и конечномерные спайковые реализации.

Конечновыборочная вероятность, слабый предел спектральной меры и асимптотический переход — три разных утверждения. Полное доказательство закона Марченко—Пастура, изотропного эквивалента и теоремы края не подменяется вычислением скалярного корня. Флуктуационные законы, критическое окно и статистический тест не входят в текущий пакет.

## Источники и проверка покрытия

- [[30_mathematics/tensor-methods/ten-source-map|Тензорная карта источников]].
- [[30_mathematics/random-matrix-theory/rmt-source-map|Карта источников RMT]].
- [[60_sources/de-lathauwer-multilinear-svd|Первичный источник HOSVD]].
- [[60_sources/davidson-szarek-gaussian-singular-values|Гауссовы сингулярные числа и официальное исправление]].
- [[60_sources/baik-silverstein-spiked-covariance|Предел спайкового собственного значения]].
- [[60_sources/paul-spiked-covariance-eigenvectors|Предел согласования собственного вектора]].

Карта показывает проверяемый учебный маршрут, а не полное покрытие монографии RMT4ML или всей теории тензорных разложений.
