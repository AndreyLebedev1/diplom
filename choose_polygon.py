import cv2

path_test = "C:\\fluodata\\track00001\\"

img = cv2.imread(f"{path_test}convert\\0_660.jpg",-1)

global arr
arr = []

def draw_circle(event, x, y, flags, param):
    if (event == cv2.EVENT_MOUSEMOVE) and (flags == cv2.EVENT_FLAG_LBUTTON):
        cv2.circle(img, (x, y), 2, (255, 255, 255), -1)
        arr.append((x,y))
        print(x, y)

cv2.namedWindow(winname="Title of Popup Window")
cv2.setMouseCallback("Title of Popup Window", draw_circle)

while True:
    cv2.imshow("Title of Popup Window", img)

    if cv2.waitKey(10) & 0xFF == 27:
        break
cv2.destroyAllWindows()