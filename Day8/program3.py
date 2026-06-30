import cv2

cap = cv2.VideoCapture(0)
is_flipped = False

while True:
    ret, frame = cap.read()
    
    if is_flipped:
        frame = cv2.flip(frame, 1)
        
    cv2.imshow('Webcam', frame)
    
    key = cv2.waitKey(1)
    if key == ord('f'):
        is_flipped = True
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
