from src.models.market_observation import MarketObservation
from src.valuation.evidence_weight import evidence_weight


def get_observation_price(observation: MarketObservation) -> float:
    if observation.observation_type == "sold":
        return observation.sold_price

    if observation.observation_type == "asking":
        return observation.asking_price

    raise ValueError(
        f"Unsupported observation type: {observation.observation_type}"
    )
