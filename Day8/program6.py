import cv2

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
writer = cv2.VideoWriter('record_video.avi', fourcc, 20.0, (640, 480))

while True:
    ret, frame = cap.read()
    
    writer.write(frame)
    cv2.imshow('Recording', frame)
    
    if cv2.waitKey(1) == 27:
        break

cap.release()
writer.release()
cv2.destroyAllWindows()
