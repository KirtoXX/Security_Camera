import numpy as np
from scipy import misc
from SVM_model import Detection_api
import time
import os
import re


def main():
    model = Detection_api()
    nb,image = model.detectFaces('test_image/004.jpg')
    print(nb)
    misc.imsave('temp/004.jpg',image)

if __name__ == '__main__':
    main()