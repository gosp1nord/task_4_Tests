import pytest
import work
import unittest.mock


DOC_NUMBER = [("10006", True), ("11-2", True), ("32100", False), (11223, False)]
DOC_NUMBER_NAME = [("10006", "Аристарх Павлов"), ("11-2", "Геннадий Покемонов"), ("32100", None), (11223, None)]
DOC_LIST_NAME = [{"Василий Гупкин", "Геннадий Покемонов", "Аристарх Павлов"}]
DOC_NUMBER_REMOVE = [
    ("10007", False),
    ("11-3", False),
    ('2207 876234', True)
]
NEW_SHELF_NUMBER = [("1", ('1', False)), ("2", ('2', False)), ("4", ('4', True))]
DOC_DEL_NUMBER = [("10006", ('10006', True)), ("11-2", ('11-2', True))]
DOC_NUMBER_SHELF = [("10006", "2"), ("11-2", "1"), ("32100", None), (11223, None)]
DOC_TO_SHELF = [
    ("10006", "1", 'Документ номер "10006" был перемещен на полку номер "1"'),
    ("11-2", "6", 'Документ номер "11-2" был перемещен на полку номер "6"'),
    ("32100", "3", 'Документ номер "32100" был перемещен на полку номер "3"')
]
DOC_SHOW = [
    ({"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"}, 'passport "2207 876234" "Василий Гупкин"'),
    ({"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"}, 'invoice "11-2" "Геннадий Покемонов"')
]
ALL_DOCS_SHOW = [['passport "2207 876234" "Василий Гупкин"', 'invoice "11-2" "Геннадий Покемонов"', 'insurance "10006" "Аристарх Павлов"']]
ADD_DOC = [
    ("236", "invoice", "Сергей Светлов", "3", '3'),
    ("22-9", "invoice", "Евгений", "2", '2')
]

class Test_work:

    @pytest.mark.parametrize('doc_number, exp_result', DOC_NUMBER)
    def test_check_document_existance(self, doc_number, exp_result):
        assert work.check_document_existance(doc_number) == exp_result

    @pytest.mark.parametrize('doc_number, exp_result', DOC_NUMBER_NAME)
    def test_get_doc_owner_name(self, doc_number, exp_result):
        with unittest.mock.patch('builtins.input', return_value=doc_number):
            assert work.get_doc_owner_name() == exp_result
    #
    @pytest.mark.parametrize('exp_result', DOC_LIST_NAME)
    def test_get_all_doc_owners_names(self, exp_result):
        assert work.get_all_doc_owners_names() == exp_result

    @pytest.mark.parametrize('shelf_number, exp_result', NEW_SHELF_NUMBER)
    def test_add_new_shelf(self, shelf_number, exp_result):
        assert work.add_new_shelf(shelf_number) == exp_result

    @pytest.mark.parametrize('doc_number, exp_result', DOC_NUMBER_SHELF)
    def test_get_doc_shelf(self, doc_number, exp_result):
        with unittest.mock.patch('builtins.input', return_value=doc_number):
            assert work.get_doc_shelf() == exp_result

    @pytest.mark.parametrize('doc_number, shelf_number, exp_result', DOC_TO_SHELF)
    def test_move_doc_to_shelf(self, doc_number, shelf_number, exp_result):
        assert work.move_doc_to_shelf(doc_number, shelf_number) == exp_result

    @pytest.mark.parametrize('docs, exp_result', DOC_SHOW)
    def test_show_document_info(self, docs, exp_result):
        assert work.show_document_info(docs) == exp_result

    @pytest.mark.parametrize('exp_result', ALL_DOCS_SHOW)
    def test_show_all_docs_info(self, exp_result):
        assert work.show_all_docs_info() == exp_result

    @pytest.mark.parametrize('doc_number, doc_type, owner, shelf, exp_result', ADD_DOC)
    def test_add_new_doc(self, doc_number, doc_type, owner, shelf, exp_result):
        assert work.add_new_doc(doc_number, doc_type, owner, shelf) == exp_result

    @pytest.mark.parametrize('doc_number, exp_result', DOC_DEL_NUMBER)
    def test_delete_doc(self, doc_number, exp_result):
        with unittest.mock.patch('builtins.input', return_value=doc_number):
            assert work.delete_doc() == exp_result

    @pytest.mark.parametrize('doc_number, exp_result', DOC_NUMBER_REMOVE)
    def test_remove_doc_from_shelf(self, doc_number, exp_result):
        assert work.remove_doc_from_shelf(doc_number) == exp_result




