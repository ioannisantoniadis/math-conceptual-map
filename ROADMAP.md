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

## Phase 2 — Algebra, geometry, metric spaces, topology — planned

- [ ] Abstract algebra beyond groups: rings, fields (formal treatment —
      Phase 1's `06-number-systems` used "field" informally), homomorphisms
      developed in depth.
- [ ] Geometry: Euclidean geometry's axiomatic history, coordinates,
      affine spaces, a first pass at manifolds.
- [ ] Metric spaces and topological spaces — both previewed in Phase 1's
      `07-mathematical-structures` comparison table and referenced from
      `09-vector-spaces`'s "what a vector space is NOT" section; this is
      where those forward references get paid off.
- [ ] Update `00-the-map.qmd`'s master diagram: move the Phase 2 nodes from
      dashed/"later" to solid, add their real edges.
- [ ] Consider starting a `scripts/figures/` computed-diagram pipeline
      (matching `../modern-ai-systems-and-methods`'s pattern) once the map
      has enough nodes for a force-directed layout to show real structure —
      not worth it at Phase 1's node count.

## Phase 3 — Analysis, calculus, differential equations — planned

- [ ] Limits, continuity, differentiation, integration named as *theory*,
      not recomputed — explicitly building on Phase 1's numbers/functions
      chapters and Phase 2's topology.
- [ ] Real analysis as the rigorous foundation calculus was historically
      invented two centuries before, closing the loop `00-the-map.qmd`
      opened with that exact example.
- [ ] Differential equations: what one *is* mathematically (a statement
      about a function via its derivatives), ODEs vs. PDEs, dynamical
      systems.

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
