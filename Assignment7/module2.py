import cv2

camera = cv2.VideoCapture(0)

while True:
    read_ok, frame = camera.read()
    if not read_ok:
        break
    
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow("Grayscale Feed", gray_img)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
