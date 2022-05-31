from analysis import *
import cv2

path_test = "C:\\fluodata\\track00001\\"
i = 1
if i > 9:
    frame = cv2.imread(f"{path_test}000{i}_400.tiff", -1)

if i <= 9:
    frame = cv2.imread(f"{path_test}0000{i}_400.tiff", -1)

frame = bytescaling(frame)
frame = cv2.normalize(frame, dst=None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
print(frame.shape)
cv2.imshow("reader", frame[350:450, 550:650])
cv2.waitKey(0)