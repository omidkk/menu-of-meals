from app import db


class MealWeekModel(db.Model):
    """
    Data model for Meal Week DB table.
    """

    __tablename__ = "meal_week"

    week_id = db.Column(db.BIGINT, primary_key=True)
    meal_id = db.Column(db.BIGINT, primary_key=True)

    def _to_dict(self):
        return {
            "week_id": self.week_id,
            "meal_id": self.meal_id,
        }

    def _clone(self):
        return MealWeekModel(week_id=self.week_id, meal_id=self.meal_id,)
