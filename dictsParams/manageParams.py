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
        elif self.name_fun == "auto_augment":
            return self.auto_augment()
        elif self.name_fun == "erasing":
            return self.erasing()
        elif self.name_fun == "crop_fraction":
            return self.crop_fraction()
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
        

        elif self.name_fun == "RandomCrop":
            return self.RandomCrop()
        elif self.name_fun == "RandomRotate90":
            return self.RandomRotate90()
        elif self.name_fun == "Resize":
            return self.Resize()
        elif self.name_fun == "Rotate":
            return self.Rotate()
        elif self.name_fun == "PixelDropout":
            return self.PixelDropout()
        elif self.name_fun == "TimeMasking":
            return self.TimeMasking()
        elif self.name_fun == "TimeReverse":
            return self.TimeReverse()
        elif self.name_fun == "Transpose":
            return self.Transpose()
        elif self.name_fun == "VerticalFlip":
            return self.VerticalFlip()  
        else:
            raise ValueError(f"Метод: {self.name_fun} не существует")


    def Affine(self):
        scale = [1, 10]
        translate_px = [1, 10] 
        rotate = [0, 360]
        shear = [0, 100]
        interpolation = [
            cv2.INTER_NEAREST,
            cv2.INTER_LINEAR,
            cv2.INTER_CUBIC,
            cv2.INTER_AREA,
            cv2.INTER_LANCZOS4,
            cv2.INTER_BITS,
            cv2.INTER_NEAREST_EXACT,
            cv2.INTER_MAX          
        ]
        return {
            "scale": scale,
            "translate_px": translate_px,
            "rotate": rotate,
            "shear": shear,
            "interpolation": interpolation
        }

        
    def AtLeastOneBBoxRandomCrop(self):
        height = [100, 1024]
        width = [100, 1024]
        erosion_factor = [0, 1]
        return {
            "height": height,
            "width": width,
            "erosion_factor": erosion_factor
        }
    

    def BBoxSafeRandomCrop(self):
        erosion_rate = [0, 1]
        return {"erosion_rate": erosion_rate}
    

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
        return {
            "height": height,
            "width": width,
            "pad_if_needed": pad_if_needed,
            "pad_position": pad_position,
            "border_mode": border_mode
        }
    

    def CoarseDropout(self):
        num_holes_range = [(1,2), 'int']
        hole_height_range = [(0.1, 0.2), "float"]
        hole_width_range = [(0.1, 0.2), "float"]
        fill = [0, 255]
        return {
            "num_holes_range": num_holes_range,
            "hole_height_range": hole_height_range,
            "hole_width_range": hole_width_range,
            "fill": fill
        }


    def ConstrainedCoarseDropout(self):
        num_holes_range = [(1,2), "int"]
        hole_height_range = [(0.1, 0.2), "float"]
        hole_width_range = [(0.1, 0.2), "float"]
        fill = [0, 255]
        return {
            "num_holes_range": num_holes_range,
            "hole_height_range": hole_height_range,
            "hole_width_range": hole_width_range,
            "fill": fill
        }


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
        return {
            "x_min": x_min,
            "y_min": y_min,
            "x_max": x_max,
            "y_max": y_max,
            "pad_if_needed": pad_if_needed,
            "pad_position": pad_position,
            "border_mode": border_mode
        }
    

    def CropAndPad(self):
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
        return {
            "percent": percent,
            "pad_mode": pad_mode,
            "keep_size": keep_size
        }
        

    def CropNonEmptyMaskIfExists(self):
        height = [100, 1024]
        width = [100, 1024]
        return {
            "height": height,
            "width": width
        }
    

    def D4(self):
        return {}
    

    def ElasticTransform(self):
        alpha = [0, 1000]
        sigma = [0, 100]
        alpha_affine = [0, 100]
        interpolation = [
            cv2.INTER_NEAREST,
            cv2.INTER_LINEAR,
            cv2.INTER_CUBIC,
            cv2.INTER_AREA,
            cv2.INTER_LANCZOS4,
            cv2.INTER_BITS,
            cv2.INTER_NEAREST_EXACT,
            cv2.INTER_MAX          
        ]
        approximate = [
            False,
            True
        ]
        same_dxdy = [
            False,
            True
        ]
        return {
            "alpha": alpha,
            "sigma": sigma,
            "alpha_affine": alpha_affine,
            "interpolation": interpolation,
            "approximate": approximate,
            "same_dxdy": same_dxdy
        }
    

    def Erasing(self):
        scale = [(0, 1), "float"]
        ratio = [(0, 1), "float"]
        fill = [0, 255]
        return {
            "scale": scale,
            "ratio": ratio,
            "fill": fill
        }
    

    def FrequencyMasking(self):
        freq_mask_param = [1, 100]
        return {"freq_mask_param": freq_mask_param}


    def GridDistortion(self):
        num_steps = [1, 10]
        distort_limit = [0, 1]
        interpolation = [
            cv2.INTER_NEAREST,
            cv2.INTER_LINEAR,
            cv2.INTER_CUBIC,
            cv2.INTER_AREA,
            cv2.INTER_LANCZOS4,
            cv2.INTER_BITS,
            cv2.INTER_NEAREST_EXACT,
            cv2.INTER_MAX          
        ]
        normalized = [
            True,
            False
        ]
        return {
            "num_steps": num_steps,
            "distort_limit": distort_limit,
            "interpolation": interpolation,
            "normalized": normalized
        }


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
        return {
            "ratio": ratio,
            "random_offset": random_offset,
            "unit_size_range": unit_size_range,
            "holes_number_xy": holes_number_xy,
            "shift_xy": shift_xy,
            "fill": fill
        }


    def GridElasticDeform(self):
        num_grid_xy = [(8,10), "int"]
        magnitude = [1, 100]
        interpolation = [
            cv2.INTER_NEAREST,
            cv2.INTER_LINEAR,
            cv2.INTER_CUBIC,
            cv2.INTER_AREA,
            cv2.INTER_LANCZOS4,
            cv2.INTER_BITS,
            cv2.INTER_NEAREST_EXACT,
            cv2.INTER_MAX,
            "asda"          
        ]
        return {
            "num_grid_xy": num_grid_xy,
            "magnitude": magnitude,
            "interpolation": interpolation
        }


    def HorizontalFlip(self):
        return {}


    def LongestMaxSize(self):
        max_size = [100, 2048]
        return {"max_size": max_size}


    def Morphological(self):
        scale = [(2,3), "int"]
        operation = [
            "erosion",
            "dilation"
        ]
        return {
            "scale": scale,
            "operation": operation
        }


    def NoOp(self):
        return {}


    def OpticalDistortion(self):
        distort_limit = [(-0.5, 0.5), "float"]
        shift_limit = [0, 1]
        interpolation = [
            cv2.INTER_NEAREST,
            cv2.INTER_LINEAR,
            cv2.INTER_CUBIC,
            cv2.INTER_AREA,
            cv2.INTER_LANCZOS4,
            cv2.INTER_BITS,
            cv2.INTER_NEAREST_EXACT,
            cv2.INTER_MAX          
        ]
        return {
            "distort_limit": distort_limit,
            "shift_limit": shift_limit,
            "interpolation": interpolation
        }


    def OverlayElements(self):
        return {}


    def Pad(self):
        padding = [0, 100]
        fill = [0, 255]
        return {
            "padding": padding,
            "fill": fill
        }


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
            cv2.INTER_LINEAR,
            cv2.INTER_CUBIC,
            cv2.INTER_AREA,
            cv2.INTER_LANCZOS4,
            cv2.INTER_BITS,
            cv2.INTER_NEAREST_EXACT,
            cv2.INTER_MAX          
        ]
        return {
            "scale": scale,
            "keep_size": keep_size,
            "fit_output": fit_output,
            "interpolation": interpolation
        }


    def PixelDropout(self):

        dropout_prob = [0, 1]
        per_channel = [
            False,
            True
        ]

        return {
            "dropout_prob": dropout_prob,
            "per_channel": per_channel
        }


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
        return {
            "height": height,
            "width": width,
            "pad_if_needed": pad_if_needed,
            "pad_position": pad_position
        }
    

    def RandomRotate90(self):
        return {}


    def Resize(self):
        height = [100, 2048]
        width = [100, 2048]
        interpolation = [
            cv2.INTER_NEAREST,
            cv2.INTER_LINEAR,
            cv2.INTER_CUBIC,
            cv2.INTER_AREA,
            cv2.INTER_LANCZOS4,
            cv2.INTER_BITS,
            cv2.INTER_NEAREST_EXACT,
            cv2.INTER_MAX          
        ]
        return {
            "height": height,
            "width": width,
            "interpolation": interpolation
        }


    def Rotate(self):
        limit = [(0, 360), "int"]
        interpolation = [
            cv2.INTER_NEAREST,
            cv2.INTER_LINEAR,
            cv2.INTER_CUBIC,
            cv2.INTER_AREA,
            cv2.INTER_LANCZOS4,
            cv2.INTER_BITS,
            cv2.INTER_NEAREST_EXACT,
            cv2.INTER_MAX          
        ]
        border_mode = [
            cv2.BORDER_CONSTANT,
            cv2.BORDER_REPLICATE,
            cv2.BORDER_REFLECT,
            cv2.BORDER_WRAP,
            cv2.BORDER_REFLECT_101
        ]
        return {
            "limit": limit,
            "interpolation": interpolation,
            "border_mode": border_mode
        }


    def ThinPlateSpline(self):
        scale_range = [(0.2, 0.4), "float"]
        num_control_points = [1, 100]
        interpolation = [
            cv2.INTER_NEAREST,
            cv2.INTER_LINEAR,
            cv2.INTER_CUBIC,
            cv2.INTER_AREA,
            cv2.INTER_LANCZOS4,
            cv2.INTER_BITS,
            cv2.INTER_NEAREST_EXACT,
            cv2.INTER_MAX          
        ]
        return {
            "scale_range": scale_range,
            "num_control_points": num_control_points,
            "interpolation": interpolation
        }


    def TimeMasking(self):
        time_mask_param = [1, 100]
        return {"time_mask_param": time_mask_param}


    def TimeReverse(self):
        return {}


    def Transpose(self):
        return {}


    def VerticalFlip(self):
        return {}
    

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
        return {
            "noise_type": noise_type,
            "spatial_mode": spatial_mode
        }


    def AdvancedBlur(self):
        blur_limit = [(3, 7), "int"]
        sigma_x_limit= [(0.2, 1), "float"]
        sigma_y_limit= [(0.2, 1), "float"]
        rotate_limit = [(-90, 90), "int"]
        beta_limit = [(0.5, 8), "float"]
        noise_limit = [(0.9, 1.1), "float"]
        return {
            "blur_limit": blur_limit,
            "sigma_x_limit": sigma_x_limit,
            "sigma_y_limit": sigma_y_limit,
            "rotate_limit": rotate_limit,
            "beta_limit": beta_limit,
            "noise_limit": noise_limit
        }


    def AutoContrast(self):
        return {"p": [0, 1]}


    def Blur(self):
        blur_limit = [(3, 7), "int"]
        return {"blur_limit": blur_limit}


    def CLAHE(self):
        clip_limit = [1, 10]
        tile_grid_size = [(8, 8), "int"]
        return {
            "clip_limit": clip_limit,
            "tile_grid_size": tile_grid_size
        }


    def ChannelDropout(self):
        channel_drop_range = [(1, 3), "int"]
        fill_value = [0, 255]
        return {
            "channel_drop_range": channel_drop_range,
            "fill_value": fill_value
        }


    def ChannelShuffle(self):
        return {"p": [0, 1]}


    def ChromaticAberration(self):
        distortion_scale = [(-0.02, 0.02), "float"]
        secondary_distortion_limit = [(-0.05, 0.05), "float"]
        return {
            "distortion_scale": distortion_scale,
            "secondary_distortion_limit": secondary_distortion_limit
        }


    def ColorJitter(self):
        brightness = [(0.8, 1.2), "float"]
        contrast = [(0.8, 1.2), "float"]
        saturation = [(0.8, 1.2), "float"]
        hue = [(-0.5, 0.5), "float"]
        return {
            "brightness": brightness,
            "contrast": contrast,
            "saturation": saturation,
            "hue": hue
        }


    def Defocus(self):
        radius = [(3, 10), "int"]
        alias_blur = [(0.1, 0.5), "float"]
        return {
            "radius": radius,
            "alias_blur": alias_blur
        }


    def Downscale(self):
        scale_min = [(0.25, 0.25), "float"]
        return {"scale_min": scale_min}


    def Emboss(self):
        alpha = [(0, 0.5), "float"]
        strength = [(0.2, 0.7), "float"]
        return {
            "alpha": alpha,
            "strength": strength
        }


    def Equalize(self):
        mode = ['cv', 'pil', "cv"]
        by_channels = [True, False]
        return {
            "mode": mode,
            "by_channels": by_channels
        }


    def FDA(self):
        beta_limit = [(0, 0.1), "float"]
        return {"beta_limit": beta_limit}


    def FancyPCA(self):
        alpha = [(0, 0.1), "float"]
        return {"alpha": alpha}


    def FromFloat(self):
        return {"p": [0, 1]}


    def GaussNoise(self):
        var_limit = [(0.2, 0.44), "int"]
        mean = [(0, 0), "float"]
        per_channel = [True, False]
        return {
            "var_limit": var_limit,
            "mean": mean,
            "per_channel": per_channel
        }


    def GaussianBlur(self):
        blur_limit = [0, 100]
        sigma_limit = [(0.5, 3), "float"]
        return {
            "blur_limit": blur_limit,
            "sigma_limit": sigma_limit
        }


    def GlassBlur(self):
        sigma = [0, 1]
        max_delta = [0, 100]
        iterations = [0, 5]
        return {
            "sigma": sigma,
            "max_delta": max_delta,
            "iterations": iterations
        }


    def HueSaturationValue(self):
        hue_shift_limit = [(-20, 20), "int"]
        sat_shift_limit = [(-30, 30), "int"]
        val_shift_limit = [(-20, 20), "int"]
        return {
            "hue_shift_limit": hue_shift_limit,
            "sat_shift_limit": sat_shift_limit,
            "val_shift_limit": val_shift_limit
        }


    def ISONoise(self):
        color_shift_limit = [(0.01, 0.05), "float"]
        intensity = [(0.1, 0.5), "float"]
        return {
            "color_shift_limit": color_shift_limit,
            "intensity": intensity
        }


    def Illumination(self):
        mode = ['linear', 'corner', 'gaussian']
        intensity_range = [(0.01, 0.2), "float"]
        effect_type = ['brighten', 'darken', 'both']
        angle_range= [(0, 360), "float"]
        center_range = [(0.1, 0.9), "float"]
        sigma_range = [(0.2, 1), "float"]
        return {
            "mode": mode,
            "intensity_range": intensity_range,
            "effect_type": effect_type,
            "angle_range": angle_range,
            "center_range": center_range,
            "sigma_range": sigma_range
        }


    def ImageCompression(self):
        compression_typ =[
            'jpeg',
            'webp',
            'jpeg'
        ]
        quality_range = [(99, 100), "int"]
        return {
            "compression_typ": compression_typ,
            "quality_range": quality_range
        }


    def InvertImg(self):
        return {"p": [0, 1]}


    def MedianBlur(self):
        blur_limit = [0, 10]
        return {"blur_limit": blur_limit}


    def MotionBlur(self):
        blur_limit = [(3, 7), "int"]
        allow_shifted = [
            True,
            False
        ]
        angle_range = [(0, 360),"float"]
        direction_range = [(-1, 1), "float"]
        return {
            "blur_limit": blur_limit,
            "allow_shifted": allow_shifted,
            "angle_range": angle_range,
            "direction_range": direction_range
        }


    def MultiplicativeNoise(self):
        multiplier = [(0.5, 1.5), "float"]
        per_channel = [True, False]
        elementwise = [True, False]
        return {
            "multiplier": multiplier,
            "per_channel": per_channel,
            "elementwise": elementwise
        }


    def Normalize(self):
        mean = [(0.485, 0.456, 0.406), "float"]
        std = [(0.229, 0.224, 0.225), "float"]
        max_pixel_value = [255, 1]
        return {
            "mean": mean,
            "std": std,
            "max_pixel_value": max_pixel_value
        }


    def PixelDistributionAdaptation(self):
        transform_type = ['pca',
                          'standard',
                          'pca'
                        ]
        return {"transform_type": transform_type}


    def PlanckianJitter(self):
        mode = ['blackbody',
                'CIED',
                'blackbody'
            ]
        strength = [(0, 1), "float"]
        return {"mode": mode, "strength": strength}


    def PlasmaBrightnessContrast(self):
        alpha = [(0, 1), "float"]
        beta = [(0, 1), "float"]
        return {"alpha": alpha, "beta": beta}


    def PlasmaShadow(self):
        alpha = [(0, 1), "float"]
        beta = [(0, 1), "float"]
        return {"alpha": alpha, "beta": beta}


    def Posterize(self):
        num_bits = [(4, 8), "int"]
        return {"num_bits": num_bits}


    def RGBShift(self):
        r_shift_limit = [(-20, 20), "int"]
        g_shift_limit = [(-20, 20), "int"]
        b_shift_limit = [(-20, 20), "int"]
        return {
            "r_shift_limit": r_shift_limit,
            "g_shift_limit": g_shift_limit,
            "b_shift_limit": b_shift_limit
        }


    def RandomBrightnessContrast(self):
        brightness_limit = [(-0.2, 0.2), "float"]
        contrast_limit = [(-0.2, 0.2), "float"]
        brightness_by_max = [True, False]
        return {
            "brightness_limit": brightness_limit,
            "contrast_limit": contrast_limit,
            "brightness_by_max": brightness_by_max
        }


    def RandomFog(self):
        fog_coef_lower = [(0.3, 1.0), "float"]
        fog_coef_upper = [(0.3, 1.0), "float"]
        alpha_coef = [(0.08, 0.1), "float"]
        return {
            "fog_coef_lower": fog_coef_lower,
            "fog_coef_upper": fog_coef_upper,
            "alpha_coef": alpha_coef
        }


    def RandomGamma(self):
        gamma_limit = [(80, 120), "int"]
        return {"gamma_limit": gamma_limit}


    def RandomGravel(self):
        gravel_roi = [(0, 1), "float"]
        number_of_patches = [(1, 5), "int"]
        return {"gravel_roi": gravel_roi, "number_of_patches": number_of_patches}


    def RandomRain(self):
        slant_lower = [(-10, 10), "int"]
        drop_length = [0, 100]
        drop_width = [1, 100]
        return {
            "slant_lower": slant_lower,
            "drop_length": drop_length,
            "drop_width": drop_width
        }


    def RandomShadow(self):
        shadow_roi = [0.5, 0.5, 0.5, 0.5]
        num_shadows_lower = [1, 3]
        num_shadows_upper = [3, 5]
        shadow_dimension = [0.1, 0.5]
        return {
            "shadow_roi": shadow_roi,
            "num_shadows_lower": num_shadows_lower,
            "num_shadows_upper": num_shadows_upper,
            "shadow_dimension": shadow_dimension
        }


    def RandomSnow(self):
        brightness_coeff = [(2.5, 3.5), "float"]
        snow_point_range = [(0.1, 0.3), "float"]
        method = [
            'bleach',
            'texture',
            'bleach',
        ]
        return {
            "brightness_coeff": brightness_coeff,
            "snow_point_range": snow_point_range,
            "method": method
        }


    def RandomSunFlare(self):
        flare_roi = [0.5, 0.5, 0.5, 0.5]
        angle_lower = [0, 360]
        angle_upper = [0, 360]
        num_flare_circles_lower = [1, 3]
        num_flare_circles_upper = [3, 5]
        src_radius = [0.1, 0.5]
        src_color = [(0, 255), (0, 255), (0, 255)]
        return {
            "flare_roi": flare_roi,
            "angle_lower": angle_lower,
            "angle_upper": angle_upper,
            "num_flare_circles_lower": num_flare_circles_lower,
            "num_flare_circles_upper": num_flare_circles_upper,
            "src_radius": src_radius,
            "src_color": src_color
        }


    def RandomToneCurve(self):
        scale = [0, 1]
        per_chanel = [
            False,
            True
        ]
        return {"scale": scale, "per_chanel": per_chanel}


    def RingingOvershoot(self):
        blur_limit = [(3, 7), "int"]
        return {"blur_limit": blur_limit}
    

    def SaltAndPepper(self):
        noise_density = [(0.01, 0.06), "float"]
        salt_vs_pepper = [(0.4, 0.6), "float"]
        return {
            "noise_density": noise_density,
            "salt_vs_pepper": salt_vs_pepper
        }


    def Sharpen(self):
        alpha = [(0, 1), "float"]
        lightness = [(0, 1), "float"]
        return {
            "alpha": alpha,
            "lightness": lightness
        }


    def ShotNoise(self):
        intensity = [(0, 1), "float"]
        return {"intensity": intensity}


    def Solarize(self):
        threshold = [(128, 255), "int"]
        return {"threshold": threshold}


    def Spatter(self):
        mean = [(0, 1), "float"]
        std = [(0, 1), "float"]
        gauss = [True, False]
        return {
            "mean": mean,
            "std": std,
            "gauss": gauss
        }


    def Superpixels(self):
        p_replace = [(0, 1), "float"]
        n_segments = [(100, 200), "int"]
        max_size = [(128, 256), "int"]
        interpolation = [
            cv2.INTER_NEAREST,
            cv2.INTER_LINEAR,
            cv2.INTER_CUBIC,
            cv2.INTER_AREA,
            cv2.INTER_LANCZOS4,
            cv2.INTER_BITS,
            cv2.INTER_NEAREST_EXACT,
            cv2.INTER_MAX          
        ]
        return {
            "p_replace": p_replace,
            "n_segments": n_segments,
            "max_size": max_size,
            "interpolation": interpolation
        }


    def TemplateTransform(self):
        img_weight = [(0, 1), "float"]
        template_weight = [(0, 1), "float"]
        return {
            "img_weight": img_weight,
            "template_weight": template_weight
        }


    def TextImage(self):
        text = ['example']
        font = ['arial']
        size = [(10, 50), "int"]
        color = [(0, 0, 0), (255, 255, 255)]
        thickness = [(1, 3), "int"]
        return {
            "text": text,
            "font": font,
            "size": size,
            "color": color,
            "thickness": thickness
        }


    def ToFloat(self):
        return {"p": [0, 1]}


    def ToGray(self):
        return {"p": [0, 1]}


    def ToRGB(self):
        return {"p": [0, 1]}


    def ToSepia(self):
        return {"p": [0, 1]}


    def UnsharpMask(self):
        blur_limit = [(3, 7), "int"]
        sigma_limit = [(0, 10), "float"]
        alpha = [(0, 1), "float"]
        threshold = [(0, 255), "float"]
        return {
            "blur_limit": blur_limit,
            "sigma_limit": sigma_limit,
            "alpha": alpha,
            "threshold": threshold
        }


    def ZoomBlur(self):
        max_factor = [(1.0, 1.5), "float"]
        step_factor = [(0.01, 0.1), "float"]
        return {
            "max_factor": max_factor,
            "step_factor": step_factor
        }
    

    def hsv_h(self):
        hsv_h = [0, 1]
        return {"hsv_h": hsv_h}
    

    def hsv_s(self):
        hsv_s = [0, 1] 
        return {"hsv_s": hsv_s}
    

    def hsv_v(self):
        hsv_v = [0, 1]
        return {"hsv_v": hsv_v}
    

    def degrees(self):
        degrees = [0, 180]
        return {"degrees": degrees}
    

    def translate(self):
        translate = [0, 1]
        return {"translate": translate}
    

    def scale(self):
        scale = [0, 10]
        return {"scale": scale}
    

    def shear(self):
        shear = [0, 180]
        return {"shear": shear}
    

    def perspective(self):
        perspective = [0, 0.001]
        return {"perspective": perspective}
    

    def flipud(self):
        flipud = [0, 1]
        return {"flipud": flipud}
    

    def fliplr(self):
        fliplr = [0, 1]
        return {"fliplr": fliplr}
    

    def bgr(self):
        bgr = [0, 1]
        return {"bgr": bgr}
    

    def mosaic(self):
        mosaic = [0, 1]
        return {"mosaic": mosaic}
    

    def mixup(self):
        mixup = [0, 1]
        return {"mixup": mixup}
    

    def copy_paste(self):
        copy_paste = [0, 1]
        return {"copy_paste": copy_paste}
    

    def copy_paste_mode(self):
        copy_paste_mode = [
            "flip",
            "mixup",
            "flip"
        ]
        return {"copy_paste_mode": copy_paste_mode}
    

    def auto_augment(self):
        auto_augment = [
            "randaugment",
            "autoaugment",
            "augmix"
        ]
        return {"auto_augment": auto_augment}
    

    def erasing(self):
        erasing = [0, 0.9]
        return {"erasing": erasing}
    

    def crop_fraction(self):
        crop_fraction = [0, 1]
        return {"crop_fraction": crop_fraction}


