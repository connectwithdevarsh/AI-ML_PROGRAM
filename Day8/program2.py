import cv2

cap = cv2.VideoCapture(0)
is_gray = False

while True:
    ret, img = cap.read()
    
    if is_gray:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
    cv2.imshow('Video', img)
    
    k = cv2.waitKey(1)
    if k == ord('g'):
        is_gray = True
    elif k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
