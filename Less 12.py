import cv2
from PIL import Image
image_path = 'cat.jpg'
cat_face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
image = cv2.imread(image_path)
cat_face = cat_face_cascade.detectMultiScale(image)
cat = Image.open(image_path)
mustache = Image.open('mustache.png')
cat = cat.convert("RGBA")
mustache = mustache.convert("RGBA")
for(x, y, w, h) in cat_face:
    mustache = mustache.resize((w, int(h/3)))
    cat.paste(mustache, (x, int(y+h/1.5)), mustache)
    cat.save("cat_with_mustache.png")
    cat_with_mustache = cv2.imread("cat_with_mustache.png")
    cv2.imshow("Cat_with_mustache", cat_with_mustache)
    cv2.waitKey()