---
id: rmt-source-map
title: "Source map курса по теории случайных матриц"
aliases: ["RMT source map", "Карта источников RMT"]
type: map
status: canonical
publish: true
areas: [random-matrix-theory, high-dimensional-statistics]
concepts: [empirical-spectral-distribution, resolvent-stieltjes-transform, marchenko-pastur-law, spiked-covariance-transition]
prerequisites: [random-matrix-theory-map]
ai_domains: [statistical-learning, kernels, neural-networks, graph-ml, optimization, tensor-learning]
source_refs:
  - id: rmt4ml-2022
    pages: "1-446 PDF pages"
    role: primary
  - id: rmt-local-notes
    pages: "RMT Markdown folder"
    role: intuition
  - id: louart2018randomnn
    pages: "1-59 PDF pages"
    role: primary
  - id: couillet2011wirelessrmt
    pages: "41-267 PDF pages"
    role: secondary
  - id: goulart2022randomtensors
    pages: "1-36 PDF pages"
    role: primary
  - id: seddik2022randomtensors
    pages: "1-45 PDF pages"
    role: primary
  - id: lebeau2025tensor
    pages: "1-64 PDF pages"
    role: primary
level: advanced
created: 2026-07-10
updated: 2026-07-27
---

# Source map курса по теории случайных матриц

## Основная монография

| Раздел RMT4ML | Страницы | Целевой материал | Состояние |
|---|---:|---|---|
| 1.1 Ловушки статистики большой размерности | 7–18 | [[30_mathematics/random-matrix-theory/modules/01-high-dimensional-spectra]] | review |
| 1.2 Теория случайных матриц как ответ | 19–38 | [[30_mathematics/random-matrix-theory/modules/01-high-dimensional-spectra]] | review |
| 1.3 План книги и программные материалы | 39–42 | [[30_mathematics/random-matrix-theory/random-matrix-theory-map]] | review |
| 2.1 Фундаментальные объекты | 44–50 | [[20_concepts/empirical-spectral-distribution]], [[20_concepts/resolvent-stieltjes-transform]] | review |
| 2.2 Основополагающие результаты | 51–90 | [[30_mathematics/random-matrix-theory/theorems/marchenko-pastur-law]]; модуль 2 запланирован | partial |
| 2.3 Продвинутый анализ выборочных ковариаций | 91–97 | модуль 2 | planned |
| 2.4 Предварительные сведения по статистическому выводу | 98–112 | модуль 3 | planned |
| 2.5 Спайковые модели | 113–126 | [[30_mathematics/random-matrix-theory/theorems/spiked-covariance-transition]] | review |
| 2.6 Модели «сигнал плюс шум» и деформированный Вигнер | 127–142 | модуль 2 | planned |
| 2.7 Концентрация меры в RMT | 143–159 | модуль 2 | planned |
| 2.8 Итоги | 160–161 | карта зависимостей | planned |
| 2.9 Упражнения | 162–168 | лабораторные работы | planned |
| 3.1 Обнаружение и оценивание в моделях «сигнал плюс шум» | 171–187 | модуль 3 | planned |
| 3.2 Оценивание расстояний между ковариациями | 188–199 | модуль 3 | planned |
| 3.3 M-оценки матрицы рассеяния | 200–214 | модуль 3 | planned |
| 3.4–3.5 Итоги и практикум | 215–224 | модуль 3 и лаборатория | planned |
| 4.1 Базовая постановка ядровых методов | 227–229 | модуль 4 | planned |
| 4.2 Случайные ядровые матрицы расстояний и скалярных произведений | 230–246 | модуль 4 | planned |
| 4.3 Правильное масштабирование ядра | 247–261 | модуль 4 | planned |
| 4.4 Следствия для ядровых методов | 262–293 | модуль 4 | planned |
| 4.5–4.6 Итоги и практикум | 294–298 | модуль 4 и лаборатория | planned |
| 5.1 Случайные нейронные сети | 299–317 | модуль 5 | planned |
| 5.2 Динамика градиентного спуска в линейных сетях | 318–324 | модуль 5 | planned |
| 5.3 Рекуррентные сети и эхо-состояния | 325–332 | модуль 5 | planned |
| 5.4–5.5 Итоги и практикум | 333–338 | модуль 5 и лаборатория | planned |
| 6.1 Обобщённый линейный классификатор | 340–352 | модуль 6 | planned |
| 6.2 Метод опорных векторов большой размерности | 353–357 | модуль 6 | planned |
| 6.3–6.4 Итоги и практикум | 358–364 | модуль 6 и лаборатория | planned |
| 7.1 Сообщества в плотных графах | 366–383 | модуль 7 | planned |
| 7.2 Переход к разреженным графам | 384–390 | модуль 7 | planned |
| 7.3–7.4 Итоги и практикум | 391–394 | модуль 7 и лаборатория | planned |
| 8.1 От гауссовых смесей к концентрированным векторам и GAN | 395–404 | модуль 8 | planned |
| 8.2 Универсальность в широком смысле для ML | 405–407 | модуль 8 | planned |
| 8.3 Обсуждение и выводы | 408–410 | итоговая карта | planned |

