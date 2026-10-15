# Survival analysis lectures (Quarto slides)

Two lectures sharing one UCL theme. Each renders to reveal.js slides (a single self-contained
HTML file) and a 16:9 Beamer handout (PDF).

    quarto render Lecture1.qmd          # Lecture I: overall survival
    quarto render Lecture2.qmd          # Lecture II: relative (net) survival
    quarto preview Lecture2.qmd         # live preview while editing

Files
- `Lecture1.qmd`, `Lecture2.qmd` — the slides
- `ucl.scss` (HTML) and `beamer-ucl.tex` (PDF) — UCL theme (same as the STAT0008 slides)
- `gh-widget.html` — the interactive GH-structure sliders in Lecture II (plain JavaScript,
  works offline and when the HTML file is opened directly)
- `_filters/colour-spans.lua` — coloured text: [text]{.pop} (blue, population hazard),
  [text]{.exc} (red, excess hazard); also {.obs} / {.cens}
- `figures/` — UCL logo, censoring diagram, GH-structure plots (PDF version), BBC screenshot
- `_tools/` — scripts that redraw the figures (Python + matplotlib)
- `references.bib` — merged bibliography for both lectures

Maths macros are defined twice: in the hidden block on the first content slide (HTML) and in
`beamer-ucl.tex` (PDF). Keep them in sync.
