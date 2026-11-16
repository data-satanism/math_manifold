---
id: pom-geometry-lab
title: "Геометрическая лаборатория популяционного поиска"
aliases: []
type: lab
status: canonical
publish: true
areas: [optimization, riemannian-geometry, information-geometry]
concepts: [population-search, exponential-map, mixture-distributions, rsdfo]
prerequisites: [linear-algebra, calculus, probability]
ai_domains: [numerical-optimization]
source_refs:
  - id: source-fong-tino-population-optimization
    pages: "Главы 1–10, с. 1–165"
    role: primary
level: advanced
created: 2026-11-16
updated: 2026-11-16
---

# Геометрическая лаборатория популяционного поиска


[Карта курса](30_mathematics/population-optimization-manifolds/pom-map) · [Указатель разделов](30_mathematics/population-optimization-manifolds/pom-source-map)

Координаты, траектории и подписи к ним рассчитаны из формул или из хода алгоритма. Ракурс и масштаб внутри сцены фиксированы. На последнем кадре GIF есть пауза, чтобы сравнить значения и положение объектов.

## Опыты по шагам

1. **Проверить перенос в главе 2.** Проследите жёлтую стрелку по трём дугам. Вектора остаются касательными и единичными. В начале стрелка совпадает с $e_1$, после полного обхода направлена вдоль $e_2$. Для проверки измените ориентацию обхода и перенесите новый вектор тем же способом.
2. **Проверить массу в главе 5.** Жёлтая ячейка отдаляется от нуля касательной плоскости. Вычислите $\sin r/r$ в её середине и затем разделите исходную плотность на этот множитель. Для диска радиуса $\pi/2$ интеграл исправленной плотности равен 1. Без множителя обратного якобиана получится $8/\pi^2$.
3. **Проследить одно поколение Extended RSDFO.** Сначала откройте локальный шаг с 18 пробами, затем смену поколений на сфере. Во втором опыте положительная цель равна $2+0{,}35x_3+0{,}85x_3^2$, оставляют три компоненты, а доля обследования равна 0,36. Сравните рекорд по измеренным точкам и среднее смеси. Для среднего по равномерной шапке положите $c=\cos r$. Тогда случайная величина $u=x^\top q$ для центра $q$ равномерна на $[c,1]$, её первые два момента равны $(1+c)/2$ и $(1+c+c^2)/3$. Эти моменты дают оценку компоненты аналитически. Число измерений включает локальные пробы и оценку центров. Раскраска сферы вычислена для рисунка и в бюджет поиска не входит.
4. **Проверить роль весов в главе 8.** На поверхности $F(a,b)$ сравните $(10,1)$ и $(10,2)$. Затем откройте тетраэдр. На первой фазе вычисленные шаги повышают $H_\epsilon$, пока линейная цель $J$ уменьшается. После удаления компоненты нормировка меняет грань. Возрастание $H_\epsilon$ проверяется на каждом шаге внутри фиксированной грани.
5. **Сравнить локальные и глобальные масштабы в главе 9.** В опыте с двумя главными углами на каждом шаге испытываются четыре пары. Шаг уменьшается, если ни одна проба не улучшила значение. След остаётся на внешнем кольце, хотя значение на внутреннем меньше. Для лестницы Иакова показаны три соседние области и их склейки. Положение труб на схеме не задаёт расстояния или глобальные минимумы из опыта книги.

## Численные проверки

| Опыт | Проверяемая величина | Результат |
| --- | --- | --- |
| Ковариация | Погрешность двух перенесённых собственных значений | 2.2e-16 |
| Локальный шаг | Цель в начале и в новом центре | 2,3026 → 2,5581 |
| Популяция | Лучшее измерение при 591 вызовах цели | 2,4349 → 3,1843 |
| Симплекс | Значение $H_\epsilon$ на полном тетраэдре | -13,4312 → -12,5165 |
| Грассман | Локальная оценка и минимум радиальной цели | -1,2532 и -2,8739 |


## Иллюстрации

