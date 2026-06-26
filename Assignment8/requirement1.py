import cv2

cap = cv2.VideoCapture(0)
mode = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord("m"):
        mode = 1
    elif key == ord("q"):
        break
    
    if mode == 1:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        display_frame = cv2.flip(gray, 1)
    else:
        display_frame = frame
    
    cv2.imshow("Live Surveillance", display_frame)

cap.release()
cv2.destroyAllWindows()
