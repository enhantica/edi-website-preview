# Set up Python

Use `edi` to access EasyDiffraction from Python scripts and notebooks.

## Current availability

Set up Python from a configured edi source checkout. The [edi repository](https://github.com/enhantica/edi) declares the build requirements and package availability.

Python is a binding over edi's native product core. An environment that contains only the Python source files is insufficient: the matching compiled `edi._edi` extension and its engine dependencies must be available.

## Use the configured source environment

In an authorized source checkout with its SDK access configured, the declared build command is:

```console
pixi run core-build
```

Use that checkout's environment for Python:

```console
pixi run python -c "import edi; print(edi.Project)"
pixi run python -m edi --help
```

The current product metadata requires Python 3.12 or later; the repository's environment chooses its declared interpreter and dependencies. Native SDK access may require organization credentials, so these commands are not a promise of an anonymous build from a fork.

## Work in a notebook

Choose a notebook kernel from the same configured environment. A notebook and a terminal should import the same `edi` installation, especially when using a local native build.

Begin with an [existing complete project](projects.md). Save your starting project separately before running a scan, since scan analysis writes progress files as it runs.

## Explore without a source build

[Try the web application](https://enhantica.github.io/edi/webapp/) to explore the project model and examples while package distribution is being prepared.
