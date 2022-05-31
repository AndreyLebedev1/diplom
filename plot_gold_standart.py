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

path_test = "C:\\fluodata\\track00002\\"
#f = open(f'{path_test}test.txt', 'r')
#a = f.readline()
#a = parsing(a)
b = 60
i = 12
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
        frame_gold_standart = cv2.imread(f"{path_test}convert\\{i}_660.png", -1)
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
    mask = mask_gs*255
    #cv2.imshow("1",mask)
    cv2.imwrite(f"{path_test}masks\\{i}mask.jpg", mask)
    #cv2.waitKey(0)
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

t[6]+=50
t[7]+=100
for i in range(8,len(t)):
    t[i]+=100

t[19]+=50
t[20]+=100
for i in range(21,len(t)):
    t[i]+=100

t[27]+=100
for i in range(28,len(t)):
    t[i]+=100

t[36]+=100
for i in range(37,len(t)):
    t[i]+=100





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
plt.plot(t,Int,'.-')
#plt.plot(t,Int_mil)
d_csrt = []
d_tld = []
d_mf = []
d_ms = []
for i in range(len(Int)):
    d_csrt.append(Int_csrt[i] - Int[i])
    d_tld.append(Int_tld[i] - Int[i])
    d_mf.append(Int_median_flow[i] - Int[i])
    d_ms.append(Int_mosse[i] - Int[i])
#plt.plot(t,Int_csrt)
#plt.plot(t,Int_tld)
#plt.plot(t,Int_mosse)
#plt.plot(t,Int_median_flow)

#plt.plot(t,d_csrt)
#plt.plot(t,d_tld)
#plt.plot(t,d_ms)
#plt.plot(t,d_mf)




#plt.legend(['gold standart', 'MIL', 'CSRT', 'TLD', 'MOSSE', 'Median Flow'])
plt.legend(['gold standart', 'CSRT', 'TLD', 'MOSSE', 'Median Flow'])
#plt.legend(['CSRT', 'TLD', 'MOSSE', 'Median Flow'])

# Specify the Column Names while initializing the Table
myTable = PrettyTable(["Tracker name", "СКО", "MaxError"])

# Add rows
myTable.add_row(["CSRT", str(getCKO(Int,Int_csrt)), str(getMaxErr(Int,Int_csrt))])
myTable.add_row(["TLD", str(getCKO(Int,Int_tld)), str(getMaxErr(Int,Int_tld))])
myTable.add_row(["MOSSE", str(getCKO(Int,Int_mosse)),str(getMaxErr(Int,Int_mosse))])
myTable.add_row(["Median Flow", str(getCKO(Int,Int_median_flow)),str(getMaxErr(Int,Int_median_flow))])


print(myTable)

#plt.xlabel('Number of frame')
plt.xlabel('Time[sec]')
plt.ylabel('Normalize intencity')
#plt.ylabel('Deviation of normalize intencity')

plt.show()
