# data/

Everything here is gitignored except this file. Record provenance in
experiments/ cards instead of committing cohort files.

Expected datasets for early passes:

- AMP PD (Accelerating Medicines Partnership Parkinson's Disease) Knowledge
  Platform: WGS, transcriptomics, proteomics. Requires Terra access and
  controlled-access approval.
- PPMI (Parkinson's Progression Markers Initiative): clinical and biomarker
  longitudinal data. Requires registration.
- Open Targets Platform: target-disease association evidence.
- GWAS Catalog: replicated Parkinson's risk loci with effect sizes.
- CellxGene: public single-cell atlases, including Parkinson's brain
  single-nucleus collections.

Rule: download into data/raw/, derive into data/derived/, document every
download (URL, access date, terms) in the experiment card that used it.
