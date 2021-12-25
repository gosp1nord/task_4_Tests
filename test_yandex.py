import pytest
import requests


token = 'здесь вставить ключ API'
CHEK_LIST = [
        (token, 'fold_1', 201),
        (token, 'fold_1', 409),
        (token, '//_1', 404),
        ('111222333444555666', 'fold_1', 401),
        (token, 'fold_1', 409),
        (token, 'fold_1', 409),
        (token, 'fold_1', 409)
    ]


def create_folder(token, name):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'OAuth {token}'
    }
    params = {
        'path': name
    }
    response = requests.put(url=url, headers=headers, params=params)
    return response.status_code


class Test_Y:

    @pytest.mark.parametrize('token, name, exp_result', CHEK_LIST)
    def test_create_folder(self, token, name, exp_result):
        assert create_folder(token, name) == exp_result
