# Workflow: from literature to drylab experiment to registry

Created 2026-09-27. This is the operating loop for the project. It combines the
research workspace (Biomni Lab), public DeepMind/Isomorphic tools, the Sidi Chen
lab's screening methodology as an evidence template, and drylab compute on
brev.dev (NVIDIA GPU instances). Nothing here does wet lab work.

## The loop

1. **Research pass (Biomni Lab).** Run the kickoff prompt (or a follow-up) in a
   named Biomni project with the project context from docs/PROJECT_BRIEF.md.
   Attach resources with @ (PubMed, Open Targets, GWAS Catalog, UniProt, GEO,
   CellxGene). Require linked sources, run Scientific Review, export the report
   and the machine-readable shortlist table.
2. **Registry update.** Merge the shortlist into src/parkinsons_discovery/.
   Each new hypothesis gets an id, claim type, status, sources, falsification
   plan, and do-not-assume note. Run `pytest` and `pd-registry check` before
   committing.
3. **Drylab triage.** For each hypothesis, pick the cheapest computational test
   that could kill it (see the triage table below). If a test needs GPU, it runs
   on brev.dev. Write an experiments/<id>/README.md card first: question, data,
   method, expected runtime, cost ceiling, and the decision rule (what result
   parks the hypothesis vs. promotes it).
4. **Drylab run (brev.dev).** Spin up a GPU instance, run the analysis, save
   results and environment info into the experiment card, tear the instance
   down. Data stays out of git; results and conclusions go in.
5. **Registry verdict.** Update the hypothesis status (unreviewed / parked /
   falsified / active-with-citation) citing the experiment card. Iterate.

## Resource map

| Stage | Tool | What it contributes | Access |
| --- | --- | --- | --- |
| Literature + data research | Biomni Lab (docs.biomni.phylo.bio) | Agent with 150+ tools, databases, cloud workspaces; Scientific Review pass | Owner's workspace, app.phylo.bio |
| Structure / interactions | AlphaFold 3 (AlphaFold Server) | Protein-ligand, protein-nucleic complexes relevant to alpha-synuclein handling and target biology | Public web server, daily entry limits |
| Variant interpretation | AlphaMissense | Missense effect predictions for candidate genes | Public |
| Noncoding GWAS | AlphaGenome / AlphaGenome Atlas (Sept 2026) | Predicted molecular effects of every human SNV; prioritize Parkinson's GWAS loci for mechanism and cell type | Public |
| Protein design | AlphaProteo | Binder design if a hypothesis reaches that stage | Limited access |
| Screening methodology | Sidi Chen lab (sidichenlab.org): Perturb-DBiT, in vivo CRISPR screens, TCPGdb, pegFinder, DeepSCan | The evidence bar: spatially resolved, in vivo, causality-first perturbation screening. Adapted *computationally* (drylab): in-silico Perturb-seq reanalysis, screen-design and guide-design thinking. The lab works in cancer; no result is imported, only method standards | Public papers and tools |
| Drylab compute | brev.dev (NVIDIA) | On-demand GPU instances with CUDA, Docker, Jupyter preinstalled; multi-cloud capacity; good for scRNA-seq reanalysis, model training, docking pipelines, small fine-tunes | Owner account |
| Cohort data | AMP PD, PPMI, Open Targets, GWAS Catalog, CellxGene | Genomics, transcriptomics, proteomics, clinical progression, target evidence | Some gated (see data/README.md) |

## Drylab experiment menu on brev.dev

Ranked by cost, cheapest first. Start every hypothesis at the top and move down
only if it survives.

1. **Data reanalysis (CPU/hours, small GPU).** CellxGene and AMP PD
   transcriptomics: does the target gene's perturbation signature match disease
   signature reversal? Datasets like these are the cheapest falsification test
   that exists.
2. **Genetic prioritization (CPU).** Cross-reference GWAS Catalog loci with
   AlphaGenome Atlas predictions: which Parkinson's risk variants change
   regulation of which genes, in which cell types? Feeds H-LYSOSOME-style
   hypotheses with citations.
3. **Signature/perturbation modeling (single GPU).** Reanalyze public
   Perturb-seq datasets with Chen-lab-style causality thinking: is the glial or
   neuronal state causal or reactive? Directly tests H-MICROGLIA.
4. **Structure work (GPU).** AlphaFold 3 server for hypothesis-generating
   complexes; local GPU only for downstream analysis of downloaded structures.
   Respect the public server's limits; do not plan production docking around it.
5. **Small model training (1-4 GPUs).** Biomarker classifiers, progression
   models on PPMI/AMP PD longitudinal data, ADMET proxy models for shortlisted
   molecules. Write the experiment card with train/test splits fixed before
   looking at outcomes.

## Rules that keep this honest

- One experiment card per run, with cost recorded, before the instance starts.
- A drylab result can park a hypothesis but can never make a clinical claim.
- Chen-lab methods are the quality bar; their disease area is cancer. Nothing
  transfers except standards.
- If the bottleneck on a shortlisted hypothesis is manufacturing or delivery
  rather than biology, say so on the card. That is the owner's home turf and a
  legitimate kill reason.
- Every brev.dev instance gets torn down when the card is written. No idle GPU
  burn.
