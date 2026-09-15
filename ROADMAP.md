# Roadmap

Phased plan following `SPEC.md` §23, adapted after scaffolding: Phase 1 was
extended to include a full arc through linear algebra (not just foundations
and numbers) so the MVP demonstrates the whole problem → abstraction →
consequence pattern once, end to end, rather than stopping mid-argument.
Each phase should leave the site in a complete, cross-linked, non-stub state
— no chapter published ahead of the ones it depends on.

## Phase 1 — Foundational spine (logic → linear algebra) — **done**

- [x] Repo scaffolded as a Quarto book, matching `../optimization-lab` and
      `../modern-ai-systems-and-methods`'s conventions: flat
      `docs/chapters/NN-slug.qmd`, grouped by `part:` in `_quarto.yml`
      rather than `SPEC.md`'s originally-suggested nested per-discipline
      folders. GitHub Pages deploy via `.github/workflows/docs.yml`, on
      push to `main` when `docs/**` changes. Decided during scaffolding,
      not from `SPEC.md` itself — see `CLAUDE.md`.
- [x] The four-graph model (historical / formal-foundations / conceptual /
      pedagogical) established as the site's core discipline in
      `docs/chapters/00-the-map.qmd`, including a comparison table (Sets,
      Groups, Vector spaces, Limits/calculus) making the gaps between the
      four orderings concrete rather than asserted.
- [x] Master Mermaid map (`00-the-map.qmd`) covering the MVP's nodes plus
      lighter/dashed nodes for planned-but-unwritten structures and
      theories, so the graph's shape is visible before every node exists.
- [x] Foundations: `01-what-is-mathematics`, `02-logic-and-proof`,
      `03-sets` (including Russell's paradox as the motivating reason naive
      set theory needed axiomatizing), `04-relations-and-functions`,
      `05-axioms-and-definitions` (the meta step-back on what "axiom" and
      "definition" mean, deliberately placed *after* the reader has seen
      concrete examples of both, not before).
- [x] Objects: `06-number-systems` — $\mathbb{N} \to \mathbb{Z} \to
      \mathbb{Q} \to \mathbb{R} \to \mathbb{C}$ as a chain of "what problem
      forced this extension, what was gained, what was lost" rather than a
      list to memorize.
- [x] Structures: `07-mathematical-structures` (the object/structure/
      theory/application distinction made explicit, inserted between
      Numbers and Groups per the reasoning in the planning conversation —
      not in `SPEC.md`'s literal suggested walkthrough order, but listed in
      its suggested file tree), `08-groups`, `09-vector-spaces` (the
      spec's flagship template example — four genuinely different
      motivating examples before the axioms, then what breaks without each
      axiom).
- [x] Theories: `10-linear-algebra` — linear maps, matrices as coordinate
      representations of maps (not the maps themselves), eigenvalues as an
      instance of the invariance theme, and an explicit "why ML cares"
      closing bridge.
- [x] `appendix-glossary.qmd` seeded with ~24 terms introduced across Phase
      1; `appendix-references.qmd` states the sourcing policy (MacTutor →
      SEP → primary sources → textbooks) without yet accumulating a real
      bibliography, per `SPEC.md` §7's explicit instruction not to.
- [x] Content voice decided as flowing narrative prose (matching sibling
      repos), not `SPEC.md` §6's literal numbered template — a deliberate
      departure, recorded in `CLAUDE.md` so it isn't silently reverted.
- [x] GitHub repo created (public, `ioannisantoniadis/math-conceptual-map`),
      pushed, GitHub Pages wired to the Actions workflow, topics added. Live
      site and workflow run both confirmed, not just assumed from a
      green-looking config.
