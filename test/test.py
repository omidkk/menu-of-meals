# pylint: disable=redefined-outer-name

from datetime import datetime

import pytest

from app.create_app import create_app
from app.services.menu_service import MenuService

app = create_app()


@pytest.fixture
def invalid_date():
    date = "2022-02-28"
    return datetime.strptime(date, "%Y-%m-%d"), "MEAL_KIT"


@pytest.fixture
def invalid_type():
    date = "2021-03-01"
    return datetime.strptime(date, "%Y-%m-%d"), "something"


@pytest.fixture
def valid_input():
    date = "2021-03-01"
    return datetime.strptime(date, "%Y-%m-%d"), "MEAL_KIT"


def test_invalid_input(invalid_date, invalid_type):
    with app.app_context():
        response_invalid_date = MenuService.get_date_menu(invalid_date[1], invalid_date[0])
        response_invalid_type = MenuService.get_date_menu(invalid_type[1], invalid_type[0])

    assert response_invalid_date == []
    assert response_invalid_type == []


def test_valid_input(valid_input):
    with app.app_context():
        response = MenuService.get_date_menu(valid_input[1], valid_input[0])

    assert response != []
