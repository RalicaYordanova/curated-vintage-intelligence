from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()

@router.get("/items/review")
def review_item():
  return "Review Page" 
