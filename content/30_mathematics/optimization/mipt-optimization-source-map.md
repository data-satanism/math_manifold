---
id: mipt-optimization-source-map
title: "Карта источника: методы оптимизации МФТИ"
aliases: ["Карта курса оптимизации"]
type: source
status: canonical
publish: true
areas: [optimization, source-mapping]
concepts: [source-coverage, content-overlap]
prerequisites: []
ai_domains: [machine-learning, automl]
source_refs:
  - id: mipt-optimization-course
    pages: "7–394"
    role: primary
level: advanced
created: 2026-08-11
updated: 2026-08-12
---

# Карта источника: методы оптимизации МФТИ

Карта сохраняет соответствие пособию, лекциям и практическим заданиям. Материал, уже подробно изложенный в курсах линейной алгебры, функционального и численного анализа, не копируется: модуль оптимизации добавляет постановку задачи, условия применимости алгоритма и экспериментальный ракурс.

| Модуль | Пособие | Лекции | Дополнение к существующему графу |
|---|---|---|---|
| [[30_mathematics/optimization/modules/01-problem-geometry|1. Постановка и геометрия]] | C1–C4, C8–C9, с. 7–77, 117–147 | L1–L2 | выбор нормы, допустимого множества и параметризации |
| [[30_mathematics/optimization/modules/02-gradient-methods-ml|2. Градиентные методы]] | L3–L5, L7–L8, L14–L15, с. 201–257, 273–305, 374–394 | L3–L5, L7–L8, L14–L15 | скорость, шум и вычислительный бюджет обучения |
| [[30_mathematics/optimization/modules/03-constraints-structure-splitting|3. Ограничения и расщепление]] | C6–C7, C10, с. 90–116, 148–167 | L6, L9–L13, L15 | проекция, Франк—Вульф, зеркальный спуск и ADMM |
| [[30_mathematics/optimization/modules/04-duality-regularization-kkt|4. Двойственность и ККТ]] | C5–C8, с. 78–132 | L8, L11, L13 | цена ограничений, двойственный разрыв и регуляризация |
| [[30_mathematics/optimization/modules/05-stochastic-online-time-series|5. Стохастическая и последовательная оптимизация]] | с. 248–257, 288–305, 374–394 | L5, L8, L14–L15 | временной дрейф и корректная проверка без утечки будущего |
| [[30_mathematics/optimization/modules/06-conic-sdp-kernel|6. Коническая и полуопределённая оптимизация]] | C8–C10, с. 117–167 | L12 | положительно полуопределённые матрицы, ядра и барьеры |
| [[30_mathematics/optimization/modules/07-derivative-free-bayesian-automl|7. Безградиентная и байесовская оптимизация]] | с. 389–394 | L15 | дорогие эксперименты, суррогатная модель и AutoML |
| [[30_mathematics/optimization/modules/08-linear-programming-discrete-relaxations|8. Линейное программирование и релаксации]] | C9–C11, с. 133–175 | L9, L15 | дискретный выбор, симплекс и округление |
| [[30_mathematics/optimization/modules/09-second-order-curvature|9. Методы второго порядка]] | C2, с. 21–42 | L6–L7, L15 | гессиан-векторные произведения, область доверия и демпфирование |
| [[30_mathematics/optimization/modules/10-nonsmooth-proximal|10. Негладкая оптимизация]] | C5–C6, с. 78–104 | L8, L11 | субградиенты, проксимальный шаг и мягкий порог |
| [[30_mathematics/optimization/modules/11-variance-reduction-finite-sums|11. Снижение дисперсии]] | с. 248–257, 374–388 | L5, L14 | SVRG, SAGA и SARAH для конечных сумм |
| [[30_mathematics/optimization/modules/12-primal-dual-minimax-robust|12. Прямо-двойственные и минимаксные методы]] | C7–C8, с. 105–132 | L11, L13 | седловая динамика, экстраградиент и устойчивые цели |
| [[30_mathematics/optimization/modules/13-optimization-experiment-protocol|13. Протокол эксперимента]] | с. 248–257, 374–394 | L5, L14–L15 | равный бюджет, неопределённость и воспроизводимость |

## Контроль пересечений

- матричные нормы, обусловленность и разложения остаются каноническими в [[30_mathematics/linear-algebra/boss-linear-algebra-source-map|линейной алгебре]] и численном анализе;
- теоремы о неподвижной точке и неявной функции остаются в функциональном анализе;
- концентрационные оценки стохастических градиентов связываются с курсом вероятности;
- положительно полуопределённые матрицы Грама связываются с [[30_mathematics/kernel-methods/kernel-methods-source-map|ядерными методами]];
- новые страницы оптимизации добавляют алгоритмический выбор, критерии остановки и честный протокол сравнения.
