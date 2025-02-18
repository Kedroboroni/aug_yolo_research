import cv2




class manageParams:

    def __init__(self, parent):

        self.name_fun = parent
        #дальше, описываем методы по названию функций, в них описываем кажду переменную, которая у нее есть
        #Делаем return этих параметров и возварщаем это из класса
        #ВНЕ ФАЙЛА Передаем эти параметры в partial

        #return parent()

    def get_params(self):
        if self.name_fun == "Affine":
            return self.Affine()
        elif self.name_fun == "AtLeastOneBBoxRandomCrop":
            return self.AtLeastOneBBoxRandomCrop()
        elif self.name_fun == "BBoxSafeRandomCrop":
            return self.BBoxSafeRandomCrop()
        elif self.name_fun == "CenterCrop":
            return self.CenterCrop()
        elif self.name_fun == "CoarseDropout":
            return self.CoarseDropout()
        elif self.name_fun == "ConstrainedCoarseDropout":
            return self.ConstrainedCoarseDropout()
        elif self.name_fun == "Crop":
            return self.Crop()
        elif self.name_fun == "CropAndPad":
            return self.CropAndPad()
        elif self.name_fun == "CropNonEmptyMaskIfExists":
            return self.CropNonEmptyMaskIfExists()
        elif self.name_fun == "D4":
            return self.D4()
        elif self.name_fun == "ElasticTransform":
            return self.ElasticTransform()
        elif self.name_fun == "Erasing":
            return self.Erasing()
        elif self.name_fun == "FrequencyMasking":
            return self.FrequencyMasking()
        elif self.name_fun == "GridDistortion":
            return self.GridDistortion()
        elif self.name_fun == "GridDropout":
            return self.GridDropout()
        elif self.name_fun == "GridElasticDeform":
            return self.GridElasticDeform()
        elif self.name_fun == "HorizontalFlip":
            return self.HorizontalFlip()
        elif self.name_fun == "LongestMaxSize":
            return self.LongestMaxSize()
        elif self.name_fun == "Morphological":
            return self.Morphological()
        elif self.name_fun == "NoOp":
            return self.NoOp()
        elif self.name_fun == "OpticalDistortion":
            return self.OpticalDistortion()
        elif self.name_fun == "OverlayElements":
            return self.OverlayElements()
        elif self.name_fun == "Pad":
            return self.Pad()
        elif self.name_fun == "Perspective":
            return self.Perspective()
        elif self.name_fun == "ThinPlateSpline":
            return self.ThinPlateSpline()
        elif self.name_fun == "hsv_h":
            return self.hsv_h()
        elif self.name_fun == "hsv_s":
            return self.hsv_s()
        elif self.name_fun == "hsv_v":
            return self.hsv_v()
        elif self.name_fun == "degrees":
            return self.degrees()
        elif self.name_fun == "translate":
            return self.translate()
        elif self.name_fun == "scale":
            return self.scale()
        elif self.name_fun == "shear":
            return self.shear()
        elif self.name_fun == "perspective":
            return self.perspective()
        elif self.name_fun == "flipud":
            return self.flipud()
        elif self.name_fun == "fliplr":
            return self.fliplr()
        elif self.name_fun == "bgr":
            return self.bgr()
        elif self.name_fun == "mosaic":
            return self.mosaic()
        elif self.name_fun == "mixup":
            return self.mixup()
        elif self.name_fun == "copy_paste":
            return self.copy_paste()
        elif self.name_fun == "copy_paste_mode":
            return self.copy_paste_mode()
        elif self.name_fun == "auto_augument":
            return self.auto_augument()
        elif self.name_fun == "erasing":
            return self.erasing()
        elif self.name_fun == "crop_fraction":
            return self.crop_fraction()
        else:
            raise ValueError(f"Метод: {self.name_fun} не существует")
            
        #!!!!!!!Добавить все услвоия, или подумать как этого не делать, но созранить возврат функций по self.name_fun

    def Affine(self):
        import albumentations as a
        a.Affine()
        scale = [1, 10]
        translate_percent = [0, 5]
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
        return (height, width, erosion_factor)
    

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
        num_holes_range = [(1,2), "int"]
        hole_height_range = [(0.1, 0.2), "float"]
        hole_width_range = [(0.1, 0.2), "float"]
        fill = [0, 255]
        return (num_holes_range, hole_height_range, hole_width_range, fill)


    def Crop(self):
        x_min = [0, 10]
        y_min = [0, 10]
        x_max = [1024, 2048]
        y_max = [1024, 2048]
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
            cv2.INTER_AREA,
            cv2.INTER_BITS,
            cv2.INTER_LINEAR,
            cv2.INTER_CUBIC,
            cv2.INTER_MAX,
            cv2.INTER_NEAREST_EXACT
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
            cv2.INTER_AREA,
            cv2.INTER_BITS,
            cv2.INTER_LINEAR,
            cv2.INTER_CUBIC,
            cv2.INTER_MAX,
            cv2.INTER_NEAREST_EXACT
        ]
        normalized = [
            True,
            False
        ]
        return (num_steps, distort_limit, interpolation, normalized)


    def GridDropout(self):
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
        magnitude = [1, 100]
        interpolation = [
            cv2.INTER_NEAREST,
            cv2.INTER_AREA,
            cv2.INTER_BITS,
            cv2.INTER_LINEAR,
            cv2.INTER_CUBIC,
            cv2.INTER_MAX,
            cv2.INTER_NEAREST_EXACT
        ]
        return (num_grid_xy, magnitude, interpolation)


    def HorizontalFlip(self):
        return ()


    def LongestMaxSize(self):
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
            cv2.INTER_AREA,
            cv2.INTER_BITS,
            cv2.INTER_LINEAR,
            cv2.INTER_CUBIC,
            cv2.INTER_MAX,
            cv2.INTER_NEAREST_EXACT
        ]
        return (distort_limit, shift_limit, interpolation)


    def OverlayElements(self):
        return ()


    def Pad(self):
        padding = [0, 100]
        fill = [0, 255]
        return (padding, fill)


    def Perspective(self):
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
            cv2.INTER_AREA,
            cv2.INTER_BITS,
            cv2.INTER_LINEAR,
            cv2.INTER_CUBIC,
            cv2.INTER_MAX,
            cv2.INTER_NEAREST_EXACT
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
            cv2.INTER_AREA,
            cv2.INTER_BITS,
            cv2.INTER_LINEAR,
            cv2.INTER_CUBIC,
            cv2.INTER_MAX,
            cv2.INTER_NEAREST_EXACT
        ]
        return (height, width, interpolation)


    def Rotate(self):
        limit = [(0, 360), "int"]
        interpolation = [
            cv2.INTER_NEAREST,
            cv2.INTER_AREA,
            cv2.INTER_BITS,
            cv2.INTER_LINEAR,
            cv2.INTER_CUBIC,
            cv2.INTER_MAX,
            cv2.INTER_NEAREST_EXACT
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
            cv2.INTER_AREA,
            cv2.INTER_BITS,
            cv2.INTER_LINEAR,
            cv2.INTER_CUBIC,
            cv2.INTER_MAX,
            cv2.INTER_NEAREST_EXACT
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
    

    def AdditiveNoise(self):
        noise_type = [
            'uniform',
            'gaussian',
            'laplace',
            'beta'
        ]
        spatial_mode = [
            'constant',
            'per_pixel',
            'shared'
        ]
        return (noise_type, spatial_mode)


    def AdvancedBlur(self):
        blur_limit = [(3, 7), "int"]
        sigma_x_limit= [(0.2, 1), "float"]
        sigma_y_limit= [(0.2, 1), "float"]
        rotate_limit = [(-90, 90), "int"]
        beta_limit = [(0.5, 8), "float"]
        noise_limit = [(0.9, 1.1), "float"]
        return (blur_limit, sigma_x_limit, sigma_y_limit, rotate_limit, beta_limit, noise_limit)


    def AutoContrast(self):
        return ()


    def Blur(self):
        blur_limit = [(3, 7), "int"]
        return (blur_limit,)


    def CLAHE(self):
        clip_limit = [1, 10]
        tile_grid_size = [(8, 8), "int"]
        return (clip_limit, tile_grid_size)


    def ChannelDropout(self):
        channel_drop_range = [(1, 3), "int"]
        fill_value = [0, 255]
        return (channel_drop_range, fill_value)


    def ChannelShuffle(self):
        return ()


    def ChromaticAberration(self):
        distortion_scale = [(-0.02, 0.02), "float"]
        secondary_distortion_limit = [(-0.05, 0.05), "float"]
        return (distortion_scale, secondary_distortion_limit)


    def ColorJitter(self):
        brightness = [(0.8, 1.2), "float"]
        contrast = [(0.8, 1.2), "float"]
        saturation = [(0.8, 1.2), "float"]
        hue = [(-0.5, 0.5), "float"]
        return (brightness, contrast, saturation, hue)


    def Defocus(self):
        radius = [(3, 10), "int"]
        alias_blur = [(0.1, 0.5), "float"]
        return (radius, alias_blur)


    def Downscale(self):
        scale_min = [(0.25, 0.25), "float"]
        return (scale_min)


    def Emboss(self):
        alpha = [(0, 0.5), "float"]
        strength = [(0.2, 0.7), "float"]
        return (alpha, strength)


    def Equalize(self):
        mode = ['cv', 'pil']
        by_channels = [True, False]
        return (mode, by_channels)


    def FDA(self):
        beta_limit = [(0, 0.1), "float"]
        return (beta_limit,)


    def FancyPCA(self):
        alpha = [(0, 0.1), "float"]
        return (alpha,)


    def FromFloat(self):
        return ()


    def GaussNoise(self):
        var_limit = [(0.2, 0.44), "int"]
        mean = [(0, 0), "float"]
        per_channel = [
            True,
            False
        ]
        return (var_limit, mean, per_channel)


    def GaussianBlur(self):
        blur_limit = [0, 100]
        sigma_limit = [(0.5, 3), "float"]
        return (blur_limit,sigma_limit)


    def GlassBlur(self):
        sigma = [0, 1]
        max_delta = [0, 100]
        iterations = [0, 5]
        return (sigma, max_delta, iterations)


    def HueSaturationValue(self):
        hue_shift_limit = [(-20, 20), "int"]
        sat_shift_limit = [(-30, 30), "int"]
        val_shift_limit = [(-20, 20), "int"]
        return (hue_shift_limit, sat_shift_limit, val_shift_limit)


    def ISONoise(self):
        color_shift_limit = [(0.01, 0.05), "float"]
        intensity = [(0.1, 0.5), "float"]
        return (color_shift_limit, intensity)


    def Illumination(self):
        mode = [
            'linear',
            'corner',
            'gaussian'
        ]
        intensity_range = [(0.01, 0.2), "float"]
        effect_type = [
            'brighten',
            'darken',
            'both'
        ]
        angle_range= [(0, 360), "float"]
        center_range = [(0.1, 0.9), "float"]
        sigma_range = [(0.2, 1), "float"]
        return (mode, intensity_range, effect_type, angle_range, center_range, sigma_range)


    def ImageCompression(self):
        compression_typ =[
            'jpeg',
            'webp'
        ]
        quality_range = [(99, 100), "int"]
        return (compression_typ, quality_range)


    def InvertImg(self):
        return ()


    def MedianBlur(self):
        blur_limit = [0, 10]
        return (blur_limit,)


    def MotionBlur(self):
        blur_limit = [(3, 7), "int"]
        allow_shifted = [
            True,
            False
        ]
        angle_range = [(0, 360),"float"]
        direction_range = [(-1, 1), "float"]
        return (blur_limit,allow_shifted, angle_range, direction_range)


    def MultiplicativeNoise(self):
        multiplier = [(0.9, 1.1), "float"]
        per_channel = [True, False]
        return (multiplier, per_channel)


    def Normalize(self):
        mean = [(0, 255), "int"]
        std = [(0, 255), "int"]
        max_pixel_value = [(1, 255), "int"]
        return (mean, std, max_pixel_value)


    def PixelDistributionAdaptation(self):
        transform_type = ['pca', 'standard']
        return (transform_type,)


    def PlanckianJitter(self):
        mode = ['blackbody', 'CIED']
        strength = [(0, 1), "float"]
        return (mode, strength)


    def PlasmaBrightnessContrast(self):
        alpha = [(0, 1), "float"]
        beta = [(0, 1), "float"]
        return (alpha, beta)


    def PlasmaShadow(self):
        alpha = [(0, 1), "float"]
        beta = [(0, 1), "float"]
        return (alpha, beta)


    def Posterize(self):
        num_bits = [(4, 8), "int"]
        return (num_bits,)


    def RGBShift(self):
        r_shift_limit = [(-20, 20), "int"]
        g_shift_limit = [(-20, 20), "int"]
        b_shift_limit = [(-20, 20), "int"]
        return (r_shift_limit, g_shift_limit, b_shift_limit)


    def RandomBrightnessContrast(self):
        brightness_limit = [(-0.2, 0.2), "float"]
        contrast_limit = [(-0.2, 0.2), "float"]
        return (brightness_limit, contrast_limit)


    def RandomFog(self):
        fog_coef_lower = [(0.3, 1.0), "float"]
        fog_coef_upper = [(0.3, 1.0), "float"]
        alpha_coef = [(0.08, 0.1), "float"]
        return (fog_coef_lower, fog_coef_upper, alpha_coef)


    def RandomGamma(self):
        gamma_limit = [(80, 120), "int"]
        return (gamma_limit,)


    def RandomGravel(self):
        gravel_roi = [(0, 1), "float"]
        number_of_patches = [(1, 5), "int"]
        return (gravel_roi, number_of_patches)


    def RandomRain(self):
        slant_lower = [(-10, 10), "int"]
        drop_length = [0, 100]
        drop_width = [1, 100]
        return (slant_lower, drop_length, drop_width)


    def RandomShadow(self):
        return ()


    def RandomSnow(self):
        brightness_coeff = [(2.5, 3.5), "float"]
        snow_point_range = [(0.1, 0.3), "float"]
        method = [
            'bleach',
            'texture'
        ]
        return (brightness_coeff, snow_point_range, method)


    def RandomSunFlare(self):
        return ()


    def RandomToneCurve(self):
        scale = [0, 1]
        per_chanel = [
            False,
            True
        ]
        return (scale, per_chanel)


    def RingingOvershoot(self):
        blur_limit = [(3, 7), "int"]
        return (blur_limit,)


    def SaltAndPepper(self):
        noise_density = [(0.01, 0.06), "float"]
        salt_vs_pepper = [(0.4, 0.6), "float"]
        return (noise_density, salt_vs_pepper)


    def Sharpen(self):
        alpha = [(0, 1), "float"]
        lightness = [(0, 1), "float"]
        return (alpha, lightness)


    def ShotNoise(self):
        intensity = [(0, 1), "float"]
        return (intensity,)


    def Solarize(self):
        threshold = [(128, 255), "int"]
        return (threshold,)


    def Spatter(self):
        mean = [(0, 1), "float"]
        std = [(0, 1), "float"]
        gauss = [True, False]
        return (mean, std, gauss)


    def Superpixels(self):
        p_replace = [(0, 1), "float"]
        n_segments = [(100, 200), "int"]
        max_size = [(128, 256), "int"]
        interpolation = [
            cv2.INTER_NEAREST,
            cv2.INTER_LINEAR,
            cv2.INTER_CUBIC,
            cv2.INTER_AREA
        ]
        return (p_replace, n_segments, max_size, interpolation)


    def TemplateTransform(self):
        img_weight = [(0, 1), "float"]
        template_weight = [(0, 1), "float"]
        return (img_weight, template_weight)


    def TextImage(self):
        text = ['example']
        font = ['arial']
        size = [(10, 50), "int"]
        color = [(0, 0, 0), (255, 255, 255)]
        thickness = [(1, 3), "int"]
        return (text, font, size, color, thickness)


    def ToFloat(self):
        return ()


    def ToGray(self):
        return ()


    def ToRGB(self):
        return ()


    def ToSepia(self):
        return ()


    def UnsharpMask(self):
        blur_limit = [(3, 7), "int"]
        sigma_limit = [(0, 1), "float"]
        alpha = [(0, 1), "float"]
        threshold = [(0, 1), "float"]
        return (blur_limit, sigma_limit, alpha, threshold)


    def ZoomBlur(self):
        max_factor = [(1.0, 1.5), "float"]
        step_factor = [(0.01, 0.1), "float"]
        return (max_factor, step_factor)
    

    def hsv_h(self):
        hsv_h = [0, 1]
        return (hsv_h,)
    

    def hsv_s(self):
        hsv_s = [0, 1] 
        return (hsv_s,)
    

    def hsv_v(self):
        hsv_v = [0, 1]
        return (hsv_v,)
    

    def degrees(self):
        degrees = [0, 180]
        return (degrees,)
    

    def translate(self):
        translate = [0, 1]
        return (translate,)
    

    def scale(self):
        scale = [0, 10]
        return (scale,)
    

    def shear(self):
        shear = [0, 180]
        return (shear,)
    

    def perspective(self):
        perspective = [0, 0.01]
        return (perspective,)
    

    def flipud(self):
        flipud = [0, 1]
        return (flipud,)
    

    def fliplr(self):
        fliplr = [0, 1]
        return (fliplr,)
    

    def bgr(self):
        bgr = [0, 1]
        return (bgr,)
    

    def mosaic(self):
        mosaic = [0, 1]
        return (mosaic,)
    

    def mixup(self):
        mixup = [0, 1]
        return (mixup,)
    

    def copy_paste(self):
        copy_paste = [0, 1]
        return (copy_paste,)
    

    def copy_paste_mode(self):
        copy_paste_mode = [
            "flip",
            "mixup"
        ]
        return (copy_paste_mode,)
    

    def auto_augument(self):
        auto_augment = [
            "randaugment",
            "autoaugment",
            "augmix"
        ]
        return (auto_augment,)
    

    def erasing(self):
        erasing = [0, 0.9]
        return (erasing,)
    

    def crop_fraction(self):
        crop_fraction = [0, 1]
        return (crop_fraction,)

    #