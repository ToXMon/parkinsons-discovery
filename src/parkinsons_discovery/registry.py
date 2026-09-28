"""Seed registry. Rows are questions with a source to re-check, not results.

Clinical wording comes from the Parkinson's Foundation pipeline page
(https://www.parkinsons.org/research/pipeline) as fetched on 2026-09-27;
that page said it reflected data through July 2026. Re-verify before acting.
"""

from parkinsons_discovery.models import (
    CLINICAL_STATUSES, Claim, Hypothesis, Modality, Status,
)

PIPELINE = "https://www.parkinsons.org/research/pipeline"
SEEDED_ON = "2026-09-27"
_PAGE = (
    f"Seeded on {SEEDED_ON} from a fetch of the Parkinson's Foundation pipeline page, "
    "which said it reflected data through July 2026. Confirm on that page and on a "
    "primary source before acting on it."
)


def _h(**kwargs):
    return Hypothesis(**kwargs)


_SEED = (
    _h(
        id="H-SNCA-ANTIBODY",
        statement="An antibody against aggregated alpha-synuclein slows motor progression in idiopathic Parkinson's.",
        modality=Modality.BIOLOGIC,
        claim=Claim.SLOW,
        status=Status.CLINICAL_ONGOING,
        why_it_is_here=(
            _PAGE
            + " Lead: prasinezumab (Roche/Genentech). The page said Phase 2b PADOVA"
            + " (June 2025, 586 participants) missed its primary progression endpoint"
            + " (HR 0.84, p=0.0657) with a pre-specified levodopa subgroup at HR 0.79,"
            + " p=0.04, and Phase 3 PARAISO (about 900 participants) began November 2025,"
            + " primary completion expected June 2029."
        ),
        what_would_falsify=(
            "PARAISO, or another adequately powered trial of this modality, misses its"
            + " progression endpoint and no pre-specified subgroup replicates. A binding"
            + " score does not reopen it."
        ),
        do_not_assume=(
            "An ongoing Phase 3 trial is not evidence the hypothesis is true. A missed"
            + " primary endpoint is not a win because a subgroup moved. A CSF biomarker"
            + " shift is not the same as slowed clinical progression."
        ),
        genes=("SNCA",),
        leads=(PIPELINE,),
    ),
    _h(
        id="H-LRRK2-IDIOPATHIC",
        statement="Inhibiting LRRK2 kinase slows progression in idiopathic Parkinson's.",
        modality=Modality.SMALL_MOLECULE,
        claim=Claim.SLOW,
        status=Status.CLINICAL_NEGATIVE,
        why_it_is_here=(
            _PAGE
            + " Lead: BIIB122 (Biogen/Denali). The page said the LUMA Phase 2b trial"
            + " (about 648 participants) missed its primary endpoint in May 2026 and"
            + " development in idiopathic Parkinson's was discontinued."
        ),
        what_would_falsify=(
            "Already weakened for idiopathic disease if that readout is confirmed. Park"
            + " this id unless a later idiopathic trial of a named LRRK2 inhibitor hits a"
            + " progression endpoint. Do not reopen it from a docking score."
        ),
        do_not_assume=(
            "This failure does not automatically close H-LRRK2-CARRIER or every"
            + " non-kinase LRRK2 idea. Those start from a late negative, not a blank page."
        ),
        genes=("LRRK2",),
        leads=(PIPELINE,),
    ),
    _h(
        id="H-LRRK2-CARRIER",
        statement="Inhibiting LRRK2 kinase slows progression in LRRK2 variant carriers even if it failed in idiopathic disease.",
        modality=Modality.SMALL_MOLECULE,
        claim=Claim.SLOW,
        status=Status.CLINICAL_ONGOING,
        why_it_is_here=(
            _PAGE
            + " The same page said BEACON, a Phase 2a study of BIIB122 in LRRK2 variant"
            + " carriers, was ongoing with results expected in the first half of 2027."
        ),
        what_would_falsify=(
            "BEACON misses its stated endpoint, or the enrolled variant class is not the"
            + " population you would pursue. A kinase-domain model is not a substitute."
        ),
        do_not_assume=(
            "Carrier biology and idiopathic biology are the same. An ongoing Phase 2a is"
            + " not support."
        ),
        genes=("LRRK2",),
        leads=(PIPELINE,),
    ),
    _h(
        id="H-GBA1-MODULATOR",
        statement="A small-molecule GCase modulator slows progression in GBA1-associated Parkinson's.",
        modality=Modality.SMALL_MOLECULE,
        claim=Claim.SLOW,
        status=Status.CLINICAL_NEGATIVE,
        why_it_is_here=(
            _PAGE
            + " Lead: BIA 28-6156 (Bial). The page said ACTIVATE (Phase 2b, 273"
            + " participants with GBA1 mutations) missed primary and key secondary"
            + " endpoints in June 2026 and development for this indication was stopped."
        ),
        what_would_falsify=(
            "Confirm the miss. If it holds, park small-molecule GCase modulation of this"
            + " type. A different molecule, population, or endpoint gets its own id."
        ),
        do_not_assume=(
            "A failed modulator closes GBA1 biology or justifies a gene-therapy version."
            + " H-GCASE-ACTIVATOR is a separate program."
        ),
        genes=("GBA1",),
        leads=(PIPELINE,),
    ),
    _h(
        id="H-GCASE-ACTIVATOR",
        statement="A GCase activator other than BIA 28-6156 can slow progression in GBA1-associated Parkinson's.",
        modality=Modality.SMALL_MOLECULE,
        claim=Claim.SLOW,
        status=Status.UNREVIEWED,
        why_it_is_here=(
            _PAGE
            + " Lead: GT-02287, listed with Phase 1b extension data expected September"
            + " 2026. That is early safety and biomarker work, not a progression result."
            + " This id exists so the failed modulator is not reused as evidence here."
        ),
        what_would_falsify=(
            "The Phase 1b program stops, or a later controlled trial misses a progression"
            + " endpoint in the GBA1 population. Serum enzyme activity is not that endpoint."
        ),
        do_not_assume=(
            "Phase 1b enrollment means the activator hypothesis survived ACTIVATE. It has"
            + " not been tested at that bar yet."
        ),
        genes=("GBA1",),
        leads=(PIPELINE,),
    ),
    _h(
        id="H-CELL-REPLACE",
        statement=(
            "Dopaminergic progenitors implanted in the putamen restore motor function."
            + " This is a restoration claim, not a claim the graft stops disease elsewhere."
        ),
        modality=Modality.CELL_THERAPY,
        claim=Claim.RESTORE,
        status=Status.CLINICAL_ONGOING,
        why_it_is_here=(
            _PAGE
            + " Lead: bemdaneprocel (BlueRock/Bayer), hESC-derived dopamine neurons."
            + " The page said Phase 3 exPDite-2 treated its first patient in September 2025."
        ),
        what_would_falsify=(
            "The Phase 3 motor endpoint is missed, or published follow-up shows the graft"
            + " does not survive and innervate. A differentiation sketch is not a substitute."
        ),
        do_not_assume=(
            "Cell replacement stops progression or replaces non-dopaminergic circuits."
            + " Manufacturing detail stays out of this repo; that is the operator's day job."
        ),
        genes=(),
        leads=(PIPELINE,),
    ),
    _h(
        id="H-GDNF-GENE",
        statement="AAV delivery of GDNF to the putamen slows nigrostriatal degeneration rather than only changing symptoms.",
        modality=Modality.GENE_THERAPY,
        claim=Claim.SLOW,
        status=Status.CLINICAL_ONGOING,
        why_it_is_here=(
            _PAGE
            + " Lead: AB-1005, described as AAV2 GDNF in Phase 2 REGENERATE-PD with RMAT"
            + " designation in February 2025, still enrolling, estimated primary completion"
            + " 2028. Older GDNF delivery studies were mixed; this id keeps those separate."
        ),
        what_would_falsify=(
            "Controlled human data show symptom change without a progression or imaging"
            + " signal that survives placebo, or delivery cannot reach the target region."
        ),
        do_not_assume=(
            "A gene-therapy label means disease modification. Do not design new vectors"
            + " here; the open question is whether the biological claim is intact."
        ),
        genes=("GDNF",),
        leads=(PIPELINE,),
    ),
    _h(
        id="H-ASO-SNCA",
        statement="Lowering SNCA RNA in the right cells slows progression without the synaptic harm too little alpha-synuclein could cause.",
        modality=Modality.ANTISENSE,
        claim=Claim.SLOW,
        status=Status.UNREVIEWED,
        why_it_is_here=(
            _PAGE
            + " The page said SNCA ASOs were preclinical with early human safety data"
            + " emerging and no program named. This id stays unreviewed until a primary"
            + " paper or registry entry is filed."
        ),
        what_would_falsify=(
            "Human or primate data show the knockdown needed to affect pathology also"
            + " impairs synaptic function, or a named program already failed for that reason."
        ),
        do_not_assume=(
            "SNCA multiplication disease means partial knockdown is safe. Cell type, degree"
            + " of lowering, and allele selectivity are the hypothesis itself."
        ),
        genes=("SNCA",),
        leads=(PIPELINE,),
    ),
    _h(
        id="H-NLRP3",
        statement="Inhibiting NLRP3 slows progression because microglial inflammasome activity is causal, not only reactive.",
        modality=Modality.SMALL_MOLECULE,
        claim=Claim.SLOW,
        status=Status.UNREVIEWED,
        why_it_is_here=(
            _PAGE
            + " Lead: dapansutrile, described as entering Phase 2 (DAPA-PD) with recruitment"
            + " expected early 2026. That may be stale relative to the July 2026 page update."
        ),
        what_would_falsify=(
            "The trial does not start or misses a progression endpoint. A postmortem"
            + " microglial expression change is not enough to keep this active."
        ),
        do_not_assume=(
            "Neuroinflammation on a slide is a drug target. This id is a named molecule in a"
            + " named trial, not a general inflammation hypothesis."
        ),
        genes=(),
        leads=(PIPELINE,),
    ),
    _h(
        id="H-MITO-IDIOPATHIC",
        statement="Restoring mitophagy slows idiopathic Parkinson's, not only disease in biallelic PINK1 or PRKN carriers.",
        modality=Modality.UNSPECIFIED,
        claim=Claim.SLOW,
        status=Status.UNREVIEWED,
        why_it_is_here=(
            "Recessive early-onset genes put mitochondria on the list. No paper filed here"
            + " yet shows the same node is causal and druggable in idiopathic disease."
        ),
        what_would_falsify=(
            "Human genetics and tissue data do not support a mitochondrial node outside the"
            + " recessive forms, or interventions that move the node fail a progression"
            + " endpoint in the population you would enroll."
        ),
        do_not_assume=(
            "A PINK1 or PRKN genotype is evidence a mitochondrial drug helps sporadic PD."
        ),
        genes=("PINK1", "PRKN", "PARK7"),
        leads=(),
    ),
    _h(
        id="H-MICROGLIA",
        statement="Changing a microglial state that is causal, not only reactive, slows progression.",
        modality=Modality.UNSPECIFIED,
        claim=Claim.SLOW,
        status=Status.UNREVIEWED,
        why_it_is_here=(
            "Inflammation is repeatedly reported in Parkinson's tissue. This repo has not"
            + " separated a causal microglial program from a response to neuron loss. A"
            + " perturbation screen would test that; none exists here. The Sidi Chen lab"
            + " (Yale) runs such screens in cancer; their method is an evidence-quality"
            + " reference, not an importable result."
        ),
        what_would_falsify=(
            "In the datasets you trust, microglial changes are downstream of neuron loss and"
            + " human genetics does not implicate a tractable microglial gene worth a modality."
        ),
        do_not_assume=("A postmortem expression difference is a target."),
        genes=(),
        leads=(),
    ),
)


def hypotheses():
    return _SEED


def get(hypothesis_id):
    for item in _SEED:
        if item.id == hypothesis_id:
            return item
    return None


def validate():
    problems = []
    seen = set()
    for item in _SEED:
        if item.id in seen:
            problems.append(f"duplicate id: {item.id}")
        seen.add(item.id)
        if not item.id.startswith("H-"):
            problems.append(f"{item.id}: id must start with H-")
        for field in ("statement", "why_it_is_here", "what_would_falsify", "do_not_assume"):
            if not getattr(item, field).strip():
                problems.append(f"{item.id}: empty {field}")
        if item.status in CLINICAL_STATUSES and not item.leads:
            problems.append(f"{item.id}: clinical status requires a lead URL")
        for lead in item.leads:
            if not lead.startswith("https://"):
                problems.append(f"{item.id}: lead is not an https URL: {lead}")
        lowered = item.statement.lower()
        if "cure" in lowered:
            problems.append(f"{item.id}: statement overclaims the clinical bar")
    return problems
