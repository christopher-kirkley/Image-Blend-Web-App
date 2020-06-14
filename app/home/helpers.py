import os
import cv2 as cv
import numpy as np


def image_weight(image_list):
    percent = 1/len(image_list)
    return percent

def create_file_list(directory):
    file_list = os.listdir(directory)
    image_list = [f'{directory}/{file_}' for file_ in file_list if file_.endswith(('jpg','jpeg', 'png',))]
    return image_list

def resize(img, size):
    sh, sw = size
    h, w, *_ = img.shape
    aspect = w/h

    # interpolation method
    if h > sh or w > sw: # shrinking image
        interp = cv.INTER_AREA
    else: # stretching image
        interp = cv.INTER_CUBIC

    if aspect < 1:
        # Vertical image
        new_w = int(round(sw*aspect))
        new_h = sh
        padding = (sw - new_w)/2
        pad_left, pad_right = int(np.ceil(padding)), int(np.floor(padding))
        pad_top, pad_bot = 0, 0
    elif aspect > 1:
        # Horizontal image
        new_w = sw
        new_h = int(round(sh/aspect))
        padding = (sh - new_h)/2
        pad_top, pad_bot = int(np.ceil(padding)), int(np.floor(padding))
        pad_left, pad_right = 0, 0
    else:
        # Square image
        new_w = sw
        new_h = sh
        pad_top, pad_bot, pad_left, pad_right = 0, 0, 0, 0
    
    if len(img.shape) == 2:
         img = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
    elif img.shape[2] == 4:
        img = img[:,:,:3]

    img = cv.resize(img, (new_w, new_h), interpolation=interp)
    img = cv.copyMakeBorder(img, pad_top, pad_bot, pad_left, pad_right, borderType=cv.BORDER_CONSTANT, value=(255, 255, 255))
    print(img.shape)
    return img

