# Design record: use the upstream Zensical design

- **Status:** accepted direction for the documentation prototypes.
- **Date:** 2026-10-29.
- **Scope:** both navigation alternatives and the comparison page.

The previous prototypes overrode the theme's content width, margins, typography, header, navigation,
colors and landing-page layout. Those overrides are removed. The owner requested Zensical's
Projects-page design directly, with EasyDiffraction's accent and official branding only.

Use the modern theme shipped in Zensical 0.0.73. The published reference is
`https://zensical.org/projects/`. Its `modern/main.4ab2de0c.min.css` and
`modern/palette.b60ce83d.min.css` are the same theme assets emitted by this version. Native theme
defaults load Inter and JetBrains Mono. Keep its content width, spacing, navigation, page outline,
heading styles, buttons, admonitions and cards. Authored content selects those components without
overriding their styling. The light theme contains no dark hero or custom dark panels.

Theme configuration selects the native `light blue` primary/accent palette for EasyDiffraction.
Custom `extra_css`, `extra_javascript`, font overrides and template overrides are absent.

## Official branding

Assets are copied unchanged from `https://github.com/easyscience/assets-branding` at commit
`46ab481bfe6d3b196f9609b17cd46cda7a0fadd8`:

| Upstream path | Preview asset | Use |
| --- | --- | --- |
| `easydiffraction/icons/color.png` | `assets/icon.png` | Native header logo and favicon |
| `easydiffraction/logos/light.svg` | `assets/logo-light.svg` | About-page wordmark |

The upstream BSD-3-Clause licence is retained in `BRANDING-LICENSE`. Application screenshots
continue to come from edi's existing public documentation.

## Selected navigation

On 2026-10-29 the owner selected the interface-first direction: Home, Get started, Application,
Python, CLI, Learn and About. Most visitors work through one interface, so its procedures and
reference material belong under an explicit primary tab. Shared concepts remain in Learn.

New content is added to `surfaces/`. The comparison entry points to that working documentation;
the earlier `workflows/` variant remains available as a reference. Both keep the native theme.
Production integration into edi remains a separate reviewed change.

Legacy documentation is adapted to the current edi generation rather than copied as an API or
distribution promise. Source revisions, adapted subjects and current implementation checks are
recorded in `CONTENT-SOURCES.md`; upstream attribution and licences are retained.
