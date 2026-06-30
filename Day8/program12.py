import cv2

video = cv2.VideoCapture(0)

while True:
    ret, img = video.read()
    
    cv2.putText(img, "Live Camera", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.imshow('Live Text', img)
    
    if cv2.waitKey(1) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
