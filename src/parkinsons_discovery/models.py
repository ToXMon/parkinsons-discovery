"""Evidence states for a hypothesis. None of them means a therapy works."""

from dataclasses import dataclass
from enum import Enum


class Modality(str, Enum):
    SMALL_MOLECULE = "small_molecule"
    BIOLOGIC = "biologic"
    ANTISENSE = "antisense"
    GENE_THERAPY = "gene_therapy"
    CELL_THERAPY = "cell_therapy"
    UNSPECIFIED = "unspecified"


class Claim(str, Enum):
    SLOW = "slow_progression"
    STOP = "stop_progression"
    RESTORE = "restore_function"
    SYMPTOM = "symptom_control"


class Status(str, Enum):
    UNREVIEWED = "unreviewed"
    ACTIVE = "active"
    PARKED = "parked"
    FALSIFIED = "falsified"
    CLINICAL_NEGATIVE = "clinical_negative"
    CLINICAL_ONGOING = "clinical_ongoing"


CLINICAL_STATUSES = frozenset({Status.CLINICAL_NEGATIVE, Status.CLINICAL_ONGOING})


@dataclass(frozen=True)
class Hypothesis:
    id: str
    statement: str
    modality: Modality
    claim: Claim
    status: Status
    why_it_is_here: str
    what_would_falsify: str
    do_not_assume: str
    genes: tuple = ()
    leads: tuple = ()

    def format(self) -> str:
        genes = ", ".join(self.genes) if self.genes else "none listed"
        lines = [
            self.id,
            f"status: {self.status.value}",
            f"modality: {self.modality.value}",
            f"claim: {self.claim.value}",
            f"genes: {genes}",
            "",
            self.statement,
            "",
            "Why it is in the registry:",
            self.why_it_is_here,
            "",
            "What would falsify or park it:",
            self.what_would_falsify,
            "",
            "Do not assume:",
            self.do_not_assume,
            "",
            "Leads to verify:",
        ]
        if self.leads:
            lines.extend(f"- {lead}" for lead in self.leads)
        else:
            lines.append("- none yet; add a source before treating this as active")
        return chr(10).join(lines) + chr(10)
