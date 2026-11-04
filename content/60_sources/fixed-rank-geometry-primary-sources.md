---
id: source-fixed-rank-geometry
title: 'Источники: геометрия фиксированного ранга, факторпространства и LoRA'
aliases: []
type: source
status: canonical
publish: true
areas:
- numerical-linear-algebra
- differential-geometry
concepts:
- fixed-rank-manifold
- gauge-invariance
- riemannian-optimization
prerequisites: []
ai_domains:
- parameter-efficient-fine-tuning
- compression
source_refs:
- id: source-fixed-rank-geometry
  pages: Точные границы чтения и привязки указаны в тексте
  role: primary
level: advanced
created: '2026-11-03'
updated: '2026-11-03'
---

# Источники геометрической главы

Карточка относится к [[30_mathematics/computational-algebra-principles/modules/cap-g01-fixed-rank-geometry|модулю Г01]], [[30_mathematics/computational-algebra-principles/theorems/cap-fixed-rank-tangent|теореме проектора]], [[30_mathematics/computational-algebra-principles/concepts/cap-factor-gauge|факторной симметрии]] и [[50_bridges/cap-lora-gauge|переносу в LoRA]].

## 1. Вложенное многообразие матриц

Bart Vandereycken. **Low-Rank Matrix Completion by Riemannian Optimization.** SIAM Journal on Optimization, 23(2), 2013, 1214–1236. DOI [10.1137/110845768](https://doi.org/10.1137/110845768).

[Авторская PDF-копия опубликованной статьи](https://www.unige.ch/math/vandereycken/papers/published_Vandereycken_2013.pdf), [препринт](https://arxiv.org/abs/1209.3834).

Основной агент прочитал §2.1–2.2 и сопутствующие фрагменты §3, просмотрел изображения журнальных страниц 1218–1219. Независимый редактор также сверил нужные утверждения по PDF препринта. Используются Proposition 2.1, метрика (2.4), проектор (2.5), градиент (2.6), локальная SVD-ретракция (2.7)–(2.8). Полное чтение 23 страниц статьи не заявляется; её теорема сходимости с дополнительными условиями не переносится в учебный модуль.

На журнальной с. 1219 рядом с (2.8) напечатано условие неоднозначности через два значения внутри сохраняемого блока. В учебном тексте используется правильный разрыв $\sigma_r(Y)>\sigma_{r+1}(Y)$ на границе усечения. Это подтверждено самостоятельным примером $Y=I_2,r=1$ и стандартной характеристикой наилучшего рангового приближения. Кратность внутри сохраняемого блока не делает усечённую матрицу неоднозначной.

## 2. Факторпространства и метрики

Bamdev Mishra, Gilles Meyer, Silvère Bonnabel, Rodolphe Sepulchre. **Fixed-rank matrix factorizations and Riemannian low-rank optimization.** [arXiv:1209.0430](https://arxiv.org/abs/1209.0430).

Независимый редактор прочитал необходимые фрагменты о GL(r)-симметрии, вертикальном пространстве и инвариантной метрике; в его проверенной версии это PDF-с. 5 и 9. Основной модуль использует это как указатель и проверяет нужную алгебру самостоятельно: эквивалентность полных факторов, ядро производной, положительность и инвариантность приведённой формы. Полное чтение и реализация алгоритмов статьи не заявляются. Метрика на факторпространстве не отождествляется с индуцированной метрикой Фробениуса матриц.

## 3. Прикладная мотивация: Riemannion

Vladimir Bogachev, Vladimir Aletov, Alexander Molozhavenko, Denis Bobkov, Vera Soboleva, Aibek Alanov, Maxim Rakhuba. **LoRA meets Riemannion: Muon Optimizer for Parametrization-independent Low-Rank Adapters.** [arXiv:2507.12142v2](https://arxiv.org/abs/2507.12142v2), 1 октября 2025 года; [полный HTML](https://arxiv.org/html/2507.12142v2). Первичная версия подана 16 июля 2025 года.

Проверены §§3–6: фиксированный ранг, матричная постановка, инициализация ненулевого адаптера с компенсацией в замороженных весах и получение градиентных произведений. Уровень чтения остальных разделов и опубликованная версия учитываются отдельно в [[60_sources/hse-low-rank-publications|реестре новой подборки]]. Данные авторов об обучении не выдаются за наши опыты.

## Что доказано составителем

Блочная карта ранга через дополнение Шура; описание ядра факторного дифференциала; проектор через ортогональные блоки; скалярный контрпример факторному шагу; проверка первого порядка ретракции через точную кривую; сингулярный симметричный срез. Используются стандартные результаты SVD-аппроксимации, оценка возмущения сингулярных чисел и гладкость спектрального проектора отделённого кластера. Последняя не выводится здесь заново из комплексного интеграла резольвенты.

Карточка источников и все связанные новые страницы остаются в review без разрешения публикации.
