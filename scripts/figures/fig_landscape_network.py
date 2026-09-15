"""The master map: a computed layered-DAG layout of this site's graph,
replacing the Mermaid subgraph+labeled-edges diagram that rendered with a
near-black subgraph fill clashing against the site's light theme and edges
routed outside their subgraph boxes.

A generic force-directed spring layout was tried first and rejected: this
graph is small and nearly tree-shaped (long, sparsely-branching chains), and
neither spring_layout nor kamada_kawai_layout account for node size, so both
collapsed entire chains into overlapping node clusters instead of spacing
them out — a real failure mode of those algorithms on sparse/path-like
graphs, not a styling issue. What this graph actually calls for is a
longest-path layering (a small Sugiyama-style DAG layout, computed below via
topological sort), which places every node by its real graph-theoretic depth
rather than by hand-placed coordinates or by a force simulation not suited
to this graph's shape.

Node color marks the part a chapter belongs to (matching docs/_quarto.yml);
hollow, dashed-border nodes are planned chapters that don't exist yet. Edge
direction (arrowheads) shows the "prerequisite for / generalizes to / used
in" relationships the chapter prose names explicitly — this figure
intentionally does not also put a text label on every edge, which is what
made the Mermaid version unreadable at this node count.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _theme import apply_theme, savefig, CATEGORICAL, INK, MUTED, SURFACE

import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.lines import Line2D
from matplotlib.patches import FancyArrowPatch

# node -> (label, part index, is_later)
NODES = {
    "L":   ("Logic &\nProof", 0, False),
    "S":   ("Sets", 0, False),
    "RF":  ("Relations &\nFunctions", 0, False),
    "AD":  ("Axioms &\nDefinitions", 0, False),
    "N":   ("Number\nSystems", 1, False),
    "MS":  ("What Is a\nStructure?", 2, False),
    "G":   ("Groups", 2, False),
    "VS":  ("Vector\nSpaces", 2, False),
    "MET": ("Metric\nSpaces", 2, True),
    "TOP": ("Topological\nSpaces", 2, True),
    "LA":  ("Linear\nAlgebra", 3, False),
    "AA":  ("Abstract\nAlgebra", 3, True),
    "AN":  ("Analysis", 3, True),
    "ML":  ("Machine\nLearning", 4, True),
    "PHY": ("Physics", 4, True),
}

EDGES = [
    ("L", "S"), ("S", "RF"), ("RF", "AD"), ("RF", "N"), ("N", "MS"),
    ("MS", "G"), ("MS", "VS"), ("G", "AA"),
    ("VS", "LA"), ("VS", "MET"), ("MET", "TOP"),
    ("LA", "ML"), ("LA", "PHY"), ("AN", "RF"),
]

# AN -> RF is a deliberate "built on" back-reference (Analysis reuses
# Relations & Functions), not a forward dependency — for *layering only* it
# is treated as RF -> AN so Analysis is placed after RF, then drawn with its
# real (reversed, dashed) arrow direction below.
LAYERING_EDGES = [(u, v) if (u, v) != ("AN", "RF") else ("RF", "AN") for u, v in EDGES]

PART_NAMES = ["Foundations", "Objects", "Structures", "Theories", "Applications"]


def compute_layers() -> dict:
    dag = nx.DiGraph()
    dag.add_nodes_from(NODES)
    dag.add_edges_from(LAYERING_EDGES)
    depth = {}
    for node in nx.topological_sort(dag):
        preds = list(dag.predecessors(node))
        depth[node] = 0 if not preds else max(depth[p] for p in preds) + 1
    return depth


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

    g = nx.DiGraph()
    g.add_nodes_from(NODES)
    g.add_edges_from(EDGES)

    fig, ax = plt.subplots(figsize=(13, 6.5))
    fig.subplots_adjust(top=0.86, bottom=0.14, left=0.02, right=0.98)

    xs = [p[0] for p in pos.values()]
    ys = [p[1] for p in pos.values()]
    ax.set_xlim(min(xs) - 1.1, max(xs) + 1.1)
    ax.set_ylim(min(ys) - 1.0, max(ys) + 1.0)

    radius = 0.62

    # Edges first, so nodes draw on top of the arrow tails/heads.
    for u, v in g.edges():
        pu, pv = pos[u], pos[v]
        later_edge = NODES[u][2] or NODES[v][2]
        back_edge = (u, v) == ("AN", "RF")
        rad = -0.25 if back_edge else 0.08
        arrow = FancyArrowPatch(
            pu, pv, connectionstyle=f"arc3,rad={rad}",
            arrowstyle="-|>", mutation_scale=14,
            linewidth=1.1, color=MUTED,
            alpha=0.85 if not later_edge else 0.55,
            linestyle="solid" if not later_edge else (0, (4, 3)),
            shrinkA=17, shrinkB=17,
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
                circ = plt.Circle(
                    (x, y), radius, facecolor=SURFACE, edgecolor=color,
                    linewidth=1.8, linestyle=(0, (3, 2)), zorder=2,
                )
                text_color = color
            else:
                circ = plt.Circle(
                    (x, y), radius, facecolor=color, edgecolor=SURFACE,
                    linewidth=1.6, zorder=2,
                )
                text_color = "white"
            ax.add_patch(circ)
            ax.text(
                x, y, label, ha="center", va="center",
                fontsize=7.6, color=text_color,
                fontweight="bold" if not later else "normal",
                zorder=3, linespacing=1.2,
            )
        legend_handles.append(
            Line2D([0], [0], marker="o", linestyle="",
                   markerfacecolor=color, markeredgecolor=SURFACE,
                   markersize=11, label=part_name)
        )

    legend_handles.append(
        Line2D([0], [0], marker="o", linestyle="", markerfacecolor=SURFACE,
               markeredgecolor=MUTED, markeredgewidth=1.6, markersize=11,
               label="planned, not yet written")
    )

    ax.set_title(
        "This site's graph — layered by longest conceptual-prerequisite path,\n"
        "color marks which part a chapter belongs to, hollow = planned",
        fontsize=12.5, color=INK, pad=14,
    )
    fig.legend(
        handles=legend_handles, loc="lower center", ncol=6,
        fontsize=9, frameon=False, labelcolor=MUTED,
        bbox_to_anchor=(0.5, 0.0), bbox_transform=fig.transFigure,
        columnspacing=1.3, handletextpad=0.5, handlelength=1.1,
    )
    ax.set_axis_off()
    ax.set_aspect("equal")

    savefig(fig, "landscape-network.png")


if __name__ == "__main__":
    main()
