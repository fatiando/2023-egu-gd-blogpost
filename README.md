# Post for EGU Geodynamics Blog

| **Information** | |
|---|---|
| **Title** | Fatiando a Terra: a journey into open-source software for Geophysics |
| **Author** | [Santiago Soler][santisoler] |
| **Editor** | [Constanza Rodriguez Piceda][constanza] |

## How to build

The text of the blogpost can be found in `blogpost.md`, a Markdown file that
can be converted to a PDF, docx or even into a website with [pandoc][pandoc].
So first you will have to [install pandoc][pandoc-install].

We will also use `make` to build the blogpost into different formats. `make` is
available in most GNU/Linux distributions, and it can be installed in Windows
through [`conda`][conda]:

```bash
conda install -c conda-forge make
```

Then clone this repository with:

```bash
git clone https://github.com/fatiando/2023-egu-gd-blogpost
```

### Generate a PDF

To build a PDF version of the blogpost, pandoc will use LaTeX, so be sure to
have a LaTeX distribution installed in your system.

To build the PDF file we just need to run:

```bash
make pdf
```

A `_build/blogpost.pdf` file will be automatically created.

### Generate a .docx

To build a `.docx` version of the blogpost we just need to run:

```bash
make docx
```

A `_build/blogpost.docx` file will be automatically created.

### Generate a website

To build an HTML version of the blogpost we just need to run:

```bash
make html
```

A `_build/index.html` file will be automatically created.

Alternatively, if you install [`livereload`][livereload], you can run:

```bash
make serve
```

It will automatically build the `_build/index.html` and serve it so you can
view it in your web browser.

### License

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png


[santisoler]: https://www.santisoler.com
[constanza]: https://www.plymouth.ac.uk/staff/constanza-rodriguez-piceda
[pandoc]: https://pandoc.org
[pandoc-install]: https://pandoc.org/installing.html
[conda]: https://github.com/conda-forge/miniforge
[livereload]: https://livereload.readthedocs.io

