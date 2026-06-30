import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    flip_v = cv2.flip(frame, 0)
    
    cv2.imshow('Flipped Vertically', flip_v)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
