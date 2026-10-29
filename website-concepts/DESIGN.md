# Design record: use the upstream Zensical design

- **Status:** accepted direction for the documentation prototypes.
- **Date:** 2026-10-29.
- **Scope:** the selected documentation and archived navigation alternative.

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
Documentation pages retain native content styling, fonts and templates. The
2026-10-29 wordmark request adds a header-only `assets/branding.css`: fit the unchanged official
wordmark within the native toolbar height, show it on mobile, and hide the duplicate brand label.
The favicon retains the official icon. This header rule is shared by both navigation prototypes. The selected homepage also has the
scoped landing-page design described below.

## Official branding

Assets are copied unchanged from `https://github.com/easyscience/assets-branding` at commit
`46ab481bfe6d3b196f9609b17cd46cda7a0fadd8`:

| Upstream path | Preview asset | Use |
| --- | --- | --- |
| `easydiffraction/icons/color.png` | `assets/icon.png` | Favicon |
| `easydiffraction/logos/light.svg` | `assets/logo-light.svg` | Light header logo and About-page wordmark |
| `easydiffraction/logos/dark.svg` | `assets/logo-dark.svg` | Dark header logo |

The upstream BSD-3-Clause licence is retained in `BRANDING-LICENSE`. Application screenshots
continue to come from edi's existing public documentation.

## Selected navigation

On 2026-10-29 the owner selected the interface-first direction: Home, Get started, User guide, Application,
Python, Command Line and About. Most visitors work through one interface, so its procedures and
reference material belong under an explicit primary tab. Shared concepts and the analysis workflow belong in User guide, before Application.

New content is added to `surfaces/`. The public site root opens that working documentation directly;
the earlier `workflows/` variant remains available as a reference. Existing `/surfaces/` URLs
remain compatibility aliases with canonical URLs at the root. Both keep the native theme.
The owner requested removal of the prototype chooser and the label **Command Line** on 2026-10-29.
Production integration into edi remains a separate reviewed change.

Legacy documentation is adapted to the current edi generation rather than copied as an API or
distribution promise. Source revisions, adapted subjects and current implementation checks are
recorded in `CONTENT-SOURCES.md`; upstream attribution and licences are retained.

## Shared-guide decision — 2026-10-29

The owner requested that shared material in the former Python library guide be made generic
and placed before Application. Extend the existing Learn content into **User guide**; do not
create parallel scientific guides under each interface or enlarge Get started into a manual.
Get started handles orientation, availability and a first run. User guide owns Introduction,
Concept, Data formats, Parameters, Glossary, fitting modes, fit assessment and the complete
Project → Structure → Experiment → Analysis → Report workflow.

Every workflow stage explains the scientific model and links to interface procedures. Application
owns controls, Python owns objects and calls, and Command Line owns commands/options. Move
the application first-refinement walkthrough and interface-specific example instructions into
those sections. Remove code and GUI-specific instructions from the common explanations.

Prior art is the former `surfaces/docs/learn/` section and diffraction-lib's
`docs/docs/user-guide/analysis-workflow/` chapters. Existing shared links move to `/user-guide/`;
`redirects.json` records old `/learn/` routes and the builder emits static redirects. The existing
`/surfaces/` compatibility copy receives the same redirects, with canonical URLs at the root.
This uses the same pre-build/post-build approach as the preview's existing compatibility copy,
without relying on an unsupported generator plugin. Check every redirect target and exercise
the original and `/surfaces/` URLs in the browser.

Historical calculator lists, Bayesian samplers, automatic report-on-project-save behaviour and
old Python access/key tables are not carried over as current edi promises. Current procedure
examples remain checked against edi; the common model explains the concepts without obsolete APIs.

## Focused landing-page decision — 2026-10-29

The owner requested a clean, light, modern homepage inspired by Zensical's single-hero homepage,
with introductory text, Try the web app and Get started buttons, and one real application screenshot
on the right. Replace the previous selected homepage's stacked screenshot, cards, task table,
workflow list, technical explanation and source footer. Their information already has homes in
Get started, User guide, the interface sections and About. Source attribution remains in
CONTENT-SOURCES.md. The archived workflow-first alternative is retained as historical prior art.

The selected Home uses a page-specific template and stylesheet. The template inherits Zensical's
header, navigation, search, fonts and runtime; it adds only the landing CSS and omits the footer.
The stylesheet is loaded only on Home and scopes its content rules to the hero. Documentation
pages keep the native Zensical design. There are no theme-wide width or typography changes,
animations, decorative badges, extra feature sections or new JavaScript. The official wordmark
and existing light application screenshot are unchanged.

Use the exact owner-provided slogan, **Making diffraction data analysis and modelling easy**.
Only **diffraction** and **easy** use the EasyDiffraction primary blue; the other words retain
the normal dark text.

Use an adaptive grid: text beside the screenshot when both have room, then a stacked layout
on tablets and phones. Keep fluid type, wrapping buttons, the screenshot's intrinsic ratio and
visible keyboard focus. Check narrow phones, tablets, ordinary laptops and large/high-resolution
displays for clipping, horizontal overflow, action visibility and screenshot loading.

