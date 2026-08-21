from src.ingestion.models import JewelryExtraction
from src.models.jewelry_item import JewelryItem


def test_extraction_and_item_have_same_domain_fields():
    extraction_fields = set(JewelryExtraction.model_fields.keys())
    item_fields = set(JewelryItem.model_fields.keys())

    assert extraction_fields == item_fields
