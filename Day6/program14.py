import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    flip = cv2.flip(frame, 1)
    
    cv2.imshow('Original frame', frame)
    cv2.imshow('Grayscale frame', gray)
    cv2.imshow('Horizontally flipped frame', flip)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
