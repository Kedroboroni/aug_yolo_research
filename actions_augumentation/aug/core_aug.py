#Файл в котором описаны функции для работы с анотациями аугументации (файлы разметки)
#Анотация и коментарии созданы с помощью GIGA Code
import cv2
from uuid import uuid4
import numpy as np

def read_yolo_annotations(path_txtFile: str) -> np.array:
    """
    Считывает аннотации из текстового файла.
    
    Параметры:
    path_txtFile (str): Путь к текстовому файлу с аннотациями.
    
    Возвращает:
    np.array: Массив с аннотациями или пустой массив, если аннотации отсутствуют.
    """
    if len(read_yolo_class(path_txtFile)) == 0:
        return np.array([])

    else: 
        result = np.append(
            read_yolo_class(path_txtFile),
            read_yolo_coordinates(path_txtFile),
            axis=1
        )
        print(path_txtFile)
    
    return result

def read_yolo_class(path_txtFile: str) -> np.array:
    """
    Считывает классы из текстового файла.
    
    Параметры:
    path_txtFile (str): Путь к текстовому файлу с классами.
    
    Возвращает:
    np.array: Массив с классами.
    """
    classes = []
    with open(path_txtFile, 'r', encoding="utf-8") as file:
        lines = file.readlines()

    for line in lines:
        if len(line.strip().split()) == 6:
            class_id1, class_id2, _, _, _, _ = map(str, line.strip().split())
            class_id = class_id1 + class_id2
        else:
            class_id, _, _, _, _ = map(str, line.strip().split())

        classes.append([class_id])

    return np.array(classes)

def read_yolo_coordinates(path_txtFile: str) -> np.array:
    """
    Считывает координаты из текстового файла.
    
    Параметры:
    path_txtFile (str): Путь к текстовому файлу с координатами.
    
    Возвращает:
    np.array: Массив с координатами.
    """
    coordinates = []
    with open(path_txtFile, 'r', encoding="utf-8") as file:
        lines = file.readlines()

    for line in lines:
        if len(line.strip().split()) == 6:
            _, _, x_center, y_center, width, height = map(str, line.strip().split())
        else:
            _, x_center, y_center, width, height = map(str, line.strip().split())
        coordinates.append(
            [
                abs(float(x_center)), 
                abs(float(y_center)), 
                abs(float(width)), 
                abs(float(height))
            ]
        )
        
    return np.array(coordinates)

def save_yolo_annotations(path_txtFile: str, coordinates) -> bool:
    """
    Сохраняет аннотации в текстовый файл.
    
    Параметры:
    path_txtFile (str): Путь к текстовому файлу для сохранения аннотаций.
    coordinates (np.array): Координаты для сохранения.
    
    Возвращает:
    bool: True, если сохранение прошло успешно, иначе False.
    """
    try:
        result = np.array(coordinates, dtype=float)
        np.savetxt(path_txtFile,
                   result,
                   fmt='%g %.6f %.6f %.6f %.6f',
                   delimiter=' '
                   )
    except:
        return False
    
    return True

def save_result_transform(path_directory: str, new_image, new_coordinate, flag=None) -> None:
    """
    Сохраняет результат аугментации в указанной директории.
    
    Параметры:
    path_directory (str): Путь к директории для сохранения.
    image (np.ndarray): Изображение для сохранения.
    new_coordinate: Новые координаты для сохранения.
    flag: Флаг для определения типа сохранения.
    
    Возвращает:
    None
    """
    name_obj = uuid4()

    if flag is None:

        cv2.imwrite(rf"{path_directory}\{name_obj}.jpg", new_image)
        save_yolo_annotations(rf"{path_directory}\{name_obj}.txt", new_coordinate)
    
    else:
        cv2.imwrite(rf"{path_directory}\Нерпавильная_разметка_{name_obj}.jpg", new_image)
        save_yolo_annotations(rf"{path_directory}\Нерпавильная_разметка_{name_obj}.txt", new_coordinate)

def apply_transform_get_coordinate(image, coordinates, transformParent) -> tuple:
    """
    Применяет аугментации к изображению и возвращает измененное изображение и новые координаты.
    
    Параметры:
    image (np.ndarray): Исходное изображение.
    coordinates (list): Координаты объектов в формате YOLO.
    transformParent: Функция аугментации.
    
    Возвращает:
    tuple: Измененное изображение, новые координаты и флаг.
    """
    bboxes = []
    class_labels = []
    for class_id, x_center, y_center, width, height in coordinates:

        bboxes.append([abs(float(x_center)), abs(float(y_center)), abs(float(width)), abs(float(height))])
        class_labels.append(abs(int(class_id)))
    try:
        result = transformParent(image=image, bboxes=bboxes, class_labels=class_labels)
    except ValueError:
        return image, coordinates, 1
    
    new_coordinates = np.array(
        [
            [
                result['class_labels'][i],
                points[0],
                points[1],
                points[2],
                points[3]
            ]
            for i, points in enumerate(result['bboxes'])
        ]
    )
            
    return result["image"], new_coordinates, None





if __name__ == "__main__":
    
    pass




