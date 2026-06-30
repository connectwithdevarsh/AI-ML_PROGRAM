import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    
    big_img = cv2.resize(img, (1280, 720))
    
    cv2.imshow('HD Feed', big_img)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
