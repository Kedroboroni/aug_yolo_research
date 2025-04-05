import sys, os
sys.path.append(os.path.dirname(
                    os.path.dirname(
                        os.path.dirname(
                            os.path.abspath(__file__)
                        )
                    )
                )
            )
sys.path.append(os.path.dirname(
                    os.path.dirname(
                        os.path.dirname(
                            os.path.dirname(
                                os.path.abspath(__file__)
                            )
                        )
                    )
                )
            )

    # Путь к site-packages вашей виртуальной среды

venv_site_packages = rf".venv\Lib\site-packages"
if venv_site_packages not in sys.path:
    sys.path.insert(0, venv_site_packages)

from ultralytics import YOLO
import os





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
dictParams = {key: float(value[i]) if is_float(value[i]) else value[i] for i,key in enumerate(keys)}


def main(path_dataset):

    path_yaml_data = rf"{path_dataset}\data.yaml"
    save_dirs = rf"runs\detect\train_AutoContrast" 
    device = 0
    epochs = 250
    img_size = 640
    save_plot = True
    batch_size = -1
    pretrained = False

    model = YOLO(rf"yolo11n.pt")

    results = model.train(data = path_yaml_data,
                            epochs = epochs,
                            imgsz = img_size,
                            plots = save_plot,
                            save_dir = save_dirs,
                            device = device,
                            batch = batch_size,
                            pretrained = pretrained,
                            **dictParams
                        )

    print("\nОбучения закончилось. \nЧтобы продолжить и отчистить кэш введите clear_")
    clear_ = None
    while clear_ != "clear_":
        clear_ = input()


if __name__ == "__main__":

    main(path_dataset)
    if   os.path.exists(rf"{path_dataset}\valid\labels.cache"):
        os.remove(rf"{path_dataset}\valid\labels.cache")
        print("Отчистили кэш val")
    if os.path.exists(rf"{path_dataset}\train\labels.cache"):
        os.remove(rf"{path_dataset}\train\labels.cache")
        print("Отчистили кэш train")
    exit_ = None
    print("Для выхода введите exit_")
    while exit_ != "exit_":
        
        exit_ = input()
        
        
        
        
        
    
    