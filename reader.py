from analysis import *
import cv2

path_test = "C:\\fluodata\\track00001\\"
i = 22

frame = cv2.imread(f"{path_test}convert\\0.png",-1)

cv2.imshow("",frame)
cv2.waitKey(0)

if i > 9:
    frame = cv2.imread(f"{path_test}000{i}_400.tiff", -1)

if i <= 9:
    frame = cv2.imread(f"{path_test}0000{i}_660.tiff", -1)

frame = bytescaling(frame)
frame = cv2.normalize(frame, dst=None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
cv2.imshow("reader", frame)
cv2.waitKey(0)