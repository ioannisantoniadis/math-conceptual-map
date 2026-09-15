"""When each idea in 00-the-map.qmd's comparison first appeared, roughly.

A wrapped two-row chain rather than one 8-box row: eight boxes in a single
row at readable font size doesn't fit a normal page width, which is exactly
what went wrong with the Mermaid version this replaces (illegibly squeezed
boxes). Single-hue (not categorical) fill, since this is one sequence, not
several groups needing to be told apart.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _theme import apply_theme, savefig, CATEGORICAL, INK, MUTED, SURFACE

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

NODES = [
    "Arithmetic & geometry\n(antiquity)",
    "Algebra\nal-Khwārizmī, 9th c.;\nsymbolic algebra, 16th–17th c.",
    "Calculus\nNewton/Leibniz, 1660s–80s\n(informal infinitesimals)",
    "Rigorous analysis\nCauchy 1820s, Weierstrass 1870s\n(ε–δ limits)",
    "Set theory\nCantor, 1870s–80s",
    "Formal axiomatic foundations\nFrege, Peano, Zermelo–Fraenkel\n~1889–1922",
    "Abstract algebra\nformal group axioms:\nCayley 1854, Weber 1893",
    "Topology as a formal object\nHausdorff, 1914",
]

FILL = "#eaf1fb"  # light tint of categorical slot 1
EDGE = CATEGORICAL[0]


def draw_row(ax, nodes, y, x_start, box_w, box_h, gap):
    centers = []
    for i, label in enumerate(nodes):
        x = x_start + i * (box_w + gap)
        box = FancyBboxPatch(
            (x, y), box_w, box_h,
            boxstyle="round,pad=0.02,rounding_size=0.06",
            linewidth=1.3, facecolor=FILL, edgecolor=EDGE,
        )
        ax.add_patch(box)
        ax.text(
            x + box_w / 2, y + box_h / 2, label,
            ha="center", va="center", fontsize=7.6, color=INK, linespacing=1.35,
        )
        centers.append((x, y, box_w, box_h))
    return centers


def arrow(ax, p0, p1):
    ax.add_patch(FancyArrowPatch(
        p0, p1, arrowstyle="-|>", mutation_scale=12,
        linewidth=1.2, color=MUTED, shrinkA=2, shrinkB=2,
    ))


def main() -> None:
    apply_theme()
    fig, ax = plt.subplots(figsize=(11, 4.6))

    box_w, box_h, gap = 2.3, 1.15, 0.4
    row1 = NODES[:4]
    row2 = NODES[4:]

    y1, y2 = 2.7, 0.6
    x_start = 0.2

    c1 = draw_row(ax, row1, y1, x_start, box_w, box_h, gap)
    c2 = draw_row(ax, row2, y2, x_start, box_w, box_h, gap)

    for a, b in zip(c1, c1[1:]):
        arrow(ax, (a[0] + a[2], a[1] + a[3] / 2), (b[0], b[1] + b[3] / 2))
    for a, b in zip(c2, c2[1:]):
        arrow(ax, (a[0] + a[2], a[1] + a[3] / 2), (b[0], b[1] + b[3] / 2))

    # row1 end -> row2 start, routed entirely through the whitespace gap
    # between the two rows (not through row2's boxes, which is what a
    # naive corner-to-corner arrow would cross).
    last1 = c1[-1]
    first2 = c2[0]
    lx = last1[0] + last1[2] / 2       # x-center of last row-1 box
    fx = first2[0] + first2[2] / 2     # x-center of first row-2 box
    mid_y = (y1 + (y2 + box_h)) / 2    # a y strictly between the two rows

    ax.add_line(Line2D([lx, lx], [y1, mid_y], color=MUTED, linewidth=1.2))
    ax.add_line(Line2D([lx, fx], [mid_y, mid_y], color=MUTED, linewidth=1.2))
    arrow(ax, (fx, mid_y), (fx, y2 + box_h))

    ax.set_xlim(-0.1, x_start + 4 * (box_w + gap) + 0.3)
    ax.set_ylim(0.3, 4.1)
    ax.set_axis_off()
    ax.set_aspect("equal")

    savefig(fig, "historical-timeline.png")


if __name__ == "__main__":
    main()
