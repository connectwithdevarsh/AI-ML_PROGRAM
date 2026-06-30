import cv2

cap = cv2.VideoCapture(0)
count = 0

while True:
    ret, frame = cap.read()
    count = count + 1
    
    text = "Frame: " + str(count)
    cv2.putText(frame, text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    
    cv2.imshow('Frame Count', frame)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
