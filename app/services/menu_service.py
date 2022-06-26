from app.persistence.menu_persistence import MenuPersistence
from datetime import datetime


class MenuService:
    @classmethod
    def get_date_menu(cls, meal_type: str, date: datetime):
        return MenuPersistence.get_menu_by_date_type(meal_type, date)
