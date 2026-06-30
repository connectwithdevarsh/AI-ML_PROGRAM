import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('Gray Capture', gray)
    
    k = cv2.waitKey(1)
    if k == ord('c'):
        cv2.imwrite('gray_photo.jpeg', gray)
    elif k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
