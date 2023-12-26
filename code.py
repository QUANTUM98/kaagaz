import cv2
import numpy as np

image = cv2.imread(r'D:\Kaagaz\Kaagaz\original_image.jpg')
image = cv2.resize(image, None, fx=0.9, fy=0.9)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
contours, hierarchy = cv2.findContours(binary, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
image_copy = image.copy()
cv2.drawContours(image_copy, contours, -1, (0, 255, 0), thickness=2, lineType=cv2.LINE_AA)

mask = np.zeros_like(gray)
cv2.drawContours(mask, contours, -1, (255), thickness=cv2.FILLED)

x, y, w, h = cv2.boundingRect(mask)

cropped_image = image[y:y+h, x:x+w]
cv2.imshow('Grayscale Image', gray)
cv2.imshow('Drawn Contours', image_copy)
cv2.imshow('Binary Image', binary)
cv2.imshow('Cropped Image', cropped_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
