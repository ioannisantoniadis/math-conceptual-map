# Mathematics: From Computational Tools to Mathematical Structure

A conceptual map of mathematics for people who already know how to use it —
not a course, not a taxonomy, but a graph of *why* mathematical objects,
structures, and theories were invented, what they generalize, and how a
matrix, a group, and a random variable end up obeying the same theorems.

- Site: **[ioannisantoniadis.github.io/math-conceptual-map](https://ioannisantoniadis.github.io/math-conceptual-map/)**

## What this is

Most STEM curricula teach mathematics as toolkits: differentiate this,
invert that, solve this system. That's genuinely useful and this site
doesn't re-teach it. What it targets instead is the layer most of those
curricula skip — what a mathematical object actually *is*, why a given
structure is defined by exactly those axioms and not some other list, which
ideas generalize which, and where a familiar tool sits in the broader
landscape. It follows a problem → abstraction → consequence pattern
throughout, and it insists — starting with [the map](docs/chapters/00-the-map.qmd)
— on keeping four things separate that are usually conflated: a concept's
*historical* origin, its *formal* foundation, its *conceptual* prerequisites,
and the *pedagogical* order that best motivates it. These are four different
graphs over the same ideas, and they don't always agree.

## Current scope

The site currently covers its foundational spine — logic through linear
algebra — as a deliberately small, complete arc rather than a sprawling
stub-filled tree. See [`ROADMAP.md`](ROADMAP.md) for what's built, what's
planned next (algebra beyond groups, geometry, topology, analysis,
probability, optimization, and an explicit machine-learning bridge), and the
phased order it'll arrive in.

## Repository layout

```
docs/                  Quarto book — the site source
  _quarto.yml            book config, chapter order, parts, theme
  chapters/*.qmd          the chapters, flat, grouped into parts by _quarto.yml
  appendix-*.qmd           glossary, references
  theme.scss               site theme (shared visual language with sibling repos)
SPEC.md                 the original project specification this repo implements
CLAUDE.md               repo-specific context for AI assistants working here
ROADMAP.md              phased plan and decision log
```

## Building the site locally

Needs the [Quarto CLI](https://quarto.org/docs/get-started/):

```bash
quarto preview docs   # live-reloading local preview
quarto render docs    # one-shot build to docs/_site/
```

## License

MIT License. See [`LICENSE`](LICENSE).
