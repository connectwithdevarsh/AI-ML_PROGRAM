import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    cv2.imshow('Live Feed', frame)
    
    key = cv2.waitKey(1)
    if key & 0xFF == ord('x'):
        break

cap.release()
cv2.destroyAllWindows()
