import numpy as np
from scipy import misc
from SVM_model import Detection_api
import time
import os
import re

def get_list(time):
    all_image_list = os.listdir('Persion_image')
    result = []
    for path in all_image_list:
        try:
            _,n = re.search(time,path).span()
            if n == 15:
                result.append(path)
        except:
            None
    return result

def main():
    l1 = get_list('2017-09-03-1125')
    print(l1)

if __name__ == '__main__':
    main()