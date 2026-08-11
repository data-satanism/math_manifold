---
id: lab-needham-release-1a-widgets
title: "Интерактивы Нидхема: релиз 1A"
aliases: ["Needham release 1A interactives"]
type: lab
status: canonical
publish: true
areas: [complex-analysis, scientific-visualization]
concepts: [complex-multiplication, mobius-transformation, conformality]
prerequisites: [vca-01-complex-geometry, vca-03-mobius-inversion, vca-04-amplitwist-derivative]
ai_domains: [scientific-communication]
source_refs:
  - id: needham-visual-complex-analysis-1997
    pages: "9-14, 126-130, 189-215"
    role: visual-reference
level: intermediate
created: 2026-07-30
updated: 2026-08-12
---

# Интерактивы Нидхема: релиз 1A

## Состав

1. [Комплексное умножение и формула Эйлера](80_assets/interactive/complex-multiplication-euler.html).
   [Статический SVG](80_assets/complex-analysis/interactive-complex-multiplication-euler.svg).
2. [Образы обобщённых окружностей](80_assets/interactive/mobius-generalized-circles.html).
   [Статический SVG](80_assets/complex-analysis/interactive-mobius-generalized-circles.svg).
3. [Комплексный якобиан и конформность](80_assets/interactive/complex-jacobian-conformality.html).
   [Статический SVG](80_assets/complex-analysis/interactive-complex-jacobian-conformality.svg).

## Контракт реализации

- только локальные HTML, CSS и JavaScript, без серверной части и внешних библиотек;
- нативные ползунки и переключатели доступны с клавиатуры;
- холст перестраивается вместе с параметрами, а численные значения озвучиваются через `aria-live`;
- компоновка переходит в один столбец на узком экране;
- каждый интерактив содержит содержательный статический SVG;
- русские подписи являются основными;
- сценарий отказа виден в самом эксперименте, а не спрятан в примечании.

## Проверяемые инварианты

### Комплексное умножение

$$
|wz|=|w||z|,
\qquad
\arg(wz)=\arg w+\arg z\pmod{2\pi}.
$$

### Преобразование Мёбиуса

Выборка точек обобщённой окружности под картой $M(z)=1/(z-p)$ должна аппроксимировать окружность или прямую. При приближении к полюсу точки намеренно обрезаются и интерактив сообщает о численной чувствительности.

### Комплексный якобиан

При $\delta=0$ сингулярные числа равны, поэтому окружность остаётся окружностью. При $\delta>0$ получается эллипс. При $s=0$ образ схлопывается в точку, что отделяет изотропию от сохранения информации.

## Визуальная проверка

Проверить вручную:

1. desktop и ширину 375 пикселей;
2. изменение каждого параметра клавишами стрелок;
3. читаемость подписей без масштабирования страницы;
4. наличие статического fallback при отключённом JavaScript;
5. отсутствие сетевых запросов.
