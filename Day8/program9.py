import cv2
import time

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('myvideo.avi', fourcc, 20.0, (640, 480))

start = time.time()

while True:
    ret, frame = cap.read()
    
    out.write(frame)
    cv2.imshow('Timed Recording', frame)
    
    elapsed = time.time() - start
    if elapsed > 10:
        break
        
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
