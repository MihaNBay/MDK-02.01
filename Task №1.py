import sqlite3 as sql
import os

def create_db(name):
    if name != "":
        if not os.path.exists(f"{name}.db"):
            with sql.connect(f"{name}.db") as connection:
                cursor = connection.cursor()

                cursor.execute("""
                CREATE TABLE IF NOT EXISTS datelist (
                    name TEXT,
                    city TEXT,
                    age INTEGER
                )""")

                print(f"База данных с название {name} создана успешно! Поля для ввода Имя, Город и Возраст.")
        else:
            print("Ошибка, база данных с таким название уже существует.")
    else:
        print("Ошибка, введите название новой базы данных.")

def add_date(name, value_name, value_city, value_age):
    with sql.connect(f"{name}.db") as connection:
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO datelist(name, city, age) VALUES (?, ?, ?)""", (value_name, value_city, value_age))

def get_date(name):
    with sql.connect(f"{name}.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM datelist")
        user = cursor.fetchall()
        print(user)

while True:
    try:
        num = int(input("\nВведите номер команды.\n 1. Создать новую базу данных\n 2. Прочитать базу данных\n 3. Добавить значения в базу данных\n 0. Для выхода из программы\n Поле ввода: "))
    except:
        print("Вводите только номер команды!")
        break

    if num == 0:
        print("Вы завершили работать с программой.")
        break
    else:
        if num == 1:
            name = input("Для создание новой базы данных, введите название базы данных без .db(Пример: primerdb): ")
            create_db(name)
        elif num == 2:
            name = input("Для вывода данных с базы данных, введите название базы данных без .db(Пример: primerdb): ")
            get_date(name)
        elif num == 3:
            name = input("Для добавления значения в базу данных, введите название базы данных без .db(Пример: primerdb): ")
            value_name = input("Введите имя: ")
            value_city = input("Введите город: ")
            value_age = int(input("Введите возраст: "))
            add_date(name, value_name, value_city, value_age)

