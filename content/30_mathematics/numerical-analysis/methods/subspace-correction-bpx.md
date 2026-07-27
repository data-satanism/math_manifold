---
id: subspace-correction-bpx-method
title: "Параллельные коррекции на подпространствах и предобусловливатель BPX"
aliases: ["Метод коррекций на подпространствах", "BPX"]
type: method
status: canonical
publish: true
areas: [numerical-analysis, numerical-linear-algebra]
concepts: [subspace-correction, additive-preconditioner, bpx, domain-decomposition]
prerequisites: [nla-24-multigrid-subspace-corrections]
ai_domains: [distributed-optimization, multiscale-learning]
source_refs:
  - id: tyrtyshnikov-numerical-analysis
    pages: "249-250"
    role: primary
level: research
created: 2026-07-15
updated: 2026-07-27
---

# Параллельные коррекции на подпространствах и предобусловливатель BPX

## Схема

Для подпространств $V_i$ и локальных приближённых обратных $R_i$ строится

$$
B=\sum_{i=1}^m R_iQ_i.
$$

Каждая локальная поправка вычисляется независимо, после чего поправки суммируются. Для вложенных пространств и сглаживателей возникает предобусловливатель BPX.

## Практическая проверка

1. Убедиться, что подпространства покрывают все направления.
2. Контролировать устойчивость разложения энергии.
3. Ограничить перекрытие и взаимодействие локальных поправок.
4. Сравнить число итераций вместе с коммуникационной стоимостью.

## Режимы отказа

Непокрытое направление создаёт ядро; чрезмерное перекрытие многократно исправляет одну компоненту; неточный локальный решатель может нарушить положительную определённость.

## Визуализация

![Дополняющие масштабы образуют устойчивую сумму локальных коррекций](80_assets/numerical-analysis/gpt-image-v5/nla-ch23-multigrid-insight.png)

## Источник

[[60_sources/tyrtyshnikov-numerical-analysis|Тыртышников]], §23.11, стр. 249–250.

