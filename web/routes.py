from fastapi import APIRouter

router = APIRouter()

@router.get("/items/review")
def review_item():
  Return "Review Page" 
