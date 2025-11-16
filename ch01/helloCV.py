import sys
from pathlib import Path

import cv2


print('Hello, OpenCV', cv2.__version__)

root_path = Path(__file__).resolve().parent

img = cv2.imread(str(root_path / 'cat.bmp'))

if img is None:
    print('Image load failed!')
    sys.exit()
    
cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
cv2.imshow('image', img)
cv2.waitKey()

cv2.destroyAllWindows()