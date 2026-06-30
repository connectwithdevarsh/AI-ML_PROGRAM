import cv2
import time

cap = cv2.VideoCapture(0)
count = 0

while True:
    ret, frame = cap.read()
    cv2.imshow('Auto Capture', frame)
    
    if count < 3:
        filename = "photo_" + str(count) + ".jpg"
        cv2.imwrite(filename, frame)
        count = count + 1
        cv2.waitKey(2000)
        
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
