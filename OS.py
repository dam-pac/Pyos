import os
import sqlite3
def delete_file(file_name):
    try:
        os.remove(f"{os.path.abspath(file_name)}")
        return 0
    except FileNotFoundError:
        return 1
    except:
        return 2
def cwd():
    try:
        return os.getcwd()
    except:
        return 1
def cd(path):
    try:
        os.chdir(path)
        return 0
    except FileNotFoundError:
        return 1
    except:
        return 2
def dir(path="."):
    try:
        return os.listdir(path)
    except FileNotFoundError:
        return 1
    except:
        return 2
def clear():
    os.system("clear")
def login():
    # start
    connection = sqlite3.connect('user_data.db')
    cursor = connection.cursor()
    try:
        cursor.execute('SELECT username FROM users')
        users = cursor.fetchall()
        _ = True
        while _ == True:
            username = input("LOGIN: ")
            password = input("PASSWORD: ")
            for i in users:
                if username == i:
                    login_suc = True
                    cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
                    passworddb = cursor.fetchall()
                    for i in passworddb:
                        if i == password:
                            print(f"Welcome to the PYOS {username}!")
                            return [username, True]
                else:
                    login_suc = False
    except sqlite3.OperationalError:
        # создание пользователя
        print("Creating users to this PYOS...")
        print("WELCOME to the USERCREATOR tool! == Usercreator program start automatically ==")
        _ = True
        while _ == True:
            newuser = input("Input a new Username: ")
            newpassword = input(f"Input a new Password for {newuser}: ")
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                )
                ''')
            connection.commit()
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (newuser, newpassword,))
            connection.commit()
            connection.close()
            login()
            return
