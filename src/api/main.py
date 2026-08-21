from fastapi import FastAPI
from pydantic import BaseModel
from src.web.routes import router

from src.models.market_observation import MarketObservation
from src.valuation.service import valuate

app = FastAPI(
    title="CVI Valuation API",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {"status": "ok"}


class ValuationRequest(BaseModel):
    observations: list[MarketObservation]
    external_anchor: float | None = None

@app.post("/valuation")
def calculate_valuation(request: ValuationRequest):
    baseline = valuate(
        request.observations,
        external_anchor=request.external_anchor,
    )

    return {
        "baseline": baseline,
        "evidence_count": len(request.observations),
        "anchor_used_for_baseline": False,
    }

app.include_router(router)

