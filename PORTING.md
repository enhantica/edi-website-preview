# Bringing the design back to edi

`website-concepts/` has the same paths as edi's `codex/zensical-design-concepts` branch. During
this exploration, make design changes in this preview repository and treat its `main` branch as
the active documentation-design source. The application and production documentation continue
to live in edi.

The initial edi commit is recorded in `EDI_SOURCE_COMMIT`. The preview baseline tag identifies
the matching initial copy. Later design changes can be transferred as an ordinary patch:

```sh
git remote add website-preview https://github.com/enhantica/edi-website-preview.git
git fetch website-preview main tag edi-website-preview-baseline-2026-10-29
git diff edi-website-preview-baseline-2026-10-29 website-preview/main -- website-concepts/ > /tmp/website-preview.patch
git apply --check /tmp/website-preview.patch
git apply /tmp/website-preview.patch
```

Run these from edi on the design branch or a successor that contains the recorded source commit.
If the remote already exists, fetch it instead of adding it again. Review any intervening changes
to the same files before applying the patch.

This copies only the design sources. It deliberately excludes this repository's root README,
source-snapshot marker, licence copy and independent Pages workflow. Integrating the chosen
design with edi's actual documentation, notebook generation and existing Pages/web-app deployment
is a separate reviewed change. The design alternatives themselves remain available for comparison.
