---
id: source-oseledets-tensor-train
title: "Oseledets: разложение тензорного поезда"
aliases: ["Tensor-Train Decomposition", "Oseledets 2011", "Первичный источник TT"]
type: source
status: canonical
publish: true
areas: [tensor-methods, numerical-linear-algebra, source-mapping]
concepts: [tensor-train, unfolding-rank, source-verification]
prerequisites: []
ai_domains: [model-compression, scientific-machine-learning]
source_refs:
  - id: oseledets-tensor-train-2011
    pages: "Журнальные с. 2295–2317; PDF 1–23"
    role: primary
level: research
created: 2026-10-01
updated: 2026-10-02
---

# Oseledets: разложение тензорного поезда

## Библиографический паспорт

I. V. Oseledets. **Tensor-Train Decomposition**. SIAM Journal on Scientific Computing, 33(5), 2011, с. 2295–2317. [DOI 10.1137/090752286](https://doi.org/10.1137/090752286).

[Страница автора о публикации](https://oseledets.github.io/news/tensor-train-decomposition-paper-finally-published/) указывает журнальную версию. Для проверки доступна [полная журнальная копия в университетском архиве](https://users.math.msu.edu/users/iwenmark/Teaching/CMSE890/TENSOR_oseledets2011.pdf), 23 страницы. В этой копии печатная страница равна номеру PDF-страницы плюс 2294. Исходные страницы и рисунки статьи не включаются в учебный экспорт.

## Точная привязка

| Результат | Печатные страницы | PDF-страницы |
| --- | --- | --- |
| Формат TT, размеры ядер и граничные ранги | 2296–2297, формулы (1.2)–(1.3) | 2–3 |
| Развёртки на последовательных разрезах | 2297–2298, формула (2.1) | 3–4 |
| Достижимость рангов развёрток | 2298–2299, теорема 2.1 | 4–5 |
| Оценка ошибки TT-SVD | 2299–2300, теорема 2.2 | 5–6 |
| Существование лучшего TT-приближения и квазиоптимальность | 2300, следствие 2.4 | 6 |
| Алгоритм TT-SVD с заданным допуском | 2301, алгоритм 1 | 7 |

## Роль в атласе

Первичный источник для [[30_mathematics/tensor-methods/modules/ten-04-tensor-networks|модуля о TT]]. Он заменяет ошибочную привязку TT-результата к статье Kolda–Bader. Определение цепочки и утверждение о точных рангах не распространяются автоматически на все тензорные сети.

Оценка ошибки и квазиоптимальность перечислены для дальнейшего углубления; наличие этой карточки не означает, что их доказательства уже изложены в курсе.
