import os

folder = "Evidence_Photos"

if not os.path.exists(folder):
    os.makedirs(folder)

files = os.listdir(folder)
for f in files:
    print(f)
