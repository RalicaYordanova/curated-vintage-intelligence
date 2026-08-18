from src.ingestion.models import JewelryExtraction


def test_gm_signature_does_not_imply_brand():
    extraction = JewelryExtraction(
        signature_text="GM",
        brand=None,
    )

    assert extraction.signature_text == "GM"
    assert extraction.brand is None
