# EasyDiffraction website preview

A temporary public design workspace for the unified EasyDiffraction website, built with the free
Zensical generator. It contains documentation concepts, branding assets, real application
screenshots and build tooling. It does not contain the edi or crysta implementation.

- [Compare the concepts](https://enhantica.github.io/edi-website-preview/)
- [A — choose your interface](https://enhantica.github.io/edi-website-preview/surfaces/)
- [B — follow your workflow](https://enhantica.github.io/edi-website-preview/workflows/)
- [Shared workflow with interface tabs](https://enhantica.github.io/edi-website-preview/workflows/guides/refine/)

The visible brand is **EasyDiffraction**; code examples use **edi**. These are design prototypes:
page organization, wording and styling are still being discussed. The web-app buttons open the
existing edi application; this repository does not build or host another copy of the application.

## Continue the design

Edit `website-concepts/surfaces/docs/` or `website-concepts/workflows/docs/`, including each one's
`assets/concept.css`. Navigation is declared in the adjacent `mkdocs.yml` files. Push to `main`
to rebuild and publish both alternatives automatically. The Pages workflow can also be run manually.

See [local build instructions](website-concepts/README.md). The preview builds without a native
edi build, a crysta checkout, private access tokens, or a paid Zensical subscription.

## Return the selected design to edi

The source layout matches the original edi branch `codex/zensical-design-concepts`. The original
edi snapshot is recorded in `EDI_SOURCE_COMMIT`; the initial preview commit is tagged
`edi-website-preview-baseline-2026-10-29`. See [PORTING.md](PORTING.md) for a reviewable transfer
that excludes this repository's independent hosting workflow.

The source and existing product assets carry edi's BSD-3-Clause licence. Zensical has its own
MIT licence. Screenshots are actual images already present in edi's public documentation.

