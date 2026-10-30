# ADR-0011: Shared badges and workflow symbols

Date: 2026-10-30
Status: accepted — owner requests consistency across all pages

Use the native tag registry's label, colour role and Font Awesome 5 icon/glyph wherever measurement badges appear. Keep icon-free tags icon-free when the GUI has no symbol. Glossary definitions and explicit short measurement labels use the shared badge renderer; code blocks, filenames and equations retain their original notation. Do not use the abbreviation CLI in user-facing prose; use Command Line.

Present experiment-label meanings as compact two-column tables grouped by purpose, fitting mode and measurement attributes. Keep existing definition anchors for incoming links. Avoid a heading and description that merely repeat one another.

The workflow diagram, stage table, stage links and workflow navigation use the same Material icons declared by ADR-0002. The SVG embeds the actual bundled icon paths rather than approximations or generated artwork. Its container scrolls on narrow screens to keep the labels readable without causing page overflow.

Strict builds validate links. Inspect coloured badges, native glyphs, all definition anchors, workflow stage links and vectors, responsive scrolling, dark/light themes and glossary/catalogue consistency. Renderers must be stable when run repeatedly.