## Native color-mode toggle — 2026-10-29

The owner requested the mode switch beside Search, as on Zensical's site. The earlier single
light palette deliberately omitted that switch; replace it with the native default/slate palette
list and its sun/moon toggle in both prototypes. Light is the initial default, and the native
runtime retains the visitor's selection. The hero uses the same foreground/background/accent
variables as the theme, so light mode remains fully light and dark mode uses the native dark
scheme. Do not add a custom theme-toggle script.

Use the official light and dark wordmarks unchanged from the same branding revision above.
A logo-only template partial emits both image variants; the branding CSS shows the matching one.
Check switching, persistence after reload and navigation, visible search controls and wordmarks,
and layout at different viewport widths and device pixel ratios.

## Single adaptive wordmark — 2026-10-29

The owner's iPhone screenshots showed both light/dark images in the header and a shrunken
wordmark followed by duplicate site-name text in the drawer. Replace the two-image logo in
both prototypes with one inline SVG derived from the official light wordmark. Preserve the
geometry and blue symbol; set only the lettering group's fill to `currentColor` so the native
light/dark theme supplies its color. Prefix gradient IDs separately for header and drawer.
The original official SVG files remain unchanged as source assets.

The native drawer title assumed an icon plus a separate name. Its narrow override removes
that repeated name and gives the single wordmark the same visual height as the header.
Use a new `wordmark.css` URL so a cached earlier branding stylesheet cannot leave the old
icon sizing in place. There is no image visibility switching or custom theme JavaScript.

Check the open mobile drawer, not just the closed header, in both schemes. Require exactly
one SVG per logo slot, no image pair or extra site-name text, consistent logo dimensions,
unique gradient IDs and lettering that changes color while the symbol remains unchanged.
Also check navigation and keyboard focus, and exercise the markup with custom CSS blocked.

## Independent documentation and workflow navigation — 2026-10-29

The owner requested standalone documentation for EasyDiffraction, clearer navigation and a home
for the scientific theory. Remove the redundant Get started primary tab. The Home Get started
button opens User guide, whose entry table points directly to each interface's setup and first
refinement. Remove the separate onboarding tree and retain its URLs as redirects.

Application, Python and Command Line share the same left-navigation order: Start here, Project,
Structure, Experiment, Analysis and Report. Add Reference only where needed. Procedures remain
interface-specific; the command line consumes prepared structure/experiment inputs and its
pages say so without inventing editing commands. User guide owns the common workflow. Replace
Plan and assess with the actual Fitting modes, Fit quality and Examples topics.

Place Physics before About. It owns the scientific explanations, equations and conventions;
User guide owns the practical analysis decisions. Begin with diffraction/scattering, profiles,
refinement/statistics and conventions, citing public scientific sources. Do not expose an
unfiltered research corpus or imply that every general physics topic is an implemented feature.

Remove release-history sections, old-documentation links, migration prose and authoring source
footers from published user pages. Preserve attribution, licences and source notes in the
repository-level CONTENT-SOURCES.md and third-party notices. Retain factual setup and capability
limits without presenting the website as a comparison with another product generation.

The owner also requested the landing-page typeface from easydiffraction.org. Its live
`css/style.min.css` declares Nunito (Google Fonts, weights 400–800). Use that face only in the
hero and its actions, keep the native documentation font, reduce the buttons' padding/rounding,
and give the screenshot more width on desktop while retaining stacked mobile layouts.


### Preview publishing decision (2026-10-29)

The owner clarified that preview `main` is their work-in-progress review surface. Push working increments directly to main and let Pages deploy them, even while the wider design/content task is unfinished. Do not hold normal progress on a separate checkpoint branch waiting for a completed production migration. Report what changed and which checks remain.

### Scientific reference and retrieval contract

Physics is grouped into diffraction model, peak profiles, intensity corrections, experiment model, refinement/statistics and reference lookups. Exact model tokens and parameter names resolve to stable section/equation anchors. Render equations only on Physics pages with locally bundled MathJax. Preserve native Zensical article/sidebar typography.

A JSON catalogue records source snapshot, model/parameter scope, scientific units and effective roles. Metadata refinability alone does not prove fitting admission. Features and roadmap distinguishes all four interfaces and prepared-project execution from editing. Plain Markdown and llms.txt are generated from these same pages rather than maintained as a competing scientific source. The export supports future assistant retrieval; this change does not add an application chat backend.


### Home: larger product view and interface links (2026-10-29)

Extend the existing screenshot-on-the-right hero: keep the slogan aligned with the native header, give the screenshot more of the available space to the right, and keep the full application image visible. On narrow screens the screenshot follows the text and uses a little more of the viewport width.

A single quiet group below the action buttons identifies Web app, Desktop app, Python and Command Line. Use the bundled Zensical Lucide icons and Python mark with readable names; each link opens the relevant interface documentation. Keep the primary web-app action distinct. Avoid extra cards or homepage sections. The interface links wrap into a regular two-column layout on small screens.
