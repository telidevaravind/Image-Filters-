import numpy as np
#from scipy.misc import toimage
import cv2
#import math
from matplotlib import pyplot as plt 

imageFileName = input("enter the image name with absolute path:\n ")
image = cv2.imread(imageFileName, 0)
height, width = image.shape
print ('height:\n', height)
print ('width:\n', width)
# print 'channels:\n', channels
m = 3
n = 3
print ('The size of the filter is: %d * %d\n' % (3, 3))
pad = int((n - 1) / 2)
print ('pad:\n', pad)
image_org = cv2.copyMakeBorder(image, pad, pad, pad, pad, cv2.BORDER_CONSTANT)
m_new = m//2
n_new = n//2
ind = range(-m_new, m_new + 1)
sobel_filter = np.asarray(np.meshgrid(ind, ind))
sobel_filter_hor = sobel_filter[1]
sobel_filter_ver = sobel_filter[0]
sobel_filter_hor[:, m_new] = 2*sobel_filter_hor[:, m_new]
sobel_filter_ver[n_new, :] = 2*sobel_filter_ver[n_new, :]

def sobel_filter_horizontal():
    Blur_horizontal = np.zeros((height, width), int)
    for y in np.arange(pad, height - 1):
        for x in np.arange(pad, width - 1):
            mod = image_org[y - pad:y + pad + 1, x - pad:x + pad + 1]
            k = (mod * sobel_filter_hor).sum()
            Blur_horizontal[y - pad, x - pad] = k
    print (Blur_horizontal.shape)
    return None
sobel_filter_horizontal()

def sobel_filter_vertical():
    Blur_vertical = np.zeros((height, width), int)
    for y in np.arange(pad, height - 1):
        for x in np.arange(pad, width - 1):
            mod = image_org[y - pad:y + pad + 1, x - pad:x + pad + 1]
            k = (mod * sobel_filter_ver).sum()
            Blur_vertical[y - pad, x - pad] = k
    print (Blur_vertical.shape)
    return None
sobel_filter_vertical()

def Total_Blur():
    total_blur = np.zeros((height, width), int)
    for y in np.arange(pad, height - 1):
        for x in np.arange(pad, width - 1):
            mod = image_org[y - pad:y + pad + 1, x - pad:x + pad + 1]
            k = (mod * sobel_filter_hor).sum() + (mod * sobel_filter_ver).sum()
            total_blur[y - pad, x - pad] = k
    print (total_blur.shape)
    return plt.imshow(total_blur, cmap = 'gray')
Total_Blur()