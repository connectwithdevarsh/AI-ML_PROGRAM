import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    upside_down = cv2.flip(frame, 0)
    
    cv2.imshow("Upside Down Camera", upside_down)
    
    if cv2.waitKey(1) & 0xFF == ord("e"):
        break

cap.release()
cv2.destroyAllWindows()
