import cv2

name = input("Enter your name: ")
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    cv2.putText(frame, name, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)
    cv2.imshow('Name Display', frame)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
