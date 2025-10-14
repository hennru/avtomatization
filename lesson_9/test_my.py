from sqlalchemy import create_engine, text

# Подключение к MySQL
username = 'root'
password = 's9l6gz5amu'
host = 'localhost'
port = '3306'
database = 'AQA'

db_connection_string = "mysql+pymysql://root:s9l6gz5amu@localhost:3306/AQA"
engine = create_engine(db_connection_string)

with engine.connect() as connection:
    result= connection.execute(text("SELECT * FROM company"))
    rows= result.mappings().all()
    print(rows)
