from fastapi.testclient import TestClient
from src.api.main import app
from src.models.market_observation import MarketObservation
from src.valuation.service import valuate


client = TestClient(app)


def test_valuation_endpoint_returns_baseline():
    response = client.post(
        "/valuation",
        json={
            "observations": [
                {
                    "observation_id": "obs-sold-1",
                    "item_id": "item-001",
                    "observation_type": "sold",
                    "platform": "Vestiaire",
                    "source_type": "marketplace",
                    "sold_price": 15,
                    "sale_confirmed": True,
                },
                {
                    "observation_id": "obs-sold-2",
                    "item_id": "item-001",
                    "observation_type": "sold",
                    "platform": "eBay",
                    "source_type": "marketplace",
                    "sold_price": 18,
                    "sale_confirmed": True,
                },
            ],
            "external_anchor": 80,
        },
    )

    assert response.status_code == 200

    body = response.json()

    assert body["baseline"] == 16.5
    assert body["evidence_count"] == 2
    assert body["anchor_used_for_baseline"] is False

def test_valuation_endpoint_rejects_invalid_observation():
    response = client.post(
        "/valuation",
        json={
            "observations": [
                {
                    "observation_id": "obs-invalid",
                    "item_id": "item-001",
                    "observation_type": "sold",
                    "platform": "Vestiaire",
                    "source_type": "marketplace",
                    "sold_price": -10,
                    "sale_confirmed": True,
                }
            ]
        },
    )

    assert response.status_code == 422
def test_external_anchor_does_not_change_api_baseline():
    observations = [
        {
            "observation_id": "obs-sold-1",
            "item_id": "item-001",
            "observation_type": "sold",
            "platform": "Vestiaire",
            "source_type": "marketplace",
            "sold_price": 15,
            "sale_confirmed": True,
        },
        {
            "observation_id": "obs-sold-2",
            "item_id": "item-001",
            "observation_type": "sold",
            "platform": "eBay",
            "source_type": "marketplace",
            "sold_price": 18,
            "sale_confirmed": True,
        },
    ]

    response_a = client.post(
        "/valuation",
        json={
            "observations": observations,
            "external_anchor": 15,
        },
    )

    response_b = client.post(
        "/valuation",
        json={
            "observations": observations,
            "external_anchor": 80,
        },
    )

    assert response_a.status_code == 200
    assert response_b.status_code == 200

    assert (
        response_a.json()["baseline"]
        == response_b.json()["baseline"]
    )

def test_api_result_matches_direct_service_calculation():
    observations_json = [
        {
            "observation_id": "obs-sold-1",
            "item_id": "item-001",
            "observation_type": "sold",
            "platform": "Vestiaire",
            "source_type": "marketplace",
            "sold_price": 15,
            "sale_confirmed": True,
        },
        {
            "observation_id": "obs-sold-2",
            "item_id": "item-001",
            "observation_type": "sold",
            "platform": "eBay",
            "source_type": "marketplace",
            "sold_price": 18,
            "sale_confirmed": True,
        },
    ]

    response = client.post(
        "/valuation",
        json={
            "observations": observations_json,
            "external_anchor": 80,
        },
    )

    observations = [
        MarketObservation(**observation)
        for observation in observations_json
    ]

    direct_baseline = valuate(
        observations,
        external_anchor=80,
    )

    assert response.status_code == 200
    assert response.json()["baseline"] == direct_baseline
