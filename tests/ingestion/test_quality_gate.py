from src.ingestion.models import JewelryExtraction
from src.validation.ingestion_quality_gate import validate_extraction


def test_gm_signature_without_brand_passes():
    extraction = JewelryExtraction(
        signature ="GM",
        brand=None,
    )

    result = validate_extraction(extraction)

    assert extraction.signature == "GM"
    assert extraction.brand is None
    assert result.review_required is False
    assert result.warnings == []


def test_brand_inferred_from_signature_requires_review():
    extraction = JewelryExtraction(
        signature ="GM",
        brand="Grosse & Monneret",
    )

    result = validate_extraction(extraction)

    assert result.review_required is True
    assert (
        "Brand attribution requires evidence beyond signature text."
        in result.warnings
    )
