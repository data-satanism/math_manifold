---
id: lab-exponential-rkhs-statistical-models-figures
title: "Промпты иллюстраций: экспоненциальные модели RKHS"
aliases: ["Иллюстрации раздела 5.1 ядерных методов"]
type: lab
status: canonical
publish: true
areas: [kernel-methods, scientific-visualization]
concepts: [log-partition-function, exponential-family, structured-prediction, constraint-generation]
prerequisites: [km-04-exponential-rkhs-statistical-models]
ai_domains: [probabilistic-modeling, structured-prediction, energy-based-models]
source_refs:
  - id: hofmann-scholkopf-smola-kernel-methods-2006
    pages: "29-35"
    role: visual-source
level: advanced
created: 2026-07-21
updated: 2026-07-27
---

# Промпты иллюстраций: экспоненциальные модели RKHS

Все изображения создаются встроенной GPT.Image моделью, сохраняются в `80_assets/kernel-methods/gpt-image-v3` и проходят ручную проверку математического смысла и русских подписей. Текст в изображении является объяснительным слоем; точные утверждения находятся в Markdown-заметках.

## Общий неизменный префикс

> ICML-style scientific figure, clean academic vector infographic, white background, muted blue-gray palette with one accent color, minimal typography, precise arrows, thin lines, labeled panels, no photorealism, no 3D glossy rendering, no decorative background, conference-paper figure aesthetics, mathematically clean, visually balanced.

> Russian-first scientific labels; use English only for standard abbreviations. Clearly distinguish established result, analogy, research hypothesis, and failure mode.

## Модуль

Файл: `gpt-image-v3/exponential-rkhs-statistical-models-module-v3.png`

Промпт после общего префикса:

> Use case: scientific-educational. Landscape figure for the course module «Экспоненциальные статистические модели в RKHS». Three labeled panels and one compact warning strip. Panel A «Математическая идея»: show a smooth RKHS score surface f over inputs and answers, exponentiation into positive weights, row-wise normalization into probability bars summing to one, then arrows to «моменты» and «ковариация»; use only the simple labels «оценка f», «нормировка», «вероятность», «моменты». Panel B «Понятный образ»: a precise shared-budget analogy—several requests receive fractions of one fixed circular budget, changing one fraction forces the others to change; map requests to scores and budget shares to probabilities. Panel C «Перенос в ИИ»: a structured prediction example with one input, several candidate sequences, normalized confidence bars, and a small diagnostic comparing «модельные» versus «наблюдаемые» moments; label the connection «установлено». Warning strip «Режим отказа»: infinite normalization, expensive sum over answers, and MAP is not full uncertainty. Avoid complex formulas, English prose, neural-network decoration, and any claim that universality guarantees learning.

## Геометрия логарифмической статистической суммы

Файл: `gpt-image-v3/log-partition-moment-geometry-v3.png`

Промпт после общего префикса:

> Use case: scientific-educational. Landscape theorem figure «Геометрия логарифмической статистической суммы». Panel A «Математическая идея»: a family of weighted states entering one normalization box g; one arrow labeled «градиент = среднее», another labeled «гессиан = ковариация», with a small positive-semidefinite curvature bowl; keep formulas symbolic and exact, no invented constants. Panel B «Понятный образ»: a calibrated balance scale with «данные» on one side and «модель» on the other; imbalance arrow is the moment residual, coupled moving weights represent covariance. Panel C «Перенос в ИИ»: softmax probabilities and cross-entropy residual p minus observed label, labeled «установлено», plus a small Hessian spectrum diagnostic. Warning strip «Режим отказа»: duplicated statistics cause a flat direction; separable data can send parameter norm to infinity. Minimal Russian typography, no English words except RKHS if needed.

## Плотность экспоненциальных моделей RKHS

Файл: `gpt-image-v3/exponential-rkhs-density-universality-v3.png`

Промпт после общего префикса:

> Use case: scientific-educational. Landscape theorem figure «Плотность экспоненциальных моделей RKHS». Panel A «Математическая идея»: show a positive target density p, its finite smooth log p curve, an RKHS approximation f close to log p, then exponentiation and normalization producing q close to p; visibly show the assumption p bounded away from zero and label it «p > 0». Panel B «Понятный образ»: a flexible membrane shaped to the log-density profile, then uniformly lifted into a positive profile and rescaled to total mass one; map membrane shape to f and total fill to normalization. Panel C «Перенос в ИИ»: a small controlled kernel energy model benchmark, labeled «установлено: аппроксимация» and separately «не гарантирует обучение». Warning strip «Режим отказа»: a density touching zero breaks direct log approximation, a constant kernel cannot fit shapes, infinite normalizer. Do not claim the theorem covers zeros without extra regularization; no complex formulas.

## Условная экспоненциальная модель

Файл: `gpt-image-v3/conditional-exponential-rkhs-model-v3.png`

Промпт после общего префикса:

