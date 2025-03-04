try:
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
    venv_site_packages = rf"C:\WorkSpace\Diplom\research Augumentation\.venv\Lib\site-packages"
    if venv_site_packages not in sys.path:
        sys.path.insert(0, venv_site_packages)
    from ultralytics import YOLO




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

    path_yaml_data = rf"{path_dataset}\data.yaml"
    save_dir = rf"C:\WorkSpace\Diplom\research Augumentation\results"
    device = 0 #GPU? да, GPU
    epochs = 1
    img_size = 640
    save_plot = True

    model = YOLO("yolo11n.yaml")

    results = model.train(data = path_yaml_data,
                        epochs=epochs,
                        imgsz=img_size,
                        plots = save_plot,
                        save_dir=save_dir,
                        #device = device
                    )
except Exception as e:
    print(e)





print("----------------------------")
print("Для выхода нажмите любую кнопку")
a = input()
