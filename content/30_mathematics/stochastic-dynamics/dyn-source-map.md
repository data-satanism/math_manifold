---
id: dyn-source-map
title: "Карта источников: Динамические и стохастические системы"
aliases: ["Source map dyn"]
type: source
status: canonical
publish: true
areas: [dynamical-systems, stochastic-differential-equations, source-mapping]
concepts: [source-coverage, content-overlap]
prerequisites: [dyn-course-map]
ai_domains: [time-series, diffusion-models, control, scientific-machine-learning]
source_refs:
  - id: sarkka-solin-sde-2019
    pages: "PDF 1–324"
    role: primary
  - id: score-sde-2021
    pages: "PDF 1–36"
    role: primary
level: research
created: 2026-08-12
updated: 2026-08-12
---

# Карта источников: Динамические и стохастические системы

| № | Источник и страницы | Целевой модуль | Статус |
|---:|---|---|---|
| 1 | sarkka-solin-sde-2019, PDF 12–30 | [[30_mathematics/stochastic-dynamics/modules/dyn-01-flows-existence|Потоки, фазовые пространства и существование решений]] | canonical |
| 2 | sarkka-solin-sde-2019, PDF 12–30 | [[30_mathematics/stochastic-dynamics/modules/dyn-02-stability-lyapunov|Устойчивость, функции Ляпунова и аттракторы]] | canonical |
| 3 | sarkka-solin-sde-2019, PDF 31–50 | [[30_mathematics/stochastic-dynamics/modules/dyn-03-brownian-motion-sde|Броуновское движение и стохастические дифференциальные уравнения]] | canonical |
| 4 | sarkka-solin-sde-2019, PDF 50–66 | [[30_mathematics/stochastic-dynamics/modules/dyn-04-ito-formula|Формула Ито и стохастическое дифференцирование]] | canonical |
| 5 | sarkka-solin-sde-2019, PDF 67–84 | [[30_mathematics/stochastic-dynamics/modules/dyn-05-generator-fokker-planck|Генератор и уравнение Фоккера—Планка]] | canonical |
| 6 | sarkka-solin-sde-2019, PDF 134–171 | [[30_mathematics/stochastic-dynamics/modules/dyn-06-numerical-sde|Численные схемы для SDE: сильная и слабая сходимость]] | canonical |
| 7 | score-sde-2021, PDF 1–12, 13–23 | [[30_mathematics/stochastic-dynamics/modules/dyn-07-reverse-sde-diffusion|Обратное SDE, score-функция и diffusion models]] | canonical |
| 8 | sarkka-solin-sde-2019, PDF 205–282 | [[30_mathematics/stochastic-dynamics/modules/dyn-08-filtering-control-learning|Фильтрация, сглаживание и обучаемые модели состояния]] | canonical |

## Полное покрытие подразделов

| Источник | Глава и все входящие подразделы | Страницы | Решение или целевые модули |
|---|---|---:|---|
| sarkka-solin-sde-2019 | 1–2. Введение и ODE: линейные/общие системы, Fourier/Laplace, численные решения, Picard–Lindelöf | PDF 9–30 | dyn-01-flows-existence;dyn-02-stability-lyapunov |
| sarkka-solin-sde-2019 | 3. Практическое введение в SDE: приложения, white noise, линейные/нелинейные эвристические решения, существование и единственность | PDF 31–49 | dyn-03-brownian-motion-sde |
| sarkka-solin-sde-2019 | 4. Исчисление Ито: интеграл, формула Itô, линейные/нелинейные решения, существование, Stratonovich | PDF 50–66 | dyn-04-ito-formula |
| sarkka-solin-sde-2019 | 5. Распределения SDE: martingales/generators, Fokker–Planck, operator form, Markov/transition densities, moments | PDF 67–84 | dyn-05-generator-fokker-planck |
| sarkka-solin-sde-2019 | 6. Линейные SDE: moments, transition densities, LTI, matrix fraction, covariance, steady state, Fourier | PDF 85–105 | dyn-05-generator-fokker-planck |
| sarkka-solin-sde-2019 | 7. Теоремы: Lamperti, Wiener measure, Girsanov, h-transform, path integrals, Feynman–Kac | PDF 106–133 | reference-only |
| sarkka-solin-sde-2019 | 8. Численная симуляция: Itô–Taylor strong/weak, Runge–Kutta, Verlet, exact algorithm | PDF 134–172 | dyn-06-numerical-sde |
| sarkka-solin-sde-2019 | 9. Нелинейные приближения: assumed density, local linearization, moments, Hermite, FPK discretization, simulated правдоподобие, Wong–Zakai | PDF 173–204 | dyn-06-numerical-sde |
| sarkka-solin-sde-2019 | 10. Фильтрация и сглаживание: inference, trajectory estimates, Kushner–Stratonovich/Zakai, Kalman–Bucy, continuous-discrete фильтрации и сглаживания | PDF 205–241 | dyn-08-filtering-control-learning |
| sarkka-solin-sde-2019 | 11. Оценивание параметров: computational methods, linear SDE, approximate правдоподобие, indirect observations, EM/VB | PDF 242–258 | dyn-08-filtering-control-learning |
| sarkka-solin-sde-2019 | 12. SDE в ML: Gaussian processes, regression, covariance-to-SDE, Kalman GP, spatiotemporal GP, drift/solution approximation | PDF 259–284 | dyn-08-filtering-control-learning |
| sarkka-solin-sde-2019 | 13. Итоги, выбор метода и дальнейшие темы; справочные разделы | PDF 285–324 | reference-only |
| score-sde-2021 | 1–2. Введение; SMLD и DDPM | PDF 1–3 | dyn-07-reverse-sde-diffusion |
| score-sde-2021 | 3. Модель на основе скор-функцииing with SDE: forward perturbation, обратное SDE, score estimation, VE/VP/sub-VP | PDF 3–5 | dyn-07-reverse-sde-diffusion |
| score-sde-2021 | 4. Решение обратное SDE: numerical solvers, predictor–corrector, ODE вероятностного потока, architecture | PDF 5–8 | dyn-06-numerical-sde;dyn-07-reverse-sde-diffusion |
| score-sde-2021 | 5–6. Управляемая генерация и выводы | PDF 8–13 | dyn-07-reverse-sde-diffusion |
| score-sde-2021 | A–D. General SDE, VE/VP, probability-flow derivation/правдоподобие/sampling | PDF 13–20 | dyn-07-reverse-sde-diffusion |
| score-sde-2021 | E–H. Reverse diffusion, ancestral и predictor–corrector sampling, architecture | PDF 20–29 | dyn-06-numerical-sde;dyn-07-reverse-sde-diffusion |
| score-sde-2021 | I. Controllable generation: class conditioning, imputation, colorization, inverse problems | PDF 29–36 | dyn-07-reverse-sde-diffusion |

## Правило покрытия

Каждый указанный диапазон проверяется в исходном PDF. Если соседние подразделы объединены, их границы остаются видимыми в этой таблице и в `source_refs` модуля. Совпадающее содержание расширяет существующий узел или получает ссылку `reference-only`; отдельное определение-дубликат не создаётся.
