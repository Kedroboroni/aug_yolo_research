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
import subprocess




def on_btnStart_external(path, listKeys, dictParams):
    path_directory = path
    
    listParams = []
    for key in listKeys:
        if key in dictParams:
            listParams.append(dictParams[key])
        else:
            listParams.append(dictParamsAug_Yolo[key])

    listKeys = ','.join(listKeys)
    listParams = ','.join(map(str, listParams))
    listArgv = [path_directory, listKeys, listParams]
    #print(type(path_directory))
    #print(type(listKeys))
    #print(type(listParams))

    subprocess.Popen(
        [
            'python',
            r'C:\WorkSpace\Diplom\research Augumentation\actions_augumentation\yolo_train\yolo_run.py'
        ] + listArgv,
            creationflags=subprocess.CREATE_NEW_CONSOLE)
    print("закончили процесс")


    
