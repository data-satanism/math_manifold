---
id: probability-source-map
title: "Карта источника: High-Dimensional Probability"
aliases: ["Vershynin HDP source map", "Карта источника по высокоразмерной вероятности"]
type: map
status: canonical
publish: true
areas: [probability, high-dimensional-probability, source-mapping]
concepts: [source-integration, concentration, random-matrix, empirical-process]
prerequisites: [probability-concentration-map]
ai_domains: [statistical-learning, random-matrices, representation-learning]
source_refs:
  - id: vershynin-hdp-2026
    pages: "1-329"
    role: primary
level: advanced
created: 2026-07-27
updated: 2026-08-12
---

# Карта источника: High-Dimensional Probability

Оглавление и границы страниц проверены по визуальному рендеру PDF от 22 июля 2026 года. Каждая строка сохраняет подраздел источника, даже если несколько подразделов объединяются в один учебный модуль.

Обозначения: `R` — уже покрыто существующим узлом, `N` — новый материал курса на ревью, `P` — запланированный материал.

| Раздел | Страницы | Целевой материал | Решение |
|---|---:|---|---|
| Введение: вероятностный метод и приближённая теорема Каратеодори | 1–5 | будущая лаборатория по вероятностному методу | P |
| 1.1 Выпуклые множества и функции | 8 | [[30_mathematics/probability/modules/01-probability-refresher|модуль 1]], существующие материалы по выпуклости | R |
| 1.2 Нормы и скалярные произведения | 8–10 | [[20_concepts/norm|норма]], [[20_concepts/hilbert-space|гильбертово пространство]] | R |
| 1.3 Случайные величины и векторы | 10–12 | [[30_mathematics/probability/modules/01-probability-refresher|модуль 1]] | N |
| 1.4 Оценка объединения событий | 12–13 | [[30_mathematics/probability/modules/01-probability-refresher|модуль 1]] | N |
| 1.5 Условные вероятности | 13–15 | [[30_mathematics/probability/modules/01-probability-refresher|модуль 1]] | N |
| 1.6 Вероятностные неравенства | 15–17 | [[30_mathematics/probability/modules/01-probability-refresher|модуль 1]] | N |
| 1.7 Предельные теоремы | 17–20 | [[30_mathematics/probability/modules/01-probability-refresher|модуль 1]] | N |
| 1.8 Комментарии и упражнения | 20–24 | модуль 1, самопроверка | N |
| 2.1 Зачем нужны неравенства концентрации | 25–28 | [[30_mathematics/probability/modules/02-concentration-independent-sums|модуль 2]] | N |
| 2.2 Неравенство Хёффдинга | 28–30 | [[30_mathematics/probability/theorems/hoeffding-inequality|теорема Хёффдинга]] | N |
| 2.3 Неравенство Чернова | 30–32 | модуль 2 | N |
| 2.4 Оценка среднего медианой блоков | 32–34 | модуль 2, будущая лаборатория | N |
| 2.5 Степени случайного графа | 34–35 | модуль 2, [[40_ai_domains/graph-machine-learning|карта графового обучения]] | N |
| 2.6 Субгауссовские распределения | 35–39 | [[20_concepts/subgaussian-subexponential|субгауссовские и субэкспоненциальные величины]] | N |
| 2.7 Субгауссовские неравенства Хёффдинга и Хинчина | 39–43 | модуль 2, теорема Хёффдинга | N |
| 2.8 Субэкспоненциальные распределения | 43–47 | [[20_concepts/subgaussian-subexponential|концепт хвостов]] | N |
| 2.9 Неравенство Бернштейна | 47–49 | [[30_mathematics/probability/theorems/bernstein-inequality|теорема Бернштейна]] | N |
| 2.10 Комментарии и упражнения | 49–58 | модуль 2, самопроверка | N |
| 3.1 Концентрация нормы | 60–61 | [[30_mathematics/probability/theorems/subgaussian-norm-concentration|концентрация нормы]] | N |
| 3.2 Ковариация и PCA | 61–66 | [[30_mathematics/probability/modules/03-random-vectors-high-dimensions|модуль 3]], [[50_bridges/svd-pca-compression-lora|связь с PCA]] | N |
| 3.3 Примеры высокоразмерных распределений | 66–73 | модуль 3 | N |
| 3.4 Субгауссовские распределения в высокой размерности | 73–76 | модуль 3 | N |
| 3.5 Неравенство Гротендика и полуопределённое программирование | 76–81 | будущий модуль о случайных векторах и выпуклых релаксациях | P |
| 3.6 Максимальный разрез графа | 81–84 | будущая лаборатория по случайному округлению | P |
| 3.7 Ядерный трюк и усиление неравенства Гротендика | 84–88 | будущий мост к ядровым методам | P |
| 3.8 Комментарии и упражнения | 88–100 | модуль 3, самопроверка | N |
| 4.1 Линейная алгебра | 101–109 | существующий курс линейной алгебры | R |
| 4.2 Сети, покрытия и упаковки | 109–114 | [[30_mathematics/probability/modules/04-random-matrices|модуль 4]] | N |
| 4.3 Коды исправления ошибок | 114–116 | модуль 4, будущая лаборатория | N |
| 4.4 Верхние оценки субгауссовских случайных матриц | 116–120 | [[30_mathematics/probability/theorems/subgaussian-matrix-operator-norm|теорема об операторной норме]], модуль 4 | N |
| 4.5 Обнаружение сообществ | 120–124 | [[30_mathematics/random-matrix-theory/modules/07-graph-spectra-community-detection|RMT и графы]], модуль 4 | R |
| 4.6 Двусторонние оценки случайных матриц | 124–125 | [[30_mathematics/probability/modules/04-random-matrices|модуль 4]] | N |
| 4.7 Оценивание ковариации и кластеризация | 125–129 | модуль 4, [[50_bridges/rmt-spectral-diagnostics|спектральная диагностика]] | N |
| 4.8 Комментарии и упражнения | 129–140 | модуль 4, самопроверка | N |
| 5.1 Концентрация липшицевых функций на сфере | 141–146 | [[30_mathematics/probability/theorems/sphere-lipschitz-concentration|сферическая концентрация]], модуль 5 | N |
| 5.2 Концентрация на метрических пространствах с мерой | 146–151 | [[30_mathematics/probability/modules/05-concentration-without-independence|модуль 5]] | N |
| 5.3 Лемма Джонсона—Линденштрауса | 151–153 | [[50_bridges/random-projections-retrieval|случайные проекции и поиск]] | N |
| 5.4 Матричное неравенство Бернштейна | 153–160 | модуль 5, будущая самостоятельная теорема | N |
| 5.5 Сообщества в разреженных сетях | 160–162 | [[30_mathematics/random-matrix-theory/modules/07-graph-spectra-community-detection|RMT и графы]] | R |
| 5.6 Оценивание ковариации для общих распределений | 162–165 | модуль 5, [[50_bridges/quadratic-forms-covariance-anomaly|ковариационная диагностика]] | N |
| 5.7 Комментарии и упражнения | 165–171 | модуль 5, самопроверка | N |
| 6.1 Развязка зависимостей | 172–175 | [[30_mathematics/probability/modules/06-quadratic-forms-symmetrization|модуль 6]] | N |
| 6.2 Неравенство Хансона—Райта | 175–179 | [[30_mathematics/probability/theorems/hanson-wright-inequality|теорема Хансона—Райта]] | N |
| 6.3 Симметризация | 179–181 | модуль 6, [[50_bridges/generalization-complexity-ai|мост к сложности класса]] | N |
| 6.4 Случайные матрицы с неодинаково распределёнными элементами | 181–182 | модуль 6 | N |
| 6.5 Матричное заполнение | 182–185 | модуль 6, будущая лаборатория | N |
| 6.6 Принцип сжатия | 185–186 | модуль 6, мост к сложности класса | N |
| 6.7 Комментарии и упражнения | 186–194 | модуль 6, самопроверка | N |
| 7.1 Случайные процессы | 196–199 | [[30_mathematics/probability/modules/07-random-processes-gaussian-width|модуль 7]] | N |
| 7.2 Неравенства Слепяна, Судакова—Ферника и Гордона | 199–205 | модуль 7, дальнейшая детализация | N |
| 7.3 Точные оценки гауссовских матриц | 205–207 | модуль 7, [[30_mathematics/probability/modules/04-random-matrices|модуль 4]] | N |
| 7.4 Неравенство Судакова | 207–209 | модуль 7, [[20_concepts/gaussian-width-complexity|гауссовская ширина]] | N |
| 7.5 Гауссовская ширина | 209–214 | [[20_concepts/gaussian-width-complexity|самостоятельный концепт]] | N |
| 7.6 Случайные проекции множеств | 214–216 | модуль 7, [[50_bridges/gaussian-width-sample-complexity|сложность выборки]] | N |
| 7.7 Комментарии и упражнения | 216–221 | модуль 7, самопроверка | N |
| 8.1 Неравенство Дадли | 222–228 | [[30_mathematics/probability/theorems/dudley-integral-inequality|теорема Дадли]] | N |
| 8.2 Эмпирические процессы | 228–232 | [[30_mathematics/probability/modules/08-chaining-empirical-processes|модуль 8]] | N |
| 8.3 VC-размерность | 232–242 | модуль 8, [[30_mathematics/probability/theorems/vc-uniform-law-large-numbers|VC-закон больших чисел]] | N |
| 8.4 Теория статистического обучения | 242–245 | [[50_bridges/empirical-processes-adaptive-generalization|адаптивное обобщение]] | N |
| 8.5 Общие цепочки | 245–250 | модуль 8 | N |
| 8.6 Неравенство Шеве | 250–252 | модуль 8, дальнейшая детализация | N |
| 8.7 Комментарии и упражнения | 252–261 | модуль 8, самопроверка | N |
| 9.1 Неравенство отклонения матрицы | 262–267 | [[30_mathematics/probability/theorems/matrix-deviation-inequality|матричное отклонение]] | N |
| 9.2 Ковариация и Джонсон—Линденштраус | 267–271 | [[30_mathematics/probability/modules/09-matrix-deviations-sparse-recovery|модуль 9]], [[50_bridges/random-projections-retrieval|случайные проекции]] | N |
| 9.3 Случайные сечения и теорема выхода из сетки | 271–274 | модуль 9 | N |
| 9.4 Высокоразмерные линейные модели | 274–280 | модуль 9, [[50_bridges/structured-recovery-low-rank-adaptation|структурированное восстановление]] | N |
| 9.5 Точное разреженное восстановление | 280–285 | модуль 9, мост к структурированному восстановлению | N |
| 9.6 Отклонения для общих норм | 285–288 | модуль 9, дальнейшая детализация | N |
| 9.7 Двустороннее неравенство Шеве и теорема Дворецкого—Мильмана | 288–291 | модуль 9, дальнейшая детализация | N |
| 9.8 Комментарии и упражнения | 291–299 | модуль 9, самопроверка | N |

## Контроль источника

- PDF хранится только в `_private/sources/probability`.
- Контрольная сумма SHA-256: `3C8A3748D692DBDF83602F40D2646D5D3B66F956E7B3D06EF438F98A5B1BE226`.
- Публичный экспорт PDF запрещён условиями авторской версии и политикой портала.
- Текстовый слой используется для навигации; формулировки и страницы сверены по визуальному рендеру.
