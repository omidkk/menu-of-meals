from app import db


class WeekModel(db.Model):
    """
    Data model for Week DB table.
    """

    __tablename__ = "week"

    id = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    start_date = db.Column(db.DATE, nullable=False)
    end_date = db.Column(db.DATE, nullable=False)

    def _to_dict(self):
        return {
            "id": self.id,
            "start_date": self.credential_type_id,
            "end_date": self.credential_type_label,
        }

    def _clone(self):
        return WeekModel(
            id=self.id,
            start_date=self.start_date,
            end_date=self.end_date,
        )
