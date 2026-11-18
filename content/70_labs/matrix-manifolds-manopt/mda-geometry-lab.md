---
id: mda-geometry-lab
title: "Геометрическая лаборатория Manopt"
aliases: []
type: lab
status: canonical
publish: true
areas: [optimization, matrix-manifolds, multivariate-analysis]
concepts: [riemannian-optimization, matrix-manifolds, manifold-learning]
prerequisites: [linear-algebra, calculus]
ai_domains: [dimension-reduction, numerical-optimization]
source_refs:
  - id: source-mda-manopt-2021
    pages: "Главы 1–11, с. 1–402"
    role: primary
level: advanced
created: 2026-11-16
updated: 2026-11-18
---

# Геометрическая лаборатория Manopt

[Карта курса](30_mathematics/matrix-manifolds-manopt/mda-map) · [Все разделы и страницы](30_mathematics/matrix-manifolds-manopt/mda-source-map)

Сцены построены на небольших синтетических примерах. У репера в $\mathbb R^3$ видно оба столбца, у подпространства — плоскость и её нормаль, у симплекса — все три доли. Угол, расстояние и значение цели вычисляются из координат. В GIF ракурс и шкала сохраняются, а на заключительном кадре есть пауза для чтения.

> [!note] Как повторить опыт
> Полный сценарий и перечисленные файлы измерений находятся в авторском хранилище. На сайте доступны описание опыта и опубликованные иллюстрации. Самостоятельная проверка ниже запускается стандартным Python 3.

## Кэли и проба Армихо

Начнём с $Q_0=I_2$ и генератора $K=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)$.
Берём $Q(t)=(I+tK)(I-tK)^{-1}$ и цель $F(Q)=-Q_{21}$.
Производная $F(Q(t))$ в нуле равна $-2$. С коэффициентом Армихо $1/4$
проверяем $F(Q(t))\le -t/2$. При $t=2$ значение $-0{,}8$ не проходит проверку,
при $t=1$ значение $-1$ принимается. Дефект ортогональности обеих проб должен быть меньше $10^{-12}$.

```python
def cayley(t):
    denominator = 1.0 + t*t
    c, s = (1.0 - t*t)/denominator, 2*t/denominator
    return ((c, -s), (s, c))

results = []
for t, expected in ((2.0, False), (1.0, True)):
    q = cayley(t)
    gram = [[sum(q[k][i]*q[k][j] for k in range(2))
             for j in range(2)] for i in range(2)]
    defect = max(abs(gram[i][j] - (i == j)) for i in range(2) for j in range(2))
    loss = -q[1][0]
    accepted = loss <= -t/2
    assert defect < 1e-12 and accepted == expected
    results.append((t, loss, accepted))
print(results)
```

## Что проверить своими руками

1. **Геодезическая и нормировка.** Откройте §3.5.2 и проследите три конечные точки при $t=1$. Для единичного касательного вектора экспоненциальное отображение даёт угол $1$ рад, нормировка даёт $\arctan 1=\pi/4$, прямой шаг имеет квадрат нормы $2$. Замените $t$ на $0{,}1$ и оцените разность углов по формуле $t-\arctan t$.
2. **Поворот базиса и наклон пространства.** В §3.3.6 посмотрите на $QQ^\top$, пока оба столбца вращаются в плоскости. Затем начнётся наклон, и изменится сам проектор. Проверьте тождество $(QR)(QR)^\top=QQ^\top$ и сравните с изменением коэффициентов при покомпонентном штрафе.
3. **Скорость и допустимость шага.** В §3.5.3 сравните цель и невязку $Q^\top Q-I$. В расчёте с Кэли на одной и той же итерации можно решить линейную систему полного размера и систему размера $2p$. Размер $2p$ получается из числа столбцов в блочном разложении кососимметричной матрицы.
4. **Граница модели.** В §5.2.2 уберите первую индивидуальную дисперсию и проверьте наименьшее собственное значение полной ковариации. В §11.1.2 проследите исчезновение одного веса. Сфера квадратных корней из §11.2.3 описывает геометрию композиций с метрикой Фишера — Рао.

