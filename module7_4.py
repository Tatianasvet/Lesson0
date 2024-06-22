
import os
import time

directory = os.path.dirname(__file__)

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        file_size = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file:<30} Путь: {filepath:<80} Размер:{file_size:>5} байт,\t'
              f'Время изменения: {formatted_time},\tРодительская директория: {parent_dir}')
