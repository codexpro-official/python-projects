import cv2
import numpy as np
from pathlib import Path


dirpath = Path(input("enter directory url: "))
pathList = list()
if dirpath.exists():
    for child in dirpath.iterdir():
        if child.suffix.lower() in [".jpg", ".jpeg", ".png"]:
            pathList.append(child)


i = 0
while True:
    if i>=len(pathList):
        i = len(pathList)-1
    elif i<0:
        i = 0
    
    img = cv2.imread(str(pathList[i]))
    if img is None:
        print("Image couldn't load!")

    img = cv2.resize(img, (800,700))

    cv2.imshow(f"deepdot -slider", img)

    key = cv2.waitKey(0) & 0xFF

    if key == 83:
        i += 1
    elif key == 81:
        i -= 1
    elif key == ord('q'):
        break

cv2.destroyAllWindows()


