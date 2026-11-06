---
id: "source-cap-spectral-stability"
title: "Источники по спектральной локализации, нормам и возмущениям"
aliases: []
type: "source"
status: "canonical"
publish: true
areas: ["numerical-linear-algebra"]
concepts: []
prerequisites: []
ai_domains: ["compression"]
source_refs: []
level: "advanced"
created: "2026-11-06"
updated: "2026-11-06"
---

# Три вида спектральных гарантий

## Локализация и возмущение спектра

L. N. Trefethen, *Pseudospectra of Linear Operators*, SIAM Review 39(3), 1997, с. 383–406. В §2 сверены определения через возмущение, невязку и резольвенту. В [[cap-r07-spectral-localization]] приведено прямое доказательство конечномерной формулы через минимальное сингулярное число и собственный пример с жордановым блоком. Выпуклость поля значений показана через двумерное сжатие и сферу Блоха. [Авторский PDF](https://people.maths.ox.ac.uk/trefethen/publication/PDF/1997_72.pdf).

## Инвариантные нормы и Лидский

L. Mirsky, *Symmetric Gauge Functions and Unitarily Invariant Norms*, Quarterly Journal of Mathematics 11(1), 1960, с. 50–59. Официальная библиографическая карточка задаёт исходную тему и атрибуцию. В [[cap-r08-unitarily-invariant-norms]] доказательство характеристики и теоремы об усечении проведено через двойственность, слабое мажорирование и вариационную формулу. [Издатель](https://academic.oup.com/qjmath/article/11/1/50/1525786).

В. Б. Лидский, *О характеристических числах суммы и произведения симметрических матриц*, Доклады АН СССР 75, 1950, с. 769–772. Для библиографии использована карточка перевода. Форму неравенства для изменений упорядоченного спектра дополнительно сверили по теореме 4 в работе H. Sendov, *A Note on Lidskii’s Theorem for the Directional Derivatives of the Eigenvalues of Symmetric Matrices*, Electronic Journal of Linear Algebra 41, 2025, с. 338–341. На с. 339 сверена формула мажорирования разности. В атласе приведено самостоятельное доказательство для эрмитовых матриц через производные в простом спектре и предельный переход. [Карточка NIST](https://www.nist.gov/publications/proper-values-sum-and-product-symmetric-matrices), [Sendov, теорема 4](https://journals.uwyo.edu/index.php/ela/article/download/9483/7033).

## Подпространства

C. Davis, W. M. Kahan, *The Rotation of Eigenvectors by a Perturbation. III*, SIAM Journal on Numerical Analysis 7(1), 1970, с. 1–46. P.-Å. Wedin, *Perturbation Bounds in Connection with Singular Value Decomposition*, BIT 12, 1972, с. 99–111. Для этих двух работ сверены издательские сведения и постановки. В [[cap-r09-subspace-perturbation]] выведены нужные здесь формы оценок из уравнения невязки и эрмитова удвоения. Операторная оценка с константой один относится к упорядоченным группам с односторонним зазором. Общие теоремы оригинальных статей не воспроизводятся целиком. [Davis–Kahan](https://doi.org/10.1137/0707001), [Wedin](https://link.springer.com/article/10.1007/BF01932678).

Собственные численные примеры и нормы указаны в [[cap-rank-spectrum-lab]]. Они проверяют приведённые формулы на фиксированных данных.
