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
