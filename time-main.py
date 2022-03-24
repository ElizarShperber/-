
import time
print(time.strftime('%M',time.gmtime())) # вывод минут
print(time.strftime('%X',time.gmtime())) # время
print(time.strftime('%m',time.gmtime())) # месяц
print(time.strftime('%x',time.gmtime())) # дата
import os
start_path = os.getcwd()
print(os.listdir())  # ['SnapchatLoader', 'FBLoader', 'tmp.py', '.gitignore', 'venv', '.git']

if 'tmp.py' not in os.listdir():
    print(start_path)
    print(os.path.join(start_path, 'test'))