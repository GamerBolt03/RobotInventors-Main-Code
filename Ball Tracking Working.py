import cv2 as cv
import numpy as np

#Cap - Capture
#cv - OpenCV

lower_color = np.array([0, 100, 100])
upper_color = np.array([10, 255, 255])

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    mask = cv.inRange(hsv, lower_color, upper_color)

    result = cv.bitwise_and(frame, frame, mask=mask)

    contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv.contourArea(contour) > 500:
            x, y, w, h = cv.boundingRect(contour)
            cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv.circle(frame, (x + w//2, y + h//2), 10, (255, 0, 0), -1) 

    cv.imshow('Tracking', frame)

    if cv.waitKey(1) & 0xFF == ord('1'):
        break
    
cap.release()
cv.destroyAllWindows()
