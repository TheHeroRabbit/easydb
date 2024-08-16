import unittest
from easydb import MySQLClient


class TestMySQLClient(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 设置数据库连接信息
        cls.db = MySQLClient(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='123456',
            database='test_db'
        )
        # 创建一个测试表
        cls.db.create_table('test_table', ['id', 'name', 'value'])

    @classmethod
    def tearDownClass(cls):
        # 删除测试表
        cls.db.drop_table('test_table')
        cls.db.connect.close()

    def setUp(self):
        # 每个测试前清空表
        self.db.truncate_table('test_table')

    def test_show_tables(self):
        tables = self.db.show_tables()
        self.assertIn('test_table', tables)

    def test_show_columns(self):
        columns = self.db.show_columns('test_table')
        self.assertListEqual(columns, ['id', 'name', 'value'])

    def test_create_table(self):
        self.db.create_table('new_table', ['column1', 'column2'])
        tables = self.db.show_tables()
        self.assertIn('new_table', tables)
        self.db.drop_table('new_table')

    def test_truncate_table(self):
        self.db.insert_item('test_table', {'id': '1', 'name': 'test', 'value': '123'})
        self.db.truncate_table('test_table')
        items = self.db.select_item('test_table')
        self.assertEqual(len(items), 0)

    def test_drop_table(self):
        self.db.create_table('to_drop_table', ['column1'])
        self.db.drop_table('to_drop_table')
        tables = self.db.show_tables()
        self.assertNotIn('to_drop_table', tables)

    def test_insert_item(self):
        self.db.insert_item('test_table', {'id': '1', 'name': 'test', 'value': '123'})
        items = self.db.select_item('test_table')
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]['id'], '1')
        self.assertEqual(items[0]['name'], 'test')
        self.assertEqual(items[0]['value'], '123')

    def test_insert_items(self):
        items = [
            {'id': '1', 'name': 'test1', 'value': '123'},
            {'id': '2', 'name': 'test2', 'value': '456'}
        ]
        self.db.insert_items('test_table', items)
        results = self.db.select_item('test_table')
        self.assertEqual(len(results), 2)

    def test_delete_item(self):
        self.db.insert_item('test_table', {'id': '1', 'name': 'test', 'value': '123'})
        self.db.delete_item('test_table', {'id': '1'})
        items = self.db.select_item('test_table')
        self.assertEqual(len(items), 0)

    def test_select_item(self):
        self.db.insert_item('test_table', {'id': '1', 'name': 'test', 'value': '123'})
        items = self.db.select_item('test_table', {'id': '1'})
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]['name'], 'test')

    def test_update_item(self):
        self.db.insert_item('test_table', {'id': '1', 'name': 'test', 'value': '123'})
        self.db.update_item('test_table', {'id': '1'}, {'name': 'updated'})
        items = self.db.select_item('test_table', {'id': '1'})
        self.assertEqual(items[0]['name'], 'updated')


if __name__ == '__main__':
    unittest.main()
