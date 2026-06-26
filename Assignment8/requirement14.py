import cv2
import os

img_path = "Evidence_Photos/Image1.jpg"

if not os.path.exists("Evidence_Photos"):
    os.makedirs("Evidence_Photos")

img = cv2.imread(img_path)

if img is None:
    print("Please make sure Image1.jpg exists in Evidence_Photos folder.")
else:
    blurred_img = cv2.GaussianBlur(img, (15, 15), 0)
    cv2.imshow("Blurred Image", blurred_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
