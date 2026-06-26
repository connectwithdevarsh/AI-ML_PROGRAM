import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    cv2.imshow("Selfie Camera", frame)
    
    key_press = cv2.waitKey(1) & 0xFF
    
    if key_press == ord("s"):
        cv2.imwrite("my_selfie.jpg", frame)
    elif key_press == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
