from datetime import date
from typing import Literal

from pydantic import BaseModel, Field


class MarketObservation(BaseModel):
    observation_id: str
    item_id: str

    observation_type: Literal["sold", "asking"]

    platform: str
    source_type: str
    source_url: str | None = None
    listing_title: str | None = None

    asking_price: float | None = Field(default=None, gt=0)
    sold_price: float | None = Field(default=None, gt=0)

    currency: str = "EUR"
    sale_confirmed: bool = False

    listing_date: date | None = None
    sold_date: date | None = None
    days_to_sell: int | None = Field(default=None, ge=0)

    seller_country: str | None = None

    shipping_price: float | None = Field(default=None, ge=0)
    platform_fees: float | None = Field(default=None, ge=0)

    condition_as_listed: str | None = None
    description_raw: str | None = None
    image_url_primary: str | None = None

    reliability_score: float | None = Field(
        default=None,
        ge=0,
        le=1
    )
    notes: str | None = None
    notes: str | None = None
