import unittest
import click_data_store


class ClickTesCase(unittest.TestCase):

    def test_click_set_value(self):
        data = {}
        click_data_store.set_value(data, 'a', 2)
        self.assertEqual(data['a'], 2)

    def test_click_get_value(self):
        data = {}
        click_data_store.set_value(data, 'b', 3)
        self.assertEqual(click_data_store.get_value(data, 'b'), 3)

    def test_click_delete_value(self):
        data = {}
        click_data_store.set_value(data, 'b', 3)
        click_data_store.delete_value(data, 'b')
        self.assertEqual(click_data_store.get_value(data, 'b'), None)


if __name__ == '__main__':
    unittest.main()
