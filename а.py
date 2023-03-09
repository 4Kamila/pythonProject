import time
import cv2
from PIL import Image
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap_with = 500
cap_height = 500

while True:
    ret, img = cap.read()


    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 5)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

        arr = {y: y + h, x: x + w}
        print('---------------------')
        print('---------------------')
        print(arr)

        print('X: %d    |   Y: %d' % (x, y))
        print('x+w: %d    |   y+h: %d' % (x + w, y + h))

        # Center of roi (Rectangle)
        xx = int(x + (x + h)) / 2
        yy = int(y + (y + w)) / 2
        print('xx: %d    |   yy: %d' % (xx, yy))
        center = (xx, yy)

    cv2.imshow('img', img)

    key = cv2.waitKey(20)
    if key == 27:
        print('Stop streaming')
        break

cap.release()
cv2.destroyAllWindows()