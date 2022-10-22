import pytest
from api.models import User


@pytest.fixture(scope='function')
def get_two_users():
    new_user_1 = {
        "id": 1,
        "first_name": "TIK",
        "last_name": "TOK",
        "country": "BEL",
        "birth_date": "1993-12-24",
        "height": "170.00",
        "weight": "50.00"
    }
    new_user_2 = {
        "id": 2,
        "first_name": "UOO",
        "last_name": "UFO",
        "country": "DEN",
        "birth_date": "1994-12-24",
        "height": "180.00",
        "weight": "60.00"
    }
    return new_user_1, new_user_2

