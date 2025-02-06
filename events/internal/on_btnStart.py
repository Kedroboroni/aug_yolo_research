import time
import sys, os
sys.path.append(os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                os.path.abspath(
                    __file__
                )
            )
        )
    )
)
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from dictsParams import *
import cv2 
from actions_augumentation.aug.core_aug import read_yolo_annotations
from actions_augumentation.aug.entites_aug import *


#31


def on_btnStart(queue, path, listKeys):

    obects_in_directory = os.listdir(path)
    total_steps = int(len(obects_in_directory)/2)
    current_step = 0
    
    listParams = []
    for key in listKeys:
        listParams.append(d1[key]) # В этом словре должны быть сразу указаны дефолтные настройки каждой функции
    # Стандартные папраметры должны быть как-то выненесены и нежестко фиксированы через управление интерфесом. КАКАКАКАК?!?!?!??!
    for current_step, name_object in enumerate(obects_in_directory):

        if name_object.endswith('.txt'):

            name_img = rf"{os.path.splitext(name_object)[0]}.jpg"
            name_txt = rf"{os.path.splitext(name_object)[0]}.txt"

            if name_img in obects_in_directory and name_txt in obects_in_directory:

                name_img = rf"{path}\{os.path.splitext(name_object)[0]}.jpg"
                name_txt = rf"{path}\{os.path.splitext(name_object)[0]}.txt"

                time.sleep(0.0001)
                image = cv2.imread(name_img)
                anotation = read_yolo_annotations(name_txt)

                new_image, new_anotation, flag = apply_aug_image(image, anotation, listParams)
                save_result_transform(path, new_image, new_anotation, flag)
            
                percentage = int(((current_step/2) / total_steps) * 100)
                queue.put(percentage)

    percentage = 0  
    queue.put(None)
    




if __name__ == "__main__":

    print(intMax)
    intMax +=1
    print(intMax)