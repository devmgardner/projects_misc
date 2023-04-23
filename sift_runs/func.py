#https://www.analyticsvidhya.com/blog/2019/08/3-techniques-extract-features-from-image-data-machine-learning-python/
#https://www.geeksforgeeks.org/how-to-extract-text-from-images-with-python/
#https://stackoverflow.com/questions/27343997/using-pil-python-image-library-to-detect-image-on-screen
#https://pyautogui.readthedocs.io/en/latest/screenshot.html#the-locate-functions
#https://pyautogui.readthedocs.io/en/latest/
import pyautogui
import os, sys, time, pandas as pd, numpy as np
#import matplotlib.pyplot as plt
#from skimage.io import imread, imshow

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
#
test_image1 = os.path.join(currentdir, 'test_image_1.PNG')
button5 = os.path.join(currentdir, 'button5.PNG')
#test_image = open(test_image)
#image = imread(test_image1, as_gray=True)
#imshow(image)
#image.shape, image
location = pyautogui.locateCenterOnScreen(button5, confidence=0.5)
if not location == None:
    print(f'X = {location[0]} // Y = {location[1]}')
    pyautogui.leftClick(button5)
else:
    print(f'Image not found. Ending.')