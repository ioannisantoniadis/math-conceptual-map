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

## Phase 4 — Discrete math, probability, optimization — **done**

- [x] `21-discrete-mathematics.qmd` — combinatorics reframed as counting
      specific families of subsets/functions already defined in
      `03-sets`/`04-relations-and-functions`; graph theory (a graph's edge
      set *is* a relation) with Euler's 1736 Königsberg bridges problem as
      shared ancestor of both graph theory and topology; recurrence
      relations named as the discrete sibling of `20-differential-equations`;
      mathematical induction introduced as a third proof technique alongside
      `02-logic-and-proof`'s direct proof and contradiction, justified via
      `06-number-systems`'s successor-based construction of $\mathbb{N}$;
      discrete-vs-continuous collected explicitly as its own recurring
      thread (discrete topology vs. standard, sums vs. integrals, recurrence
      relations vs. differential equations).
- [x] `22-probability.qmd` — probability space as measure theory
      instantiated (Kolmogorov, 1933, three centuries after Pascal/Fermat's
      gambling-motivated 1654 origins — another historical/formal gap for
      `00-the-map.qmd`'s collection); random variables reframed as ordinary
      functions $\Omega\to\mathbb{R}$, not "random numbers"; expectation
      shown to be literally `19-integration`'s integral, against $P$ instead
      of ordinary length; explicit about probability *not* being simply a
      branch of analysis (`SPEC.md` §13) — independence and Bayes' rule
      named as genuinely probabilistic questions measure theory alone
      doesn't ask.
- [x] `23-optimization.qmd` — critical points and the Hessian built directly
      on `18-differentiation`; Lagrange multipliers given a geometric
      reading via `14-inner-product-spaces`'s gradient-as-steepest-direction;
      convexity tied explicitly to `00-the-map.qmd`'s local-vs-global
      thread (every local min of a convex function is global); gradient
      descent assembled, in one place, from exactly the three chapters that
      built its pieces (inner product spaces, differentiation, differential
      equations' gradient flow) rather than introduced as a standalone
      algorithm.
- [x] New `_quarto.yml` part, "Discrete Math, Probability & Optimization,"
      added after "Analysis."
- [x] `fig_landscape_network.py`: three new solid Theories nodes (Discrete
      Mathematics, Probability, Optimization) with nine new edges reflecting
      dependencies actually discussed in the chapters (e.g. Optimization fed
      by Differentiation, Inner Product Spaces, Differential Equations, and
      Probability all four, matching the "assembled from three earlier
      chapters" framing above); Optimization also connects to Machine
      Learning. Regenerated cleanly at 24 nodes/35 edges with no overlap,
      confirming Phase 3's figsize-from-data-span fix holds as the graph
      keeps growing.
- [x] Forward references paid off in two already-published chapters:
      `20-differential-equations.qmd`'s closing paragraph (previously
      pointing at "a later phase" for all of Phase 4) now links the three
      real chapters directly; `18-differentiation.qmd`'s Taylor-approximation
      aside now links `23-optimization.qmd` instead of leaving it unlinked.

## Phase 5 — Mathematics of ML, advanced map, cross-connections — **done**

- [x] `24-machine-learning.qmd` — the ML bridge chapter promised at the end
      of `10-linear-algebra.qmd`, framed explicitly as an index rather than
      a new theory: embeddings ([Vector Spaces](docs/chapters/09-vector-spaces.qmd)),
      cosine similarity ([Inner Product Spaces](docs/chapters/14-inner-product-spaces.qmd)),
      a layer's $Wx+b$ as a literal affine map ([Affine
      Spaces](docs/chapters/15-affine-spaces.qmd) — a forward reference this
      structure chapter never actually had until now), backpropagation as
      the chain rule applied systematically
      ([Differentiation](docs/chapters/18-differentiation.qmd)), loss as
      negative log-likelihood ([Probability](docs/chapters/22-probability.qmd)),
      the manifold hypothesis paying off [Euclidean
      Geometry](docs/chapters/16-euclidean-geometry.qmd)'s one-paragraph
      manifold sketch, graph-structured data closing the loop to [Discrete
      Mathematics](docs/chapters/21-discrete-mathematics.qmd). Closes the
      exact `embedding_matrix @ x` example `00-the-map.qmd` opened this
      entire site with — that chapter's bottom-up reading path now starts
      from this one.
- [x] `25-advanced-topics.qmd` — functional analysis, measure theory,
      differential geometry, category theory, each given `SPEC.md` §21's
      prescribed treatment (problem, fundamental objects/structures, what
      it connects to, where to go next) rather than this site's usual
      depth — stated explicitly in the chapter's own opening, including
      that it's the one chapter that doesn't carry a single
      object/structure/theory tag, since it surveys four theories rather
      than building one. This is a deliberate, documented exception to
      the "non-negotiable discipline" in `CLAUDE.md`, not an oversight.
