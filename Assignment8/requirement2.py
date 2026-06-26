import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    resized_feed = cv2.resize(frame, (400, 600))
    
    cv2.imshow("Monitor Feed", resized_feed)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
