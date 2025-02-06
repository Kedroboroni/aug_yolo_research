#Файл в котором описаны функции кастомной аугументации (на основе пердставленных интсурментов от albumentations)
#Анотация и коментарии созданы с помощью GIGA Code 
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import cv2
import numpy as np
import albumentations as A
from aug.core_aug import *

from convert_utils.convert import *
import random as r





def apply_aug_image(image: np.ndarray, coordinates: np.ndarray, listParams: list) -> tuple:
    """
    Применяет аугментации к изображению для класса ZRJG.
    
    Параметры:
    image (np.ndarray): Исходное изображение.
    coordinates (np.ndarray): Координаты объектов в формате YOLO.
    
    Возвращает:
    tuple: Измененное изображение, новые координаты и флаг.
    """
    transform = A.Compose(
        [func(p = 1) for func in listParams],
        bbox_params=A.BboxParams(
            format='yolo',
            label_fields=['class_labels'],
            min_visibility=0.2
        )
    )

    result, new_coordinates, flag = apply_transform_get_coordinate(image, coordinates, transform)

    return result, new_coordinates, flag





def apply_aug_image2222222(image: np.ndarray, coordinates: np.ndarray, listParams: list) -> tuple:
    """
    Применяет аугментации к изображению для класса ZRJG.
    
    Параметры:
    image (np.ndarray): Исходное изображение.
    coordinates (np.ndarray): Координаты объектов в формате YOLO.
    
    Возвращает:
    tuple: Измененное изображение, новые координаты и флаг.
    """
    transform = A.Compose(
        [
            A.Affine(),
            A.AtLeastOneBBoxRandomCrop(),
            A.BBoxSafeRandomCrop(),
            A.CenterCrop(),
            A.CoarseDropout(),
            A.ConstrainedCoarseDropout(),
            A.Crop(),
            A.CropAndPad(),
            A.CropNonEmptyMaskIfExists(),
            A.D4(),
            A.ElasticTransform(),
            A.Erasing(),
            A.FrequencyMasking(),
            A.GridDistortion(),
            A.GridDropout(),
            A.GridElasticDeform(),
            A.HorizontalFlip(),
            A.LongestMaxSize(),
            A.MaskDropout(),
            A.Morphological(),
            A.NoOp(),
            A.OpticalDistortion(),
            A.OverlayElements(),
            A.Pad(),
            A.PadIfNeeded(),
            A.Perspective(),
            A.PiecewiseAffine(),
            A.PixelDropout(),
            A.RandomCrop(),
            A.RandomCropFromBorders(),
            A.RandomCropNearBBox(),
            A.RandomGridShuffle(),
            A.RandomResizedCrop(),
            A.RandomRotate90(),
            A.RandomScale(),
            A.RandomSizedBBoxSafeCrop(),
            A.RandomSizedCrop(),
            A.Resize(),
            A.Rotate(),
            A.SafeRotate(),
            A.ShiftScaleRotate(),
            A.SmallestMaxSize(),
            A.ThinPlateSpline(),
            A.TimeMasking(),
            A.TimeReverse(),
            A.Transpose(),
            A.VerticalFlip(),
            A.XYMasking(),
            A.AdditiveNoise(),
            A.AdvancedBlur(),
            A.AutoContrast(),
            A.Blur(),
            A.CLAHE(),
            A.ChannelDropout(),
            A.ChannelShuffle(),
            A.ChromaticAberration(),
            A.ColorJitter(),
            A.Defocus(),
            A.Downscale(),
            A.Emboss(),
            A.Equalize(),
            A.FDA(),
            A.FancyPCA(),
            A.FromFloat(),
            A.GaussNoise(),
            A.GaussianBlur(),
            A.GlassBlur(),
            A.HistogramMatching(),
            A.HueSaturationValue(),
            A.ISONoise(),
            A.Illumination(),
            A.ImageCompression(),
            A.InvertImg(),
            A.MedianBlur(),
            A.MotionBlur(),
            A.MultiplicativeNoise(),
            A.Normalize(),
            A.PixelDistributionAdaptation(),
            A.PlanckianJitter(),
            A.PlasmaBrightnessContrast(),
            A.PlasmaShadow(),
            A.Posterize(),
            A.RGBShift(),
            A.RandomBrightnessContrast(),
            A.RandomFog(),
            A.RandomGamma(),
            A.RandomGravel(),
            A.RandomRain(),
            A.RandomShadow(),
            A.RandomSnow(),
            A.RandomSunFlare(),
            A.RandomToneCurve(),
            A.RingingOvershoot(),
            A.SaltAndPepper(),
            A.Sharpen(),
            A.ShotNoise(),
            A.Solarize(),
            A.Spatter(),
            A.Superpixels(),
            A.TemplateTransform(),
            A.TextImage(),
            A.ToFloat(),
            A.ToGray(),
            A.ToRGB(),
            A.ToSepia(),
            A.UnsharpMask(),
            A.ZoomBlur()
        ],
        bbox_params=A.BboxParams(
            format='yolo',
            label_fields=['class_labels'],
            min_visibility=0.2
        )
    )

    result, new_coordinates, flag = apply_transform_get_coordinate(image, coordinates, transform)

    return result, new_coordinates, flag



if __name__ == "__main__":

    import time
    import random as r

    path_image = r"C:\WorkSpace\Python\machinist_help\aug\dataset\foto.jpg"
    path_file = r"C:\WorkSpace\Python\machinist_help\aug\dataset\foto.txt"

    path_to_save = r"C:\WorkSpace\Python\machinist_help\aug\dataset"

    image = cv2.imread(path_image)
    coordinate = read_yolo_annotations(path_file)

    