---
citeproc: true
metadata:
  bibliography: "references.bib"
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
build open-source Python tools for geophysics, aimed to be used for research,
exploration and teaching.

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


## Example: Gravity fields of large-scale structures

<!--
- Tesseroids
- Example of terrain effect using tesseroids
- Leo's paper on moho inversion
- Santi's paper on gradient-boosted equivalent sources
-->

Computing the gravitational field of large structures can provide additional
insight to applications in Geodynamics.
For example, validating numerical models against observed gravity data, and
inverting for Moho depths from satellite gravity data on continental scales
[@uieda2016]
These processes introduce the challenge of accounting for the curvature of the
Earth during the gravity modelling, where the classical rectangular prisms are
not well-suited for the task.

Instead, we can build our models using _tesseroids_, also known as rectangular
prisms.
[Harmonica][harmonica] offers tools to compute their gravitational fields
on any observation point.

Let's start by downloading a topography grid with [Ensaio][ensaio]:

```python
import ensaio
import xarray as xr

topo_fname = ensaio.fetch_earth_topography(version=1)
topo = xr.load_dataarray(topo_fname)
```

Then we can build a _tesseroid layer_ using [Harmonica][harmonica], which
creates a 3D representation of the topography using tesseroids:

```python
import harmonica as hm
import boule as bl

density = xr.where(topo > 0, 2670.0, 1040.0 - 2670.0)
reference = bl.WGS84.geocentric_radius(latitude)
surface = topo + reference

tesseroids = hm.tesseroid_layer(
    coordinates=(topo.longitude, topo.latitude),
    surface=surface,
    reference=reference,
    properties={"density": density},
)
```

The `reference` is defined as the surface of the reference ellipsoid
provided by [Boule][boule], `surface` is the geocentric radii of the
topographic heights, and `density` contains the density of each tesseroid,
depending if they represent continental masses or water bodies.

We can easily compute the gravitational effect of these tesseroids with:

```python
terrain_effect = tesseroids.tesseroid_layer.gravity(coordinates, field="g_z")
```

And finally produce a plot of the computed terrain effect over South America:

![Terrain effect over South America](figs/terrain-effect.jpg)


## Open and reproducible science

<!--
- Motivations
  - open and reproducible science
  - encourage collaboration between researchers
  - promote best-practices for software development in scientific software
- Tutorials at Transform events (swung)
-->

Fatiando developers are committed to build a more open and reproducible
science.
The software developed by the project is released under open-source licences,
making it freely accessible to any researcher, and ensuring that any result
obtained through their usage could be reproduced.
Moreover, we develop these tools [in the open][contact], through a transparent
and auditable process, to which we invite everyone in the geoscientific
community to join and participate.

We also aim to promote best practices for software development among the
scientific community.
They include adding comprehensive and easy to navigate documentation for every
piece of code, extensive test suites that ensure the software works as
expected, and peer-review processes of new changes to the code.
Following these and other best practices helps to create high quality research
software, and also environments where other people can easily collaborate and
learn more about software development.

## Community

- Contributors from all around the world
- Scientific collaborations beyond papers
- Efforts to solve common problems through open-source software
- Invite people

Throughout the years, a community of developers, contributors and users raised
around Fatiando, including people from all around the world.
These interactions are another form of scientific collaboration that exceeds
co-authorship of papers.
Researchers from different regions of the world join efforts on solving common
problems through collaboratively developed tools.


## Roadmap for the future

- BIRS event
  - invite virtual participants?
- SimPEG and the ecosystem (Software Underground)
- Transform


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
