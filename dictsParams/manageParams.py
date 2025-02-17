
import cv2

import albumentations as a



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
        elif self.name_fun == "PixelDropout":
            return self.PixelDropout()
        elif self.name_fun == "RandomCrop":
            return self.RandomCrop()
        elif self.name_fun == "RandomRotate90":
            return self.RandomRotate90()
        elif self.name_fun == "Resize":
            return self.Resize()
        elif self.name_fun == "Rotate":
            return self.Rotate()
        elif self.name_fun == "ThinPlateSpline":
            return self.ThinPlateSpline()
        elif self.name_fun == "TimeMasking":
            return self.TimeMasking()
        elif self.name_fun == "TimeReverse":
            return self.TimeReverse()
        elif self.name_fun == "Transpose":
            return self.Transpose()
        elif self.name_fun == "VerticalFlip":
            return self.VerticalFlip()
        elif self.name_fun == "AdditiveNoise":
            return self.AdditiveNoise()
        elif self.name_fun == "AdvancedBlur":
            return self.AdvancedBlur()
        elif self.name_fun == "AutoContrast":
            return self.AutoContrast()
        elif self.name_fun == "Blur":
            return self.Blur()
        elif self.name_fun == "CLAHE":
            return self.CLAHE()
        elif self.name_fun == "ChannelDropout":
            return self.ChannelDropout()
        elif self.name_fun == "ChannelShuffle":
            return self.ChannelShuffle()
        elif self.name_fun == "ChromaticAberration":
            return self.ChromaticAberration()
        elif self.name_fun == "ColorJitter":
            return self.ColorJitter()
        elif self.name_fun == "Defocus":
            return self.Defocus()
        elif self.name_fun == "Downscale":
            return self.Downscale()
        elif self.name_fun == "Emboss":
            return self.Emboss()
        elif self.name_fun == "Equalize":
            return self.Equalize()
        elif self.name_fun == "FDA":
            return self.FDA()
        elif self.name_fun == "FancyPCA":
            return self.FancyPCA()
        elif self.name_fun == "FromFloat":
            return self.FromFloat()
        elif self.name_fun == "GaussNoise":
            return self.GaussNoise()
        elif self.name_fun == "GaussianBlur":
            return self.GaussianBlur()
        elif self.name_fun == "GlassBlur":
            return self.GlassBlur()
        elif self.name_fun == "HEStain":
            return self.HEStain()
        elif self.name_fun == "HistogramMatching":
            return self.HistogramMatching()
        elif self.name_fun == "HueSaturationValue":
            return self.HueSaturationValue()
        elif self.name_fun == "ISONoise":
            return self.ISONoise()
        elif self.name_fun == "Illumination":
            return self.Illumination()
        elif self.name_fun == "ImageCompression":
            return self.ImageCompression()
        elif self.name_fun == "InvertImg":
            return self.InvertImg()
        elif self.name_fun == "MedianBlur":
            return self.MedianBlur()
        elif self.name_fun == "MotionBlur":
            return self.MotionBlur()
        elif self.name_fun == "MultiplicativeNoise":
            return self.MultiplicativeNoise()
        elif self.name_fun == "Normalize":
            return self.Normalize()
        elif self.name_fun == "PixelDistributionAdaptation":
            return self.PixelDistributionAdaptation()
        elif self.name_fun == "PlanckianJitter":
            return self.PlanckianJitter()
        elif self.name_fun == "PlasmaBrightnessContrast":
            return self.PlasmaBrightnessContrast()
        elif self.name_fun == "PlasmaShadow":
            return self.PlasmaShadow()
        elif self.name_fun == "Posterize":
            return self.Posterize()
        elif self.name_fun == "RGBShift":
            return self.RGBShift()
        elif self.name_fun == "RandomBrightnessContrast":
            return self.RandomBrightnessContrast()
        elif self.name_fun == "RandomFog":
            return self.RandomFog()
        elif self.name_fun == "RandomGamma":
            return self.RandomGamma()
        elif self.name_fun == "RandomGravel":
            return self.RandomGravel()
        elif self.name_fun == "RandomRain":
            return self.RandomRain()
        elif self.name_fun == "RandomShadow":
            return self.RandomShadow()
        elif self.name_fun == "RandomSnow":
            return self.RandomSnow()
        elif self.name_fun == "RandomSunFlare":
            return self.RandomSunFlare()
        elif self.name_fun == "RandomToneCurve":
            return self.RandomToneCurve()
        elif self.name_fun == "RingingOvershoot":
            return self.RingingOvershoot()
        elif self.name_fun == "SaltAndPepper":
            return self.SaltAndPepper()
        elif self.name_fun == "Sharpen":
            return self.Sharpen()
        elif self.name_fun == "ShotNoise":
            return self.ShotNoise()
        elif self.name_fun == "Solarize":
            return self.Solarize()
        elif self.name_fun == "Spatter":
            return self.Spatter()
        elif self.name_fun == "Superpixels":
            return self.Superpixels()
        elif self.name_fun == "TemplateTransform":
            return self.TemplateTransform()
        elif self.name_fun == "TextImage":
            return self.TextImage()
        elif self.name_fun == "ToFloat":
            return self.ToFloat()
        elif self.name_fun == "ToGray":
            return self.ToGray()
        elif self.name_fun == "ToRGB":
            return self.ToRGB()
        elif self.name_fun == "ToSepia":
            return self.ToSepia()
        elif self.name_fun == "UnsharpMask":
            return self.UnsharpMask()
        elif self.name_fun == "ZoomBlur":
            return self.ZoomBlur()
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
        a.Emboss()
        alpha = [(0, 0.5), "float"]
        strength = [(0.2, 0.7), "float"]
        return (alpha, strength)

    def Equalize(self):
        a.Equalize()
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
        a.MedianBlur()
        blur_limit = [0, 10]
        return (blur_limit,)

    def MotionBlur(self):
        a.MotionBlur()
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
        slant_upper = [(-10, 10), "int"]
        drop_length = [(20, 30), "int"]
        drop_width = [(1, 2), "int"]
        drop_color = [(200, 200, 200), (255, 255, 255)]
        return (slant_lower, slant_upper, drop_length, drop_width, drop_color)

    def RandomShadow(self):
        shadow_roi = [(0, 1), "float"]
        num_shadows_lower = [(1, 2), "int"]
        num_shadows_upper = [(1, 2), "int"]
        shadow_dimension = [(5, 10), "int"]
        return (shadow_roi, num_shadows_lower, num_shadows_upper, shadow_dimension)

    def RandomSnow(self):
        snow_point_lower = [(0.1, 0.3), "float"]
        snow_point_upper = [(0.7, 1.0), "float"]
        brightness_coeff = [(2.5, 3.5), "float"]
        return (snow_point_lower, snow_point_upper, brightness_coeff)

    def RandomSunFlare(self):
        flare_roi = [(0, 1), "float"]
        angle_lower = [(0, 360), "int"]
        angle_upper = [(0, 360), "int"]
        num_flare_circles_lower = [(6, 10), "int"]
        num_flare_circles_upper = [(6, 10), "int"]
        src_radius = [(400, 800), "int"]
        src_color = [(255, 255, 255), (255, 255, 255)]
        return (flare_roi, angle_lower, angle_upper, num_flare_circles_lower, num_flare_circles_upper, src_radius, src_color)

    def RandomToneCurve(self):
        scale = [(0, 1), "float"]
        return (scale,)

    def RingingOvershoot(self):
        blur_limit = [(3, 7), "int"]
        return (blur_limit,)

    def SaltAndPepper(self):
        noise_density = [(0.001, 0.01), "float"]
        return (noise_density,)

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