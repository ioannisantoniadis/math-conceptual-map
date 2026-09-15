# math-conceptual-map — context for AI assistants

## What this is

A Quarto-book documentation site (no code package — this is a pure-content
repo, unlike its siblings `optimization-lab` and
`modern-ai-systems-and-methods`) reconstructing the conceptual architecture
of mathematics for readers who are computationally fluent (calculus, linear
algebra, probability, ML) but lack a structural mental model of what
mathematical objects, structures, and theories actually are and how they
relate. Full brief: `SPEC.md`. Full agreed architecture and rationale:
whatever conversation produced this repo — `ROADMAP.md`'s phase entries are
the durable record of decisions made, going forward.

- **Docs site**: https://ioannisantoniadis.github.io/math-conceptual-map/
  (auto-deployed to GitHub Pages on push to `main` via
  `.github/workflows/docs.yml`, only when `docs/**` changed)

## The non-negotiable discipline

Two rules from `SPEC.md` shape every chapter and are easy to violate by
accident:

1. **Four graphs, never merged.** Historical development (when an idea
   appeared), formal/logical foundations (how it's built from ZFC-level
   primitives today), conceptual dependency (what you need to *understand*
   it), and pedagogical ordering (the sequence that motivates it best) are
   four different orderings over the same ideas, and they disagree often
   (calculus predates the real-analysis foundations it now formally rests
   on by ~200 years; sets are historically recent but conceptually almost
   free). [`docs/chapters/00-the-map.qmd`](docs/chapters/00-the-map.qmd) is
   the canonical statement of this; every chapter that makes a historical
   claim should be checked against it before being taken as an implicit
   dependency claim, and vice versa.
2. **Object / structure / theory / application, kept explicit.** A specific
   thing (a matrix) vs. a pattern it carries (vector space) vs. the body of
   results about that pattern (linear algebra) vs. a domain borrowing the
   theory (ML). Defined in
   [`docs/chapters/07-mathematical-structures.qmd`](docs/chapters/07-mathematical-structures.qmd).
   The most common way a chapter goes wrong is blurring two of these levels
   without noticing. `docs/chapters/25-advanced-topics.qmd` is the one
   deliberate, documented exception — it surveys four different theories
   (functional analysis, measure theory, differential geometry, category
   theory) rather than building one, says so in its own opening paragraph,
   and carries no single tag. Don't treat that chapter as license to blur
   levels elsewhere; it's an exception because it says it is one.

## Content conventions

- **Voice**: flowing narrative prose with descriptive `##`/`###` headers —
  explicitly *not* the numbered template (`## 1. The intuition`, `## 2.
  Before this`, ...) that `SPEC.md` §6 suggests. This was a deliberate
  choice to match the voice of `../optimization-lab` and
  `../modern-ai-systems-and-methods`, made when this repo was scaffolded —
  don't revert to the numbered template without that being a fresh,
  deliberate decision.
- Every chapter still has to *cover* `SPEC.md`'s ten questions (what is it,
  why does it exist, what problem does it solve, what came before it, what
  does it generalize, what axioms define it, what follows from them, what
  familiar things instantiate it, what does it connect to, where does it
  appear later) — just woven into prose, not as a checklist with headers.
- **Problem before abstraction, always.** Motivating examples appear before
  a formal definition, never after. When an axiom is stated, the chapter
  says what breaks without it, not just that it holds.
- **Not proof-heavy.** Formal definitions appear because they clarify what's
  being claimed; full proofs are included only when the proof itself is the
  insight (e.g. $\sqrt{2}$'s irrationality in
  `06-number-systems.qmd`), never for completeness's sake.
- **Terminology discipline.** "Space," "structure," "transformation," and
  similar overloaded words get their specific meaning stated at first use in
  a chapter, not assumed.
- Historical claims carry approximate dates and, where genuinely contested
  or simplified, an explicit flag saying so — see `appendix-references.qmd`
  for the sourcing hierarchy (MacTutor → SEP → primary sources → textbooks,
  never Wikipedia as the final citation).
- Every chapter ends with an explicit "where this leads" pointer (what's
  next, and often what it generalizes into) — this is the site's substitute
  for a mechanical "Connections" footer, done inline instead.
- New citations: add the BibTeX entry to `docs/references.bib` and cite with
  `@key` in prose; remove the `placeholder` entry once a real one exists.
