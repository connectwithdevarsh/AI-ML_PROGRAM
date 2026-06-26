import cv2
import time

cap = cv2.VideoCapture(0)

w = int(cap.get(3))
h = int(cap.get(4))

fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("Patrol_Video.avi", fourcc, 20.0, (w, h))

start_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    out.write(frame)
    cv2.imshow("Automatic Patrol Recording", frame)
    
    cv2.waitKey(1)
    
    elapsed = time.time() - start_time
    if elapsed >= 15.0:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