## Итерации и контрольные величины

| Сцена | Что показывают кадры | Цель в начале и в конце |
| --- | --- | --- |
| §3.5.1 | Поток и нормируемые шаги с поиском длины | -0.851387 → -2 |
| §3.5.3 | Шаги Кэли с условием Армихо | -2.989579 → -4.996606 |
| §4.8.1 | Спуск на сфере со сглаженным штрафом | 1.231545 → -1.06944 |
| §6.2.4 | Шаги Кэли для ортогонального совмещения | 2.854172 → 2.146493e-16 |
| §9.3.1 | Градиентные шаги по углу общего базиса | 25.41922 → 1.498525 |
| §10.3.2 | Градиентные шаги по конфигурации точек | 0.9363226 → 6.187889e-07 |
| §11.1.2 | Евклидова проекция весов на симплекс | 1.626489 → 0.1450824 |

Точки в этих сценах соответствуют принятым итерациям. В схеме потока синяя кривая построена по точному решению, а квадраты соответствуют отдельному дискретному запуску с общей начальной точкой. Пунктир между итерациями помогает читать траекторию. В опыте с преобразованием Кэли максимальный остаток $\lVert Q^\top Q-I\rVert_F$ равен 8.2e-16, расхождение двух вычислений шага составляет 2.2e-15. Вблизи стационарной точки различия порядка машинного округления входят в численный допуск.

В остальных GIF параметр меняется по заданному закону. Это позволяет проследить сближение столбцов, смену базиса, разницу углов, предельную ковариацию, корреляцию и приближение к границе симплекса.

## Иллюстрации по главам

