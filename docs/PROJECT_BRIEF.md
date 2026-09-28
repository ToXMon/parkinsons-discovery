# Project brief

Created 2026-09-27. Owner context and ground rules for every research pass.

## Owner background

1. Materials scientist engineer by trade.
2. Ten years in commercial and R&D biologics, cell and gene therapy
   production operations; has seen the commercial manufacturing reality.
3. Self-taught across a large portion of the AI/ML stack.
4. Can rent cloud GPU compute easily.
5. Goal: go all the way in advanced therapies, from concept to molecule to
   indication, for Parkinson's disease.

## Inspirations and references

- Sidi Chen lab (Yale), https://sidichenlab.org/ : high-throughput in vivo
  CRISPR screening, Perturb-DBiT spatially resolved screens, in vivo CRISPR
  activation screens for combination design, and tools (TCPGdb, pegFinder,
  DeepSCan). The lab works in cancer, not Parkinson's. Treat their methods
  as an evidence-quality bar, not as transferable results.
- Google DeepMind / Isomorphic Labs: AlphaFold 3 (structure and interactions
  of all life's molecules), AlphaMissense, AlphaGenome and the AlphaGenome
  Atlas (September 2026: predicted molecular effects of every possible human
  single-nucleotide variant), AlphaProteo. Public web servers have entry
  limits; plan around them.
- Biomni Lab (https://docs.biomni.phylo.bio/), the owner's biomedical AI
  research workspace: projects with durable context, resources attached via
  @ (databases such as PubMed, UniProt, PDB, Ensembl, ClinVar, GEO, Open
  Targets, GWAS Catalog), skills, isolated cloud workspaces with GPU and
  high-memory compute, and a Scientific Review pass (a second agent that
  critiques a completed answer for unsupported claims and missing
  limitations). Follow docs.biomni.phylo.bio/how-to-prompt: state the
  outcome, give context, state constraints, ask for linked sources and
  inspectable outputs, keep refinement in one task.

## Disease-area ground truth (as of the July 2026 pipeline page)

No disease-modifying therapy is approved for Parkinson's. First-half 2026
brought two Phase 2b failures: BIIB122 (LRRK2 inhibitor, LUMA, idiopathic PD)
and BIA 28-6156 (GCase modulator, ACTIVATE, GBA1 PD). Still in play:
prasinezumab (Phase 3), bemdaneprocel (Phase 3 cell therapy), AB-1005
(Phase 2 GDNF gene therapy), BEACON (LRRK2 carriers, data expected H1 2027).
Neurology drugs historically clear Phase 1 to approval at well under 15%.
Any project claim of reversing or curing Parkinson's must clear that bar,
which is why the registry separates slow, stop, restore, and symptom claims.

## Working rules

1. Research passes run in Biomni Lab projects with the project context set
   from this brief; outputs land in docs/research/ with linked sources.
2. Hypotheses change status only with a citation filed in the repo.
3. Expensive compute gets an experiments/ card: question, data, method,
   cost, result, and what it changed in the registry.
4. Manufacturing and deliverability realism is an asset, not an afterthought:
   the owner has seen what scale-up actually requires. Flag hypotheses whose
   bottleneck is manufacturing, not biology.
5. This repo is computational. No wet-lab protocols, no self-administration
   guidance, no clinical advice.
