import cv2

cap = cv2.VideoCapture(0)
counter = 0

# Warm up delay
cv2.waitKey(1000)

while counter < 5:
    ret, frame = cap.read()
    if not ret:
        break
    
    counter = counter + 1
    file_name = "Auto_Evidence_" + str(counter) + ".jpg"
    cv2.imwrite(file_name, frame)
    print("Saved automatically: " + file_name)
    
    cv2.imshow("Automatic Capturing", frame)
    cv2.waitKey(3000)

cap.release()
cv2.destroyAllWindows()
