
#  open cv


import cv2

# # Load an image
image = cv2.imread("D:\Windows files\Pictures\O'zim.jpg")

# # Display the image
# cv2.imshow("Image", image)
# cv2.waitKey(0)  # Wait for a key press
# cv2.destroyAllWindows()



# Draw a rectangle
cv2.rectangle(image, (50, 50), (200, 200), (0, 255, 0), 3)

# Add text
cv2.putText(image, "Hello, Traffic!", (50, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

cv2.imshow("Shapes and Text", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


blurred_image = cv2.GaussianBlur(image, (15, 15), 0)
cv2.imshow("Blurred Image", blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

