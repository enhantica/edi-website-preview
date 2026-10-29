# Documentation sources and adaptation

The interface-first site is the selected working design. Its content draws from the earlier
EasyDiffraction website, library and application documentation while describing current edi
behaviour. Source links appear at the end of the substantive guides.

## Source inventory

| Source | Revision inspected | Material used |
| --- | --- | --- |
| `easyscience/EasyDiffractionWww` | `c01095953d9be3d7c02ca67d231ab1b180385ed0` | `content/home.yaml` and `content/footer.yaml`: product introduction, scientific purpose, readable files and user entry points |
| `easyscience/diffraction-lib` | local documentation snapshot `0d9f10e412a0cd08d4dd0af95845dd9bb597dcdf`; upstream master `c0654956a1281f1ea3f3467c3367167f93edee18` also inspected | `docs/docs/user-guide/`, workflow, glossary, parameters and formats; `quick-reference/` and introduction for the user-documentation progression |
| `easyscience/EasyDiffractionBeta` | `ec1d04ee36036dd092fdd8b779e99767afca6e5d` | README and earlier application workflow: visual analysis, model/pattern inspection, reporting and user-oriented entry points |
| `enhantica/edi` | `cea605412f4844abb9463ee2a01ba7cd97fd75ab`, also contained in the design baseline recorded by `EDI_SOURCE_COMMIT` | Current user guides, Python facade and bindings, argument parser, application controls and checked example catalogue |

Repository references:

- <https://github.com/easyscience/EasyDiffractionWww>
- <https://github.com/easyscience/diffraction-lib>
- <https://github.com/easyscience/EasyDiffractionBeta>
- <https://github.com/enhantica/edi>

The local library snapshot supplies conceptual material; the linked public guides may evolve on
master. Current edi instructions are checked against the recorded product snapshot, not inferred
by renaming the earlier library's import package.

## What was adapted

- **Home and Get started:** a screenshot-led product introduction, direct browser entry, interface
  selection, a first refinement and truthful setup/availability information.
- **Application:** the shared project-to-report progression, with actual current controls for
  structures, experiments, data intake, background, exclusions, fitting modes, scans and files.
- **Python:** the library guide's progression from a project to its structures, experiments,
  calculation, fit and results; examples use current factories, facade calls and report methods.
- **CLI:** the same project-driven workflow, with the current `fit`, `calc`, `export`, `undo` and
  `report` commands and their persistence/reporting options.
- **Learn:** scientific concepts, a glossary, formats, parameters, fitting modes, interpretation
  and links into the current examples.
- **About:** product background, current licensing, support, contribution and citation guidance.

## Generation differences resolved

- The current calculation engine is crysta; the earlier CrysPy/CrysFML backend selection is not
  described as a current edi feature.
- Earlier downloadable releases and `pip install easydiffraction` instructions are not used to
  promise a distribution of the new `edi` library.
- The application calls its structural page **Structure**; older **Model** terminology is
  adapted to the current navigation.
- Browser persistence is described by browser and project origin: selected local writes in
  Chrome/Edge, browser-held projects and zip copies where those local handles are unavailable.
- `fit --dry` and `calc --dry` execute without saving; `undo --dry` previews a restoration.
  Archive inputs and output folders are explained separately.
- A Python calculation stores results on experiments; it does not return a new pattern object.
- PDF reporting is an application capability; Python/CLI report instructions describe the
  formats and methods they actually support.
- A historical release's DOI is not presented as a DOI for the current edi preview.

## Attribution and scope

The text is adapted and expanded for the current product. The library and Beta source licences
are retained in `third-party/`; branding provenance and its licence are recorded separately in
`DESIGN.md` and `BRANDING-LICENSE`. Website messaging is attributed to its source file; obsolete
download links, backend descriptions and release metadata are not reproduced as current claims.

Python examples have been checked against the source and parsed for syntax. They have not all
been executed against a newly built native edi environment as part of this documentation-only
preview. This is an expanded documentation draft, not a claim that every historical API page or
tutorial has been migrated or independently revalidated.
