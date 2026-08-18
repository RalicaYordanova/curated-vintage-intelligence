from typing import Optional

from pydantic import BaseModel, Field


class JewelryExtraction(BaseModel):
    """
    Facts extracted directly from the user's raw text.
    No unsupported attribution or interpretation belongs here.
    """

    brand: Optional[str] = None
    category: Optional[str] = None

    signature_text: Optional[str] = None

    era_text: Optional[str] = None
    material_text: Optional[str] = None
    condition_text: Optional[str] = None

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
