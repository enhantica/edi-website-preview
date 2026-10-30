# Example refinement from the Command Line

[Download the example project](../assets/interfaces/example-project.zip) and extract it. Open a terminal in the containing folder, using your [standalone executable](standalone.md) or [Python package environment](python.md).

## Run without saving

<!-- example:cli -->
=== "Standalone"

    ```console
    edi fit pd-neut-cwl_y2o3-spodi --dry
    ```

=== "Python package"

    ```console
    python -m edi fit pd-neut-cwl_y2o3-spodi --dry
    ```
<!-- /example -->

`--dry` runs the refinement and leaves the starting files unchanged.

## Save the result

=== "Standalone"

    ```console
    edi fit path/to/project --output refined-project
    ```

=== "Python package"

    ```console
    python -m edi fit path/to/project --output refined-project
    ```

Replace `path/to/project` with the extracted example folder. See [Run a refinement](fit.md) for progress, output and cancellation options.
