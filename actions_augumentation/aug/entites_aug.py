#Файл в котором описаны функции кастомной аугументации (на основе пердставленных интсурментов от albumentations)
#Анотация и коментарии созданы с помощью GIGA Code 
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import cv2
import numpy as np
import albumentations as A
from actions_augumentation.aug.core_aug import *
import os





def apply_aug_image(image: np.ndarray, coordinates: np.ndarray, listFunctions: list) -> tuple:
    """
    Применяет аугментации к изображению для класса ZRJG.
    
    Параметры:
    image (np.ndarray): Исходное изображение.
    coordinates (np.ndarray): Координаты объектов в формате YOLO.
    
    Возвращает:
    tuple: Измененное изображение, новые координаты и флаг.
    """

    transform_ = A.Compose(
        [func(p = 1) for func in listFunctions],
        bbox_params=A.BboxParams(
            format='yolo',
            label_fields=['class_labels'],
            min_visibility=0.2
        )
    )

    result, new_coordinates, flag = apply_transform_get_coordinate(image, coordinates, transform_)

    return result, new_coordinates, flag



    


if __name__ == "__main__":
    

    

    image = cv2.imread(r"C:\WorkSpace\Diplom\research Augumentation\actions_augumentation\aug\dataset\foto.jpg")
    anotation = anotation = read_yolo_annotations(r"C:\WorkSpace\Diplom\research Augumentation\actions_augumentation\aug\dataset\foto.txt")

    transform_ = A.Compose(
        [A.GridElasticDeform((8,100), 22)],
        bbox_params=A.BboxParams(
            format='yolo',
            label_fields=['class_labels'],
            min_visibility=0.2
        )
    )

    result, new_coordinates, flag = apply_transform_get_coordinate(image, anotation, transform_)
    #new_image, new_anotation, flag = apply_aug_image(result, new_coordinates, flag)
    save_result_transform(r"C:\WorkSpace\Diplom\research Augumentation\actions_augumentation\aug\dataset", result, new_coordinates, ["123"], flag)