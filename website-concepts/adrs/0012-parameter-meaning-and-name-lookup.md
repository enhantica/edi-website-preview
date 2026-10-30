# ADR-0012: Separate parameter meanings from interface-name lookup

Date: 2026-10-30
Status: accepted — owner confirms no units in the name-comparison tables, units in explanations

Keep Parameter names focused on comparing GUI/Edi/Python/CIF names. Use two-column tables with native category icons and readable parameter names, without a Units column. Retain aliases where useful in the naming view.

The Physics reference explains the parameter: readable heading, native description, declared units and calculation role, and model options or unit-dependent forms where applicable. Do not repeat GUI/Python/CIF name blocks in every explanation. Keep a precise Names across interfaces link to the corresponding category table. Stable parameter/category anchors remain unchanged for native help and existing links.

Use restrained entry boundaries and native headings to make each parameter block clear. Units stay visible in explanations; anisotropic beta is dimensionless while B/U components use squared-length units. Empty metadata does not justify inventing a unit. Preserve source-backed descriptions, restrictions and equation links.

Validate every native category/item link, all naming tabs and return anchors, unit-dependent displacement forms, preserved options, readable headings and desktop/phone layout in both themes.

Keep core structure and experiment categories before persistence/report metadata. Reader descriptions for cell dimensions and fractional coordinates expand the existing crystallography explanation; other entries retain native descriptions. Category return anchors wrap the visible caption so native browser navigation works after selecting a different naming tab, without an additional tab-switching script.
