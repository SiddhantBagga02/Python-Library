import cv2

# Load the image
image = cv2.imread('C:\Users\siddh\Downloads\Images\JollyRogerMac.png')

# Flip the image horizontally
flipped_image = cv2.flip(image, 1)

# Save the flipped image
cv2.imwrite('C:\Users\siddh\Downloads\Images\JollyRogerMac.png', flipped_image)

# Display the original and flipped images
cv2.imshow('Original Image', image)
cv2.imshow('Flipped Image', flipped_image)

# Wait for any key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()