- [x] `00-the-map.qmd`'s three Mermaid diagrams replaced with computed
      static figures (`scripts/figures/`) after the live page showed the
      master map rendering with a near-black subgraph fill and edges routed
      outside subgraph boxes — a real defect, caught by actually
      screenshotting the deployed page, not by re-reading the source. This
      pulls forward what was originally planned as a Phase 2 "maybe" (see
      the removed bullet below); a generic force-directed layout was tried
      first (`spring_layout`, then `kamada_kawai_layout`) and both collapsed
      this graph's sparse chains into overlapping nodes, so the master map
      uses a computed longest-path DAG layering instead — see
      `fig_landscape_network.py`'s docstring.

## Phase 2 — Algebra, geometry, metric spaces, topology — **done**

- [x] Abstract algebra beyond groups: `11-rings-and-fields.qmd` — rings and
      fields with real axioms (formalizing "field," used informally by
      Phase 1's `06-number-systems` and `09-vector-spaces`), distributivity
      motivated by what breaks without it, zero divisors as the
      non-$\mathbb{Z}$ way a ring can fail to be a field. Ring/field
      homomorphisms named but not developed in depth — full treatment (and
      any dedicated abstract-algebra theory chapter beyond this structure
      one) still open.
- [x] Metric spaces and topological spaces — `12-metric-spaces.qmd` and
      `13-topological-spaces.qmd`, paying off the forward references from
      Phase 1's `07-mathematical-structures` comparison table and
      `09-vector-spaces`'s "what a vector space is NOT" section (both
      chapters' tables/links updated to point at real chapters instead of
      "later").
