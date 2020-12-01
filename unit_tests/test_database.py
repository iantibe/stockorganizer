import unittest
from Database import Database


class MyTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_get_stock_id(self):
        pass

    def test_wrong_argument_in_get_stock_id(self):
        pass

    def test_no_results_in_get_stock_id(self):
        pass

    def test_get_stock(self):
        pass

    def test_wrong_parameter_get_stock(self):
        pass

    def test_get_stock_with_no_saved_transactions(self):
        pass

    def test_create_new_stock(self):
        pass

    def test_wrong_argument_create_new_stock(self):
        pass

    def test_save_transaction(self):
        pass

    def test_wrong_arguemnt_save_transaction(self):
        pass

    def test_wrong_argument_save_transaction(self):
        pass

    def test_return_value_save_transaction(self):
        pass

    def test_get_transaction(self):
        pass

    def test_wrong_input_get_transaction(self):
        pass

    def test_delete_transaction(self):
        pass

    def test_wrong_argument_delete_transaction(self):
        pass

    def test_delete_stock(self):
        pass

    def test_delete_stock_wrong_argument(self):
        pass



if __name__ == '__main__':
    unittest.main()
