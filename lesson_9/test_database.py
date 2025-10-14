from sqlalchemy import create_engine, inspect, text

db_connection_string = "postgresql://dbviv:p_kir@localhost:5432/AQA"
db = create_engine(db_connection_string)


def test_db_connection():
    # Используем инспектор для получения информации о таблицах
    inspector = inspect(db)

    # Получаем список таблиц
    tables = inspector.get_table_names()
    assert 'persons' in tables  # Проверяем, что таблица persons существует

    # Используем инспектор для получения информации о таблицах
    names = inspector.get_table_names()
    assert names[0] == 'tags'

    #select * from company
def test_select():
    connection = db.connect()
    result = connection.execute(text("SELECT * FROM company"))
    rows = result.mappings().all()
    row1 = rows[0]
    assert row1['id'] == 1
    assert row1['name'] == "QA 'Тестировщик'"

    connection.close()

#SELECT * FROM company WHERE id = 1
def test_select_1_row():
    connection = db.connect()
    sql_statement = text("SELECT * FROM company WHERE id = :company_id")
    result = connection.execute(sql_statement, {"company_id": 1})
    rows = result.mappings().all()

    assert len(rows) == 1
    assert rows[0]["name"] == "QA 'Тестировщик'"

    connection.close()

#SELECT * FROM company WHERE is_active = true AND id >= 65
def test_select_1_row_with_two_filters():
    connection = db.connect()
    sql_statement = text("SELECT * FROM company "
                             "WHERE is_active = :is_active AND id >= :id")
    result = connection.execute(sql_statement, {'id': 65, 'is_active': True})
    rows = result.mappings().all()

    assert len(rows) == 48

    connection.close()