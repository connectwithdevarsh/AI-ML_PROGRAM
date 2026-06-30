import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    
    small_img = cv2.resize(img, (320, 240))
    
    cv2.imshow('320x240 Feed', small_img)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
