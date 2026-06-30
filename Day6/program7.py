import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    flip_h = cv2.flip(frame, 1)
    
    cv2.imshow('Flipped Horizontally', flip_h)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
