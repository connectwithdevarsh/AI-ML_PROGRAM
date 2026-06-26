import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret:
        small_pic = cv2.resize(frame, (250, 250))
        cv2.imwrite("profile_pic.jpg", small_pic)
        print("Profile Picture Saved")
        break

cap.release()
cv2.destroyAllWindows()