> Use case: scientific-educational. Landscape method figure «Условная экспоненциальная модель RKHS». Panel A «Математическая идея»: a matrix with input rows x and candidate-answer columns y, score cells f(x,y), each row passed through normalization to probability bars; a joint-kernel link connects similar input-answer pairs. Panel B «Понятный образ»: a route map from one origin to several destinations; route scores become shares of one flow only after a toll-gate normalization, with a clear mapping from route to candidate answer. Panel C «Перенос в ИИ»: show three compact examples—classification, sequence labeling, and Gaussian-process classification—with one common score-to-probability mechanism; label «установлено». Warning strip «Режим отказа»: exact sum over structures may be intractable; approximate inference biases moments; MAP is not Bayesian averaging. Russian labels only except RKHS and GP.

## Двойственность структурированного мягкого отступа

Файл: `gpt-image-v3/structured-soft-margin-duality-v3.png`

Промпт после общего префикса:

> Use case: scientific-educational. Landscape theorem figure «Двойственность структурированного мягкого отступа». Panel A «Математическая идея»: for each input show one correct structured output and several competitors; arrows form difference features «правильный − конкурент»; only close competitors receive nonzero dual weights and become «опорные пары»; show a positive-semidefinite Gram matrix of these difference features without detailed entries. Panel B «Понятный образ»: a tournament table where the winner must lead each rival by a fixed margin; only near-ties require referee attention, precisely mapped to nonzero multipliers. Panel C «Перенос в ИИ»: sequence or parse-tree prediction with highlighted offending competitor and a checkable margin residual, labeled «установлено». Warning strip «Режим отказа»: indefinite kernel makes the quadratic problem nonconvex; infinite answer space needs an oracle; sparsity is not guaranteed. No English prose.

## Гарантия добавления ограничений

Файл: `gpt-image-v3/constraint-generation-epsilon-guarantee-v3.png`

Промпт после общего префикса:

> Use case: scientific-educational. Landscape theorem figure «Гарантия ε-точности при добавлении ограничений». Panel A «Математическая идея»: an iterative working set starts small; a separation oracle finds the most violated constraint; add it, re-optimize, repeat; stop only when maximum violation is at most ε; show objective lower bound from relaxation and upper bound after adding ε to slack. Panel B «Понятный образ»: a security inspector finds the largest loophole, adds that rule to an active checklist, and certifies no loophole larger than ε; explicitly map inspector to oracle and loophole size to violation. Panel C «Перенос в ИИ»: structured sequence decoding with a dynamic-programming oracle and a plot of maximum violation decreasing, labeled «установлено при точном оракуле». Warning strip «Режим отказа»: approximate oracle can miss a violation, unfair schedule can ignore examples, nonconvex neural decoder is outside the theorem. Avoid displaying the long iteration-bound formula; no invented constants.

## AI-мост

Файл: `gpt-image-v3/log-partition-kernels-energy-models-bridge-v3.png`

Промпт после общего префикса:

> Use case: scientific-educational. Landscape bridge figure «Логарифмическая статистическая сумма → ядерные и энергетические модели». Use bridge panel titles «Математическая структура», «Интуитивный перенос», «ИИ: механизм и проверка» plus «Режим отказа». First panel: score f, exponentiation, normalization, probability, moment residual, covariance curvature in one precise flow. Second panel: fixed total budget divided among competing requests, with exact mapping score→request and probability→budget share. Third panel: two established branches—softmax or CRF with exact normalized probabilities, and GP classification distinguishing posterior mode from integration; one research-hypothesis branch for neural energy models shown with a dashed outline. Include diagnostics «остаток моментов», «калибровка», «ошибка нормировки». Failure strip: infinite partition function, biased approximate inference, singular statistics, expressiveness does not imply generalization. Russian-first labels, standard abbreviations CRF, GP, RKHS allowed, no English prose.

## Контрольные суммы

Встроенный режим GPT.Image; окончательные отобранные файлы:

| Файл | SHA-256 |
|---|---|
| `conditional-exponential-rkhs-model-v3.png` | `8c38113fd4f3c2a648a3acec706e54f0ed30479f54a1c10c27bcb63825c3cfcf` |
| `constraint-generation-epsilon-guarantee-v3.png` | `74dc4f07553397800359f81655c285d82d2a36aedaa8856ccf7e59653170de0e` |
| `exponential-rkhs-density-universality-v3.png` | `541df146a64ef250f050eb4a6e7feed90476a732b9079db137a3c1284573cc29` |
| `exponential-rkhs-statistical-models-module-v3.png` | `c9e41d35977328be1401e382de0f859a4a00b4f8b777208b2b6aa8a0e2c65595` |
| `log-partition-kernels-energy-models-bridge-v3.png` | `4b27f6c1039ebf3dd8608f189be2826c79c9ad0f72190ef9bc085726c0dfa273` |
| `log-partition-moment-geometry-v3.png` | `6d45a688c17829174b48ffae5308f7bb9b912e65aa7602d19904e2775e933789` |
| `structured-soft-margin-duality-v3.png` | `4433d2d26ce5a5709b3f7a151929cd2760230dd411b60331276d7ca6260bcbc2` |
