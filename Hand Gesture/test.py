import cv2 as cv
import numpy as np

img = cv.imread('/home/om/Downloads/Backup/Open_CV_basics/group2.webp')
cv.imshow('original', img)

# convert it in grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Lady', gray)

# Import classifiers
cascade = cv.CascadeClassifier('/home/om/Downloads/Backup/Open_CV_basics/harcascade_face_reg_default.xml')

# Now we can find no of faces found as it returns the coordinates of rectangle for each face found
rect_found = cascade.detectMultiScale(gray, 1.1, 3)

print(f'Number of faces found = {len(rect_found)}')

# We can make rectangle on the face also
for (x, y, w, h) in rect_found:

    print(x)

    drawn = cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 1)
    #drawn = cv.circle(drawn, (x_centre, y_centre),1, (0, 0, 255), 1)
cv.imshow('Drawn', drawn)

cv.waitKey(0)