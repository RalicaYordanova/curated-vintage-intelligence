from src.models.market_observation import MarketObservation
from src.valuation.service import valuate


def test_external_anchor_does_not_change_baseline():
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
    ]

    baseline_a = valuate(
        observations,
        external_anchor=15,
    )

    baseline_b = valuate(
        observations,
        external_anchor=80,
    )

    assert baseline_a == baseline_b
