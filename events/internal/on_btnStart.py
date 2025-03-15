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
from functools import partial
import random as r




def on_btnStart(queue, path, listKeys, dictParams, p):

    obects_in_directory = os.listdir(path)
    total_steps = int(len(obects_in_directory)/2 * p)
    current_step = 0
    listFunctions = []
    for key in listKeys:
        if key in dictParams:
            listFunctions.append(dictParams[key])

        else:
            listFunctions.append(partial(dictInternalAug_brightness_and_transform_settings[key]))

    
    anotations_in_directory = [anotation for anotation in obects_in_directory if anotation.endswith('.txt')]
    k = int(len(anotations_in_directory) * p)
    path_anotation_part = r.sample(anotations_in_directory, k = k)

    for current_step, name_object in enumerate(path_anotation_part):

        if name_object.endswith('.txt'):

            name_img = rf"{os.path.splitext(name_object)[0]}.jpg"
            name_txt = rf"{os.path.splitext(name_object)[0]}.txt"

            if name_img in obects_in_directory and name_txt in obects_in_directory:

                name_img = rf"{path}\{os.path.splitext(name_object)[0]}.jpg"
                name_txt = rf"{path}\{os.path.splitext(name_object)[0]}.txt"

                
                image = cv2.imread(name_img)
                anotation = read_yolo_annotations(name_txt)

                for j,i in enumerate(listFunctions):

                    new_image, new_anotation, flag = apply_aug_image(image, anotation, [i])
                    save_result_transform(path, new_image, new_anotation, listKeys[j], flag)
                                  
                percentage = int(((current_step/2) / total_steps) * 100)
                queue.put(percentage)
        
    

    percentage = 0  
    queue.put(None)
    
