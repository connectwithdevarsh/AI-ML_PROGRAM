import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret:
        small_frame = cv2.resize(frame, (250, 250))
        cv2.imwrite("customer_record.jpg", small_frame)
        print("Customer Record Saved")
        break

cap.release()
cv2.destroyAllWindows()
