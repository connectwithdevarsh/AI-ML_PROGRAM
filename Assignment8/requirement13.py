import cv2
import os

img_path = "Evidence_Photos/Image1.jpg"

if not os.path.exists("Evidence_Photos"):
    os.makedirs("Evidence_Photos")

img = cv2.imread(img_path)

if img is None:
    print("Please make sure Image1.jpg exists in Evidence_Photos folder.")
else:
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale Image", gray_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
