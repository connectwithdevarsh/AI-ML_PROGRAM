import cv2
import time

cap = cv2.VideoCapture(0)
start = time.time()

while True:
    ret, frame = cap.read()
    
    elapsed = int(time.time() - start)
    text = "Elapsed Time: " + str(elapsed) + " seconds"
    
    cv2.putText(frame, text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
    cv2.imshow('Timer', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
