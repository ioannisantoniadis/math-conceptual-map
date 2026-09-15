# Figure scripts

Each `fig_*.py` script is a small, self-contained Python program that
computes a diagram and renders it to a static PNG in `docs/images/`. Quarto
does not execute Python at render time; these images are pre-generated and
checked into the repo like any other asset.

These replaced an earlier all-Mermaid version of `00-the-map.qmd`'s
diagrams: Mermaid's `flowchart TD` with subgraphs rendered with a near-black
subgraph fill that clashed against the site's light theme, and routed edges
outside their subgraph boundaries. See the module docstring at the top of
`fig_landscape_network.py` for the full account, including why a generic
force-directed layout (`networkx.spring_layout` / `kamada_kawai_layout`) was
tried and rejected in favor of a computed DAG longest-path layering.

Setup:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r scripts/figures/requirements.txt
```

Regenerate a single figure:

```bash
python3 scripts/figures/fig_landscape_network.py
```

Regenerate everything:

```bash
for f in scripts/figures/fig_*.py; do python3 "$f"; done
```

`fig_social_preview.py` is the odd one out: it renders the same graph as
`fig_landscape_network.py`, reusing that script's `NODES`/`EDGES`/
`compute_layers()` directly rather than duplicating the graph data, at a
fixed 2560x1280px (2x GitHub's recommended 1280x640) for use as the
README hero image and the repo's GitHub social-preview / link-preview
thumbnail. The fixed canvas size gives a smaller inches-per-data-unit than
`fig_landscape_network.py`'s data-derived figsize, so its node label font
size had to be scaled down separately to avoid overflowing the (same-size)
node circles — see that script's docstring and inline comment. GitHub's
social preview image itself has no public API for uploading; it's set once
by hand at Settings → General → Social preview, using this file.

Every script imports `apply_theme()` and the shared palette from `_theme.py`
so all figures across all chapters look like one system — new figure
scripts should do the same rather than styling matplotlib ad hoc. The
categorical palette in `_theme.py` is the validated instance from
Anthropic's `dataviz` skill reference palette (the same source
`../optimization-lab`'s `viz/theme.py` cites) — if you add or reorder
categorical colors, re-validate with that skill's
`scripts/validate_palette.js` before shipping.

After regenerating a figure, `quarto render docs` and actually look at the
output before considering the change done — see `CLAUDE.md`'s note on how
the Mermaid bug this pipeline replaced was originally caught.
