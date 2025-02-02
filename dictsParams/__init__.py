from functools import partial
from albumentations import *



dictInternalAug_brightness_settings = {
    "AdditiveNoise": partial(AdditiveNoise, p=0.5),
    "AdvancedBlur": partial(AdvancedBlur, p=0.5),
    "AutoContrast": partial(AutoContrast, p=0.5),
    "Blur": partial(Blur, p=0.5),
    "CLAHE": partial(CLAHE, p=0.5),
    "ChannelDropout": partial(ChannelDropout, p=0.5),
    "ChannelShuffle": partial(ChannelShuffle, p=0.5),
    "ChromaticAberration": partial(ChromaticAberration, p=0.5),
    "ColorJitter": partial(ColorJitter, p=0.5),
    "Defocus": partial(Defocus, p=0.5),
    "Downscale": partial(Downscale, p=0.5),
    "Emboss": partial(Emboss, p=0.5),
    "Equalize": partial(Equalize, p=0.5),
    "FDA": partial(FDA, p=0.5),
    "FancyPCA": partial(FancyPCA, p=0.5),
    "FromFloat": partial(FromFloat, p=0.5),
    "GaussNoise": partial(GaussNoise, p=0.5),
    "GaussianBlur": partial(GaussianBlur, p=0.5),
    "GlassBlur": partial(GlassBlur, p=0.5),
    "HistogramMatching": partial(HistogramMatching, p=0.5),
    "HueSaturationValue": partial(HueSaturationValue, p=0.5),
    "ISONoise": partial(ISONoise, p=0.5),
    "Illumination": partial(Illumination, p=0.5),
    "ImageCompression": partial(ImageCompression, p=0.5),
    "InvertImg": partial(InvertImg, p=0.5),
    "MedianBlur": partial(MedianBlur, p=0.5),
    "MotionBlur": partial(MotionBlur, p=0.5),
    "MultiplicativeNoise": partial(MultiplicativeNoise, p=0.5),
    "Normalize": partial(Normalize, p=0.5),
    "PixelDistributionAdaptation": partial(PixelDistributionAdaptation, p=0.5),
    "PlanckianJitter": partial(PlanckianJitter, p=0.5),
    "PlasmaBrightnessContrast": partial(PlasmaBrightnessContrast, p=0.5),
    "PlasmaShadow": partial(PlasmaShadow, p=0.5),
    "Posterize": partial(Posterize, p=0.5),
    "RGBShift": partial(RGBShift, p=0.5),
    "RandomBrightnessContrast": partial(RandomBrightnessContrast, p=0.5),
    "RandomFog": partial(RandomFog, p=0.5),
    "RandomGamma": partial(RandomGamma, p=0.5),
    "RandomGravel": partial(RandomGravel, p=0.5),
    "RandomRain": partial(RandomRain, p=0.5),
    "RandomShadow": partial(RandomShadow, p=0.5),
    "RandomSnow": partial(RandomSnow, p=0.5),
    "RandomSunFlare": partial(RandomSunFlare, p=0.5),
    "RandomToneCurve": partial(RandomToneCurve, p=0.5),
    "RingingOvershoot": partial(RingingOvershoot, p=0.5),
    "SaltAndPepper": partial(SaltAndPepper, p=0.5),
    "Sharpen": partial(Sharpen, p=0.5),
    "ShotNoise": partial(ShotNoise, p=0.5),
    "Solarize": partial(Solarize, p=0.5),
    "Spatter": partial(Spatter, p=0.5),
    "Superpixels": partial(Superpixels, p=0.5),
    "TemplateTransform": partial(TemplateTransform, p=0.5),
    "TextImage": partial(TextImage, p=0.5),
    "ToFloat": partial(ToFloat, p=0.5),
    "ToGray": partial(ToGray, p=0.5),
    "ToRGB": partial(ToRGB, p=0.5),
    "ToSepia": partial(ToSepia, p=0.5),
    "UnsharpMask": partial(UnsharpMask, p=0.5),
    "ZoomBlur": partial(ZoomBlur, p=0.5),
}

