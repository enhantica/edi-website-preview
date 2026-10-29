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
| Main navigation | Home, Get started, Application, Python, Command Line, Learn, About | Home, Get started, Guides, Tutorials, Reference, About |
| Best entry | A visitor already knows which interface they want | A visitor knows what analysis they want to perform |
| Shared material | Scientific concepts and examples in Learn | Scientific guides with interface-specific instructions |
| Application | Desktop and web have one application home | Application entry points feed the common workflow |
| Contributor content | Quiet footer link, outside the primary user navigation | Quiet footer link, outside the primary user navigation |

The homepage introduces the product and offers the real web app. Documentation pages retain the
Zensical horizontal navigation, grouped left navigation and right-hand page outline. Python use is
a user workflow; contributor documentation concerns changing the product itself.

Both alternatives use the standard Zensical modern theme, native Inter and JetBrains Mono font
loading, and its default light scheme. The only theme color selection is EasyDiffraction's light
blue primary/accent. There is no custom theme stylesheet, JavaScript or template override.
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
- `https://github.com/easyscience/assets-branding`: the official color icon and light-background
  wordmark, with the upstream revision and retained licence recorded in `DESIGN.md`.
- `docs/dev/design/app-screenshots/edi/`: existing product screenshots. Their provenance is recorded
  in that directory's `provenance.yml`. Concept assets are copies of those existing images, not
  generated representations of the application.
- Current `docs/user/` and the edi example catalogue are the authority for product instructions.
  Historical download versions, backend claims and old installation commands are not carried over.

The preview is being expanded into the selected documentation structure. It does not claim to finish the
documentation migration, supply a desktop release, publish to PyPI, or port all historical content.
The proposed architecture and remaining production work are recorded in ADR-0053.