| Место | Что видно | Вывод | Файлы |
| --- | --- | --- | --- |
| [1](30_mathematics/matrix-manifolds-manopt/chapters/mda-01-introduction) | Сфера и линия уровня | Минимум на окружности, SVD выбирает полюс. | [PNG](80_assets/matrix-manifolds-manopt/gpt-image-static-v2/mda-01-procrustes.png) |
| [2.5](30_mathematics/matrix-manifolds-manopt/chapters/mda-02-matrix-calculus#25-матричные-дифференциалы-и-градиенты) | График квадратичной функции и касательная плоскость | Линейная часть задаёт первый отклик, вертикальный зазор квадратичен. | [PNG](80_assets/matrix-manifolds-manopt/gpt-image-static-v2/mda-02-differential.png) |
| [3.1.6](30_mathematics/matrix-manifolds-manopt/chapters/mda-03-matrix-manifolds#316-прямоугольное-косоугольное-многообразие-obnp) | Две единичные стрелки и дуга между ними | Нормировка сохраняет длины, но допускает близость к вырождению. | [PNG](80_assets/matrix-manifolds-manopt/gpt-image-static-v2/mda-03-oblique.png) · [GIF](80_assets/matrix-manifolds-manopt/pca-geometry-v1/mda-03-oblique.gif) |
| [3.3.6](30_mathematics/matrix-manifolds-manopt/chapters/mda-03-matrix-manifolds#336-карты-и-факторизация-по-базисам-на-gnp) | Две стрелки, плоскость и нормаль на сфере | Внутренний поворот меняет репер, наклон меняет проектор. | [PNG](80_assets/matrix-manifolds-manopt/gpt-image-static-v2/mda-03-grassmann.png) · [GIF](80_assets/matrix-manifolds-manopt/pca-geometry-v1/mda-03-grassmann.gif) |
| [3.4.3](30_mathematics/matrix-manifolds-manopt/chapters/mda-03-matrix-manifolds#343-касательные-движения-репера-штифеля) | Ортонормированный репер, пробные точки и возвращённый репер | Касательное уравнение гарантирует допустимость в первом порядке. | [PNG](80_assets/matrix-manifolds-manopt/gpt-image-static-v2/mda-03-stiefel.png) |
| [3.5.1](30_mathematics/matrix-manifolds-manopt/chapters/mda-03-matrix-manifolds#351-динамические-системы) | Сфера с полем дисперсии и две траектории | Оба процесса уменьшают одну и ту же цель и остаются на сфере. | [PNG](80_assets/matrix-manifolds-manopt/gpt-image-static-v2/mda-03-flow.png) · [GIF](80_assets/matrix-manifolds-manopt/pca-geometry-v1/mda-03-flow.gif) |
| [3.5.2](30_mathematics/matrix-manifolds-manopt/chapters/mda-03-matrix-manifolds#352-метрика-геодезические-перенос-и-ретракции) | Объемный эллипсоид и соответствующая сфера | Линейная замена сохраняет длины в выбранной взвешенной метрике. | [PNG](80_assets/matrix-manifolds-manopt/gpt-image-static-v2/mda-03-ellipsoid.png) |
| [3.5.2](30_mathematics/matrix-manifolds-manopt/chapters/mda-03-matrix-manifolds#352-метрика-геодезические-перенос-и-ретракции) | Сфера, касательная плоскость, геодезическая и нормировка | Одинаковая начальная скорость допускает разные конечные точки. | [PNG](80_assets/matrix-manifolds-manopt/gpt-image-static-v2/mda-03-geodesic.png) · [GIF](80_assets/matrix-manifolds-manopt/pca-geometry-v1/mda-03-geodesic.gif) |
| [3.5.3](30_mathematics/matrix-manifolds-manopt/chapters/mda-03-matrix-manifolds#353-шаг-кэли-и-малое-линейное-решение) | Две траектории концов ортонормированного репера | Пересчитанный кососимметричный генератор обеспечивает допустимый шаг. | [PNG](80_assets/matrix-manifolds-manopt/gpt-image-static-v2/mda-03-cayley.png) · [GIF](80_assets/matrix-manifolds-manopt/pca-geometry-v1/mda-03-cayley.gif) |
| [4.2](30_mathematics/matrix-manifolds-manopt/chapters/mda-04-pca#42-определение-и-основные-свойства) | Плоскость проекций, ковариационный эллипс и репер | Поворот меняет дисперсии координат и их корреляцию, сохраняя общую дисперсию. | [PNG](80_assets/matrix-manifolds-manopt/gpt-image-static-v2/mda-04-pca-rotation.png) · [GIF](80_assets/matrix-manifolds-manopt/pca-geometry-v1/mda-04-pca-rotation.gif) |
| [4.8.1](30_mathematics/matrix-manifolds-manopt/chapters/mda-04-pca#481-ортонормированные-разреженные-нагрузки) | Ковариационное поле на сфере и вычисленные итерации | Штраф меняет направление с учётом цены ненулевых нагрузок. | [PNG](80_assets/matrix-manifolds-manopt/gpt-image-static-v2/mda-04-sparse-pca.png) · [GIF](80_assets/matrix-manifolds-manopt/pca-geometry-v1/mda-04-sparse-pca.gif) |
| [5.2.2](30_mathematics/matrix-manifolds-manopt/chapters/mda-05-factor-analysis#522-выборочная-модель) | Ковариационный эллипсоид и индивидуальные масштабы по осям | Одна индивидуальная дисперсия может обращаться в нуль при невырожденной ковариации. | [PNG](80_assets/matrix-manifolds-manopt/gpt-image-static-v2/mda-05-heywood.png) · [GIF](80_assets/matrix-manifolds-manopt/pca-geometry-v1/mda-05-heywood.gif) |
| [6.2.4](30_mathematics/matrix-manifolds-manopt/chapters/mda-06-procrustes#624-обычный-ортонормированный-анализ-прокруста) | Два облака в трех измерениях и остатки по соответствиям | Шаги Кэли уменьшают остаток, сохраняя ориентацию и расстояния внутри облака. | [PNG](80_assets/matrix-manifolds-manopt/gpt-image-static-v2/mda-06-procrustes.png) · [GIF](80_assets/matrix-manifolds-manopt/pca-geometry-v1/mda-06-procrustes.gif) |
| [7.2.1](30_mathematics/matrix-manifolds-manopt/chapters/mda-07-lda#721-стандартные-канонические-переменные) | Эллипсоид внутригрупповой нормы и направления | Отбеливание учитывает различия внутригрупповой дисперсии. | [PNG](80_assets/matrix-manifolds-manopt/gpt-image-static-v2/mda-07-lda.png) |
| [8.2](30_mathematics/matrix-manifolds-manopt/chapters/mda-08-cca#82-классическая-постановка-и-решение-cca) | Единичная сфера оценок и геометрия главного угла | Угол между одномерными пространствами оценок измеряет каноническую корреляцию. | [PNG](80_assets/matrix-manifolds-manopt/gpt-image-static-v2/mda-08-cca.png) · [GIF](80_assets/matrix-manifolds-manopt/pca-geometry-v1/mda-08-cca.gif) |
| [9.3.1](30_mathematics/matrix-manifolds-manopt/chapters/mda-09-cpc#931-градиенты-и-условия-оптимальности) | Два ковариационных эллипса и общий поворот осей | При несовместимых собственных осях итерации ищут компромисс по общей цели. | [PNG](80_assets/matrix-manifolds-manopt/gpt-image-static-v2/mda-09-cpc.png) · [GIF](80_assets/matrix-manifolds-manopt/pca-geometry-v1/mda-09-cpc.gif) |
| [10.3.2](30_mathematics/matrix-manifolds-manopt/chapters/mda-10-mds#1032-прямая-подгонка-расстояний) | Трёхмерное размещение и целевые длины рёбер | Градиент стресса перемещает точки с учётом ошибок истинных расстояний. | [PNG](80_assets/matrix-manifolds-manopt/gpt-image-static-v2/mda-10-mds-stress.png) · [GIF](80_assets/matrix-manifolds-manopt/pca-geometry-v1/mda-10-mds-stress.gif) |
| [10.8.5](30_mathematics/matrix-manifolds-manopt/chapters/mda-10-mds#1085-сингулярное-разложение-высшего-порядка) | Куб индексов тензора и три пересекающиеся координатные плоскости | Покомпонентно лучшие направления могут пересечься в нулевой ячейке. | [PNG](80_assets/matrix-manifolds-manopt/gpt-image-static-v2/mda-10-hosvd.png) |
| [11.1.2](30_mathematics/matrix-manifolds-manopt/chapters/mda-11-simplexes#1112-определение-задачи) | Треугольная выпуклая оболочка и движение смеси по ней | При проецируемом градиентном спуске с фиксированными архетипами один вес может стать нулём. | [PNG](80_assets/matrix-manifolds-manopt/gpt-image-static-v2/mda-11-archetypes.png) · [GIF](80_assets/matrix-manifolds-manopt/pca-geometry-v1/mda-11-archetypes.gif) |
| [11.2.3](30_mathematics/matrix-manifolds-manopt/chapters/mda-11-simplexes#1123-геометрия-симплекса-в-clr-координатах) | Положительный октант сферы и треугольник долей | До границы расстояние Фишера — Рао остаётся конечным, а расстояние Эйтчисона растёт без границы. | [PNG](80_assets/matrix-manifolds-manopt/gpt-image-static-v2/mda-11-simplex-metrics.png) · [GIF](80_assets/matrix-manifolds-manopt/pca-geometry-v1/mda-11-simplex-metrics.gif) |

## Воспроизведение

Нужны Python 3.10 или новее, NumPy, SciPy, Matplotlib и Pillow. Из корня авторского хранилища запустите:

```powershell
python -X utf8 -B 70_labs/figures/matrix-manifolds-manopt/render_manopt.py --jobs 3
```

Сценарий сохраняет кадры 720 × 1280, контрольные числа, длительности и контрольные суммы файлов. Чтобы проверить один сюжет в отдельной папке, передайте параметры `--scene mda-03-geodesic`, `--out` и `--ledger`. Примеры на MATLAB в главах снабжены пояснениями к интерфейсу Manopt. Вычислительные проверки лаборатории выполнены на Python.
