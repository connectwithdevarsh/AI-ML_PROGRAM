import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    cv2.imshow('Capture Image', img)
    
    k = cv2.waitKey(1)
    if k == ord('c'):
        cv2.imwrite('capture.jpeg', img)
        print("Image captured!")
    elif k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
