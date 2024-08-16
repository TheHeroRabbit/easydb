# EasyDB - A Simplified Python Database Client for MySQL and SQLite

## 简介

本项目提供了两个 Python 类，`MySQLClient` 和 `SQLiteClient`，用于简化 MySQL 和 SQLite 数据库的常用操作。通过这两个类，用户可以轻松地连接到数据库，执行表的创建、数据的插入、更新、删除和查询等操作。

## 特性

- **易于使用**：提供简洁的接口以进行数据库操作。
- **支持多种操作**：支持创建表、插入数据、更新数据、删除数据和查询数据等基本功能。
- **自动提交**：每次操作后自动提交更改，确保数据一致性。
- **支持字典格式的数据操作**：允许使用字典格式插入和更新数据，提高代码可读性。

## 安装

在使用这两个类之前，请确保安装了 `pymysql` 和 `sqlite3` 库。可以通过以下命令安装 `pymysql`：

```bash
pip install pymysql
```

> 注意：`sqlite3` 是 Python 标准库的一部分，通常无需单独安装。

## 用法

### 初始化

#### MySQLClient

```python
from easydb import MySQLClient

# 创建 MySQLClient 实例
db = MySQLClient(host='127.0.0.1', port=3306, user='your_username', password='your_password', database='your_database')
```

#### SQLiteClient

```python
from easydb import SQLiteClient

# 创建 SQLiteClient 实例
db = SQLiteClient()
```

### 方法调用示例

以下是 `MySQLClient` 和 `SQLiteClient` 中方法的调用示例。由于两个类的方法相同，可以使用相同的代码进行调用。

```python
# 显示所有表
tables = db.show_tables()
print("Tables:", tables)

# 创建新表
db.create_table('users', ['id', 'name', 'email'])

# 插入一条数据
db.insert_item('users', {'id': '1', 'name': 'Alice', 'email': 'alice@example.com'})

# 插入多条数据
db.insert_items('users', [
    {'id': '2', 'name': 'Bob', 'email': 'bob@example.com'},
    {'id': '3', 'name': 'Charlie', 'email': 'charlie@example.com'}
])

# 查询数据
results = db.select_item('users')
print("Users:", results)

# 更新数据
db.update_item('users', {'id': '1'}, {'email': 'alice_new@example.com'})

# 删除数据
db.delete_item('users', {'id': '2'})

# 显示列名
columns = db.show_columns('users')
print("Columns:", columns)

# 清空表
db.truncate_table('users')

# 删除表
db.drop_table('users')
```

## 注意事项

- 在使用类进行数据库操作之前，请确保数据库服务已启动（对于 MySQL）并且连接信息正确。
- 对于数据的插入和更新操作，确保提供的字典与表结构相符。
- 在进行删除和更新操作时，请谨慎使用条件，以避免误操作。
