# EasyDiffraction website concepts

Working Zensical prototypes for discussion of the unified public website. EasyDiffraction is the
public brand; `edi` remains the package and code name. These builds are isolated from the existing
documentation, native product builds and Pages workflow.

## Compare the alternatives

The interface-first navigation is the selected base. New documentation is added to `surfaces/`;
the earlier workflow-first alternative remains as a reference. The content adaptation is recorded
in [CONTENT-SOURCES.md](CONTENT-SOURCES.md).

| | A: choose your interface | B: follow your workflow |
| --- | --- | --- |
| Main navigation | Home, User guide, Application, Python, Command Line, Physics, About | Home, Get started, Guides, Tutorials, Reference, About |
| Best entry | A visitor already knows which interface they want | A visitor knows what analysis they want to perform |
| Shared material | Scientific concepts, workflow and examples in User guide | Scientific guides with interface-specific instructions |
| Application | Desktop and web have one application home | Application entry points feed the common workflow |
| Contributor content | Quiet footer link, outside the primary user navigation | Quiet footer link, outside the primary user navigation |

The homepage introduces the product and offers the real web app. Documentation pages retain the
Zensical horizontal navigation, grouped left navigation and right-hand page outline. Python use is
a user workflow; contributor documentation concerns changing the product itself.

Both alternatives use the standard Zensical modern theme, native Inter and JetBrains Mono font
loading, and native light/dark schemes with a switch next to Search. Light is the initial default. The only theme color selection is EasyDiffraction's light
blue primary/accent. Documentation pages use the native content design and templates. The selected Home has a
page-specific adaptive landing layout; no custom JavaScript is used. A small wordmark
stylesheet sizes the single adaptive SVG in the header and drawer without a duplicate label.
The public root opens the selected documentation directly. See [DESIGN.md](DESIGN.md).

## Build and preview

From the repository root, using a Python interpreter supported by Zensical:

```sh
python -m venv website-concepts/.venv
website-concepts/.venv/bin/python -m pip install -r website-concepts/requirements.txt
website-concepts/.venv/bin/python website-concepts/build.py
website-concepts/.venv/bin/python -m http.server 8873 --bind 127.0.0.1 --directory website-concepts/_build
```

Open `http://127.0.0.1:8873/` for the selected documentation. Existing `/surfaces/` links remain available as compatibility aliases; the earlier alternative is at `/workflows/`. Build only one alternative by passing `surfaces` or `workflows` to
`build.py`. Build products and caches are ignored. Authored concept pages and review screenshots
are retained on the branch.

For a hosted preview, pass `--base-url https://enhantica.github.io/edi-website-preview/` to
`build.py`. This supplies the publishing prefix through temporary configurations without changing
the authored local-preview URLs. The build also checks generated internal links and asset paths.

Browser captures can be reproduced with `capture.py surfaces` and `capture.py workflows` after
installing `playwright==1.64.1` in the preview environment. Set `BROWSER_EXECUTABLE` to an installed
Chromium-compatible browser; this checkout used `/opt/brave.com/brave/brave`. The capture command
serves the built concepts on a temporary loopback port, records browser checks, takes desktop and
mobile screenshots, and then stops its browser and server. It does not download a browser.

## Source material and boundaries

- `https://easydiffraction.org/`: product promise, screenshot-led introduction and direct entry actions.
- `https://docs.easydiffraction.org/lib/latest/`: the Project → Structure → Experiment → Analysis →
  Report workflow, glossary, formats, parameters and scientific examples.
- `https://docs.easydiffraction.org/app/`: grouped task navigation and application workflow.
- `https://easydiffraction.github.io/`: direct product and platform entry points.
- The supplied Zensical screenshots: horizontal section navigation, grouped local navigation,
  page outline, readable content width and restrained contributor navigation.
- `https://github.com/easyscience/assets-branding`: the official color icon and light/dark-background
  wordmarks, with the upstream revision and retained licence recorded in `DESIGN.md`.
- `docs/dev/design/app-screenshots/edi/`: existing product screenshots. Their provenance is recorded
  in that directory's `provenance.yml`. Concept assets are copies of those existing images, not
  generated representations of the application.
- Current `docs/user/` and the edi example catalogue are the authority for product instructions.
  Historical download versions, backend claims and old installation commands are not carried over.

The preview is being expanded into the selected documentation structure. It does not claim to finish the
documentation migration, supply a desktop release, publish to PyPI, or port all historical content.
The proposed architecture and remaining production work are recorded in ADR-0053.

