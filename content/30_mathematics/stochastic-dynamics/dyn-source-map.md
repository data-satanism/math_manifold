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
updated: 2026-09-03
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
| 7 | score-sde-2021, PDF 1–12, 13–23 | [[30_mathematics/stochastic-dynamics/modules/dyn-07-reverse-sde-diffusion|Обратное SDE, скор-функция и диффузионные модели]] | canonical |
| 8 | sarkka-solin-sde-2019, PDF 205–282 | [[30_mathematics/stochastic-dynamics/modules/dyn-08-filtering-control-learning|Фильтрация, сглаживание и обучаемые модели состояния]] | canonical |

## Полное покрытие подразделов

| Источник | Глава и все входящие подразделы | Страницы | Решение или целевые модули |
|---|---|---:|---|
| sarkka-solin-sde-2019 | 1–2. Введение и ODE: линейные и общие системы, преобразования Фурье и Лапласа, численные решения, теорема Пикара—Линделёфа | PDF 9–30 | dyn-01-flows-existence;dyn-02-stability-lyapunov |
| sarkka-solin-sde-2019 | 3. Практическое введение в SDE: приложения, белый шум, линейные и нелинейные эвристические решения, существование и единственность | PDF 31–49 | dyn-03-brownian-motion-sde |
| sarkka-solin-sde-2019 | 4. Исчисление Ито: интеграл, формула Ито, линейные и нелинейные решения, существование, интерпретация Стратоновича | PDF 50–66 | dyn-04-ito-formula |
| sarkka-solin-sde-2019 | 5. Распределения SDE: мартингалы и генераторы, уравнение Фоккера—Планка, операторная форма, марковские переходные плотности и моменты | PDF 67–84 | dyn-05-generator-fokker-planck |
| sarkka-solin-sde-2019 | 6. Линейные SDE: моменты, переходные плотности, стационарные линейные системы, матричные дроби, ковариация, установившийся режим и преобразование Фурье | PDF 85–105 | dyn-05-generator-fokker-planck |
| sarkka-solin-sde-2019 | 7. Теоремы: преобразование Ламперти, мера Винера, теорема Гирсанова, h-преобразование, интегралы по траекториям и формула Фейнмана—Каца | PDF 106–133 | reference-only |
| sarkka-solin-sde-2019 | 8. Численное моделирование: сильные и слабые схемы Ито—Тейлора, методы Рунге—Кутты и Верле, точный алгоритм | PDF 134–172 | dyn-06-numerical-sde |
| sarkka-solin-sde-2019 | 9. Нелинейные приближения: аппроксимация плотности, локальная линеаризация, моменты, полиномы Эрмита, дискретизация FPK, приближённое правдоподобие и предел Вонга—Закая | PDF 173–204 | dyn-06-numerical-sde |
| sarkka-solin-sde-2019 | 10. Фильтрация и сглаживание: вероятностный вывод, оценивание траекторий, уравнения Кушнера—Стратоновича и Закая, фильтр Калмана—Бьюси, непрерывно-дискретные методы | PDF 205–241 | dyn-08-filtering-control-learning |
| sarkka-solin-sde-2019 | 11. Оценивание параметров: вычислительные методы, линейные SDE, приближённое правдоподобие, косвенные наблюдения, EM и вариационный байесовский вывод | PDF 242–258 | dyn-08-filtering-control-learning |
| sarkka-solin-sde-2019 | 12. SDE в машинном обучении: гауссовские процессы, регрессия, переход от ковариации к SDE, представление гауссовского процесса фильтром Калмана, пространственно-временные процессы, аппроксимация дрейфа и решения | PDF 259–284 | dyn-08-filtering-control-learning |
| sarkka-solin-sde-2019 | 13. Итоги, выбор метода и дальнейшие темы; справочные разделы | PDF 285–324 | reference-only |
| score-sde-2021 | 1–2. Введение; SMLD и DDPM | PDF 1–3 | dyn-07-reverse-sde-diffusion |
| score-sde-2021 | 3. Моделирование на основе скор-функции с помощью SDE: прямое возмущение, обратное SDE, оценивание скор-функции, варианты VE, VP и sub-VP | PDF 3–5 | dyn-07-reverse-sde-diffusion |
| score-sde-2021 | 4. Решение обратного SDE: численные решатели, схема предиктор—корректор, ODE потока вероятности и архитектура | PDF 5–8 | dyn-06-numerical-sde;dyn-07-reverse-sde-diffusion |
| score-sde-2021 | 5–6. Управляемая генерация и выводы | PDF 8–13 | dyn-07-reverse-sde-diffusion |
| score-sde-2021 | A–D. Общие SDE, VE/VP, вывод уравнения потока вероятности/правдоподобие/генерация выборок | PDF 13–20 | dyn-07-reverse-sde-diffusion |
| score-sde-2021 | E–H. Обратная диффузия, последовательная генерация выборок и схема предиктор—корректор, архитектура | PDF 20–29 | dyn-06-numerical-sde;dyn-07-reverse-sde-diffusion |
| score-sde-2021 | I. Управляемая генерация: условная генерация по классу, восстановление пропусков, раскрашивание, обратные задачи | PDF 29–36 | dyn-07-reverse-sde-diffusion |

## Правило покрытия

Каждый указанный диапазон проверяется в исходном PDF. Если соседние подразделы объединены, их границы остаются видимыми в этой таблице и в `source_refs` модуля. Совпадающее содержание расширяет существующий узел или получает ссылку `reference-only`; отдельное определение-дубликат не создаётся.
