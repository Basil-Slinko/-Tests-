import main
import pytest


positive_test = [201, 409]
negative_test = [400, 401, 403, 404, 406, 423, 429, 503, 507]


class TestCreateNewFolder:

    @pytest.mark.parametrize('http_code', positive_test)
    def test_create_a_folder_positive_test(self, http_code):
        assert main.create_a_folder() == http_code, 'Папка создана'

    @pytest.mark.parametrize('http_code', negative_test)
    def test_create_a_folder_positive_test(self, http_code):
        assert main.create_a_folder() != http_code, f'Папку создать не удалось. ' \
                                                    f'Код ошибки -- {http_code}'
