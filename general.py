from analysis import *
import cv2

analisis = analisiss()
global x, y, list
i = 0
list = []
def getPoint(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        #print([np.float32(x),np.float32(y)])
        list.append([[x,y]])
path_test = "C:\\fluodata\\track00001\\"
#path =  "E:\\FLUODATA\\test\\set1"
#f = open('C:\\fluodata\\test.txt', 'w')

while True:
    try:
        if i > 9:
            frame = cv2.imread(f"{path_test}000{i}_660.tiff", -1)

        if i <= 9:
            frame = cv2.imread(f"{path_test}0000{i}_660.tiff", -1)

        frame = bytescaling(frame)
        frame = cv2.normalize(frame, dst=None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    except:
        break

    try:
        cv2.putText(frame, "LBM to select point, ESC to go to next img", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.imshow("frame", frame)
        if not cv2.setMouseCallback("frame", getPoint) == None:
            cv2.setMouseCallback("frame", getPoint)
    except:
        continue

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        i += 1
        print(f'Frame {i+1}, Num coord: {len(list)+1}')
        print(list)
        #f.write('Hello \n World')
#    if cv2.waitKey(0) == ord('s'):
#        f.close()
