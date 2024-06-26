import tkinter as tk
from tkinter import messagebox, TOP
import keyboard
import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import random
import os

username = os.getenv('USERNAME')

def code():
    first_number = random.randint(1, 9) * 1000
    second_number = random.randint(0, 9) * 100
    third_number = random.randint(0, 9) * 10
    fourth_number = random.randint(0, 9)
    return first_number+second_number+third_number+fourth_number

ACCESS_CODE = code()

#Подключение к бд и отправка кода
try:
    # Подключение к существующей базе данных
    connection = psycopg2.connect(dbname='Authentication',
                                  user="KVA",
                                  password="sa",
                                  )
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    # Курсор для выполнения операций с базой данных
    cursor = connection.cursor()
    cursor.execute("Update university_users set code = %s where username = %s", (ACCESS_CODE, username))
    results = cursor.fetchall()
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()

def on_key_event(event):
    global ACCESS_CODE
    if event.event_type == keyboard.KEY_DOWN and event.name == 'enter':  # Проверяем только при нажатии клавиши 'enter'
        if int(entry.get()) == ACCESS_CODE:
            root.destroy()
            keyboard.unhook_all()
        else:
            messagebox.showerror("Ошибка", "Неверный код!")
            entry.delete(0, 'end')
    return False

import pyautogui

keyboard.block_key('Ctrl')
keyboard.block_key('Shift')
keyboard.block_key('Esc')
keyboard.block_key('Alt')
keyboard.block_key('Win')


#создание окна
root = tk.Tk()
root.attributes("-fullscreen", True)
root.title("Введите код доступа")

label = tk.Label(root, text="Введите код доступа:", font=("Arial", 14))
label.pack()
label.place(relx=0.5, rely=0.4, anchor='center')

entry = tk.Entry(root, show="*")
entry.pack()
entry.place(relx=0.5, rely=0.5, anchor='center')




keyboard.hook(on_key_event)

root.mainloop()