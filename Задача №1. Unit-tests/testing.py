import main
from unittest import mock


class TestSecretaryProgram:

    def test_check_document_existance(self):
        assert main.check_document_existance('10006') == True

    def test_get_doc_owner_name(self):
        with mock.patch('builtins.input', return_value="10006"):
            assert main.get_doc_owner_name() == "Аристарх Павлов"

    def test_get_all_doc_owners_names(self):
        assert main.get_all_doc_owners_names() == {'Василий Гупкин', 'Геннадий Покемонов', 'Аристарх Павлов'}

    def test_add_new_shelf(self):
        assert main.add_new_shelf('4') == ('4', True)

    def test_append_doc_to_shelf(self):
        main.append_doc_to_shelf('11-11', '5')
        assert main.directories['5'][0] == '11-11'

    def test_get_doc_shelf(self):
        with mock.patch('builtins.input', return_value='10006'):
            assert main.get_doc_shelf() == '2'

    def test_move_doc_to_shelf(self):
        with mock.patch('builtins.input', side_effect=['10006', '3']):
            assert main.move_doc_to_shelf() == 'Документ номер "10006" был перемещен на полку номер "3"'

    def test_add_new_doc(self):
        with mock.patch('builtins.input', side_effect=['6765 090000', 'passport', 'Антон Иванов', '5']):
            assert main.add_new_doc() == '5'

    def test_delete_doc(self):
        with mock.patch('builtins.input', return_value='10006'):
            assert main.delete_doc() == ('10006', True)

