from sqlalchemy import create_engine, text

# Замените на свои данные
username = 'dbviv'
password = ''
host = 'localhost'
port = '5432'
database = 'QA'

engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database}')

# Пример использования
with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM company"))
    rows = result.mappings().all()
    print(rows)