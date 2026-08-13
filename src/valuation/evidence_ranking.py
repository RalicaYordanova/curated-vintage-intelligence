from src.models.market_observation import MarketObservation
from src.valuation.evidence_weight import evidence_weight


def rank_evidence(
    observations: list[MarketObservation],
) -> list[MarketObservation]:
    return sorted(
        observations,
        key=lambda obs: evidence_weight(obs.observation_type),
        reverse=True,
    )

def test_empty_evidence_returns_empty_list():
    assert rank_evidence([]) == []
