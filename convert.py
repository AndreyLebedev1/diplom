import numpy as np
from analysis import *
import cv2
import re
import matplotlib.pyplot as plt
def getInt(img,x,y,a):
    aver = 0
    roi_img = img[x-int(round(a/2)):x+int(round(a/2)), y-int(round(a/2)):y+int(round(a/2))]
    sum = np.sum(roi_img)
    return sum/roi_img.size

def getIROIImg(img,y,x,a):
    roi_img = img[x-int(round(a/2)):x+int(round(a/2)), y-int(round(a/2)):y+int(round(a/2))]
    return roi_img

def parsing(str):
    str = str.split(' ')
    for i in range(len(str)):
        str[i] = re.sub("[^0-9]", "", str[i])
    return str

path_input = "C:\\fluodata\\track00002\\"
path_output = "C:\\fluodata\\track00002\\convert\\"

i = 0
len = '660'

while True:
    try:
        if i > 9:
            frame = cv2.imread(f"{path_input}000{i}_{len}.tiff", -1)

        if i <= 9:
            frame = cv2.imread(f"{path_input}0000{i}_{len}.tiff", -1)

        frame = bytescaling(frame)
        #frame = cv2.normalize(frame, dst=None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
        cv2.imwrite(f"{path_output}{i}_{len}.jpg", frame)
        #cv2.imshow("reader", frame)
        #cv2.waitKey(0)
        i+=1
    except:
        break