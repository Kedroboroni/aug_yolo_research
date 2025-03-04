#Файл в котором описаны функции конвертации координат, файлов, из одного типа в другой (из yolo в x1,y1,x2,y2 d yolo_formate и наоборот)
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import json
from PIL import Image
from aug.core_aug import *
import numpy as np





def polygon_to_bbox(polygon_str: str) -> tuple[list[float], list[tuple[float, float]]]:
    """
    Преобразует строку, представляющую полигон, в ограничивающий прямоугольник (bbox).
    
    Параметры:
    polygon_str (str): Строка, представляющая полигон в формате "{(x1;y1);(x2;y2);...}".
    
    Возвращает:
    tuple: Кортеж, содержащий:
        - Список с координатами границ [min_x, min_y, max_x, max_y].
        - Список кортежей с координатами точек полигона.
    """
    points = polygon_str.strip("{}").split(");(")
    coordinates = [tuple(map(float, point.replace("(", "").replace(")", "").split(";"))) for point in points]
    min_x = min(coord[0] for coord in coordinates)
    max_x = max(coord[0] for coord in coordinates)
    min_y = min(coord[1] for coord in coordinates)
    max_y = max(coord[1] for coord in coordinates)

    return [min_x, min_y, max_x, max_y], coordinates


def yolo_to_x1y1x2y2(coordinate: np.array, image_size) -> np.array:
    """
    Преобразует координаты из формата YOLO в формат (x1, y1, x2, y2).
    
    Параметры:
    coordinate (np.array): Координаты в формате YOLO.
    image_size (tuple): Размеры изображения (высота, ширина, каналы).
    
    Возвращает:
    np.array: Массив с преобразованными координатами.
    """
    result = []
    
    image_height, image_width, _ = image_size

    result = np.array(
        [
            [
                int(classe),
                (abs(float(x_center)) * image_width) - (abs(float(width)) * image_width) / 2,
                (abs(float(y_center)) * image_height) - (abs(float(height)) * image_height) / 2,
                (abs(float(x_center)) * image_width) + (abs(float(width)) * image_width) / 2,
                (abs(float(y_center)) * image_height) + (abs(float(height)) * image_height) / 2
            ]
            for classe, x_center, y_center, width, height in coordinate
        ], dtype=int
    )

    return result


def x1y1x2y2_to_yolo(bbox: list[float],
                    image_width: float,
                    image_height: float,
                    class_id: int) -> str:
    """
    Нормализует bbox и формирует строку в формате YOLO.
    
    Параметры:
    bbox (list[float]): Список с координатами границ [min_x, min_y, max_x, max_y].
    image_width (float): Ширина изображения.
    image_height (float): Высота изображения.
    class_id (int): Идентификатор класса.
    
    Возвращает:
    str: Строка в формате YOLO, содержащая идентификатор класса и нормализованные координаты.
    """
    min_x, min_y, max_x, max_y = bbox

    x_center = abs((min_x + max_x) / 2 / image_width)
    y_center = abs((min_y + max_y) / 2 / image_height)
    width = abs((max_x - min_x) / image_width)
    height = abs((max_y - min_y) / image_height)

    return f"{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}"


def convert_oldClass_to_newClass(
                                    file_path: str,
                                    replacment_list: list[tuple[str, str]]
                                ):
    """
    Функция для изменения классов в старом файле
    
    Параметры:
    file_path: Путь к файлу (строка)
    replacment_list: Список замен (список кортежей, где каждый кортеж состоит из двух строк)
    Кортеж, содержащий статус выполнения (булевый) и результат (булевый или исключение)
    """

    classe = read_yolo_class(file_path)
    coordinate = read_yolo_coordinates(file_path)

    for value in replacment_list:
        if value[0] in classe:
            list_index = np.where(classe == value)

            for i in list_index[0]:
                classe[i] = int(value[1])

        if len(classe) == 0:     
            return np.array([])
        
        else:
            result = np.append(
                classe,
                coordinate,
                axis = 1
            )
        
    save_yolo_annotations(file_path, result)

    return result


def convert_json_to_yolo(json_path: str, image_path: str):
    """
    Преобразует данные из JSON-файла в формат YOLO и сохраняет их в текстовый файл.

    Параметры:
    json_path (str): Путь к входному JSON-файлу, содержащему данные о целях.
    image_path (str): Путь к изображению, необходимый для получения размеров.

    Возвращает:
    None: Функция не возвращает значения, но создает текстовый файл с данными в формате YOLO.
    """
    yolo_list = []
    with open(json_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    with Image.open(image_path) as image:
        image_width, image_height = image.size

    targets = data.get("targets", [])
    if targets:
        
        for i in targets:
            polygon_str = i.get("polygon")
            class_id = i.get("class_id", "unknown")

            if polygon_str:
                bbox, _ = polygon_to_bbox(polygon_str)
                yolo_line = x1y1x2y2_to_yolo(bbox, image_width, image_height, class_id)
                yolo_list.append([yolo_line])
        
        with open(f"{os.path.dirname(json_path)}\\{os.path.splitext(os.path.basename(json_path))[0]}.txt", 'w', encoding="utf-8") as file:
            for item in yolo_list:
                file.write(item[0] + '\n')
    
    return True
    




    
if __name__ == "__main__":

    import cv2

    path = r"C:\WorkSpace\dataset\all"

    replcae_list = [
    (0.0, 0), ("0.0", 0), ("Человек", 0), ("человек", 0),
    (1.0, 1), ("1.0", 1), ("БМП", 1), ("БРОНЕАВТОМОБИЛЬ", 1), ("БРОНЕМАШИНА", 1), ("БТР", 1), ("Бронемашина", 1),
    ("ГРУЗ.АВТО", 1), ("ГРУЗОВОЙАВТОМОБИЛЬ", 1), ("Грузовойавто", 1), ("Грузовойавтомобиль", 1), ("РЛС", 1), ("ТАНК", 1), ("Танк", 1),
    ("ЛЕГК.АВТО", 3), ("Легковойавтомобиль", 3),
    ("КВАДРОКОПТЕР", 4), ("САМОЛЁТ", 4), ("Самолет", 4),
    ("ГАУБИЦА", 5), ("Гаубица", 5), ("ЗРК", 5), ("ЗРУ", 5), ("РСЗО", 5), ("САУ", 5), ("Миномет", 5),
    ("Корабль", 6), ("Лодка", 6)]

    for name_file in os.listdir(path):
        if name_file.endswith(".txt"):

            path_file = rf"{path}\{name_file}"
            convert_oldClass_to_newClass(path_file, replcae_list)


    





    
