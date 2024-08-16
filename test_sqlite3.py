import unittest
from easydb import SQLiteClient


class TestSQLiteClient(unittest.TestCase):

    def setUp(self):
        """
        每个测试前执行，初始化数据库连接，并清空所有表
        """
        self.db = SQLiteClient()
        self.db.cursor.execute("DROP TABLE IF EXISTS test_table;")
        self.db.connect.commit()

    def tearDown(self):
        """
        每个测试后执行，关闭数据库连接
        """
        self.db.connect.close()

    def test_create_table(self):
        self.assertTrue(self.db.create_table('test_table', ['column1', 'column2']))
        tables = self.db.show_tables()
        self.assertIn('test_table', tables)

    def test_show_columns(self):
        self.db.create_table('test_table', ['column1', 'column2'])
        columns = self.db.show_columns('test_table')
        self.assertListEqual(columns, ['column1', 'column2'])

    def test_truncate_table(self):
        self.db.create_table('test_table', ['column1', 'column2'])
        self.db.insert_item('test_table', {'column1': 'value1', 'column2': 'value2'})
        self.db.truncate_table('test_table')
        items = self.db.select_item('test_table')
        self.assertEqual(len(items), 0)

    def test_drop_table(self):
        self.db.create_table('test_table', ['column1', 'column2'])
        self.assertTrue(self.db.drop_table('test_table'))
        tables = self.db.show_tables()
        self.assertNotIn('test_table', tables)

    def test_insert_item(self):
        self.db.create_table('test_table', ['column1', 'column2'])
        self.assertTrue(self.db.insert_item('test_table', {'column1': 'value1', 'column2': 'value2'}))
        items = self.db.select_item('test_table')
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0], ('value1', 'value2'))

    def test_insert_items(self):
        self.db.create_table('test_table', ['column1', 'column2'])
        items = [
            {'column1': 'value1', 'column2': 'value2'},
            {'column1': 'value3', 'column2': 'value4'}
        ]
        self.assertTrue(self.db.insert_items('test_table', items))
        result = self.db.select_item('test_table')
        self.assertEqual(len(result), 2)

    def test_delete_item(self):
        self.db.create_table('test_table', ['column1', 'column2'])
        self.db.insert_item('test_table', {'column1': 'value1', 'column2': 'value2'})
        self.assertTrue(self.db.delete_item('test_table', {'column1': 'value1'}))
        items = self.db.select_item('test_table')
        self.assertEqual(len(items), 0)

    def test_select_item(self):
        self.db.create_table('test_table', ['column1', 'column2'])
        self.db.insert_item('test_table', {'column1': 'value1', 'column2': 'value2'})
        items = self.db.select_item('test_table', {'column1': 'value1'})
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0], ('value1', 'value2'))

    def test_update_item(self):
        self.db.create_table('test_table', ['column1', 'column2'])
        self.db.insert_item('test_table', {'column1': 'value1', 'column2': 'value2'})
        self.assertTrue(self.db.update_item('test_table', {'column1': 'value1'}, {'column2': 'new_value'}))
        items = self.db.select_item('test_table', {'column1': 'value1'})
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0][1], 'new_value')


if __name__ == '__main__':
    unittest.main()
