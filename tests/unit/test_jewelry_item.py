import pytest
from pydantic import ValidationError

from src.models.jewelry_item import JewelryItem


def test_create_valid_jewelry_item():
    item = JewelryItem(
        brand="Miriam Haskell",
        category="Bracelet",
        condition="Very Good",
        purchase_price=70.0
    )

    assert item.brand == "Miriam Haskell"
    assert item.category == "Bracelet"
    assert item.purchase_price == 70.0


def test_negative_purchase_price_is_rejected():
    with pytest.raises(ValidationError):
        JewelryItem(
            category="Bracelet",
            condition="Good",
            purchase_price=-10
        )
        
def test_missing_category_is_rejected():
    with pytest.raises(ValidationError):
        JewelryItem(
            condition="Very Good"
        )
