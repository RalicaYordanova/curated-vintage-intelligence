from dataclasses import dataclass, field

from src.ingestion.models import JewelryExtraction


@dataclass
class QualityGateResult:
    review_required: bool = False
    warnings: list[str] = field(default_factory=list)


def validate_extraction(
    extraction: JewelryExtraction,
) -> QualityGateResult:
    warnings = []

    if extraction.signature and extraction.brand:
        warnings.append(
            "Brand attribution requires evidence beyond signature text."
        )

    return QualityGateResult(
        review_required=bool(warnings),
        warnings=warnings,
    )
