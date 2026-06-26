import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    cv2.imshow("ATM Camera View", frame)
    
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord("s"):
        cv2.imwrite("atm_snapshot.jpg", frame)
    elif key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
