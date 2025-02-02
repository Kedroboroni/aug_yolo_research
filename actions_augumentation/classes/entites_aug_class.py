#В этом файле описаны функции, для аугументирования классов (тоесть функции альбументатион применяются только к интересующему нас классу)
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import cv2
import albumentations as A
import numpy as np
from convert_utils.convert import yolo_to_x1y1x2y2
from aug.core_aug import read_yolo_annotations
from random import randint
from uuid import uuid4
from aug.core_aug import *
from aug.engine import *

def apply_aug_class(image, coordinate_yolo, names_class, listParams) -> list:
    """
    Применяет аугментации к изображениям для класса RGGHR.
    
    Параметры:
    image (np.ndarray): Исходное изображение.
    coordinate_yolo (np.array): Координаты объектов в формате YOLO.
    names_class (list): Список идентификаторов классов для аугментации.
    
    Возвращает:
    list: Список с измененным изображением и координатами.
    """
    print(listParams)
    result = image.copy()
    target_coordinate = yolo_to_x1y1x2y2(coordinate_yolo, result.shape)
    
    for bbox in target_coordinate:

        if int(bbox[0]) in names_class:
        
            _, x_min, y_min, x_max, y_max = bbox
            cropped_image = image[y_min:y_max, x_min:x_max]

            transform = A.Compose(
                listParams
            )
    
            result[y_min:y_max, x_min:x_max] = transform(image=cropped_image)["image"]

    return [result, coordinate_yolo]






if __name__ == "__main__":

    image = cv2.imread(r"C:\WorkSpace\Python\machinist_help\aug\dataset\foto.jpg")
    anotation = read_yolo_annotations(r"C:\WorkSpace\Python\machinist_help\aug\dataset\foto.txt")
    name_class = [0]
    
    
    #j = change_classes_RIHR(image, anotation, name_class)
    print(type(j[0]), type(j[1]))
    