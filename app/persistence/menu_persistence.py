from datetime import datetime

from sqlalchemy import and_, func

from app import db
from app.model.meal_model import MealModel
from app.model.meal_week_model import MealWeekModel
from app.model.week_model import WeekModel


class MenuPersistence:
    @classmethod
    def get_menu_by_date_type(cls, meal_type: str, date: datetime) -> list:
        result = (
            db.session.query(WeekModel, MealWeekModel, MealModel)
            .with_entities(MealModel.name)
            .filter(and_(WeekModel.start_date <= date, WeekModel.end_date >= date))
            .filter(MealWeekModel.week_id == WeekModel.id)
            .filter(func.lower(MealModel.type) == func.lower(meal_type), MealModel.id == MealWeekModel.meal_id)
            .all()
        )

        result = [x for xs in result for x in xs]
        return result