- **Never hardcode a chapter number in prose** ("chapter 8", "Chapter 1
  picks up..."). Quarto numbers chapters by their position in
  `_quarto.yml`'s `chapters:` list, which has already shifted twice as
  Phase 2 inserted chapters mid-sequence — a hardcoded number silently goes
  stale the next time a chapter is inserted before it. `00-the-map.qmd`'s
  concept-comparison table and "five threads" closing paragraph both had
  this bug (caught and fixed when Phase 3 shifted numbering again); link by
  title (`[Groups](08-groups.qmd)`) instead, never by ordinal.

## Structure

Quarto book, chapters flat under `docs/chapters/NN-slug.qmd`, grouped into
parts (Map / Foundations / Objects / Structures / Theories / Appendices) via
`docs/_quarto.yml` — **not** the nested per-discipline folder tree
`SPEC.md` §4 originally suggested; that got superseded when this repo was
deliberately restructured to match `../optimization-lab` and
`../modern-ai-systems-and-methods`'s Quarto-book conventions.

**`docs/_quarto.yml`'s `chapters:` list is the authoritative reading order —
filename numbers are not.** `11-rings-and-fields.qmd`, `12-metric-spaces.qmd`,
and `13-topological-spaces.qmd` read, in the actual book, *before*
`09-vector-spaces.qmd`/`10-linear-algebra.qmd`'s numbers would suggest
(Rings and Fields sits between Groups and Vector Spaces; Metric and
Topological Spaces sit between Vector Spaces and Linear Algebra) — they were
numbered to continue the existing sequence rather than to force a rename of
already-published, already-cross-linked files. Quarto numbers sections by
TOC position, not filename, so this is invisible to readers; it only matters
if you're scanning `ls docs/chapters` expecting numeric order to be reading
order.

**Diagrams are computed static figures, not Mermaid.** Mermaid was tried
first for `00-the-map.qmd` and dropped after its `flowchart TD` with
subgraphs rendered with a near-black subgraph fill that clashed against the
site's light theme, plus edges routed outside their subgraph boxes — a real
rendering defect, confirmed by screenshotting the live page, not a taste
call. `scripts/figures/*.py` (matching `../modern-ai-systems-and-methods`'s
pattern) now generates every diagram in `00-the-map.qmd` as a static PNG in
`docs/images/`, using `scripts/figures/_theme.py` for shared styling
(palette is the validated categorical instance from the `dataviz` skill's
reference palette — same source `../optimization-lab`'s `viz/theme.py`
cites — checked with `validate_palette.js` in adjacent-pairs mode, which is
the right mode here since every node carries a direct label plus a legend,
not bare unlabeled marks). The master map
(`fig_landscape_network.py`) specifically uses a **computed longest-path DAG
layering** (topological sort), not `networkx.spring_layout` or
`kamada_kawai_layout` — both were tried and both collapsed this graph's long
sparse chains into overlapping node clusters, since neither accounts for
node size and neither suits a small, nearly-tree-shaped graph. Regenerate
after editing a figure script:
```bash
python3 scripts/figures/fig_landscape_network.py   # or whichever script changed
```
then `quarto render docs` and look at the actual output — this project's one
prior visualization bug (the Mermaid map) was caught exactly by looking at
the rendered page, not by the source looking plausible.

## Dev workflow

Needs the [Quarto CLI](https://quarto.org/docs/get-started/) (not a Python
package, install separately):

```bash
quarto preview docs   # live-reloading local preview
quarto render docs    # one-shot build to docs/_site/
```

No test suite, no linter — this is prose and Mermaid, not code. The
closest thing to CI is the docs-build workflow itself
(`.github/workflows/docs.yml`); a broken Mermaid fence or bad cross-link is
caught by `quarto render` failing or producing a visibly broken page, not by
an automated check.

## Current status

All 5 planned phases are built — 25 chapters, logic through a conceptual-
coverage preview of functional analysis/measure theory/differential
geometry/category theory. There is no in-flight "next phase" recorded as of
this writing — before starting new work, check `ROADMAP.md`'s "Non-goals"
section and the git log for anything more recent than what's summarized
there, and check with the owner what's actually wanted next (new
disciplines, more depth on an existing chapter, or something else) rather
than assuming more chapters are expected in a particular area.
