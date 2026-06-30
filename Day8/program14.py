import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    
    cv2.putText(img, "OpenCV Project", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow('Watermark', img)
    
    k = cv2.waitKey(1)
    if k == ord('c'):
        cv2.imwrite('watermark_image.jpeg', img)
    elif k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
