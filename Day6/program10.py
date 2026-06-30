import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    negative = cv2.bitwise_not(frame)
    
    cv2.imshow('Negative Effect', negative)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
