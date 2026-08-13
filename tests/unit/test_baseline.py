from src.models.market_observation import MarketObservation
from src.valuation.baseline import get_observation_price


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
