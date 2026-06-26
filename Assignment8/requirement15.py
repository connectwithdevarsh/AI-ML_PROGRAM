import cv2
import os

input_folder = "Evidence_Photos"
out_resized = "Resized_Evidence"
out_gray = "Gray_Evidence"
out_blurred = "Blurred_Evidence"

os.makedirs(out_resized, exist_ok=True)
os.makedirs(out_gray, exist_ok=True)
os.makedirs(out_blurred, exist_ok=True)

if not os.path.exists(input_folder):
    os.makedirs(input_folder)

files = os.listdir(input_folder)

for f in files:
    if f.endswith(".jpg") or f.endswith(".jpeg") or f.endswith(".png"):
        path = os.path.join(input_folder, f)
        img = cv2.imread(path)
        
        if img is not None:
            # 1. Resize Image
            resized = cv2.resize(img, (200, 200))
            cv2.imwrite(os.path.join(out_resized, f), resized)
            
            # 2. Convert to Grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(os.path.join(out_gray, f), gray)
            
            # 3. Apply Blur
            blurred = cv2.GaussianBlur(img, (15, 15), 0)
            cv2.imwrite(os.path.join(out_blurred, f), blurred)

print("Batch processing completed successfully.")
