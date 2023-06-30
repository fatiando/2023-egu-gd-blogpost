---
title: "Fatiando a Terra: research with open-source software"
---

# Fatiando a Terra: research with open-source software

<!--
Mention:

- introduce the project
- history
- what you can do with fatiando
- motivations and ultimate goals
  - open and reproducible science
  - encourage collaboration between researchers
  - promote best-practices for software development in scientific software
- connections to geodynamics
  - forward modelling with tesseroids
  - moho inversions with tesseroids
- mention simpeg and the ecosystem
- invite ppl to the website
- who develops it?

Figures:

- Logo
- map of visits to the website?
- 3d plot of prisms?
- gravity map over bushveld?
- gravity correction with tesseroids over southamerica?

Layout:

- Introduce the project
- Why?
- Who?
-->


[Fatiando a Terra][fatiando] is a community-driven project with the goal to
build open-source Python tools for geophysics.

The project started in South America more than ten years ago, as part of the
PhD dissertations of a [group of graduate students][founders] from Rio de
Janeiro, Brazil.
Throughout the years, the project reached higher levels of maturity and gained
[contributors][contributors] and [core developers][developers] from different
regions of the world.

> Fun fact: Fatiando a Terra means "slicing the Earth" in Portuguese.

Nowadays the project is composed by a set of different Python libraries, each
one with a specific goal and scope. [Verde][verde] offers tools for spatial
data handling and interpolation, with a machine-learning taste.
[Harmonica][harmonica] provides tools for processing and modelling gravity and
magnetic data, while [Boule][boule] hosts reference ellipsoids (e.g. WGS84)
that can perform coordinate conversions and normal gravity calculations.
Lastly, [Pooch][pooch] offers easy to use tools for downloading and caching
data files from the web, and [Ensaio][ensaio] provides curated open-licensed
geophysical datasets useful for research and teaching.



## What you can do with Fatiando tools?

<!--
- Interpolating large datasets with gb-eqls
- Modelling gravitational fields of continental or global scales structures
  with tesseroids
    - Moho inversions
    - Validation of geodynamics numerical simulations
- Processing gravity data
-->

Fatiando tools can be used in several different geophysical applications.
For example, computing the gravitational fields of large structures can provide
relevant insight to Geodynamic applications, like validating numerical models
against observed gravity data, or inverting Moho depths from satellite gravity
data on continental scales [@uieda2016].
[Harmonica][harmonica] allows to calculate the gravitational field of large
scale structures using [_tesseroids_][tesseroids], also known as spherical
prisms, that take into account the curvature of the Earth.
They come handy also in data processing steps, like terrain correction.

![Terrain effect over South America computed using
tesseroids.](figs/terrain-correction-south-america.png)

[Harmonica][harmonica]'s [gradient-boosted equivalent sources][gb-eq] allow to
interpolate very large gravity and magnetic datasets relying on the equivalent
sources technique. For example, they allowed us to generate a regular grid of
almost 2 million gravity observations over Australia [@soler2021].

![Observed and interpolated a large gravity dataset over Australia. The
interpolation was carried out through Gradient-boosted equivalent
sources.](figs/australia.png)

Moreover, [Harmonica][harmonica] and [Boule][boule] offer all the tools needed
to process gravity data, from observed gravity up to gridded residuals:
removing normal gravity with [Boule][boule]'s ellipsoids, computing the terrain
correction by forward modelling a model of the topography, removing the
regional field with deep equivalent sources, and producing a gridded product of
the residual field using equivalent sources.

![Processed gravity data over Bushveld, Southern Africa: (a) observed gravity
data, (b) gravity disturbance. (c) Bouguer gravity disturbance, and (d) regular
grid of the residual field.](figs/south-africa-gravity.png)


## Open and reproducible science

<!--
- Motivations
  - open and reproducible science
  - encourage collaboration between researchers
  - promote best-practices for software development in scientific software
- Tutorials at Transform events (swung)
-->

Fatiando developers and contributors are committed to build a more open and
reproducible science.
All its software is released under open-source licences, making it freely
accessible to any researcher, and helping to make scientific results obtained
by using it more reproducible.

Moreover, we develop these tools in the open, through a transparent and
auditable process, to which [we invite everyone to join and
participate][contact].
This process had created opportunities for collaborations between researchers
from around the world, beyond the scientific paper: joining efforts to solve
common problems and build tools in a collaboratively way.

We also aim to promote best practices for software development among the
scientific community, like creating good documentation, writing tests that
guarantee the software works as expected, and peer-reviewing new additions to
the code.
Following these and other best practices helps to create high quality research
software, and set the environment for other people to easily collaborate
and learn more about software development.


## Roadmap for the future

<!--
- BIRS event
  - invite virtual participants?
- SimPEG and the ecosystem (Software Underground)
- Transform
-->

We expect great things for the future of the project.
By the end of July, the Fatiando a Terra and [SimPEG][simpeg] communities will
join in a [BIRS Workshop][birs] in Banff, Canada, to work on future roadmaps
for the two projects and to join efforts to create further interactions.

We plan to keep building the project, developing new tools, and improving the
existing ones. Along the way we expect to gain more contributors, enlarge the
community and strengthen the relationships with the rest of the Python
geoscientific ecosystem.

## References

::: {#refs}
:::


[fatiando]: https://www.fatiando.org
[contact]: https://www.fatiando.org/contact/
[founders]: https://www.fatiando.org/community/#project-founders
[contributors]: https://www.fatiando.org/community/#package-authors
[developers]: https://www.fatiando.org/community/#steering-council
[boule]: https://www.fatiando.org/boule
[harmonica]: https://www.fatiando.org/harmonica
[verde]: https://www.fatiando.org/verde
[pooch]: https://www.fatiando.org/pooch
[ensaio]: https://www.fatiando.org/ensaio
[tesseroid-layer]: https://www.fatiando.org/ensaio
[simpeg]: https://simpeg.xyz
[birs]: https://birs-2023.softwareunderground.org
[gb-eq]: https://www.fatiando.org/harmonica/latest/user_guide/equivalent_sources/gradient-boosted-eqs.html
[tesseroids]: https://www.fatiando.org/harmonica/latest/user_guide/forward_modelling/tesseroid.html#tesseroid
