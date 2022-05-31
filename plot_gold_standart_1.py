import re
import numpy as np
from analysis import *
import cv2
import re
import matplotlib.pyplot as plt
from prettytable import PrettyTable

def getMaxErr(a,b):
    err = []
    for i in range(len(a)):
        err.append(abs(b[i] - a[i]))
    maxerr = np.max(err)
    return maxerr

def getCO(a,b):
    co = []
    for i in range(len(a)):
        co.append(abs(b[i] - a[i]))
    co_num = np.mean(co)
    return co_num

def getCKO(a,b):
    cko = []
    for i in range(len(a)):
        cko.append(abs(b[i]**2 - a[i]**2))
    cko_num = np.mean(cko)
    return cko_num


def getInt(img):
    sum = np.sum(img)
    return sum

def getIROIImg(img,y,x,a):
    roi_img = img[x-int(round(a/2)):x+int(round(a/2)), y-int(round(a/2)):y+int(round(a/2))]
    return roi_img

def parsing(str):
    str = str.split(' ')
    for i in range(len(str)):
        str[i] = re.sub("[^0-9]", "", str[i])
    return str

path_test = "C:\\fluodata\\track00001\\"
#f = open(f'{path_test}test.txt', 'r')
#a = f.readline()
#a = parsing(a)
b = 60
i = 1
j = 0
t = []
Int = []
Int_csrt = []
Int_mil = []
Int_mosse = []
Int_tld = []
Int_median_flow = []


while True:
    try:
        frame_gold_standart = cv2.imread(f"{path_test}convert\\{i}.png", -1)
        frame_gold_standart = bytescaling(frame_gold_standart)
        frame_csrt = cv2.imread(f"{path_test}tracking_base\\CSRT\\{i}.jpg",-1)
        frame_csrt = bytescaling(frame_csrt)
        frame_mil = cv2.imread(f"{path_test}tracking_base\\MIL\\{i}.jpg", -1)
        frame_mil = bytescaling(frame_mil)
        frame_mosse = cv2.imread(f"{path_test}tracking_base\\MOSSE\\{i}.jpg", -1)
        frame_mosse = bytescaling(frame_mosse)
        frame_tld = cv2.imread(f"{path_test}tracking_base\\TLD\\{i}.jpg", -1)
        frame_tld = bytescaling(frame_tld)
        frame_median_flow = cv2.imread(f"{path_test}tracking_base\\MEDIANFLOW\\{i}.jpg", -1)
        frame_median_flow = bytescaling(frame_median_flow)

    except:
        break

    limit = 27
    ret0, mask_gs = cv2.threshold(frame_gold_standart, limit, 1, 0)
    ret1, mask_csrt = cv2.threshold(frame_csrt, limit, 1, 0)
    ret2, mask_mil = cv2.threshold(frame_mil, limit, 1, 0)
    ret3, mask_mosse = cv2.threshold(frame_mosse, limit+2, 1, 0)
    ret4, mask_tld = cv2.threshold(frame_tld, limit, 1, 0)
    ret5, mask_median_flow = cv2.threshold(frame_median_flow, limit, 1, 0)

    frame_gold_standart = mask_gs*frame_gold_standart
    frame_csrt = mask_csrt*frame_csrt
    frame_mil = mask_mil*frame_mil
    frame_mosse_old = frame_mosse
    frame_mosse = mask_mosse*frame_mosse
    frame_mosse = frame_mosse[0:frame_mosse.shape[0], int(frame_mosse.shape[1]/2):frame_mosse.shape[1]]
    frame_tld = mask_tld*frame_tld
    frame_median_flow = mask_median_flow*frame_median_flow


    #cv2.imshow("frame_csrt", frame_csrt)
    #cv2.imshow("frame_mil", frame_mil)
    #cv2.imshow("frame_mosse", frame_mosse)
    #cv2.imshow("1",frame_mosse)
    #cv2.imshow("frame_tld", frame_tld)
    #cv2.imshow("frame_mf", frame_median_flow)
    #cv2.imshow("frame_gold_standart",frame_gold_standart)
    #cv2.waitKey(0)

    Int.append(getInt(frame_gold_standart))
    Int_tld.append(getInt(frame_tld))
    Int_csrt.append(getInt(frame_csrt))
    Int_mil.append(getInt(frame_mil))
    Int_mosse.append(getInt(frame_mosse))
    Int_median_flow.append(getInt(frame_median_flow))
    t.append(i)
    if i == 66:
        i+=2
    else:
        i+=1
    j+=2
for i in range(1,len(Int_csrt)):
    Int[i] = Int[i]/Int[0]
    Int_csrt[i] = Int_csrt[i]/Int_csrt[0]
    Int_tld[i] = Int_tld[i]/Int_tld[0]
    Int_mosse[i] = Int_mosse[i]/Int_mosse[0]
    Int_median_flow[i] = Int_median_flow[i] / Int_median_flow[0]
    Int_mil[i] = Int_mil[i] / Int_mil[0]
Int[0] = 1
Int_mil[0] = 1
Int_tld[0] = 1
Int_mosse[0] = 1
Int_csrt[0] = 1
Int_median_flow[0] = 1
plt.grid(True)
plt.plot(t,Int)
#plt.plot(t,Int_mil)
plt.plot(t,Int_csrt)
plt.plot(t,Int_tld)
plt.plot(t,Int_mosse)
plt.plot(t,Int_median_flow)
#plt.legend(['gold standart', 'MIL', 'CSRT', 'TLD', 'MOSSE', 'Median Flow'])
plt.legend(['gold standart', 'CSRT', 'TLD', 'MOSSE', 'Median Flow'])

# Specify the Column Names while initializing the Table
myTable = PrettyTable(["Tracker name", "СКО", "СО", "MaxError"])

# Add rows
myTable.add_row(["CSRT", str(getCKO(Int,Int_csrt)), str(getMaxErr(Int,Int_csrt))])
myTable.add_row(["TLD", str(getCKO(Int,Int_tld)), str(getMaxErr(Int,Int_tld))])
myTable.add_row(["MOSSE(BEST)", str(getCKO(Int,Int_mosse)),str(getMaxErr(Int,Int_mosse))])
myTable.add_row(["Median Flow", str(getCKO(Int,Int_median_flow)),str(getMaxErr(Int,Int_median_flow))])

print(myTable)

plt.show()
