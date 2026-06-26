import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    mirrored = cv2.flip(frame, 1)
    resized = cv2.resize(frame, (300, 300))
    
    cv2.imshow("Original Feed", frame)
    cv2.imshow("Grayscale Feed", gray)
    cv2.imshow("Mirror Feed", mirrored)
    cv2.imshow("Resized Feed", resized)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
