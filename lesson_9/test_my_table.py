import pytest
from sqlalchemy import create_engine, text

# Подключение к MySQL
db_connection_string = "mysql+pymysql://root:s9l6gz5amu@localhost:3306/AQA"
engine = create_engine(db_connection_string)


def test_create_species():
    with engine.connect() as connection:
        sql = text(
            "INSERT INTO species (species_id, species_name) VALUES (:id, :name)")
        connection.execute(sql, {"id": 25, "name": "пёс"})
        connection.commit()


def test_update_species():
    with engine.connect() as connection:
        sql = text(
            "UPDATE species SET species_name = :name WHERE species_id = :id")
        connection.execute(sql, {"name": 'кот', "id": 25})
        connection.commit()


def test_delete_species():
    with engine.connect() as connection:
        sql = text("DELETE FROM species WHERE species_id = :id")
        connection.execute(sql, {"id": 25})
        connection.commit()
