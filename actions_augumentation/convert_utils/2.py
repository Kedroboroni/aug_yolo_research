from PIL import Image
import os



def convert_png_to_jpg(directory):
    # Проверяем, существует ли указанная директория
    if not os.path.exists(directory):
        print(f"Директория {directory} не существует.")
        return

    # Проходим по всем файлам в директории
    for filename in os.listdir(directory):
        # Проверяем, что файл имеет расширение .png
        if filename.endswith(".png"):
            # Полный путь к файлу
            png_path = os.path.join(directory, filename)
            
            # Открываем изображение
            with Image.open(png_path) as img:
                # Создаем новое имя файла с расширением .jpg
                jpg_filename = os.path.splitext(filename)[0] + ".jpg"
                jpg_path = os.path.join(directory, jpg_filename)
                
                # Сохраняем изображение в формате JPEG
                img.convert("RGB").save(jpg_path, "JPEG")
                print(f"Файл {png_path} пересохранен как {jpg_path}")

# Укажите путь к директории с PNG-файлами
directory = r"C:\WorkSpace\dataset\all"
convert_png_to_jpg(directory)







# Укажите путь к директории с изображениями
directory = r"C:\WorkSpace\dataset\all"

# Проходим по всем файлам в директории
for filename in os.listdir(directory):
    # Проверяем, что файл имеет расширение .png
    if filename.endswith(".png"):
        # Полный путь к файлу
        file_path = os.path.join(directory, filename)

        os.remove(file_path)
        print(f"Файл -> {file_path}----УДАЛЕН")