- [x] Cross-disciplinary consistency and link-integrity pass: every
      remaining "a later phase of this site" placeholder that Phase 5
      actually resolved was found (`grep -n "later phase"`) and repointed
      to a real chapter — in `09-vector-spaces`, `10-linear-algebra`,
      `16-euclidean-geometry` (twice), `19-integration` (twice),
      `20-differential-equations`, `21-discrete-mathematics`,
      `22-probability`, and `23-optimization`'s closing paragraph, which
      had been the single explicit list of everything this phase needed to
      cover. Two placeholders were deliberately left alone because Phase 5
      never covered them (topology's connectedness/compactness in
      `13-topological-spaces`; PDEs in `20-differential-equations`) — both
      genuinely still open, not missed. Full-site link-integrity, stale-
      chapter-number, and orphan-chapter (no inbound links) checks all
      passed clean at 25 chapters / 51 cross-reference targets.
- [x] New `_quarto.yml` parts, "Applications" and "Advanced Topics," added
      after "Discrete Math, Probability & Optimization."
- [x] `fig_landscape_network.py`: Machine Learning moved from hollow to
      solid; a new solid Advanced Topics node added, fed by What Is a
      Structure? (category theory generalizes its homomorphism pattern),
      Inner Product Spaces (functional analysis), Probability (measure
      theory), Euclidean Geometry (differential geometry), and Machine
      Learning. Physics is now the map's only remaining hollow node.
      `fig_social_preview.py` regenerated automatically from the same data
      (no code changes needed — it imports `NODES`/`EDGES` directly).

## Post-Phase-5 spec audit — **done**

A full walkthrough of `SPEC.md` §1–26 against the finished site, requested
after Phase 5, found four real gaps (not documented deviations — actual
misses) and fixed all four:

- [x] §10's ML bridge tree names Information Theory as a peer to Linear
      Algebra/Analysis/Optimization/Probability/Geometry; `24-machine-learning.qmd`
      had none of it. Added a section deriving entropy, KL divergence, and
      mutual information as [Probability](docs/chapters/22-probability.qmd)
      expectations, and showing cross-entropy loss (already in the chapter)
      *is* a KL divergence in different notation, not a third idea.
- [x] §9.5's "Approximation" theme was never named as one of `00-the-map.qmd`'s
      recurring threads, despite every piece of it (Taylor approximation,
      Euler's method, gradient descent) already existing scattered across
      later chapters. Added as a sixth thread, collecting them.
- [x] §15's "If you've done X" sections were missing from exactly the areas
      `SPEC.md` names explicitly: differentiation, integration, differential
      equations, probability, and optimization each got one; machine
      learning got a closing "If you've trained a model" section
      consolidating the whole chapter's translations in the format `SPEC.md`'s
      own $A\vec{x}=\vec{b}$ example uses. `CLAUDE.md` gained a standing rule
      so this can't quietly regress again the way it just did.
- [x] §18's "What Changed" comparison tables existed in exactly one place
      (`07-mathematical-structures.qmd`); `SPEC.md` asks for the pattern
      reused, not literally everywhere. Added two more at spots where the
      prose was already narrating a gained/lost or discrete/continuous
      pairing a table just makes scannable: a Gained/Lost table in
      `06-number-systems.qmd`, a Discrete/Continuous table in
      `21-discrete-mathematics.qmd`. Deliberately not added everywhere —
      `CLAUDE.md` records the "does this spot deserve one" heuristic instead
      of a rule to apply it universally.

Two items remain genuinely, permanently unsatisfied relative to `SPEC.md`'s
literal text, both already logged as deliberate — see `CLAUDE.md`'s
"Structure" and "Content conventions" sections: §19's glossary uses a
compact one-line-plus-link format rather than the spec's 5-part
(intuition/definition/examples/related/map-location) structure per term,
matching sibling-repo convention; §4's `CONTRIBUTING.md` was never created,
also matching that neither sibling repo has one.

## `appendix-classification.qmd` — **done**

User feedback after reviewing the master map: it only shows one node in
the Objects category (Number Systems), which read as the map being
incomplete rather than as the deliberate one-node-per-*chapter* convention
it actually is — most objects (a vector, a matrix, a random variable) are
discussed inside a structure or theory chapter rather than getting a page
of their own, so they never became their own node. A second graph at
concept granularity was considered and rejected: at ~65-70 glossary-level
concepts, the edges would reproduce the exact illegible-clutter problem the
Mermaid replacement (see the Phase 1 entry above) was built to avoid. Built
a table instead — every glossary term reclassified into the map's own five
categories (Foundations/Objects/Structures/Theories/Applications), with a
**Notes** column carrying the terms that don't cleanly fit one of the four
non-Foundations boxes (properties like convex/bijective, maps like
homomorphism/linear map, theorems like Bayes' rule) rather than forcing a
bad fit. Reuses existing glossary content entirely — no new mathematical
exposition, per the user's explicit "don't add more content" steer.
Cross-linked from the glossary and from `07-mathematical-structures.qmd`.

## Non-goals

Not a textbook substitute, not proof-heavy, not attempting exhaustive
coverage of any single field (`SPEC.md` §21's "conceptual coverage rather
than exhaustive coverage"). Not re-teaching computation the target reader
already has. Not a strict hierarchy — cross-links deliberately point to more
than one "parent" chapter where the mathematics genuinely does.
