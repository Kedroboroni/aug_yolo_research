#Анотация и коментарии созданы с помощью GIGA 
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from aug.core_aug import *
from convert_utils.convert import *
from aug.entites_aug import *
import cv2
import numpy as np
import albumentations as A
from typing import List


def draw_bounding_boxes(image: np.ndarray, coordinates, name=None) -> np.ndarray:
    """
    Рисует ограничивающие рамки на изображении.
    
    Параметры:
    image (np.ndarray): Изображение, на котором будут нарисованы рамки.
    coordinates (list): Список координат объектов в формате (class_id, x_center, y_center, width, height).
    
    Возвращает:
    np.ndarray: Изображение с нарисованными рамками.
    """      
    for _, x1, y1, x2, y2 in coordinates:      
        
        result = cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 255), 2)

    #if name:
        #cv2.putText(image, str(int(name)), (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 20)
    
    return result



if __name__ == "__main__":

    path_image = r"C:\WorkSpace\Python\machinist_help\aug\dataset\8_img0311.jpg"
    path_anotation = r"C:\WorkSpace\Python\machinist_help\aug\dataset\8_img0311.txt"

    image = cv2.imread(path_image)
    anotation = read_yolo_annotations(path_anotation)

    coordinate = yolo_to_x1y1x2y2(anotation, image.shape)

    new_image = draw_bounding_boxes(image, coordinate)

    cv2.imwrite("test.jpg", new_image)
    #for i in range(10):

        #image, anotation = change_image_GRCC(image, anotation)
        #save_result_transform(r"C:\WorkSpace\Python\machinist_help\aug\dataset", image, anotation)
        #print(i)
