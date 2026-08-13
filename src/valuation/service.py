from src.models.market_observation import MarketObservation
from src.valuation.baseline import calculate_baseline


def valuate(
    observations: list[MarketObservation],
    external_anchor: float | None = None,
) -> float:
    return calculate_baseline(observations)
