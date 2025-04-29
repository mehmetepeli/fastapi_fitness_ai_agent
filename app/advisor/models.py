from typing import List, Optional
from pydantic import BaseModel, Field
from enum import Enum

class ActivityLevel(str, Enum):
    SEDENTARY = "sedentary"
    LIGHT = "light"
    MODERATE = "moderate"
    VERY_ACTIVE = "very_active"
    ATHLETE = "athlete"

class Goal(str, Enum):
    WEIGHT_LOSS = "weight_loss"
    MUSCLE_GAIN = "muscle_gain"
    MAINTENANCE = "maintenance"
    ENDURANCE = "endurance"
    STRENGTH = "strength"

class Exercise(BaseModel):
    name: str
    sets: int
    reps: int
    rest_time: int = Field(..., description="Rest time in seconds")

class Meal(BaseModel):
    name: str
    calories: int
    protein: float
    carbs: float
    fats: float
    timing: str = Field(..., description="breakfast, lunch, dinner, snack")

class Profile(BaseModel):
    age: int
    weight: float
    height: float
    gender: str
    activity_level: ActivityLevel
    fitness_goal: Goal
    dietary_restrictions: List[str] = []
    injuries: List[str] = []
    preferred_workout_time: str
    available_equipment: List[str] = []
    workout_days_per_week: int

class ReportResult(BaseModel):
    workout_plan: List[Exercise] = Field(description="Exercise plan")
    meal_plan: List[Meal] = Field(description="Meal plan")
    daily_calories: int = Field(description="Daily calories")
    macros: dict = Field(description="Macros")
    tips: List[str] = Field(description="Personal fitness and nutrition tips")
    weekly_schedule: dict = Field(description="Weekly workout and meal time schedule")
    motivational_quote: str = Field(description="Motivational quote")