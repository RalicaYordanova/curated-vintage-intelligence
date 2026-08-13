from src.models.market_observation import MarketObservation
from src.valuation.evidence_weight import evidence_weight
from statistics import median


def get_observation_price(observation: MarketObservation) -> float:
    if observation.observation_type == "sold":
        return observation.sold_price

    if observation.observation_type == "asking":
        return observation.asking_price

    raise ValueError(
        f"Unsupported observation type: {observation.observation_type}"
    )

def calculate_baseline(
    observations: list[MarketObservation],
) -> float:
    sold_prices = [
        observation.sold_price
        for observation in observations
        if observation.observation_type == "sold"
    ]

    if not sold_prices:
        raise ValueError("No realized-sale evidence")

    return median(sold_prices)
