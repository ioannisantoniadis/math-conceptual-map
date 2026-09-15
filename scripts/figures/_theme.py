"""Shared matplotlib theme for this site's figures.

Colors are the validated categorical palette from Anthropic's `dataviz` skill
reference instance (the same source `../optimization-lab`'s viz/theme.py
cites) — slots 1-5, checked with `validate_palette.js --mode light`
(adjacent-pairs mode; every node in this site's diagrams carries a direct
text label plus a legend, so the labeled-marks adjacent-pairs gate applies,
not the unlabeled-scatter all-pairs one). Ink/surface/gridline values match
docs/theme.scss so the site chrome and the embedded static figures read as
one system.
"""

import matplotlib.pyplot as plt
from pathlib import Path

# Fixed order — never cycle or reassign per figure.
CATEGORICAL = [
    "#2a78d6",  # 1 blue       — Foundations
    "#eb6834",  # 2 orange     — Objects
    "#1baf7a",  # 3 aqua       — Structures
    "#eda100",  # 4 yellow     — Theories
    "#e87ba4",  # 5 magenta    — Applications
]

SURFACE = "#fcfcfb"
INK = "#0b0b0b"
MUTED = "#52514e"
FAINT = "#898781"
GRIDLINE = "#e1e0d9"


def apply_theme() -> None:
    plt.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": ["Helvetica Neue", "Arial", "sans-serif"],
        "figure.facecolor": SURFACE,
        "axes.facecolor": SURFACE,
        "savefig.facecolor": SURFACE,
        "text.color": INK,
        "axes.edgecolor": GRIDLINE,
        "axes.labelcolor": MUTED,
        "xtick.color": MUTED,
        "ytick.color": MUTED,
    })


def savefig(fig, relative_path: str, dpi: int = 200) -> Path:
    out = Path(__file__).resolve().parents[2] / "docs" / "images" / relative_path
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(str(out), dpi=dpi, facecolor=SURFACE, bbox_inches="tight", pad_inches=0.15)
    print(f"wrote {out}")
    return out
