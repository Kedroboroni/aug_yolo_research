import os

def rename_files_in_directory(directory):
    # Проверяем, существует ли указанная папка
    if not os.path.exists(directory):
        print(f"Папка {directory} не существует.")
        return

    # Получаем список всех файлов в папке
    for filename in os.listdir(directory):
        # Полный путь к файлу
        file_path = os.path.join(directory, filename)

        # Проверяем, что это файл, а не папка
        if os.path.isfile(file_path):
            # Разделяем имя файла и расширение
            name, ext = os.path.splitext(filename)

            # Новое имя файла с суффиксом _3
            new_name = f"{name}_8{ext}"

            # Полный путь к новому имени файла
            new_file_path = os.path.join(directory, new_name)

            # Переименовываем файл
            os.rename(file_path, new_file_path)
            print(f"Файл {filename} переименован в {new_name}")

# Укажите путь к папке с файлами
path_to_directory = r"C:\WorkSpace\Python\machinist_help\8"

# Вызов функции для переименования файлов
rename_files_in_directory(path_to_directory)