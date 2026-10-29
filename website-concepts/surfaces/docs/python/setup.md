# Set up Python

The current library's import name is `edi`. These pages describe the current edi codebase, which is a new generation of EasyDiffraction; installation instructions for the earlier `easydiffraction` package are not interchangeable with it.

## Current availability

This preview documents a configured edi source checkout. It does not yet advertise a public package-install command for the new library. The [edi repository](https://github.com/enhantica/edi) is the source for current build requirements and package availability.

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

---

Sources: [edi package metadata](https://github.com/enhantica/edi/blob/main/pyproject.toml), [Pixi tasks](https://github.com/enhantica/edi/blob/main/pixi.toml), and [native extension loading](https://github.com/enhantica/edi/blob/main/lib/edi/__init__.py). The introductory progression follows the [earlier library first steps](https://docs.easydiffraction.org/lib/latest/user-guide/first-steps/).
