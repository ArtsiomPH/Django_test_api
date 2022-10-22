import pytest
from api.models import User
import json


class TestGETReq:
    base_url = "http://127.0.0.1:8000/api/v1/users/"

    @pytest.mark.django_db
    def test_get_returns_json_200(self, client):
        response = client.get(self.base_url)
        assert response.status_code == 200
        assert response['content-type'] == 'application/json'

    @pytest.mark.django_db
    def test_get_return_item(self, client):
        new_user = {
            "id": 1,
            "first_name": "TIK",
            "last_name": "TOK",
            "country": "BEL",
            "birth_date": "1994-12-24",
            "height": "170.00",
            "weight": "50.00"
        }
        User.objects.create(**new_user)
        new_user.update({"birth_date": "24-12-1994"})
        response = client.get(self.base_url)
        assert response.status_code == 200
        assert json.loads(response.content)['results'][0] == new_user

    @pytest.mark.django_db
    def test_get_return_correct_item(self, client, get_two_users):
        new_user_1, new_user_2 = get_two_users
        User.objects.create(**new_user_1)
        User.objects.create(**new_user_2)
        new_user_2.update({"birth_date": "24-12-1994"})

        response = client.get(self.base_url+'2/')
        assert response.status_code == 200
        assert json.loads(response.content) == new_user_2


    @pytest.mark.parametrize('type_of_ord', ('asc', 'desc'))
    @pytest.mark.parametrize('ordering_field', ('id', 'first_name', 'last_name', 'birth_date', 'height', 'weight'))
    @pytest.mark.django_db
    def test_ordering_asc_desc(self, client, get_two_users, ordering_field, type_of_ord):
        new_user_1, new_user_2 = get_two_users
        User.objects.create(**new_user_1)
        User.objects.create(**new_user_2)
        new_user_1.update({"birth_date": "24-12-1993"})
        new_user_2.update({"birth_date": "24-12-1994"})

        if type_of_ord == 'asc':
            response = client.get(path=self.base_url + f'?ordering={ordering_field}')
            assert json.loads(response.content)['results'][0] == new_user_1
        if type_of_ord == 'desc':
            response = client.get(path=self.base_url + f'?ordering=-{ordering_field}')
            assert json.loads(response.content)['results'][0] == new_user_2

    @pytest.mark.parametrize(('param', 'value'), (('id', 1), ('first_name', 'TIK'), ('last_name', 'TOK'),
                                                  ('birth_date', '1993-12-24'), ('height', '170.00'),
                                                  ('weight', '50.00')))
    @pytest.mark.django_db
    def test_return_correct_item_by_qwery_param(self, client, get_two_users, param, value):
        new_user_1, new_user_2 = get_two_users
        User.objects.create(**new_user_1)
        User.objects.create(**new_user_2)
        new_user_1.update({"birth_date": "24-12-1993"})

        response = client.get(path=self.base_url + f'?{param}={value}')
        assert json.loads(response.content)['results'][0] == new_user_1

    @pytest.mark.parametrize('param', ('min', 'max'))
    @pytest.mark.parametrize(('field', 'value'), (('height', '175.00'), ('weight', '55.00'),
                                                  ('bday', '1994-06-12')))
    @pytest.mark.django_db
    def test_return_correct_item_by_min_max_param(self, client, get_two_users, param, field, value):
        new_user_1, new_user_2 = get_two_users
        User.objects.create(**new_user_1)
        User.objects.create(**new_user_2)
        new_user_1.update({"birth_date": "24-12-1993"})
        new_user_2.update({"birth_date": "24-12-1994"})

        if param == 'min':
            response = client.get(path=self.base_url + f'?{param}_{field}={value}')
            assert json.loads(response.content)['results'][0] == new_user_2
        if param == 'max':
            response = client.get(path=self.base_url + f'?{param}_{field}={value}')
            assert json.loads(response.content)['results'][0] == new_user_1





