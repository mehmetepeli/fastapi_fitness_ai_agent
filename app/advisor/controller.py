from fastapi import APIRouter
from app.advisor.models import Profile
from app.advisor.service import analyze_profile

router = APIRouter()

@router.post("/analyze")
async def analyze(profile: Profile):
    return await analyze_profile(profile)