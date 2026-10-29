# Set up the command line

The command-line interface is part of the `edi` Python package and uses the same native calculation core. Use a configured edi environment to run it.

## Prepare the environment

Follow the [environment setup](../python/setup.md) to build the native core and make `edi` available. From that configured checkout, check the command-line entry point:

```console
pixi run python -m edi --help
```

In a terminal where that environment is already active, use:

```console
python -m edi --help
```

## Start with a complete project

A command reads the structures, experiments and analysis choices saved in a project. [Run an example](examples.md) for your first refinement, or use [project inputs and output files](files.md) for a project you already have.

## Follow the workflow

Use **Project**, **Structure**, **Experiment**, **Analysis** and **Report** in the left navigation. The command line reads prepared structures and experiments from the project; the visual application and Python provide the corresponding model-editing tools.
