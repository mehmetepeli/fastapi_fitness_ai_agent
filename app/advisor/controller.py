from fastapi import APIRouter
from app2.advisor.models import Profile
from app2.advisor.service import analyze_profile

router = APIRouter()

@router.get("/profile")
async def get_profile():
    return "Not yet implemented"

@router.post("/analyze")
async def analyze(profile: Profile):
    return await analyze_profile(profile)