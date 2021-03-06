import cv2
from scipy import misc
from imutils.object_detection import non_max_suppression
from imutils import paths
import imutils
import numpy as np

#------------------
# 导入非极大现行抑制
#
#
#-----------------

class Detection_api:
    def __init__(self):
        self.hog = cv2.HOGDescriptor()
        self.hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    def detectFaces(self,image_path):  #图片路径
        nb = 0
        image = misc.imread(image_path,mode='RGB')

        #-----preprocessing-------
        image = imutils.resize(image, width=min(400, image.shape[1]))

        #------detection-----------
        (rects, weights) = self.hog.detectMultiScale(image, winStride=(4, 4),padding = (8, 8), scale = 1.05)

        rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
        pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)
        nb = len(pick)

        #-----------rectangle image-------------
        if nb!=0:
            for (xA, yA, xB, yB) in pick:
                cv2.rectangle(image, (xA, yA), (xB, yB), (0,0, 0), 2)
        else:
            None
        #------------finish---------------------
        return nb,image