"""How mathematics is built up today from axiomatic set theory, per
00-the-map.qmd's second graph — distinct from the historical chain
(fig_historical_timeline.py) in both content and color: neutral gray here,
not blue, so the two chains aren't visually confused with each other, and
blue/categorical color stays reserved for the master map where hue actually
carries category meaning.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _theme import apply_theme, savefig, INK, MUTED, GRIDLINE

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

NODES = [
    "Logic",
    "Set theory\n(axioms)",
    "Relations",
    "Functions",
    "Numbers\n(constructed as sets)",
    "Algebraic structures\n(set + operations + axioms)",
    "Order / metric / topological\nstructures",
    "Limits, continuity,\nanalysis",
]

FILL = "#f2f1ee"
EDGE = MUTED


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

    last1 = c1[-1]
    first2 = c2[0]
    lx = last1[0] + last1[2] / 2
    fx = first2[0] + first2[2] / 2
    mid_y = (y1 + (y2 + box_h)) / 2

    ax.add_line(Line2D([lx, lx], [y1, mid_y], color=MUTED, linewidth=1.2))
    ax.add_line(Line2D([lx, fx], [mid_y, mid_y], color=MUTED, linewidth=1.2))
    arrow(ax, (fx, mid_y), (fx, y2 + box_h))

    ax.set_xlim(-0.1, x_start + 4 * (box_w + gap) + 0.3)
    ax.set_ylim(0.3, 4.1)
    ax.set_axis_off()
    ax.set_aspect("equal")

    savefig(fig, "formal-foundations.png")


if __name__ == "__main__":
    main()
