# Set up your environment

Use the browser to explore the current application immediately. Local desktop, Python and CLI work use a configured edi source environment and the native dependencies it declares.

## Browser

[Open the web app](https://enhantica.github.io/edi/webapp/). There is no Python environment to install for this route.

Start with [your first refinement](first-refinement.md) and keep a project copy on your computer when you want to retain the work. The [browser guide](../application/browser.md) explains local file access and browser storage.

## Desktop application

The current edi repository supports the desktop application on Linux x86-64 and macOS 14 or later on Apple silicon. Use the [desktop guide](../application/desktop.md) for the current source-build route.

Earlier EasyDiffraction application installers belong to the earlier product generation. Their version and platform information should be read with the matching older documentation.

## Python

The current import name is `edi`. The Python library uses the compiled edi core, so a copy of the Python source files alone is not enough.

Follow [Python setup](../python/setup.md) for the declared source build and environment checks. Current package metadata requires Python 3.12 or later; the checkout's Pixi configuration selects its working interpreter and dependencies.

## Command line

The current CLI entry point is `python -m edi`. It uses the same configured environment and native core as the Python library.

Start with [the command-line overview](../cli/index.md), then run a saved project through the [refinement guide](../cli/fit.md).

## Native dependencies and availability

A local source build consumes the pinned crysta SDK. Access to that SDK may require organisation credentials, so these instructions do not promise an anonymous build from a fork.

The [edi repository](https://github.com/enhantica/edi) and its [build configuration](https://github.com/enhantica/edi/blob/main/pixi.toml) are the authority for current build tasks and dependencies. Until a package or installer for the current generation is explicitly published, use the web app for the lowest-friction trial.

---

Sources: [edi platforms and licence](https://github.com/enhantica/edi/blob/main/README.md), [package metadata](https://github.com/enhantica/edi/blob/main/pyproject.toml), [Pixi tasks and SDK pin](https://github.com/enhantica/edi/blob/main/pixi.toml), [native SDK design](https://github.com/enhantica/edi/blob/main/docs/dev/adrs/0017-prebuilt-crysta-sdk.md).
