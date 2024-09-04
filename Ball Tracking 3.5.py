import cv2 as cv
import numpy as np

lower_color = np.array([0, 135, 135])
upper_color = np.array([6, 300, 300])

cap = cv.VideoCapture(0)

cap.set(cv.CAP_PROP_FRAME_HEIGHT, 320)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 240)

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
            cv.circle(frame, (x + w//2 + 7, y + h//2 + 7), round((h + w) / 2), (0, 255, 0), 5)
            cv.rectangle(frame, (x + w//2 + 7, y + h//2 + 7), (2000, 2000), (0, 255, 0), 2)
            cv.rectangle(frame, (x + w//2 + 7, y + h//2 + 7), (-10, -10), (0, 255, 0), 2)

            cv.putText(frame, 'Red Ball', (x + 30 + round((h + w) / 2), y - round((h + w) / 2) + 15), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv.LINE_AA)
            cv.putText(frame, "", (x, y + h + 20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv.LINE_AA)


    cv.imshow('Tracking', frame)

    if cv.waitKey(1) & 0xFF == ord('1'):
        break
    
cap.release()
cv.destroyAllWindows()
