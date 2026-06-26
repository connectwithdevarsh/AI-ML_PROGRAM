import cv2
import os

folder_name = input("Enter Folder Name: ")

if not os.path.exists(folder_name):
    os.makedirs(folder_name)

cap = cv2.VideoCapture(0)
counter = 0

print("Press 'c' to capture image")

while counter < 5:
    ret, frame = cap.read()
    if not ret:
        break
    
    cv2.imshow("Capture Feed", frame)
    
    key_press = cv2.waitKey(1) & 0xFF
    if key_press == ord("c"):
        counter = counter + 1
        img_path = os.path.join(folder_name, "Image" + str(counter) + ".jpg")
        cv2.imwrite(img_path, frame)
        print("Saved: " + img_path)

cap.release()
cv2.destroyAllWindows()
