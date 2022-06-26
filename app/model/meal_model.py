from app import db


class MealModel(db.Model):
    """
    Data model for Meal DB table.
    """

    __tablename__ = "meal"

    id = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)

    def _to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
        }

    def _clone(self):
        return MealModel(
            id=self.id,
            name=self.name,
            type=self.type,
        )
