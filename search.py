import os

def find_files_with_2_in_first_position(directory):
    # Список для хранения имен файлов
    files_with_2 = []

    # Проходим по всем файлам в указанной директории
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        # Проверяем, является ли путь файлом
        if os.path.isfile(filepath):
            with open(filepath, 'r') as file:
                # Читаем файл построчно
                for line in file:
                    # Убираем лишние пробелы и проверяем первую позицию
                    if line.strip().startswith('2'):
                        files_with_2.append(filename)
                        break  # Прерываем цикл, чтобы не проверять остальные строки

    return files_with_2

# Укажите путь к директории
directory = rf'C:\WorkSpace\Diplom\dataset_reserch\dataset_for_reserch_CSGO_70_20_10\test\labels'

# Получаем список файлов
files_with_2 = find_files_with_2_in_first_position(directory)

# Выводим результат
print("Файлы, в которых на первой позиции строки стоит '2':")
for file in files_with_2:
    print(file)