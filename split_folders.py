from yolosplitter import YoloSplitter

ys = YoloSplitter(imgFormat=['.jpg'], labelFormat=['.txt'])
df = ys.from_mixed_dir(
    input_dir=rf"C:\WorkSpace\dataset\all",
    ratio=(0.7, 0.2, 0.1)  # train:val:test
)
ys.save_split(output_dir="dataset_yolo")