#Файл в котором описаны функции кастомной аугументации (на основе пердставленных интсурментов от albumentations)
#Анотация и коментарии созданы с помощью GIGA Code 
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import cv2
import numpy as np
import albumentations as A
from aug.core_aug import *
import os
from convert_utils.convert import *





def apply_aug_image(image: np.ndarray, coordinates: np.ndarray, listParams: list) -> tuple:
    """
    Применяет аугментации к изображению для класса ZRJG.
    
    Параметры:
    image (np.ndarray): Исходное изображение.
    coordinates (np.ndarray): Координаты объектов в формате YOLO.
    
    Возвращает:
    tuple: Измененное изображение, новые координаты и флаг.
    """
    transform = A.Compose(
        [func(p = 1) for func in listParams],
        bbox_params=A.BboxParams(
            format='yolo',
            label_fields=['class_labels'],
            min_visibility=0.2
        )
    )

    result, new_coordinates, flag = apply_transform_get_coordinate(image, coordinates, transform)

    return result, new_coordinates, flag
    


if __name__ == "__main__":
    os.environ['NO_ALBUMENTATIONS_UPDATE'] = "1"

    image = cv2.imread(r"C:\WorkSpace\Diplom\research Augumentation\actions_augumentation\aug\dataset\ef23dbf2-b61f-470b-9a87-adb1df2ac81c.jpg")
    anotation = read_yolo_annotations(r"C:\WorkSpace\Diplom\research Augumentation\actions_augumentation\aug\dataset\ef23dbf2-b61f-470b-9a87-adb1df2ac81c.txt")
    
    transform = A.Compose(
        [A.Affine(scale=1.5, interpolation = 1.0,)],
        bbox_params=A.BboxParams(
            format='yolo',
            label_fields=['class_labels'],
            min_visibility=0.2
        )
    )

    result, new_coordinates, flag = apply_transform_get_coordinate(image, anotation, transform)

    print("Успех!")