The selected preview now has `Home · User guide · Application · Python · Command Line · Physics · About`. Each interface follows Start here, Project, Structure, Experiment, Analysis and Report. The homepage button enters the User guide; setup and first steps live under the relevant interface. Physics supplies model/equation anchors and a JSON catalogue; the build also emits plain Markdown under `reference/` and a root `llms.txt`. The feature matrix separates current four-interface coverage from planned scientific models.

The preview's main branch is a work-in-progress review surface: push incremental changes directly to main so the owner can follow them on Pages. A completed production migration is not required before publishing an increment.

Browser verification is recorded in `screenshots/surfaces-browser-checks.json`, produced by `python website-concepts/capture.py surfaces`. It checks every Physics page with mathematical markup, requires every equation wrapper to contain rendered SVG, catches missing local assets and JavaScript errors, verifies accessible SVG feature-status icons, and exercises the homepage, feature table and long-equation page across its declared responsive widths. Header/drawer branding and theme switching remain part of the same check. The check uses installed Chromium; no Safari/WebKit run is claimed.

For visual review, see `screenshots/surfaces-home.png`, `screenshots/surfaces-features.png`, `screenshots/surfaces-physics-displacement.png` and `screenshots/surfaces-physics-mobile-dark.png`.

The all-page report records its source commit. `screenshots/surfaces-final-checks.json` records the subsequent focused verification after native SVG feature icons were enabled, including the reported ADP page, numbered background bibliography and narrow/wide layouts. One intervening long browser session closed unexpectedly during a late viewport resize; its failed run is not represented as a successful report. The isolated follow-up passed. Scientific feature coverage was audited from the declared source snapshot; this documentation work did not rerun the native numerical comparison suites.

The later homepage/network check is `checks/network_browser.py` (run after building; use `--record` for a motion clip). `screenshots/network-checks/chromium.json` records the checked source commit, browser version, invocation and measured layout. Its screenshots and `pulse-motion.webm` show the supplied Analysis image with the title bar cropped in CSS, its rounded frame, native navigation alignment and the full-width network. The current owner-selected frame colour is `#e5e5e5`; refer to each report's source commit when viewing older captures. Checks cover real connected-edge trail geometry, independent constant speeds, fixed hover geometry, offscreen suspension, simulated visibility changes, removal/restoration cleanup, browser history and native reduced-motion emulation. `.github/workflows/check-homepage.yml` runs the same assertions in Chromium and native macOS Safari on manual dispatch; its uploaded artifacts are the source of truth for those runs. Safari does not emulate a mobile device or OS reduced-motion changes through this driver; the report records the actual viewport sizes the native window accepts.

## Native reference and teaching assets

The consolidated design authority is the relay [documentation architecture ADR](https://github.com/enhantica/relay/blob/main/knowledge/design/edi-documentation-architecture.md). Its amendment policy records explicit owner decisions; the local ADRs record implementation detail.

Build the native app's optional `edi_doc_metadata` target and save its stdout as dictionary JSON. In the same edi Python environment, run `tools/docs/python-reference.py --output python-paths.json`. Import those files with `render_parameter_reference.py --import-native EDI_ROOT --dictionary dictionary.json --python-paths python-paths.json --sdk-library SDK_LIBRARY`. This retains SDK/source hashes and the Python binding commit. The app example/tag snapshot is imported with `render_experiments.py --import-native EDI_ROOT`. Ordinary docs builds render the committed snapshots and check every native documentation target.

`capture_learning.py --edi-root EDI_ROOT` uses the example selected by the GUI manifest, calculates and fits an isolated project copy, and exports matching-axis Plotly SVGs and a real terminal transcript. It uses the existing app environment and an installed Chromium browser; set `BROWSER_EXECUTABLE` if necessary. Its input, generator and asset hashes are retained in `assets/learning/capture.json`. `render_learning.py`, called by the normal build, updates comparisons and displayed results together. For the Application tutorial, pass `--gui-capture BUNDLE` to calculate the actual saved `checkpoints/starting` and `checkpoints/refined` models from a completed native run. The importer retains these projects with the bundle; both project hashes and the GUI manifest/binary identity accompany the separate `assets/learning/gui` plots. Python and CLI retain their prepared-project outputs. All comparisons must use identical finite axes, including across excluded observations.

Display equation layout is checked with `checks/math_browser.py --browser both --output OUTPUT` after building. Install the desired Playwright browser engines and their runtime dependencies. The check exercises mobile/desktop, light/dark, actual SVG dimensions and horizontal scrolling; its WebKit control reproduces the native theme collapse with the layout fix disabled. It does not claim a physical-device Safari test.
