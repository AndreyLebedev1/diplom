#Tracking imges by 5 different trackers
#BOOSTING, KCF, GOTURN dont working

import cv2
import sys
import time
(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

if __name__ == '__main__':

    # Set up tracker.
    # Instead of MIL, you can also use

    tracker_types = ['CSRT', 'MEDIANFLOW', 'MIL', 'MOSSE', 'TLD']
    tracker_type = tracker_types[1]

    if int(minor_ver) < 3:
        tracker = cv2.Tracker_create(tracker_type)
    else:
        if tracker_type == 'BOOSTING':
            tracker = cv2.legacy.TrackerBoosting_create()
        if tracker_type == 'MIL':
            tracker = cv2.legacy.TrackerMIL_create()
        if tracker_type == 'KCF':
            tracker = cv2.legacy.TrackerKCF_create()
        if tracker_type == 'TLD':
            tracker = cv2.legacy.TrackerTLD_create()
        if tracker_type == 'MEDIANFLOW':
            tracker = cv2.legacy.TrackerMedianFlow_create()
        if tracker_type == 'GOTURN':
            tracker = cv2.TrackerGOTURN_create()
        if tracker_type == 'MOSSE':
            tracker = cv2.legacy.TrackerMOSSE_create()
        if tracker_type == "CSRT":
            tracker = cv2.legacy.TrackerCSRT_create()


    # Read video
    #video = cv2.VideoCapture(0)

    # Exit if video not opened.

    # Read first frame.

    path_test = "C:\\fluodata\\track00002\\"



    frame = cv2.imread(f"{path_test}convert\\11_660.jpg", -1)

    # Define an initial bounding box

    bbox = (287, 23, 86, 320)


    # Uncomment the line below to select a different bounding box

    bbox = cv2.selectROI(frame, False)
    print(bbox)

    # Initialize tracker with first frame and bounding box
    ok = tracker.init(frame, bbox)
    i = 12
    while True:
        # Read a new frame
        try:
            frame = cv2.imread(f"{path_test}convert\\{i}_660.jpg", -1)
        except:
            break

        # Start timer
        timer = cv2.getTickCount()

        # Update tracker
        ok, bbox = tracker.update(frame)

        # Calculate Frames per second (FPS)
        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
        print(bbox)
        img4savin = frame[int(bbox[1]):int(bbox[1])+int(bbox[3]), int(bbox[0]):int(bbox[0])+int(bbox[2])]

        #cv2.imshow("1",img4savin)
        #cv2.waitKey(0)

        cv2.imwrite(f"{path_test}tracking_base\\{tracker_type}\\{i}.jpg", img4savin)
        # Draw bounding box
        if ok:
            # Tracking success
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
        else:
            # Tracking failure
            cv2.putText(frame, "Tracking failure detected", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

        # Display tracker type on frame
        cv2.putText(frame, tracker_type + " Tracker", (100, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)

        # Display FPS on frame
        cv2.putText(frame, "FPS : " + str(int(fps)), (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)

        # Display result
        cv2.imshow("Tracking", frame)
        #cv2.imwrite(f"{path_test}tracking_base\\FULL\\full{i}.jpg", frame)
        i += 1
        time.sleep(0.5)

        # Exit if ESC pressed
        k = cv2.waitKey(1) & 0xff
        if k == 27:
            break
