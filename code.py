import cv2

image_path = r"Kaagaz\2.jpg"  
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if img is None:
    print(f"Error: Unable to load image from {image_path}")
else:
    #Resizing 
    img = cv2.resize(img, (800, 600))

    #GaussianBlur
    blurred = cv2.GaussianBlur(img, (5, 5), 0)

    edges = cv2.Canny(blurred, 30, 100)
    #showing
    cv2.imshow("Original Image", img)
    cv2.imshow("Edge Detection", edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
