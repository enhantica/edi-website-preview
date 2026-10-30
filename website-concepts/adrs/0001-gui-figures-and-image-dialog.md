# ADR-0001: GUI figures, compound highlights and image enlargement

Date: 2026-10-30
Status: implemented

## Context and prior art

The native screenshot importer and `gui-capture` renderer already pair PNGs with Qt layout metadata. The first renderer rounded and clipped the entire SVG, shrinking some figures through Zensical's `width: fit-content` default. It also omitted gallery annotations and only drew rectangles. The NOBUGS presentation's `markbox` paths instead join a selected tab to its panel in one stepped outline.

## Decision

All generated GUI figures fill the text column. The rounded clip applies only to the screenshot image; its frame and square highlight paths are separate siblings. The SVG allows visible overflow. Each highlight expands by 1.5 displayed CSS pixels on each side, recalculated from the viewBox scale by one ResizeObserver. Its outline remains two display pixels through a non-scaling stroke.

Sidebar paths join the selected native tab and the body below the tab strip, using the capture's geometry. Missing or inconsistent tab geometry refuses generation. All sidebar views show this compound shape. The same rendering path serves the walkthrough, layout guide and enlarged view; it does not alter native images or metadata.

Clicking a screenshot opens a native HTML dialog filling the viewport, with the current highlights retained. It has an accessible title, visible Close button, Escape handling, modal focus containment and focus return. The image link remains a fallback without JavaScript and supports ordinary modified clicks. The dialog uses the site's theme colors. Keyboard behavior follows the [WAI modal dialog pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/).

The Application introduction contains one **Application layout** page before one **Example refinement** page. The former merges the workspace overview and every enabled sidebar view; the latter contains the complete Y2O3/SPODI workflow. The old routes redirect to these pages.

## Verification

Build validation checks the native capture bundle and generated links, including SVG image links. Browser checks verify uniform column widths, screenshot-only clipping, square unclipped outlines, display-pixel padding after resizing, compound selected-tab paths, modal sizing/focus/close behavior, theme inheritance and the consolidated navigation and redirects. Check desktop and narrow mobile viewports.
