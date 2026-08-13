from src.models.market_observation import MarketObservation
from src.valuation.evidence_ranking import rank_evidence


def test_sold_is_ranked_before_asking():
    asking = MarketObservation(
        observation_id="obs-asking",
        item_id="dior-001",
        observation_type="asking",
        platform="eBay",
        source_type="marketplace",
        asking_price=90,
    )

    sold = MarketObservation(
        observation_id="obs-sold",
        item_id="dior-001",
        observation_type="sold",
        platform="Vestiaire",
        source_type="marketplace",
        sold_price=224,
        sale_confirmed=True,
    )

    ranked = rank_evidence([asking, sold])

    assert ranked[0].observation_type == "sold"
    assert ranked[1].observation_type == "asking"
