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
    "RNG": ("Rings &\nFields", 2, False),
    "VS":  ("Vector\nSpaces", 2, False),
    "IPS": ("Inner Product\nSpaces", 2, False),
    "MET": ("Metric\nSpaces", 2, False),
    "TOP": ("Topological\nSpaces", 2, False),
    "AFF": ("Affine\nSpaces", 2, False),
    "LA":  ("Linear\nAlgebra", 3, False),
    "EG":  ("Euclidean\nGeometry", 3, False),
    "LC":  ("Limits &\nContinuity", 3, False),
    "DIFF": ("Differentiation", 3, False),
    "INT": ("Integration", 3, False),
    "DE":  ("Differential\nEquations", 3, False),
    "DISC": ("Discrete\nMathematics", 3, False),
    "PROB": ("Probability", 3, False),
    "OPT": ("Optimization", 3, False),
    "ADV": ("Advanced\nTopics", 3, False),
    "ML":  ("Machine\nLearning", 4, False),
    "PHY": ("Physics", 4, True),
}

EDGES = [
    ("L", "S"), ("S", "RF"), ("RF", "AD"), ("RF", "N"), ("N", "MS"),
    ("MS", "G"), ("MS", "RNG"), ("MS", "VS"), ("G", "RNG"),
    ("VS", "LA"), ("VS", "IPS"), ("VS", "AFF"), ("IPS", "MET"), ("MET", "TOP"),
    ("IPS", "EG"), ("AFF", "EG"),
    ("TOP", "LC"), ("LC", "DIFF"), ("LA", "DIFF"), ("DIFF", "INT"),
    ("DIFF", "DE"), ("INT", "DE"), ("DE", "PHY"), ("DE", "ML"),
    ("LA", "ML"), ("LA", "PHY"),
    ("N", "DISC"), ("TOP", "DISC"), ("INT", "PROB"), ("DISC", "PROB"),
    ("DIFF", "OPT"), ("IPS", "OPT"), ("DE", "OPT"), ("PROB", "OPT"), ("OPT", "ML"),
    ("MS", "ADV"), ("IPS", "ADV"), ("PROB", "ADV"), ("EG", "ADV"), ("ML", "ADV"),
]

# Every edge here is a genuine forward dependency (no "built on" back-
# references at present), so layering uses EDGES directly.
LAYERING_EDGES = EDGES

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

    xs = [p[0] for p in pos.values()]
    ys = [p[1] for p in pos.values()]
    x_lo, x_hi = min(xs) - 1.1, max(xs) + 1.1
    y_lo, y_hi = min(ys) - 1.0, max(ys) + 1.0

    # figsize is derived from the actual data span (fixed inches-per-data-unit,
    # matching aspect="equal" below) rather than a constant — this graph has
    # grown from 8 to 14 layers across three rounds of edits, and a *fixed*
    # figsize at a wider graph is exactly what caused nodes to overlap and
    # clip each other's labels the first time this ran after Phase 3 added
    # four more layers: same physical width stretched over more data units
    # shrinks every node's effective on-page size. Scaling both figure
    # dimensions off the data span keeps node size and spacing constant
    # regardless of how many chapters the map grows to.
    scale = 0.62  # inches per data unit
    fig_w = (x_hi - x_lo) * scale
    fig_h = (y_hi - y_lo) * scale + 2.0  # +2in flat, for title + legend

    fig, ax = plt.subplots(figsize=(fig_w, fig_h))
    top_in, bottom_in = 0.9, 1.1
    fig.subplots_adjust(
        top=1 - top_in / fig_h, bottom=bottom_in / fig_h, left=0.02, right=0.98,
    )

    ax.set_xlim(x_lo, x_hi)
    ax.set_ylim(y_lo, y_hi)

    radius = 0.62

    # Edges first, so nodes draw on top of the arrow tails/heads.
    for u, v in g.edges():
        pu, pv = pos[u], pos[v]
        later_edge = NODES[u][2] or NODES[v][2]
        arrow = FancyArrowPatch(
            pu, pv, connectionstyle="arc3,rad=0.08",
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
