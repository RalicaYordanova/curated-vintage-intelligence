def evidence_weight(observation_type: str) -> float:
    if observation_type == "sold":
        return 1.0

    if observation_type == "asking":
        return 0.25

    raise ValueError(f"Unsupported observation type: {observation_type}")
