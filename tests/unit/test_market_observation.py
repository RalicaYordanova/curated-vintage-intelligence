
import pytest
from pydantic import ValidationError

from src.models.market_observation import MarketObservation


def test_create_valid_sold_market_observation():
    observation = MarketObservation(
        observation_id="OBS-001",
        item_id="ITEM-001",
        observation_type="sold",
        platform="Vinted",
        source_type="verified_sale",
        sold_price=52.0,
        currency="EUR",
        sale_confirmed=True
    )

    assert observation.observation_id == "OBS-001"
    assert observation.item_id == "ITEM-001"
    assert observation.observation_type == "sold"
    assert observation.sold_price == 52.0
    assert observation.platform == "Vinted"
    assert observation.sale_confirmed is True


def test_create_valid_asking_market_observation():
    observation = MarketObservation(
        observation_id="OBS-002",
        item_id="ITEM-001",
        observation_type="asking",
        platform="Etsy",
        source_type="listing",
        asking_price=89.0
    )

    assert observation.observation_type == "asking"
    assert observation.asking_price == 89.0
    assert observation.sale_confirmed is False


def test_negative_sold_price_is_rejected():
    with pytest.raises(ValidationError):
        MarketObservation(
            observation_id="OBS-003",
            item_id="ITEM-001",
            observation_type="sold",
            platform="Vinted",
            source_type="verified_sale",
            sold_price=-10
        )


def test_invalid_observation_type_is_rejected():
    with pytest.raises(ValidationError):
        MarketObservation(
            observation_id="OBS-004",
            item_id="ITEM-001",
            observation_type="maybe",
            platform="Vinted",
            source_type="listing",
            asking_price=50
        )


def test_reliability_score_above_one_is_rejected():
    with pytest.raises(ValidationError):
        MarketObservation(
            observation_id="OBS-005",
            item_id="ITEM-001",
            observation_type="asking",
            platform="Vinted",
            source_type="listing",
            asking_price=50,
            reliability_score=1.5
        )
