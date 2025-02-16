
import cv2





class manageParams:

    def __init__(self, parent):

        self.name_fun = parent
        #дальше, описываем методы по названию функций, в них описываем кажду переменную, которая у нее есть
        #Делаем return этих параметров и возварщаем это из класса
        #ВНЕ ФАЙЛА Передаем эти параметры в partial

        #return parent()

    def get_params(self):
        # Возвращаем параметры для конкретной аугментации
        if self.name_fun == "Affine":
            return self.Affine()
        
        !!!!!!!Добавить все услвоия, или подумать как этого не делать, но созранить возврат функций по self.name_fun

    def Affine(self):
        scale = [1, 10]
        translate_percent = [0, 1]
        translate_px = [1, 10] 
        rotate = [0, 360]
        shear = [0, 100]
        interpolation = [
            cv2.INTER_NEAREST,
            cv2.INTER_AREA,
            cv2.INTER_BITS,
            cv2.INTER_LINEAR,
            cv2.INTER_CUBIC,
            cv2.INTER_MAX,
            cv2.INTER_NEAREST_EXACT
        ]
        return (scale, translate_percent, translate_px, rotate, shear, interpolation)

        
    def AtLeastOneBBoxRandomCrop(self):
        height = [100, 1024]
        width = [100, 1024]
        erosion_factor = [0, 1]
        return (height, width)
    

    def BBoxSafeRandomCrop(self):
        erosion_rate = [0, 1]
        return (erosion_rate,)
    

    def CenterCrop(self):
        height = [100, 1024]
        width = [100, 1024]
        pad_if_needed = [
            False,
            True
        ]
        pad_position= [
            'center',
            'top_left',
            'top_right',
            'bottom_left',
            'bottom_right',
            'random'
        ]
        border_mode = [
            cv2.BORDER_CONSTANT,
            cv2.BORDER_WRAP,
            cv2.BORDER_TRANSPARENT,
            cv2.BORDER_ISOLATED,
            cv2.BORDER_DEFAULT
        ]
        return (height, width, pad_if_needed, pad_position, border_mode)
    

    def CoarseDropout(self):
        
        num_holes_range = [(1,2), 'int']
        hole_height_range = [(0.1, 0.2), "float"]
        hole_width_range = [(0.1, 0.2), "float"]
        fill = [0, 255]
        return (num_holes_range, hole_height_range, hole_width_range, fill)


    def ConstrainedCoarseDropout(self):
        num_holes_range = (1,2)
        hole_height_range = (0.1, 0.2)
        hole_width_range = (0.1, 0.2)
        fill = [0, 255]
        return (num_holes_range, hole_height_range, hole_width_range, fill)


    def Crop(self):
        x_min = [0, 10]
        y_min = [0, 10]
        x_max = [1024, 2048]
        y_max = [1024, 2048]
        pad_if_needed = [False, True]
        pad_position= [
            'center',
            'top_left',
            'top_right',
            'bottom_left',
            'bottom_right',
            'random'
        ]
        border_mode = [
            cv2.BORDER_CONSTANT,
            cv2.BORDER_WRAP,
            cv2.BORDER_TRANSPARENT,
            cv2.BORDER_ISOLATED,
            cv2.BORDER_DEFAULT
        ]
        return (x_min, y_min, x_max, y_max, pad_if_needed, pad_position, border_mode)
    

    def CropAndPad(self):
        px = [0, 100]
        percent = [0, 1]
        pad_mode = [
            cv2.BORDER_CONSTANT,
            cv2.BORDER_REPLICATE,
            cv2.BORDER_REFLECT,
            cv2.BORDER_WRAP,
            cv2.BORDER_REFLECT_101
        ]
        keep_size = [
            True,
            False
        ]
        return (px, percent, pad_mode, keep_size)
        

    def CropNonEmptyMaskIfExists(self):
        height = [100, 1024]
        width = [100, 1024]
        return (height, width)
    

    def D4(self):
        return ()
    

    def ElasticTransform(self):
        alpha = [0, 1000]
        sigma = [0, 100]
        alpha_affine = [0, 100]
        interpolation = [
            cv2.INTER_NEAREST,
            cv2.INTER_LINEAR,
            cv2.INTER_CUBIC
        ]
        approximate = [
            False,
            True
        ]
        same_dxdy = [
            False,
            True
        ]
        return (alpha, sigma, alpha_affine, interpolation, approximate, same_dxdy)
    

    def Erasing(self):
        scale = [(0, 1), "float"]
        ratio = [(0, 1), "float"]
        fill = [0, 255]
        return (scale, ratio, fill)
    

    def FrequencyMasking(self):
        freq_mask_param = [1, 100]
        return (freq_mask_param,)


    def GridDistortion(self):
        num_steps = [1, 10]
        distort_limit = [0, 1]
        interpolation = [
            cv2.INTER_NEAREST,
            cv2.INTER_LINEAR,
            cv2.INTER_CUBIC
        ]
        normalized = [
            True,
            False
        ]
        return (num_steps, distort_limit, interpolation, normalized)


    def GridDropout(self):
        a.GridDropout()
        ratio = [0, 1]
        random_offset = [
            True,
            False
        ]
        unit_size_range = [(0, 100), "int"]
        holes_number_xy = [(0, 100) , "int"]
        shift_xy = [(0, 512), "int"]
        fill = [0, 255]
        return (ratio,  random_offset, unit_size_range, holes_number_xy, shift_xy, fill)


    def GridElasticDeform(self):
        num_grid_xy = [(8,10), "int"]
        magnitude = [0, 10]
        interpolation = [
            cv2.INTER_NEAREST,
            cv2.INTER_LINEAR,
            cv2.INTER_CUBIC
        ]
        return (num_grid_xy, magnitude, interpolation)


    def HorizontalFlip(self):
        return ()


    def LongestMaxSize(self):
        a.LongestMaxSize()
        max_size = [100, 2048]
        return (max_size,)


    def Morphological(self):
        scale = [(2,3), "int"]
        operation = [
            "erosion",
            "dilation"
        ]
        return (scale, operation)


    def NoOp(self):
        return ()


    def OpticalDistortion(self):
        distort_limit = [(-0.5, 0.5), "float"]
        shift_limit = [0, 1]
        interpolation = [
            cv2.INTER_NEAREST,
            cv2.INTER_LINEAR,
            cv2.INTER_CUBIC
        ]
        return (distort_limit, shift_limit, interpolation)


    def OverlayElements(self):
        return ()


    def Pad(self):
        padding = [0, 100]
        fill = [0, 255]
        return (padding, fill)


    def Perspective(self):
        a.Perspective()
        scale = [0, 1]
        keep_size = [
            True,
            False
        ]
        fit_output = [
            False,
            True
        ]
        interpolation = [
            cv2.INTER_NEAREST,
            cv2.INTER_LINEAR,
            cv2.INTER_CUBIC
        ]
        return (scale, keep_size, fit_output, interpolation)


    def PixelDropout(self):

        dropout_prob = [0, 1]
        per_channel = [
            False,
            True
        ]

        return (dropout_prob, per_channel)


    def RandomCrop(self):
        height = [100, 1024]
        width = [100, 1024]
        pad_if_needed = [False, True]
        pad_position= [
            'center',
            'top_left',
            'top_right',
            'bottom_left',
            'bottom_right',
            'random'
        ]
        return (height, width, pad_if_needed, pad_position)
    

    def RandomRotate90(self):
        return ()


    def Resize(self):
        height = [100, 2048]
        width = [100, 2048]
        interpolation = [
            cv2.INTER_NEAREST,
            cv2.INTER_LINEAR,
            cv2.INTER_CUBIC
        ]
        return (height, width, interpolation)


    def Rotate(self):
        limit = [(0, 360), "int"]
        interpolation = [
            cv2.INTER_NEAREST,
            cv2.INTER_LINEAR,
            cv2.INTER_CUBIC
        ]
        border_mode = [
            cv2.BORDER_CONSTANT,
            cv2.BORDER_REPLICATE,
            cv2.BORDER_REFLECT,
            cv2.BORDER_WRAP,
            cv2.BORDER_REFLECT_101
        ]
        return (limit, interpolation, border_mode)


    def ThinPlateSpline(self):
        scale_range = [(0.2, 0.4), "float"]
        num_control_points = [1, 100]
        interpolation = [
            cv2.INTER_NEAREST,
            cv2.INTER_LINEAR,
            cv2.INTER_CUBIC
        ]
        return (scale_range, num_control_points, interpolation)


    def TimeMasking(self):
        time_mask_param = [1, 100]
        return (time_mask_param,)


    def TimeReverse(self):
        return ()


    def Transpose(self):
        return ()


    def VerticalFlip(self):
        return ()
