---
id: lab-rmt-random-features-capacity
title: "Лаборатория RMT 04. Случайные признаки, вместимость и регуляризация"
aliases: ["Random features lab", "Случайные признаки и двойной спуск"]
type: lab
status: canonical
publish: true
areas: [random-matrix-theory, random-features, scientific-computing]
concepts: [random-feature-gram-matrix, deterministic-equivalent, double-descent]
prerequisites: [random-feature-gram-deterministic-equivalent]
ai_domains: [random-features, regression, neural-networks]
source_refs:
  - id: rmt4ml-2022
    pages: "299-317"
    role: primary
  - id: louart2018randomnn
    pages: "1-19"
    role: primary
level: advanced
created: 2026-07-30
updated: 2026-08-12
---

# Лаборатория RMT 04. Случайные признаки, вместимость и регуляризация

## Исследовательский вопрос

Что происходит с ошибками обучения и теста, когда число случайных признаков проходит через число обучающих объектов?

## Эксперимент

Однослойное случайное отображение с ReLU используется как замороженный слой, а выходной линейный регрессор обучается с малой гребневой регуляризацией.

```powershell
python 70_labs/rmt/rmt_release_experiments.py `
  --experiment random-features `
  --output-dir 80_assets/random-matrix-theory/labs-v1
```

![Ошибки обучения и теста случайной признаковой модели при изменении отношения числа признаков к числу объектов](80_assets/random-matrix-theory/labs-v1/lab-random-features-double-descent.png)

## Проверки

- повторить опыт для нескольких $\gamma$;
- заменить ReLU на гладкую липшицеву активацию;
- сравнить разные реализации случайных весов;
- проверить, исчезает ли пик ошибки при усилении регуляризации.

## Граница

**Установлено.** Эксперимент соответствует модели одного случайного замороженного слоя.

**Не следует.** Кривая не является универсальным законом для обучаемых глубоких сетей.
