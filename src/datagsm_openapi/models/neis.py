"""NEIS-related models (급식, 학사일정) for DataGSM OpenAPI SDK."""

from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from .enums import MealType


class Meal(BaseModel):
    """급식 정보 (Meal Information).

    Information about school meals from NEIS.

    Attributes:
        meal_id: Meal ID
        school_code: School code
        school_name: School name
        office_code: Education office code
        office_name: Education office name
        meal_date: Meal date
        meal_type: Meal type (BREAKFAST, LUNCH, DINNER)
        meal_menu: List of menu items
        meal_allergy_info: List of allergy information
        meal_calories: Calorie information
        origin_info: Origin information of ingredients
        nutrition_info: Nutrition information
        meal_serve_count: Number of servings
    """

    meal_id: str = Field(..., alias="mealId", description="Meal ID")
    school_code: str = Field(..., alias="schoolCode", description="School code")
    school_name: str = Field(..., alias="schoolName", description="School name")
    office_code: str = Field(..., alias="officeCode", description="Education office code")
    office_name: str = Field(..., alias="officeName", description="Education office name")
    meal_date: date = Field(..., alias="mealDate", description="Meal date")
    meal_type: MealType = Field(..., alias="mealType", description="Meal type")
    meal_menu: list[str] = Field(
        default_factory=list, alias="mealMenu", description="Menu items"
    )
    meal_allergy_info: list[str] = Field(
        default_factory=list, alias="mealAllergyInfo", description="Allergy information"
    )
    meal_calories: Optional[str] = Field(None, alias="mealCalories", description="Calories")
    origin_info: Optional[str] = Field(
        None, alias="originInfo", description="Origin of ingredients"
    )
    nutrition_info: Optional[str] = Field(
        None, alias="nutritionInfo", description="Nutrition information"
    )
    meal_serve_count: Optional[int] = Field(
        None, alias="mealServeCount", description="Number of servings"
    )

    model_config = ConfigDict(populate_by_name=True)


class Schedule(BaseModel):
    """학사일정 정보 (School Schedule Information).

    Information about school academic schedules from NEIS.

    Attributes:
        schedule_id: Schedule ID
        school_code: School code
        school_name: School name
        office_code: Education office code
        office_name: Education office name
        schedule_date: Schedule date
        academic_year: Academic year
        event_name: Event name
        event_content: Event content/description
        day_category: Day category
        school_course_type: School course type
        day_night_type: Day/night type
        target_grades: Target grades for the event
    """

    schedule_id: str = Field(..., alias="scheduleId", description="Schedule ID")
    school_code: str = Field(..., alias="schoolCode", description="School code")
    school_name: str = Field(..., alias="schoolName", description="School name")
    office_code: str = Field(..., alias="officeCode", description="Education office code")
    office_name: str = Field(..., alias="officeName", description="Education office name")
    schedule_date: date = Field(..., alias="scheduleDate", description="Schedule date")
    academic_year: Optional[str] = Field(None, alias="academicYear", description="Academic year")
    event_name: Optional[str] = Field(None, alias="eventName", description="Event name")
    event_content: Optional[str] = Field(
        None, alias="eventContent", description="Event description"
    )
    day_category: Optional[str] = Field(None, alias="dayCategory", description="Day category")
    school_course_type: Optional[str] = Field(
        None, alias="schoolCourseType", description="School course type"
    )
    day_night_type: Optional[str] = Field(
        None, alias="dayNightType", description="Day/night type"
    )
    target_grades: list[int] = Field(
        default_factory=list, alias="targetGrades", description="Target grades"
    )

    model_config = ConfigDict(populate_by_name=True)
