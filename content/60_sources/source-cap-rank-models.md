---
id: "source-cap-rank-models"
title: "Источники по жёсткости, знаку и неотрицательному рангу"
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

# Три условия на представление

Материалы относятся к первым темам ветки [[cap-rank-spectrum-map]]. Официальная программа определяет предмет, а определения и результаты сверены с математическими первоисточниками. Иллюстративные примеры вычислены отдельно.

## Жёсткость матриц

L. G. Valiant, *Graph-theoretic arguments in low-level complexity*, MFCS, 1977, с. 162–176. Историческая ссылка о связи жёсткости со сложностью линейных вычислений. Оригинальная работа используется для библиографии. Доказательство связи с глубиной схем в маршрут не входит. [Библиографическая запись](https://dblp.org/rec/conf/mfcs/Valiant77.html).

A. Kumar, S. V. Lokam, V. M. Patankar, J. Sarma, *Using Elimination Theory to Construct Rigid Matrices*, версия arXiv:0910.5301v3. В §§1–2 проверены постановка через число изменённых элементов, роль поля и размерностная оценка через алгебраические множества. В [[cap-r01-rigidity]] дана своя вещественная версия доказательства почти всюду через параметризацию блоком Шура и оценку меры. Статья содержит более сильные конструкции, которые здесь не воспроизводятся. [Полный текст](https://arxiv.org/pdf/0910.5301v3).

## Знак-ранг

H. Hatami, P. Hatami, W. Pires, R. Tao, R. Zhao, *Lower Bound Methods for Sign-Rank and Their Limitations*, APPROX/RANDOM 2022, статья 22, §1, с. 22:2–22:3. Сверены строгое определение, билинейная реализация и нижняя граница через VC-размерность. В [[cap-r02-sign-rank]] дано доказательство для транспонированной ориентации таблицы, в которой точки индексируются строками. Пороговая таблица и вычисления размера 8 подготовлены для атласа. [Статья и PDF](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.APPROX/RANDOM.2022.22).

## Неотрицательная факторизация

J. E. Cohen, U. G. Rothblum, *Nonnegative Ranks, Decompositions, and Factorizations of Nonnegative Matrices*, Linear Algebra and its Applications 190, 1993, с. 149–168. В §§2–4 прочитаны определение, основные оценки, вероятностная нормировка и случай ранга не выше двух. Для [[cap-r04-nonnegative-rank]] построено доказательство на носителе конкретной матрицы и его геометрическая интерпретация через сечение симплекса. Вычисление обычного ранга и сертификат четырёх неотрицательных компонент проверены раздельно. [Авторский экземпляр](https://lab.rockefeller.edu/cohenje/PDFs/211CohenRothblumLAA1993.pdf).

[[cap-rank-model-ai-bridge|Прикладная страница]] показывает, как различаются критерии при работе с весами, таблицами решений и вероятностными смесями.
