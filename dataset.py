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

def dataset_for_training(alb):
    data = []
    data = alb
    for t in range(len(alb)):
            for z in range(8):
                for i in range(8):
                    if data[t][z][i] == 0:
                        data[t][z][i] = 1
                        pass
                    else:
                        data[t][z][i] = -1
                        pass

    filename = "image_matrix.txt"
    with open(filename, 'w') as file_object:
        file_object.write(str(data[12]))

    return data

def image_preprocessor():
    
    image = imread("/home/christian/Área de Trabalho/8_bit_alphabet.png", as_gray=True)
    fig, axs = plt.subplots(ncols=2, sharex=True, sharey=True) #, figsize=(8, 4)
    alb = []
    
    for i in range(3):
        for j in range(8):
            alb.append(resize(image[(i*100):((i+1)*100), (j*100):((j+1)*100)], (8, 8)))

    #print(len(axs))

    for t in range(len(alb)):
            for z in range(8):
                for i in range(8):
                    if alb[t][z][i] > 0.5:
                        alb[t][z][i] = 1
                        pass
                    if alb[t][z][i] <= 0.5:
                        alb[t][z][i] = 0
                        pass


    #for z in range(len(alb)):
    #    axs[z].imshow(alb[z])

    axs[0].imshow(alb[2])
    #axs[1].imshow(alb[16])
    data_for_training = dataset_for_training(alb)

    desired_response = []
    for d in range(len(alb)):
        if d == 2:
            desired_response.append(1)
        else:
            desired_response.append(-1)
    
    plt.tight_layout()
    #plt.show()

    return data_for_training, desired_response


if __name__ == '__main__':
    image_preprocessor()