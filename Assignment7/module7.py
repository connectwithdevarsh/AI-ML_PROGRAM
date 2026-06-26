import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    mirrored = cv2.flip(frame, 1)
    
    cv2.imshow("Original ATM Feed", frame)
    cv2.imshow("Mirror ATM Feed", mirrored)
    
    if cv2.waitKey(1) & 0xFF == ord("x"):
        break

cap.release()
cv2.destroyAllWindows()
