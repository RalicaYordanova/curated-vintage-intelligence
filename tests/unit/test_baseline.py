from src.models.market_observation import MarketObservation
from src.valuation.baseline import get_observation_price
from src.valuation.baseline import (
    get_observation_price,
    calculate_baseline,
)
import pytest


def test_get_observation_price_for_sold():
    observation = MarketObservation(
        observation_id="obs-sold",
        item_id="dior-001",
        observation_type="sold",
        platform="Vestiaire",
        source_type="marketplace",
        sold_price=224,
        sale_confirmed=True,
    )

    assert get_observation_price(observation) == 224

def test_get_observation_price_for_asking():
    observation = MarketObservation(
        observation_id="obs-asking",
        item_id="dior-001",
        observation_type="asking",
        platform="eBay",
        source_type="marketplace",
        asking_price=90,
    )

    assert get_observation_price(observation) == 90

def test_calculate_baseline_uses_only_sold_prices():
    observations = [
        MarketObservation(
            observation_id="obs-sold-1",
            item_id="item-001",
            observation_type="sold",
            platform="Vestiaire",
            source_type="marketplace",
            sold_price=15,
            sale_confirmed=True,
        ),
        MarketObservation(
            observation_id="obs-sold-2",
            item_id="item-001",
            observation_type="sold",
            platform="eBay",
            source_type="marketplace",
            sold_price=18,
            sale_confirmed=True,
        ),
        MarketObservation(
            observation_id="obs-asking",
            item_id="item-001",
            observation_type="asking",
            platform="Etsy",
            source_type="marketplace",
            asking_price=80,
        ),
    ]

    assert calculate_baseline(observations) == 16.5
def test_calculate_baseline_rejects_asking_only_evidence():
    observations = [
        MarketObservation(
            observation_id="obs-asking",
            item_id="item-001",
            observation_type="asking",
            platform="Etsy",
            source_type="marketplace",
            asking_price=80,
        )
    ]

    with pytest.raises(
        ValueError,
        match="No realized-sale evidence",
    ):
        calculate_baseline(observations)
