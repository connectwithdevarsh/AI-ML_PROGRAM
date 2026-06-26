import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    cv2.imshow("Command Console Feed", frame)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord("c"):
        print("Recording Start")
    elif key == ord("s"):
        print("Recording Stop")
    elif key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
