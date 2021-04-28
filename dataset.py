import numpy as np
import matplotlib.pyplot as plt
import skimage
import sys

from skimage import filters
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.data import camera
from skimage.util import compare_images
from skimage.transform import resize

np.set_printoptions(threshold=sys.maxsize)

def dataset():
    image = imread("/home/christian/Área de Trabalho/alfabeto.jpeg")
    fig, axs = plt.subplots(ncols=24, sharex=True, sharey=True, figsize=(8, 4))
    alb = []
    for i in range(6):
        for j in range(4):
            alb.append(resize(image[(i*200):((i+1)*200), (j*200):((j+1)*200)], (8, 8)))

    print(len(axs))

    for z in range(len(alb)):
        axs[z].imshow(alb[z])
    
    
    print(image[0:200, 0:200].shape)

    
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    dataset()