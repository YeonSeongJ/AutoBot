import cv2
import numpy as np
import LineManage

from os import listdir
from os.path import isfile, join

mypath = 'images/curve'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
images = np.empty(len(onlyfiles), dtype=object)
for n in range(0, len(onlyfiles)):
    images[n] = cv2.imread(join(mypath, onlyfiles[n]))

HEIGHT, WIDTH = images[0].shape[:2]

print(HEIGHT, WIDTH)

for i in images:
    LineManage.GetLine(i, HEIGHT, WIDTH)

    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

