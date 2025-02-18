
import sys
#from ultralytics import YOLO
import time

args = sys.argv[1:]


path_dataset = args[0]
keys = args[1]
value = args[2]
    #dictParams = {}

    #for i, key in enumerate(keys):
        #dictParams[key] = value[i]


print(path_dataset)
print(keys)
print(value)
a = input()
#time.sleep(10)
    #model = YOLO("yolo8n.pt")

    #results = model.train(data = path_dataset, epochs = 100, imgsz = 640, **dictParams)