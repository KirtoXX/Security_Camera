import numpy as np
from scipy import misc
from svm_model import Detection_api
import time

def main():
    img_path = 'test_image/001.jpg'
    model = Detection_api()
    n = model.detectFaces(img_path)
    print(n)
    a = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    print(a)

if __name__ == '__main__':
    main()