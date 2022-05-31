import numpy as np

from analysis import *
import cv2
import re
analisis = analisiss()
global x, y, list
h = 0
i = 0
j = 1
list = []

def parsing(str):
    str = str.split(' ')
    for i in range(len(str)):
        str[i] = re.sub("[^0-9]", "", str[i])
    return str

def getPoint(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        #print([np.float32(x),np.float32(y)])
        list.append([[x,y]])

path_test = "C:\\fluodata\\track00001\\"
#path =  "E:\\FLUODATA\\test\\set1"
f = open(f'{path_test}test.txt', 'r')
a = f.readline()
#a = a.split(' ')
#for i in range(len(a)):
#    a[i] = re.sub("[^0-9]", "", a[i])
#print(type(a[0]))

#print(np.array(a))
#print(type(np.array(a)))
a = parsing(a)



while True:
    try:
        if i > 9:
            frame = cv2.imread(f"{path_test}000{i}_400.tiff", -1)

        if i <= 9:
            frame = cv2.imread(f"{path_test}0000{i}_400.tiff", -1)

        frame = bytescaling(frame)
        frame = cv2.normalize(frame, dst=None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    except:
        break


    #print((int(a[i]), int(a[i+1])))
    cv2.putText(frame, f"Frame {i+1}", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1,(255, 0, 0), 2)
    cv2.circle(frame, (int(a[h]), int(a[h+1])), 10, (255, 0, 0))
    cv2.imshow("frame", frame)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        i += 1
        h += 2
    #print(i)