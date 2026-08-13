from src.valuation.evidence_weight import evidence_weight


def test_sold_has_higher_weight():
    assert evidence_weight("sold") == 1.0


def test_asking_has_lower_weight():
    assert evidence_weight("asking") == 0.25
