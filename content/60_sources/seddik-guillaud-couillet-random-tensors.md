---
id: source-seddik-guillaud-couillet-2022-random-tensors
title: "M. E. A. Seddik, M. Guillaud, R. Couillet — When Random Tensors Meet Random Matrices"
aliases: ["Seddik–Guillaud–Couillet 2022", "When random tensors meet random matrices"]
type: source
status: canonical
publish: true
areas: [random-matrix-theory, tensor-methods]
concepts: [spiked-tensor-model, tensor-contraction, eigenvector-alignment]
prerequisites: [probability, linear-algebra, tensor-algebra]
ai_domains: [tensor-learning, signal-recovery, dimensionality-reduction]
source_refs:
  - id: seddik2022randomtensors
    pages: "1-45 PDF pages"
    role: primary
level: advanced
created: 2026-07-13
updated: 2026-07-27
---

# When Random Tensors Meet Random Matrices

- Авторы: Mohamed El Amine Seddik, Maxime Guillaud, Romain Couillet.
- Версия: arXiv:2112.12348v3, 19 ноября 2022 года; рукопись направлена в *The Annals of Applied Probability*.
- Контрольная сумма SHA-256: `A3BD077528F2BB6D3E9AB4D01088CEFE9A24BAFC171F04CE14C1BF5CECD748EF`.
- Приватная копия: `_private/sources/rmt/additional/random-tensors.pdf`; в публичный экспорт не входит.

## Что именно установлено

Для асимметричной спайковой модели тензора порядка $d$ с гауссовским шумом задача наилучшего приближения ранга один связывается с симметричной блочной случайной матрицей, построенной из тензорных свёрток. В определённом авторами режиме роста размерностей получены почти наверное предельное сингулярное значение и согласованность оцениваемых направлений с истинным спайком.

## Карта страниц

- стр. 2–6 PDF: модель, пороги и точный статус утверждений;
- стр. 6–8: резольвента, преобразование Штильтьеса и гауссовские формулы;
- стр. 9–19: модель порядка три, предельная спектральная мера и согласованность;
- стр. 20–25: произвольный порядок и несколько ортогональных компонент;
- стр. 28–44: доказательства.

## Граница результата

Порог, при котором формулы согласованности становятся определены, не всегда совпадает с информационным или алгоритмическим порогом восстановления. В статье это различие явно обсуждается; его нельзя скрывать одним словом «фазовый переход».

