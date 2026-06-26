import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    flipped = cv2.flip(frame, 1)
    
    cv2.imshow("Original Camera Feed", frame)
    cv2.imshow("Mirror Camera Feed", flipped)
    
    if cv2.waitKey(1) & 0xFF == ord("x"):
        break

cap.release()
cv2.destroyAllWindows()
