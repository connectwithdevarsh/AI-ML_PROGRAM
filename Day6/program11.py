import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    resized = cv2.resize(frame, (500, 500))
    
    cv2.imshow('Resized Feed', resized)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