## Дополнительные источники

| Источник | Точные страницы и результат | Целевой материал | Решение |
|---|---|---|---|
| [[60_sources/louart-liao-couillet-random-neural-networks|Louart, Liao, Couillet (2018)]] | 1–19: модель случайных признаков, резольвента, ошибки обучения и тестирования; 20–53: доказательства | [[50_bridges/rmt-random-feature-networks]], модуль 5 | rewrite; established только для однослойной случайной сети |
| [[60_sources/couillet-debbah-wireless-rmt|Couillet, Debbah (2011)]] | 59–94: метод Штильтьеса и закон Марченко—Пастура; 137–222: детерминированные эквиваленты и носитель спектра; 247–266: спайки и края | модули 1–3 | reference-only; вторичный строгий источник |
| [[60_sources/goulart-couillet-comon-random-tensors|Goulart, Couillet, Comon (2022)]] | 7–19: свёртки тензора, спектральная мера и оценка спайка | [[30_mathematics/random-matrix-theory/modules/09-random-tensors]] | rewrite; различать доказанную часть для $d=3$ и гипотезу для больших $d$ |
| [[60_sources/seddik-guillaud-couillet-random-tensors|Seddik, Guillaud, Couillet (2022)]] | 2–25: асимметричный спайковый тензор, блочная матрица и согласованность направлений | [[30_mathematics/random-matrix-theory/modules/09-random-tensors]] | merge; сохранять различие порогов |
| [[60_sources/lebeau-chatelain-couillet-tensor-approximation|Lebeau, Chatelain, Couillet (2025)]] | 9–24: развёртки, усечённый многолинейный SVD и итерация высшего порядка; 26–45: RMT-доказательства | [[30_mathematics/random-matrix-theory/modules/09-random-tensors]] | rewrite; не интерпретировать как работу о LoRA |

### Исправление семантической ошибки

Файл `random matrix for LoRa.pdf`, скопированный как `rmt-lora.pdf`, фактически содержит статью о **низком многолинейном ранге тензора**. Он не относится к низкоранговой адаптации LoRA. Поэтому выбор ранга LoRA по спектральным выбросам остаётся [[50_bridges/rmt-spectral-diagnostics|исследовательской гипотезой]], а не установленным следствием нового источника.
## Локальные конспекты

| Группа | Роль | Решение |
|---|---|---|
| `Введение/Глава 1–4` | Тензорные примеры, фазовые переходы, выбор ранга | rewrite; проектные утверждения маркировать как гипотезы |
| `Глава 1/Глава 1–1.4` | Высокоразмерная интуиция, расстояния, ядра, универсальность | merge в модули 1, 4 и 8 |
| `Глава 2/Глава 2.1–2.5` | Формализм, преобразование Штильтьеса, резольвента, спайки | merge после сверки с RMT4ML |
| `Глава 2/Приложения/2.5.1` | Спектральный анализ внимания | reference-only; связь пока исследовательская |
| `Глава 3` | Линейные статистические модели | rewrite в модуле 3 |
| `Дополнение 1` и `Дополнение 2` | Репозиторные проекты и код | private-source; не публиковать автоматически |

## Контроль источника

Оригинальная папка RMT остаётся неизменной. Приватная копия `RMT4ML.pdf` имеет SHA-256 `07F6C9A1C23C1B4DF331595BBC82DC60DD04D5B8ADF46583768D380AAC465702`.

Дополнительные приватные копии и SHA-256:

- `rmt-neural-networks.pdf`: `64EC8C361190899CD773279D177A926E2AD62FD30ADC9075AC2084FE9D8F6609`;
- `rmt-wireless-communications.pdf`: `3356A19C14628661745A4C87DA5001E8A9471A99CF5B4AF521B735229904CAB3`;
- `rmt-to-random-tensors.pdf`: `425D9A777EE81AE9A9208333CEDA441894132D5AFE128E12CF23E7B3EB95B10C`;
- `random-tensors.pdf`: `A3BD077528F2BB6D3E9AB4D01088CEFE9A24BAFC171F04CE14C1BF5CECD748EF`;
- `rmt-lora.pdf`: `6E8602E810C299E5EDE01CA95E4696A0D46CAC5D24969E4F67BCF36AAC20A66D`.
