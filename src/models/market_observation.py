import pytest
from pydantic import ValidationError

from src.models.market_observation import MarketObservation


def test_create_valid_market_observation():
    observation = MarketObservation(
        brand="Monet",
        category="Earclips",
        sold_price=52.0,
        platform="Vinted",
        confirmed_sale=True
    )

    assert observation.brand == "Monet"
    assert observation.category == "Earrings"
    assert observation.sold_price == 52.0
    assert observation.platform == "Vinted"
    assert observation.confirmed_sale is True
