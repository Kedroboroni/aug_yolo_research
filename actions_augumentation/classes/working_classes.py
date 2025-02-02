#Файл для работы с классами (подсчет количества классов, найти уникалььные классы, вывести графики классов и т.д)
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import sys, os
from aug.core_aug import *
from convert_utils import convert
import matplotlib.pyplot as plt
from typing import List, Tuple
import numpy as np

def score_classes(file_path) -> np.array:
    """
    Считает количество повторений класса в словарь.
    
    Параметры:
    file_path (str): Путь к директории с текстовыми файлами.
    
    Возвращает:
    np.array: Массив с классами и их количеством.
    """
    array_txtFile = np.array(
        [
            rf"{file_path}\{file}"
            for file in os.listdir(file_path)
            if file.endswith('.txt') 
        ]
    )
    
    result = np.array([read_yolo_class(file) for file in array_txtFile])



    return result

def display_graph(data: dict) -> dict:
    """
    Выводит столбчатую диаграмму для классов, расположенных в папке.
    
    Параметры:
    data (dict): Словарь с классами и их количеством.
    
    Возвращает:
    dict: Исходный словарь с классами.
    """
    keys = list(data.keys())
    values = list(data.values())
    plt.figure(figsize=(4, 3))

    width = 0.8 / len(keys)
    rects = plt.bar(keys, values, width=1.0, color=plt.cm.rainbow(np.linspace(0, 1, len(values))))

    plt.title('Данные по классам')
    plt.xlabel('Имя класса')
    plt.ylabel('Количество')

    plt.show()

    return data

def serch_small_classes(data: dict) -> list:
    """
    Находит малочисленные классы в данных.
    
    Параметры:
    data (dict): Словарь с классами и их количеством.
    
    Возвращает:
    list: Список малочисленных классов.
    """
    result = []
    average = int(sum(data.values()) / len(data))
    max_valuses = max(data.values())
    for value in data.items():

        if value[1] < max_valuses - average:
            
            result.append(value)

    return result

def uniq_class(directory: str) -> list:
    """
    Извлекает уникальные имена объектов из текстовых файлов в указанной директории и сохраняет их в файл.
    
    Параметры:
    directory (str): Путь к директории, содержащей подпапки с текстовыми файлами.
    
    Возвращает:
    list: Список уникальных имен объектов, найденных в текстовых файлах.
    """
    path_file = [f"{directory}\\{file}" for file in os.listdir(directory)]
    
    unique_objects = set()
    for files in path_file:
        txt_files = [rf"{files}\\{file}" for file in os.listdir(files) if file.endswith('.txt')]
        print(rf"===============================\nРаботаю с папкой\n {files} \n=============================== ")
        for i, txt_file in enumerate(txt_files):
            print(i)
            
            with open(txt_file, 'r', encoding='utf-8') as file:
                for line in file:
                    words = line.strip().split()
                    if words:
                        object_name = words[0]
                        unique_objects.add(object_name)

        with open("objects.txt", 'w', encoding='utf-8') as file:
            file.write("\n".join(map(str, list(unique_objects))))

    return list(unique_objects)





if __name__ == "__main__":

    path = r"C:\WorkSpace\Python\machinist_help\aug\dataset"
    #data = read_yolo_class(path)
    data = score_classes(path)
    print(data.shape)
    #small_classes = [obj for obj in serch_small_classes(data)[0]]
    #s = display_graph(data)
    #print(small_classes)
    #print(list(data.keys()))
    #print(serch_small_classes(data))
    #print(f"----------------{s}-------------")








        