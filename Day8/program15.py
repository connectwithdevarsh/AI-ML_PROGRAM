import cv2
import random

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    r = random.randint(0, 255)
    
    cv2.putText(frame, "Watermark", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (b, g, r), 3)
    cv2.imshow('Random Color Watermark', frame)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
