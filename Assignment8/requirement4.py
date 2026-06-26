import cv2

officer_name = input("Enter Officer Name: ")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    cv2.putText(
        frame, officer_name, (200, 300), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2
    )
    cv2.imshow("Officer Monitor", frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
