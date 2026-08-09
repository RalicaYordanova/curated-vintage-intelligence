from typing import Optional
from pydantic import BaseModel, Field


class JewelryItem(BaseModel):
    brand: Optional[str] = None
    category: str
    signature: Optional[str] = None
    era: Optional[str] = None
    material: Optional[str] = None
    condition: str

    purchase_price: Optional[float] = Field(
        default=None,
        ge=0
    )

    listing_price: Optional[float] = Field(
        default=None,
        ge=0
    )

    sold_price: Optional[float] = Field(
        default=None,
        ge=0
    )

    currency: str = "EUR"
