"""Widescreen banner (GitHub social preview slot, 1280x640, and link-preview
crops for Slack/LinkedIn/etc.) reusing fig_landscape_network.py's exact
graph data and layered-DAG layout, at smaller node/font scale.

Unlike modern-ai-systems-and-methods' equivalent script, this does *not*
switch to a spring layout for the banner: this site's graph is small and
sparse enough that spring_layout collapsed it into overlapping clusters
even for the main map (see fig_landscape_network.py's docstring), so
reusing that same failed layout here would reproduce the same bug at a
smaller, harder-to-notice size. The layered-DAG layout is comfortably wider
than tall (15 columns), which suits a widescreen banner: the axes are
stretched to fill the banner (no aspect="equal" letterboxing, which shrank
the graph to a thin strip with unreadable labels), and nodes are drawn as
point-sized markers so they stay circular at any aspect ratio.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _theme import apply_theme, CATEGORICAL, INK, MUTED, SURFACE
from fig_landscape_network import NODES, EDGES, PART_NAMES, compute_layers

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import FancyArrowPatch


def main() -> None:
    apply_theme()

    depth = compute_layers()
    by_layer: dict[int, list[str]] = {}
    for node, d in depth.items():
        by_layer.setdefault(d, []).append(node)

    col_gap, row_gap = 2.1, 1.55
    pos = {}
    for d, nodes_in_layer in by_layer.items():
        n = len(nodes_in_layer)
        for i, node in enumerate(nodes_in_layer):
            y = (i - (n - 1) / 2) * row_gap
            pos[node] = (d * col_gap, y)

    xs = [p[0] for p in pos.values()]
    ys = [p[1] for p in pos.values()]
    x_lo, x_hi = min(xs) - 1.05, max(xs) + 1.05
    y_lo, y_hi = min(ys) - 0.75, max(ys) + 0.75

    # 12.8 x 6.4in @ 200dpi = 2560x1280px, exactly 2x GitHub's recommended
    # 1280x640 social preview size (retina-sharp, GitHub downsamples).
    fig, ax = plt.subplots(figsize=(12.8, 6.4))
    fig.subplots_adjust(left=0.01, right=0.99, top=0.80, bottom=0.1)

    ax.set_xlim(x_lo, x_hi)
    ax.set_ylim(y_lo, y_hi)

    node_pt = 46          # node diameter in points (stays circular at any aspect)
    shrink = node_pt / 2 + 1

    for u, v in EDGES:
        pu, pv = pos[u], pos[v]
        later_edge = NODES[u][2] or NODES[v][2]
        arrow = FancyArrowPatch(
            pu, pv, connectionstyle="arc3,rad=0.08",
            arrowstyle="-", mutation_scale=10,
            linewidth=0.9, color=MUTED,
            alpha=0.6 if not later_edge else 0.4,
            linestyle="solid" if not later_edge else (0, (4, 3)),
            shrinkA=shrink, shrinkB=shrink,
            zorder=1,
        )
        ax.add_patch(arrow)

    legend_handles = []
    for part_idx, part_name in enumerate(PART_NAMES):
        color = CATEGORICAL[part_idx]
        for n, (label, part, later) in NODES.items():
            if part != part_idx:
                continue
            x, y = pos[n]
            if later:
                ax.scatter([x], [y], s=node_pt**2, facecolor=SURFACE, edgecolor=color,
                           linewidth=1.6, linestyle=(0, (3, 2)), zorder=2)
                text_color = color
            else:
                ax.scatter([x], [y], s=node_pt**2, facecolor=color, edgecolor=SURFACE,
                           linewidth=1.3, zorder=2)
                text_color = "white"
            ax.text(
                x, y, label, ha="center", va="center",
                fontsize=6.0, color=text_color,
                fontweight="bold" if not later else "normal",
                zorder=3, linespacing=1.1,
            )
        legend_handles.append(
            Line2D([0], [0], marker="o", linestyle="",
                   markerfacecolor=color, markeredgecolor=SURFACE,
                   markersize=9, label=part_name)
        )

    fig.text(
        0.02, 0.965, "Mathematics: From Computational Tools to Structure",
        fontsize=21, fontweight="700", color=INK, ha="left", va="top",
    )
    fig.text(
        0.02, 0.905,
        "A conceptual map of mathematics for people who already know how to use it",
        fontsize=11.5, color=MUTED, ha="left", va="top",
    )

    fig.legend(
        handles=legend_handles, loc="lower center", ncol=5,
        fontsize=8.5, frameon=False, labelcolor=MUTED,
        bbox_to_anchor=(0.5, 0.0), bbox_transform=fig.transFigure,
        columnspacing=1.2, handletextpad=0.5,
    )
    ax.set_axis_off()

    out = Path(__file__).resolve().parents[2] / "docs" / "images" / "social-preview.png"
    fig.savefig(str(out), dpi=200, facecolor=SURFACE, bbox_inches=None)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
