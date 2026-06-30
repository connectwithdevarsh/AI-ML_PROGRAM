import cv2
from datetime import datetime

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    dt = str(datetime.now())
    cv2.putText(frame, dt, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
    
    cv2.imshow('Date Time', frame)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
