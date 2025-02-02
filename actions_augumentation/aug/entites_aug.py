#Файл в котором описаны функции кастомной аугументации (на основе пердставленных интсурментов от albumentations)
#Анотация и коментарии созданы с помощью GIGA Code 
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import cv2
import numpy as np
import albumentations as A
from aug.core_aug import *
from aug.engine import *
from convert_utils.convert import *
import random as r

def rotete_image(image: np.ndarray, coordinates: np.ndarray, quantity: int = 3) -> tuple:
    """
    Поворачивает изображение на заданные углы.
    
    Параметры:
    image (np.ndarray): Исходное изображение.
    coordinates (np.ndarray): Координаты объектов в формате YOLO.
    quantity (int): Количество поворотов.
    
    Возвращает:
    tuple: Измененное изображение, новые координаты и флаг.
    """
    for i in range(quantity):
        transform = A.Compose(
            [
                A.Rotate(limit=(10, r.randint(13, 360)), p=1.0)
            ], 
            bbox_params=A.BboxParams(
                format='yolo',
                label_fields=['class_labels'],
                min_visibility=0.3
            )
        )

        result, new_coordinates, flag = apply_transform_get_coordinate(image, coordinates, transform)

    return result, new_coordinates, flag

def apply_aug_image(image: np.ndarray, coordinates: np.ndarray, listParams: list) -> tuple:
    """
    Применяет аугментации к изображению для класса ZRJG.
    
    Параметры:
    image (np.ndarray): Исходное изображение.
    coordinates (np.ndarray): Координаты объектов в формате YOLO.
    
    Возвращает:
    tuple: Измененное изображение, новые координаты и флаг.
    """
    print(listParams)
    transform = A.Compose(
        listParams,
        bbox_params=A.BboxParams(
            format='yolo',
            label_fields=['class_labels'],
            min_visibility=0.2
        )
    )

    result, new_coordinates, flag = apply_transform_get_coordinate(image, coordinates, transform)

    return result, new_coordinates, flag


        




if __name__ == "__main__":

    import time
    import random as r

    path_image = r"C:\WorkSpace\Python\machinist_help\aug\dataset\foto.jpg"
    path_file = r"C:\WorkSpace\Python\machinist_help\aug\dataset\foto.txt"

    path_to_save = r"C:\WorkSpace\Python\machinist_help\aug\dataset"

    image = cv2.imread(path_image)
    coordinate = read_yolo_annotations(path_file)

    