# Biomni Lab kickoff prompt: first research pass

Paste this into a new Biomni Lab task (create a named project first, e.g.
"parkinsons-discovery", and set the project context to docs/PROJECT_BRIEF.md).
Attach this repo's docs as files, use @ to attach resources, and run
Scientific Review on the final answer.

---

You are the research agent for a Parkinson's disease-modifying therapy
discovery project. Deliver a ranked, evidence-backed shortlist of the 10 to 15
most promising biological hypotheses where AI methods plus cloud compute could
genuinely change the picture in the next two to three years, across small
molecules, biologics, antisense, gene therapy, and cell therapy.

Context: the project owner is a materials scientist with ten years in
commercial and R&D biologics and cell/gene therapy production operations,
self-taught in AI/ML, with rented cloud GPU compute available. The repo this
feeds already tracks hypotheses including alpha-synuclein antibodies, SNCA
antisense, LRRK2 (idiopathic failed 2026, carriers pending), GBA1/GCase
(one Phase 2b failure, an activator pending), GDNF gene therapy, NLRP3,
mitophagy, and microglial states. Read that as a starting map, not a constraint.

What I need from this pass:

1. Evidence audit of the current clinical landscape as of today: confirm or
   correct the statuses above against ClinicalTrials.gov and primary
   publications, especially anything that read out after July 2026.
2. Target shortlist with, for each: the causal evidence chain (human genetics,
   perturbation data, pathology), the cell type where it acts, the modality
   options, the strongest published counter-evidence, and what a computational
   project could actually contribute (target identification, patient
   stratification, molecule design, biomarker discovery, manufacturing
   optimization).
3. Explicitly evaluate the underexplored angles: spatially resolved perturbation
   screening (the Sidi Chen lab Perturb-DBiT approach) adapted to dopaminergic
   neurons or microglia; AlphaGenome Atlas for prioritizing noncoding Parkinson's
   GWAS loci; AlphaFold 3 for complexes relevant to alpha-synuclein handling;
   single-cell atlas reanalysis for causal (not reactive) glial states.
4. For each shortlisted hypothesis, a falsification plan: the cheapest analysis
   or dataset that would kill it, and the cheapest that would justify a GPU
   experiment.
5. A data access plan for AMP PD, PPMI, Open Targets, GWAS Catalog, and CellxGene,
   including what is gated and realistic approval timelines.
6. A ranked top 5 with rationale, expected compute cost, and the single next
   action for each.

Rules: link a primary source next to every claim. Separate observed results from
your interpretation. If the evidence for a claim is weak or contested, say so
plainly. Do not use the word cure for anything. Do not propose wet-lab work the
owner cannot access; flag anything whose bottleneck is manufacturing or delivery,
since the owner knows that domain well. If key information is missing, say what
it is before proceeding.

Deliverables: a report I can drop into docs/research/, plus a machine-readable
table of the shortlist (id, statement, modality, claim type, evidence status,
sources, falsification plan, next action) formatted so I can merge it into the
hypothesis registry in this repo.

When done, run Scientific Review on your answer and incorporate the corrections.
