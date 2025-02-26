
import sys
#from ultralytics import YOLO
import time

args = sys.argv[1:]

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

path_dataset = args[0]
keys = args[1]
value = args[2]

keys = keys.split(',')
value = value.split(',')

print(path_dataset)
print(keys, print(type(keys[0])), len(keys))
print(value, print(type(value [0])), len(value))


dictParams = {key: float(value[i]) if is_float(value[i]) else value[i] for i,key in enumerate(keys)}

print(dictParams)
print("Дальше тут будет запуск обучения yolo, все созранение и работа Yolo будет назходится в папке results.")

a = input()