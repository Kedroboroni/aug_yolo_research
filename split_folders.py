from yolosplitter import YoloSplitter

ys = YoloSplitter(imgFormat=['.jpg'], labelFormat=['.txt'])
df = ys.from_mixed_dir(
    input_dir=rf"C:\WorkSpace\dataset\от близнеца\Размеченые снимки",
    ratio=(0.9, 0.1, 0)  # train:val:test
)
ys.save_split(output_dir= r"dataset_yolo_")