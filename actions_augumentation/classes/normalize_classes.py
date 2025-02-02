#Файл в котором описаны функции для увеличения классов
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from classes.working_classes import *
from aug.core_aug import *
from classes.entites_aug_class import *
import random as r
#import working_3D
from aug.entites_aug import *





def heap_classes_images(path, part=0.15) -> list:
    """
    Увеличивает количество изображений для малочисленных классов, применяя различные аугментации.
    
    Параметры:
    path (str): Путь к датасету.
    part (float): Доля классов для увеличения.
    
    Возвращает:
    list: Список с результатами аугментации.
    """
    
    data = score_classes(path)
    data = {int(key): value for key, value in data.items()}
    small_classes = list(serch_small_classes(data).keys())

    paths_classes = tuple(file for file in os.listdir(path) if file.endswith(".txt"))
    path_classes_small = tuple(
        os.path.splitext(
            os.path.basename(
                file
            )
        )[0]
        for file in paths_classes
        if any(
            str(item) in read_yolo_class(
                rf"{path}/{file}"
            )
            for item in small_classes
        )
    )
    
    path_classes_small_part = r.sample(path_classes_small, int(len(path_classes_small) * part))

    choice_entites = (
        change_classes_CGGHR,
        change_classes_CGHR,
        change_classes_GDHR,
        change_classes_RDHR,
        change_classes_RGGHR,
        change_classes_RIHR
    )
    
    result = [
        r.choice(choice_entites)(
            cv2.imread(rf"{path}\{path_obj}.jpg"),
            read_yolo_annotations(rf"{path}\{path_obj}.txt"),
            small_classes
        ) 
        for path_obj in path_classes_small_part
    ]
    
    apply = [
        save_result_transform(
            path,
            obj[0],
            obj[1],
            obj[2]                                    
        )
        for obj in result
    ]
    
    return result

def heap_images(path, part=0.2) -> list:
    """
    Применяет аугментации к изображениям в указанной директории.
    
    Параметры:
    path (str): Путь к директории с изображениями.
    part (float): Доля изображений для аугментации.
    
    Возвращает:
    list: Список с результатами аугментации.
    """
    paths_anotation = tuple(os.path.splitext(os.path.basename(file))[0] for file in os.listdir(path) if file.endswith(".txt"))
    path_anotation_part = r.sample(paths_anotation, int(len(paths_anotation) * part))

    entites = (
        change_image_DCC,
        change_image_GRCC,
        change_image_IDR,
        change_image_MECR,
        change_image_ZRJG
    )
    
    result = [
        r.choice(entites)(
            cv2.imread(rf"{path}\{path_obj}.jpg"),
            read_yolo_annotations(rf"{path}\{path_obj}.txt"),
        )
        for path_obj in path_anotation_part
    ]
    
    apply = [
        save_result_transform(
            path,
            obj[0],
            obj[1],
            obj[2]                                    
        )
        for obj in result
    ]
    
    return result




if __name__ == "__main__":

    from warnings import filterwarnings
    filterwarnings("ignore", category=UserWarning)

    path = r"C:\WorkSpace\Python\machinist_help\aug\dataset"

    heap_classes_images(path, part=1)


