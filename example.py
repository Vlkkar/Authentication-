import hashlib

# Создание хеша с использованием SHA-256
message = "sa"
hash_object_md5 = hashlib.md5(message.encode())
md5_hash = hash_object_md5.hexdigest()
print(md5_hash)

import os

username = os.getenv('USERNAME')
print(f"Имя пользователя Windows: {username}")



import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
try:
    # Подключение к существующей базе данных
    connection = psycopg2.connect(dbname='Authentication',
                                  user="KVA",
                                  # пароль, который указали при установке PostgreSQL
                                  password="sa",
                                  )
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    # Курсор для выполнения операций с базой данных
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM university_users ")
    results = cursor.fetchall()

    # Вывод результатов
    for row in results:
        print(row)
    #sql_create_database = 'create database postgres_db'
    #cursor.execute(sql_create_database)
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")



