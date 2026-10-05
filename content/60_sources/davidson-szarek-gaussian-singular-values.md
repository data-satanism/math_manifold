---
id: source-davidson-szarek-gaussian-singular-values
title: "Дэвидсон—Шарек: сингулярные числа гауссовых матриц"
aliases: ["Davidson–Szarek Gaussian singular values"]
type: source
status: canonical
publish: true
areas: [random-matrix-theory, high-dimensional-statistics]
concepts: [singular-values, gaussian-concentration]
prerequisites: []
ai_domains: [covariance-estimation, pca]
source_refs:
  - id: davidson-szarek-gaussian-2001
    pages: "авторский PDF 42–43, теорема II.13; исправление 2003, PDF 1, п. 5"
    role: primary
level: research
created: 2026-10-02
updated: 2026-10-02
---

# Дэвидсон—Шарек: сингулярные числа гауссовых матриц

Kenneth R. Davidson, Stanislaw J. Szarek. *Local Operator Theory, Random Matrices and Banach Spaces*. В: Handbook on the Geometry of Banach Spaces, vol. 1, W. B. Johnson, J. Lindenstrauss (ред.), Elsevier Science, 2001, с. 317–366. Дополнение и исправления: vol. 2 (2003), с. 1819–1820.

Проверяемая версия — [авторский препринт Case Western Reserve](https://case.edu/artsci/math/szarek/TeX/DavSzaHB.pdf), 59 PDF-страниц. SHA-256: `63607ED39B3D556219C86073F5D56428D574B10703387347C0310794EA396048`. Заглавие и страницы теоремы сверены визуально.

## Точная опора

Теорема II.13, формула (12), находится на PDF 42, продолжение доказательства — PDF 43. В препринте собственная пагинация совпадает с PDF; эти номера нельзя смешивать со страницами издания 317–366.

Для прямоугольной матрицы с независимыми элементами нормального распределения источник даёт отдельные экспоненциальные оценки верхнего и нижнего сингулярных чисел. Нормировка элементов в источнике зависит от числа строк; при переносе к выборочной ковариации нормировку необходимо пересчитать явно.

В [официальном дополнении](https://case.edu/artsci/math/szarek/TeX/AddendumDavSza.pdf), PDF 1, пункт 5, исправлен аргумент нормальной функции распределения в опубликованной теореме 2.13: пропущен множитель квадратного корня из числа строк. Экспоненциальная оценка в публикации оставалась верной. В атласе используется эта проверенная экспоненциальная форма.

Иная авторская версия из Waterloo содержит 58 страниц и другое заглавие. Она не подменяет зарегистрированную здесь версию; контрольные суммы и координаты обеих версий сохранены в административном отчёте проверки источников.

Приватная проверенная копия: закрытом архиве. Она не включается в публичный экспорт.
