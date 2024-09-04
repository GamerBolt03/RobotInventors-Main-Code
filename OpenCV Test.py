import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:

    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        break

    cv2.imshow('Output', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()