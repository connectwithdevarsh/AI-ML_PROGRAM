import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    cv2.imshow("Webcam Live", frame)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord("c"):
        marked_frame = frame.copy()
        cv2.putText(
            marked_frame,
            "Security Evidence",
            (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.0,
            (0, 0, 255),
            2,
        )
        cv2.imwrite("Evidence.jpeg", marked_frame)
    elif key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