| Раздел | Что проверить на рисунке | Сцена | Файлы |
| --- | --- | --- | --- |
| [1.2](30_mathematics/population-optimization-manifolds/chapters/pom-01-introduction#12-постановка-чёрного-ящика-и-стохастическое-ослабление) | Широкое усреднение по дуге разворачивает порядок двух центров. | Вертикальный рельеф над окружностью с двумя дугами | [PNG](80_assets/population-optimization-manifolds/pca-geometry-v1/pom-01-objective-mean.png) |
| [2.2.3](30_mathematics/population-optimization-manifolds/chapters/pom-02-riemannian-geometry#223-параллельный-перенос-вдоль-заданной-кривой) | После обхода длина стрелки сохраняется, направление поворачивается на 90°. | Сферический треугольник и касательная стрелка | [PNG](80_assets/population-optimization-manifolds/pca-geometry-v1/pom-02-holonomy.png) · [GIF](80_assets/population-optimization-manifolds/pca-geometry-v1/pom-02-holonomy.gif) |
| [2.3](30_mathematics/population-optimization-manifolds/chapters/pom-02-riemannian-geometry#23-экспоненциальное-отображение-и-область-его-обратимости) | На предельном радиусе разные начальные векторы попадают в один антипод. | Граница сферической нормальной карты и две меридиональные дуги | [PNG](80_assets/population-optimization-manifolds/pca-geometry-v1/pom-02-normal-chart.png) |
| [3.3](30_mathematics/population-optimization-manifolds/chapters/pom-03-information-geometry#33-кривизна-и-двойственная-плоскостность) | Смесь вероятностей и экспоненциальная интерполяция дают разные пути при тех же концах. | Две информационно-геометрические кривые на октанте сферы | [PNG](80_assets/population-optimization-manifolds/pca-geometry-v1/pom-03-dual-paths.png) · [GIF](80_assets/population-optimization-manifolds/pca-geometry-v1/pom-03-dual-paths.gif) |
| [4.1.2](30_mathematics/population-optimization-manifolds/chapters/pom-04-probability-densities#412-объём-и-функция-плотности) | Одинаковые приращения углов дают разные площади. | Сфера с двумя равными по координатам ячейками | [PNG](80_assets/population-optimization-manifolds/pca-geometry-v1/pom-04-area.png) |
| [5.2.2](30_mathematics/population-optimization-manifolds/chapters/pom-05-inherited-densities#522-перенос-римановой-экспонентой-как-частный-случай) | У удалённой площадки якобиан меньше, поэтому плотность относительно площади растёт. | Касательный диск и две искривлённые площадки на сфере | [PNG](80_assets/population-optimization-manifolds/pca-geometry-v1/pom-05-pushforward.png) · [GIF](80_assets/population-optimization-manifolds/pca-geometry-v1/pom-05-pushforward.gif) |
| [6.3.2](30_mathematics/population-optimization-manifolds/chapters/pom-06-mixture-densities#632-двойственная-структура-без-кручения-в-семействе-смесей) | В перекрытии при равных плотностях сама координата не раскрывает метку компоненты. | Две пересекающиеся сферические шапки с различимыми областями | [PNG](80_assets/population-optimization-manifolds/pca-geometry-v1/pom-06-overlap.png) |
| [7.2.2](30_mathematics/population-optimization-manifolds/chapters/pom-07-geometry-in-optimization#722-риманов-метод-роя-частиц) | Личный и общий рекорды задают скорости в одном касательном пространстве на каждом шаге. | Сфера с траекториями частиц, общим рекордом и перенесённой скоростью | [PNG](80_assets/population-optimization-manifolds/pca-geometry-v1/pom-07-rpso.png) · [GIF](80_assets/population-optimization-manifolds/pca-geometry-v1/pom-07-rpso.gif) |
| [7.2.3](30_mathematics/population-optimization-manifolds/chapters/pom-07-geometry-in-optimization#723-риманова-cma-es) | Ковариация переносится изометрией; направление осей меняется, спектр сохраняется. | Два касательных эллипса и образ одного на сфере | [PNG](80_assets/population-optimization-manifolds/pca-geometry-v1/pom-07-covariance.png) · [GIF](80_assets/population-optimization-manifolds/pca-geometry-v1/pom-07-covariance.gif) |
| [8.1](30_mathematics/population-optimization-manifolds/chapters/pom-08-rsdfo#81-локальная-риманова-схема-rsdfo) | Лучшие пробы дают средний касательный вектор, из которого строится новый центр. | Сферическая область поиска, пробные точки и геодезический шаг центра | [PNG](80_assets/population-optimization-manifolds/pca-geometry-v1/pom-08-local.png) · [GIF](80_assets/population-optimization-manifolds/pca-geometry-v1/pom-08-local.gif) |
| [8.2.4](30_mathematics/population-optimization-manifolds/chapters/pom-08-rsdfo#824-расширение-списка-отбор-и-пересчёт-весов) | Сохранение компонент по точному среднему и обследование фронта меняют размещение новых запусков. | Сферический ландшафт, популяция шапок и старты с границы | [PNG](80_assets/population-optimization-manifolds/pca-geometry-v1/pom-08-population.png) · [GIF](80_assets/population-optimization-manifolds/pca-geometry-v1/pom-08-population.gif) |
| [8.2.5](30_mathematics/population-optimization-manifolds/chapters/pom-08-rsdfo#825-что-действительно-монотонно-при-отборе) | Повышение меньшей оценки при пропорциональных весах увеличивает её долю и может снизить среднее. | Трёхмерный график взвешенного среднего двух оценок | [PNG](80_assets/population-optimization-manifolds/pca-geometry-v1/pom-08-monotonicity.png) |
| [8.2.6](30_mathematics/population-optimization-manifolds/chapters/pom-08-rsdfo#826-обследование-границы-накопленной-области) | Внутренняя дуга круга отбрасывается, внешняя становится местом обследующего старта. | Три сферические шапки, их фронт и точки отбрасывания | [PNG](80_assets/population-optimization-manifolds/pca-geometry-v1/pom-08-frontier.png) · [GIF](80_assets/population-optimization-manifolds/pca-geometry-v1/pom-08-frontier.gif) |
| [8.3.2](30_mathematics/population-optimization-manifolds/chapters/pom-08-rsdfo#832-неподвижная-точка-проецируемого-шага) | Внутри фазы растёт логарифмическая цель H, значение линейного среднего J может снизиться. | Тетраэдр весов с переходом между гранями и вычисленными итерациями | [PNG](80_assets/population-optimization-manifolds/pca-geometry-v1/pom-08-simplex.png) · [GIF](80_assets/population-optimization-manifolds/pca-geometry-v1/pom-08-simplex.gif) |
| [9.4](30_mathematics/population-optimization-manifolds/chapters/pom-09-experiments#94-многообразия-грассмана) | Локальный поиск может остановиться на другом кольце, хотя функция на подпространствах имеет известный глобальный минимум. | Поверхность цели над двумя главными углами и локальные пробы | [PNG](80_assets/population-optimization-manifolds/pca-geometry-v1/pom-09-grassmann.png) · [GIF](80_assets/population-optimization-manifolds/pca-geometry-v1/pom-09-grassmann.gif) |
| [9.5](30_mathematics/population-optimization-manifolds/chapters/pom-09-experiments#95-лестница-иакова) | Переход между соседними областями имеет дискретный индекс; поиск внутри области использует два угла. | Три тора с отверстиями и трубчатыми соединениями | [PNG](80_assets/population-optimization-manifolds/pca-geometry-v1/pom-09-ladder.png) |
| [10.2](30_mathematics/population-optimization-manifolds/chapters/pom-10-conclusion#102-четыре-направления-дальнейшей-работы) | Среднее квадратичных расстояний минимально на всей окружности. | Сфера с массами в полюсах, дугами расстояния и экватором минимумов | [PNG](80_assets/population-optimization-manifolds/pca-geometry-v1/pom-10-frechet.png) |


## Воспроизведение

Нужны Python 3.10 или новее, NumPy, SciPy, Matplotlib и Pillow. Из корня авторского хранилища выполните команду

```powershell
python -X utf8 -B 70_labs/figures/population-optimization-manifolds/render_population.py --jobs 3
```

Параметр `--check` отдельно проверяет геометрические и численные утверждения. Для повторного построения выбранной сцены используйте `--scene` с её именем, а `--out` и `--ledger` задают отдельную папку и файл проверки. Сценарий использует тот же способ компоновки и ту же палитру, что лаборатория курса Manopt. Все выборки имеют фиксированные начальные значения генераторов. Эксперименты главы 9 разобраны по опубликованным данным. Графики лаборатории получены на отдельных малых задачах.
