from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="src/web/templates")

@router.get("/items/review")
def review_item(request: Request):
    return templates.TemplateResponse(
      request=request,
      name="review.html",
      context={},
)
