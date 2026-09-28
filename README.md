# parkinsons-discovery

A hypothesis registry for computational research toward disease-modifying
Parkinson's therapies: molecules, drugs, cell therapy, and gene therapy.

**Not a medical device. Not a treatment recommendation. Nothing here is
evidence that any therapy works.**

## What this is

The core artifact is a registry of therapy hypotheses, each with a claim type,
an evidence status, named clinical leads where they exist, and explicit
falsification and do-not-assume notes. Research passes (Biomni Lab, cloud
compute) update the registry; nothing enters it without a source.

## Owner context

Materials scientist engineer; 10 years in commercial and R&D biologics, cell
and gene therapy production operations; self-taught across much of the AI/ML
stack; rents cloud GPU compute. The goal is to go from concept to molecule to
indication, with the biology and the manufacturing reality both in view.
See docs/PROJECT_BRIEF.md.

## Quick start

```
uv venv && source .venv/bin/activate
uv pip install -e ".[dev]"
pytest
pd-registry list
pd-registry show H-LRRK2-CARRIER
```

## Layout

- src/parkinsons_discovery/ : registry package and CLI
- docs/WORKFLOW.md : the research-to-drylab loop (Biomni, DeepMind tools, Chen-lab methods, brev.dev)
- docs/research/ : kickoff prompts and research-pass outputs
- docs/decisions/ : decision records
- experiments/ : one card per drylab experiment (see experiments/README.md)
- data/ : downloads and derived files (gitignored; see data/README.md)

## Rules of the road

1. Every hypothesis carries what would falsify it and what not to assume.
2. Clinical statuses must cite a lead URL. Re-verify against primary sources.
3. No row is ever marked active without a cited source in the repo.
4. A computational score never overrides a clinical result.
