from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from src.ingestion.models import JewelryExtraction

router = APIRouter()

templates = Jinja2Templates(directory="web/templates")

@router.get("/items/review")
def review_item(request: Request):
    extraction = JewelryExtraction(
        brand="Monet",
        category="Earrings",
        signature="Monet",
        condition="Excellent",
        purchase_price=6.0,
        currency="EUR",
    )

    return templates.TemplateResponse(
        request=request,
        name="review.html",
        context={
            "extraction": extraction,
        },
    )
    
@router.post("/items/review")
def confirm_review():
    return {"message": "Review confirmed"}
