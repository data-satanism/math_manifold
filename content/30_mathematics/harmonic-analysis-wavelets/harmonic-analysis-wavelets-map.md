---
id: harmonic-analysis-wavelets-map
title: "Гармонический анализ и вейвлеты"
aliases: [Карта курса по гармоническому анализу]
type: map
status: canonical
publish: true
areas: [harmonic-analysis, wavelets]
concepts: [fourier-transform, wavelet, multiresolution-analysis, scattering]
prerequisites: [real-analysis-map, functional-analysis-map]
ai_domains: [signal-processing, representation-learning, operator-learning]
source_refs:
  - id: tao-epsilon-of-room-2010
    pages: "205–237; 279–289; 357–365"
    role: primary
  - id: tyrtyshnikov-numerical-analysis
    pages: "253–276"
    role: primary
  - id: mallat-multiresolution-wavelet-bases-1989
    pages: "1–34"
    role: primary
  - id: mallat-wavelet-representation-1989
    pages: "1–20"
    role: primary
  - id: daubechies-compact-wavelets-1988
    pages: "1–88"
    role: primary
  - id: bruna-mallat-scattering-2012
    pages: "1–15"
    role: bridge
level: research
created: 2026-08-31
updated: 2026-09-03
---
# Гармонический анализ и вейвлеты

## Назначение курса

Курс связывает строгую теорию преобразования Фурье с локализованными многомасштабными представлениями. Основной маршрут идёт от характеров и свёртки к неопределённости, дискретизации, разложениям Литтлвуда—Пэли, многоразрешающему анализу, банкам фильтров, вейвлетам Добеши и рассеянию.

## Маршрут из 12 модулей

1. [[30_mathematics/harmonic-analysis-wavelets/modules/ha-01-harmonic-viewpoint-characters|Гармонический взгляд: частоты, характеры и симметрии]]
2. [[30_mathematics/harmonic-analysis-wavelets/modules/ha-02-fourier-schwartz-inversion|Преобразование Фурье, пространство Шварца и обращение]]
3. [[30_mathematics/harmonic-analysis-wavelets/modules/ha-03-convolution-approximate-identities|Свёртка, приближения единицы и спектральные фильтры]]
4. [[30_mathematics/harmonic-analysis-wavelets/modules/ha-04-energy-decay-interpolation|Энергия, спад спектра и интерполяционные оценки]]
5. [[30_mathematics/harmonic-analysis-wavelets/modules/ha-05-uncertainty-time-frequency|Принцип неопределённости и локализация во времени и частоте]]
6. [[30_mathematics/harmonic-analysis-wavelets/modules/ha-06-sampling-dft-fft-aliasing|Дискретизация, преобразование Фурье, быстрый алгоритм и наложение спектров]]
7. [[30_mathematics/harmonic-analysis-wavelets/modules/ha-07-dyadic-littlewood-paley|Диадические полосы, разложения Литтлвуда—Пэли и регулярность]]
8. [[30_mathematics/harmonic-analysis-wavelets/modules/ha-08-continuous-wavelets-admissibility|Непрерывное вейвлетное преобразование и условие допустимости]]
9. [[30_mathematics/harmonic-analysis-wavelets/modules/ha-09-multiresolution-haar|Многоразрешающий анализ, масштабирующая функция и базис Хаара]]
10. [[30_mathematics/harmonic-analysis-wavelets/modules/ha-10-filter-banks-perfect-reconstruction|Банки фильтров, квадратурные зеркальные условия и точное восстановление]]
11. [[30_mathematics/harmonic-analysis-wavelets/modules/ha-11-compact-wavelets-sparsity|Компактный носитель, исчезающие моменты, регулярность и разреженность]]
12. [[30_mathematics/harmonic-analysis-wavelets/modules/ha-12-scattering-ai-protocol|Вейвлетное рассеяние, устойчивость к деформациям и протокол для ИИ]]

## Самостоятельные теоремные узлы

- [[30_mathematics/harmonic-analysis-wavelets/theorems/fourier-inversion-theorem|Теорема обращения Фурье]]
- [[30_mathematics/harmonic-analysis-wavelets/theorems/riemann-lebesgue-lemma|Лемма Римана—Лебега]]
- [[30_mathematics/harmonic-analysis-wavelets/theorems/fourier-convolution-theorem|Теорема о преобразовании Фурье свёртки]]
- [[30_mathematics/harmonic-analysis-wavelets/theorems/heisenberg-uncertainty-principle|Принцип неопределённости Гейзенберга для преобразования Фурье]]
- [[30_mathematics/harmonic-analysis-wavelets/theorems/poisson-summation-formula|Формула суммирования Пуассона]]
- [[30_mathematics/harmonic-analysis-wavelets/theorems/mallat-mra-wavelet-basis|Теорема Малла: из многоразрешающего анализа получается вейвлетный базис]]
- [[30_mathematics/harmonic-analysis-wavelets/theorems/perfect-reconstruction-filter-bank|Теорема о точном восстановлении параунитарного банка фильтров]]
- [[30_mathematics/harmonic-analysis-wavelets/theorems/daubechies-compact-wavelet-existence|Теорема Добеши о компактно поддержанных ортонормированных вейвлетах]]
- [[30_mathematics/harmonic-analysis-wavelets/theorems/scattering-nonexpansiveness-stability|Нерастягиваемость и деформационная устойчивость вейвлетного рассеяния]]
- [[30_mathematics/real-analysis/theorems/plancherel-theorem|Теорема Планшереля]] переиспользуется без дублирования.

## Связи с существующим графом

- [[30_mathematics/real-analysis/modules/05-fourier-distributions|Преобразование Фурье и обобщённые функции]] даёт аналитическую основу.
- [[30_mathematics/numerical-analysis/modules/25-structured-toeplitz-circulant|Циркулянты и БПФ]] остаются вычислительным узлом.
- [[30_mathematics/numerical-analysis/modules/26-hierarchical-low-rank-wavelets|Вейвлеты у Тыртышникова]] не копируются, а углубляются теорией многоразрешающего анализа и фильтров.
- [[30_mathematics/operator-learning/modules/opl-05-fourier-neural-operator|Фурье-нейронный оператор]] использует спектральные множители.
- [[30_mathematics/geometric-deep-learning/modules/gdl-05-equivariant-operators-convolution|Эквивариантные операторы]] обобщают гармонический взгляд на группы.

## Лабораторный маршрут

- [[70_labs/harmonic-analysis-wavelets/fourier-wavelet-labs|Три воспроизводимых эксперимента]].
- [[50_bridges/harmonic-localization-ai|Локализация и многомасштабные представления → архитектуры ИИ]].
- [[50_bridges/wavelets-multiresolution-representations|Вейвлеты → многоразрешающие представления в ИИ]].

## Статус выпуска

Материалы утверждены владельцем 3 сентября 2026 года и включены в публичный выпуск со статусом `canonical` и `publish: true`.
