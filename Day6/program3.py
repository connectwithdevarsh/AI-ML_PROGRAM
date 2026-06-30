import cv2
from datetime import datetime

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cv2.putText(img, time_now, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    
    cv2.imshow('Webcam with Date', img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