dictInternalAug_transform_settings = {
    "Affine": partial(Affine, scale=(0.5, 1.5), translate_percent=(0.1, 0.1), rotate=(-45, 45), shear=(-16, 16), p=1.0),
    "AtLeastOneBBoxRandomCrop": partial(AtLeastOneBBoxRandomCrop, p=1.0),
    "BBoxSafeRandomCrop": partial(BBoxSafeRandomCrop, p=1.0),
    "CenterCrop": partial(CenterCrop, height=256, width=256, p=1.0),
    "CoarseDropout": partial(CoarseDropout, max_holes=8, max_height=8, max_width=8, min_holes=1, p=1.0),
    "ConstrainedCoarseDropout": partial(ConstrainedCoarseDropout, max_holes=8, max_height=8, max_width=8, min_holes=1, p=1.0),
    "Crop": partial(Crop, x_min=0, y_min=0, x_max=256, y_max=256, p=1.0),
    "CropAndPad": partial(CropAndPad, top=10, left=10, height=256, width=256, p=1.0),
    "CropNonEmptyMaskIfExists": partial(CropNonEmptyMaskIfExists, p=1.0),
    "D4": partial(D4, p=1.0),
    "ElasticTransform": partial(ElasticTransform, alpha=1.0, sigma=50, p=1.0),
    "Erasing": partial(Erasing, p=1.0),
    "FrequencyMasking": partial(FrequencyMasking, p=1.0),
    "GridDistortion": partial(GridDistortion, num_steps=5, distort_limit=0.3, p=1.0),
    "GridDropout": partial(GridDropout, p=1.0),
    "GridElasticDeform": partial(GridElasticDeform, num_grid_xy=(5, 5), magnitude=10, p=1.0),
    "HorizontalFlip": partial(HorizontalFlip, p=1.0),
    "LongestMaxSize": partial(LongestMaxSize, max_size=256, p=1.0),
    "MaskDropout": partial(MaskDropout, p=1.0),
    "Morphological": partial(Morphological, p=1.0),
    "NoOp": partial(NoOp, p=1.0),
    "OpticalDistortion": partial(OpticalDistortion, distort_limit=0.5, shift_limit=0.5, p=1.0),
    "OverlayElements": partial(OverlayElements, p=1.0),
    "Pad": partial(Pad, border_mode=0, p=1.0),
    "PadIfNeeded": partial(PadIfNeeded, min_height=256, min_width=256, p=1.0),
    "Perspective": partial(Perspective, scale=(0.05, 0.1), p=1.0),
    "PiecewiseAffine": partial(PiecewiseAffine, scale=0.05, p=1.0),
    "PixelDropout": partial(PixelDropout, p=1.0),
    "RandomCrop": partial(RandomCrop, height=640, width=2640, p=1.0),
    "RandomCropFromBorders": partial(RandomCropFromBorders, p=1.0),
    "RandomCropNearBBox": partial(RandomCropNearBBox, p=1.0),
    "RandomGridShuffle": partial(RandomGridShuffle, p=1.0),
    "RandomResizedCrop": partial(RandomResizedCrop, height=640, width=640, p=1.0),
    "RandomRotate90": partial(RandomRotate90, p=1.0),
    "RandomScale": partial(RandomScale, scale_limit=0.1, p=1.0),
    "RandomSizedBBoxSafeCrop": partial(RandomSizedBBoxSafeCrop, height=256, width=256, p=1.0),
    "RandomSizedCrop": partial(RandomSizedCrop, min_max_height=(256, 512), height=256, p=1.0),
    "Resize": partial(Resize, height=256, width=256, p=1.0),
    "Rotate": partial(Rotate, limit=360, p=1.0),
    "SafeRotate": partial(SafeRotate, limit=45, p=1.0),
    "ShiftScaleRotate": partial(ShiftScaleRotate, shift_limit=0.0625, scale_limit=0.1, rotate_limit=45, p=1.0),
    "SmallestMaxSize": partial(SmallestMaxSize, max_size=256, p=1.0),
    "ThinPlateSpline": partial(ThinPlateSpline, p=1.0),
    "TimeMasking": partial(TimeMasking, p=1.0),
    "TimeReverse": partial(TimeReverse, p=1.0),
    "Transpose": partial(Transpose, p=1.0),
    "VerticalFlip": partial(VerticalFlip, p=1.0),
    "XYMasking": partial(XYMasking, p=1.0),
}


# в это ловаре смотри внимательно параметры, они указаны не правильно...
dictParamsAug_Yolo = {
    "epochs": [1, 2, 5, 10, 20, 50, 100],  # Количество эпох
    "batch_size": [1, 2, 4, 8, 16, 32, 64],  # Размер батча
    "learning_rate": [0.001, 0.01, 0.1, 0.0001],  # Скорость обучения
    "img_size": [320, 416, 512, 608, 640],  # Размер изображения
    "data_augmentation": [True, False],  # Использовать ли аугментацию данных
    "optimizer": ["SGD", "Adam", "RMSprop"],  # Оптимизатор
    "momentum": [0.0, 0.5, 0.9, 0.99],  # Моментум для SGD
    "weight_decay": [0.0, 0.0001, 0.001],  # Регуляризация L2
    "pretrained": [True, False],  # Использовать ли предобученные веса
    "checkpoint": [True, False],  # Сохранять ли контрольные точки
    "class_names": ["coco", "custom"],  # Названия классов

    # Параметры аугментации
    "flip": [True, False],  # Отражение изображения по горизонтали
    "rotate": [i for i in range(0,361, 12)],  # Угол поворота изображения
    "scale": [0.5, 1.0, 1.5, 2.0],  # Масштабирование изображения
    "translate": [0, 10, 20],  # Сдвиг изображения по осям
    "brightness": [0.0, 0.5, 1.0, 1.5],  # Яркость изображения
    "contrast": [0.0, 0.5, 1.0, 1.5],  # Контрастность изображения
    "saturation": [0.0, 0.5, 1.0, 1.5],  # Насыщенность изображения
    "hue": [-0.1, 0.0, 0.1],  # Оттенок изображения
}