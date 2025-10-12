from sqlalchemy import create_engine, inspect, text

# Подключение к MySQL
db_connection_string = "mysql+pymysql://root:s9l6gz5amu@localhost:3306/AQA"
db = create_engine(db_connection_string)


def test_db_connection():
    inspector = inspect(db)
    tables = inspector.get_table_names()
    assert 'persons' in tables
    names = inspector.get_table_names()
    assert 'tags' in names


def test_select():
    connection = db.connect()
    result = connection.execute(text("SELECT * FROM company"))
    rows = result.mappings().all()
    row1 = rows[0]
    assert row1['id'] == 1
    assert row1['name'] == "QA 'Тестировщик'"
    connection.close()


def test_select_1_row():
    connection = db.connect()
    sql_statement = text("SELECT * FROM company WHERE id = :company_id")
    result = connection.execute(sql_statement, {"company_id": 1})
    rows = result.mappings().all()
    assert len(rows) == 1
    assert rows[0]["name"] == "QA 'Тестировщик'"
    connection.close()


def test_select_1_row_with_two_filters():
    connection = db.connect()
    sql_statement = text(
        "SELECT * FROM company WHERE is_active = :is_active AND id >= :id")
    result = connection.execute(sql_statement, {'id': 65, 'is_active': True})
    rows = result.mappings().all()
    # оставь как в тестах, но число можно скорректировать под твои данные
    assert len(rows) == 2
    connection.close()
