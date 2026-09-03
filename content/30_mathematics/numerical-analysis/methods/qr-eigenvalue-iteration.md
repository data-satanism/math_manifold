---
id: qr-eigenvalue-iteration
title: "QR-итерация для собственных значений"
aliases: ["QR eigenvalue iteration"]
type: method
status: canonical
publish: true
areas: [numerical-analysis, numerical-linear-algebra]
concepts: [qr-algorithm, similarity-transform, deflation, schur-form]
prerequisites: [qr-factorization-theorem, power-and-subspace-iteration]
ai_domains: [spectral-diagnostics, covariance-analysis]
source_refs:
  - id: tyrtyshnikov-numerical-analysis
    pages: "93-101"
    role: primary
level: advanced
created: 2026-07-14
updated: 2026-07-27
---

# QR-итерация для собственных значений

## Базовый шаг

$$
A_{k-1}=Q_kR_k,
\qquad
A_k=R_kQ_k=Q_k^*A_{k-1}Q_k.
$$

Подобие сохраняет спектр, а накопленные $Q_k$ реализуют итерацию полного флага подпространств.

## Практический протокол

1. Уравновесить матрицу, если масштабы строк и столбцов резко различаются.
2. Привести её к хессенберговой форме.
3. Выполнять QR-шаги со сдвигами.
4. Проверять малость поддиагональных элементов относительно соседних диагоналей.
5. Дефлировать отделившиеся блоки.
6. Накопить преобразования, если нужны векторы Шура или собственные векторы.

## Критерии качества

- невязка $\|AV-VT\|$ для формы Шура $A\approx VTV^*$;
- ортогональность $\|I-V^*V\|$;
- обратная ошибка исходной матрицы;
- устойчивость найденного порядка спектра к малым возмущениям.

## Стоимость

Редукция к хессенберговой форме стоит $O(n^3)$, один последующий шаг — $O(n^2)$. Без редукции каждый шаг снова стоил бы $O(n^3)$.

## Режимы отказа

Несдвинутая схема может сходиться медленно или циклически; абсолютный критерий дефляции искажает малые или большие масштабы; собственные векторы ненормальной матрицы могут оставаться плохо обусловленными.

## Визуализация

![QR-итерация сохраняет спектр и постепенно отделяет поддиагональные блоки](80_assets/numerical-analysis/gpt-image-v2/nla-module-11-qr-eigenvalue-insight.webp)

## Источник

[[60_sources/tyrtyshnikov-numerical-analysis|Тыртышников]], §§10.1–10.8, стр. 93–101.
