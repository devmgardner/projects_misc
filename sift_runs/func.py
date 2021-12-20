#https://www.analyticsvidhya.com/blog/2019/08/3-techniques-extract-features-from-image-data-machine-learning-python/
import pyautogui
import os, sys, time, pandas as pd, numpy as np
import matplotlib.pyplot as plt
#matplotlib inline
from skimage.io import imread, imshow

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
#
test_image = os.path.join(currentdir, 'test_image_1.PNG')
#test_image = open(test_image)
image = imread(test_image, as_gray=True)
imshow(image)
image.shape, image