- [x] Inner product spaces — `14-inner-product-spaces.qmd`, formalizing the
      norm `12-metric-spaces.qmd` originally left informal (that chapter's
      own text updated to cite this one instead of the "not yet
      axiomatized" caveat). Covers norm, Cauchy–Schwarz, orthogonality, and
      the parallelogram-law test for whether a norm comes from an inner
      product; treats "normed space" as the midpoint of that generalization
      ladder rather than as its own chapter, deliberately.
- [x] Geometry: `15-affine-spaces.qmd` (points vs. vectors, affine
      combinations requiring weights to sum to 1, affine maps as "linear
      map + translation") and `16-euclidean-geometry.qmd` (Euclid's
      postulates and the two-thousand-year parallel-postulate history,
      Descartes's coordinates, Euclidean space redefined as an affine space
      whose displacements carry an inner product, a deliberately
      one-paragraph "first pass" at manifolds per this bullet's original
      scope). Both new chapters keep the object/structure/theory tag
      discipline clean — affine spaces and inner product spaces are
      *structures*, Euclidean geometry is a *theory* built from them, not
      one chapter blurring both levels.
- [x] `_quarto.yml` reordered: Structures part now reads
      Groups → Rings and Fields → Vector Spaces → Inner Product Spaces →
      Metric Spaces → Topological Spaces → Affine Spaces; Theories part
      reads Linear Algebra → Euclidean Geometry. Filenames stayed
      sequential-by-creation-order rather than being renumbered to match, to
      avoid renaming already-published/cross-linked files; see `CLAUDE.md`.
- [x] `fig_landscape_network.py`'s `NODES`/`EDGES` updated and regenerated
      each time a structure/theory above landed: Rings & Fields, Inner
      Product Spaces, Affine Spaces, Metric Spaces, and Topological Spaces
      are all solid now; Euclidean Geometry added as a solid Theories node
      fed by both Affine Spaces and Inner Product Spaces. Analysis, Machine
      Learning, and Physics remain hollow.

## Phase 3 — Analysis, calculus, differential equations — **done**

- [x] `17-limits-and-continuity.qmd` — limits and continuity named as
      *theory*, not recomputed, built explicitly on Phase 2's
      `12-metric-spaces`/`13-topological-spaces` (the $\varepsilon$–$\delta$
      definition shown to be the metric-space convergence definition
      specialized to $\mathbb{R}$, not new machinery). Real analysis framed
      as the rigorous foundation calculus was historically invented ~150
      years before (Newton/Leibniz 1660s–80s vs. Cauchy/Weierstrass
      1820s–70s), closing the loop `00-the-map.qmd` opened with that exact
      example in its historical-timeline figure; a brief, explicitly
      simplified aside on Robinson's 1960s nonstandard analysis notes the
      original infinitesimal intuition was eventually vindicated on
      different foundations.
- [x] `18-differentiation.qmd` — the derivative reframed as the best local
      linear approximation, an explicit $1\times1$ instance of
      `10-linear-algebra`'s linear maps, so that Jacobians/gradients/
      Hessians read as the same construction at higher order rather than as
      separate ad hoc rules. Weierstrass's continuous-nowhere-differentiable
      function (1872) as the historical shock underlining
      differentiability's a strictly stronger demand than continuity.
- [x] `19-integration.qmd` — Riemann sums, the fundamental theorem of
      calculus emphasized as a genuinely non-obvious unification (not a
      restated definition) of two unrelated-looking constructions, standard
      integration techniques reframed as differentiation rules run
      backwards. Lebesgue integration and improper integrals flagged and
      deferred, not developed.
- [x] `20-differential-equations.qmd` — what a differential equation *is*
      mathematically (an equation whose unknown is a function, not a
      number), ODEs vs. PDEs, order and linearity, why closed-form solutions
      are the exception rather than the rule, dynamical systems as
      "study the shape, not the formula." Closes with gradient descent as a
      discretized gradient flow, tying directly back to
      `10-linear-algebra`'s ML closing paragraph.
- [x] New `_quarto.yml` part, "Analysis," added after "Theories" for these
      four chapters.
- [x] `fig_landscape_network.py`: the old hollow "Analysis" placeholder node
      (and its one back-reference edge) removed entirely, replaced by four
      real solid nodes (Limits & Continuity, Differentiation, Integration,
      Differential Equations) with real forward edges, including
      Differentiation citing Linear Algebra as a direct prerequisite.
      Regenerating after this edit **overlapped every node's label** — figsize
      had been a fixed constant since Phase 1, and the graph had grown from
      8 to 14 layers across three rounds of edits without anyone revisiting
      that constant; fixed by deriving figsize from the actual data span
      (see the script's docstring) so this doesn't recur as the map keeps
      growing. Caught by actually rendering and looking, per this project's
      own stated norm — not assumed correct from the diff.
- [x] Three stale hardcoded "chapter N" references in `00-the-map.qmd` (from
      before Phase 2 reordered the TOC) caught and fixed while updating that
      chapter's forward references; `CLAUDE.md` gained a rule against ever
      hardcoding a chapter number in prose again.

## Phase 4 — Discrete math, probability, optimization — planned

- [ ] Discrete mathematics: combinatorics, graph theory, discrete vs.
      continuous as its own named theme.
- [ ] Probability as measure theory instantiated — probability space,
      random variables, expectation — explicit about probability *not*
      being simply a branch of analysis (`SPEC.md` §13).
- [ ] Optimization: unconstrained/constrained, convexity, and the
      calculus + linear algebra dependencies made explicit.

## Phase 5 — Mathematics of ML, advanced map, cross-connections — planned

- [ ] The ML bridge chapter promised at the end of `10-linear-algebra.qmd`:
      embeddings, gradients/Jacobians/Hessians, optimization, probability,
      and high-dimensional geometry, each traced back to the theory chapter
      it actually lives in.
- [ ] Advanced-topics overview pass: functional analysis, measure theory,
      differential geometry, category theory — conceptual coverage only
      (`SPEC.md` §21), not full treatments.
- [ ] A cross-disciplinary consistency and link-integrity pass across the
      whole site.

## Non-goals

Not a textbook substitute, not proof-heavy, not attempting exhaustive
coverage of any single field (`SPEC.md` §21's "conceptual coverage rather
than exhaustive coverage"). Not re-teaching computation the target reader
already has. Not a strict hierarchy — cross-links deliberately point to more
than one "parent" chapter where the mathematics genuinely does.
