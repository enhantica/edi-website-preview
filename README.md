# EasyDiffraction website preview

A temporary public documentation workspace for the unified EasyDiffraction website, built with the free
Zensical generator. The selected interface-first design is being expanded from the earlier
website, library and application sources. It contains documentation, branding assets, real application
screenshots and build tooling. It does not contain the edi or crysta implementation.

- [Open the selected documentation](https://enhantica.github.io/edi-website-preview/)
- [Earlier workflow-first alternative](https://enhantica.github.io/edi-website-preview/workflows/)

The visible brand is **EasyDiffraction**; code examples use **edi**. Home, Get started, User guide, Application,
Python, Command Line and About are the selected primary sections. The content is an evolving draft
checked against current edi behavior. The web-app buttons open the
existing edi application; this repository does not build or host another copy of the application.

## Continue the design

Continue editing `website-concepts/surfaces/docs/`. The earlier `workflows/` alternative is retained
as a reference.
Navigation is declared in the adjacent `mkdocs.yml` files. Use Zensical's native components and
modern theme. The shared wordmark stylesheet fits one adaptive SVG into the header and mobile drawer
without repeating the brand name. Home has a separate adaptive landing layout; documentation pages retain
the native typography, spacing and layout. The native light/dark switch sits beside Search, and
the selected mode is retained between pages. Push to `main`
to rebuild and publish the preview automatically. The Pages workflow can also be run manually.

See [local build instructions](website-concepts/README.md). The preview builds without a native
edi build, a crysta checkout, private access tokens, or a paid Zensical subscription.

## Return the selected design to edi

The source layout matches the original edi branch `codex/zensical-design-concepts`. The original
edi snapshot is recorded in `EDI_SOURCE_COMMIT`; the initial preview commit is tagged
`edi-website-preview-baseline-2026-10-29`. See [PORTING.md](PORTING.md) for a reviewable transfer
that excludes this repository's independent hosting workflow.

The source and existing product assets carry edi's BSD-3-Clause licence. Zensical has its own
MIT licence. Official logos come from `easyscience/assets-branding`; their source revision and
licence are recorded in [the design record](website-concepts/DESIGN.md). Screenshots are actual
images already present in edi's public documentation. The earlier documentation sources, current
behavior checks and retained licences are listed in [CONTENT-SOURCES.md](website-concepts/CONTENT-SOURCES.md).

