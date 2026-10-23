import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# Create 4 subplots
fig, ax = plt.subplots(nrows=2, ncols=2)

# assign variables for each subplot
plt1, plt2, plt3, plt4 = ax[0,0], ax[0,1], ax[1,0], ax[1,1]

# Turns of tick markers for graphs
for a in ax:
    for b in a:
        b.axis("off")

#--------------------#
# Color Masking Code #
#--------------------#

# load the test image with OpenCV
img = cv.imread('image/cvTestImage.jpg')
# convert the image into a numpy array
img_array = np.array(img)

# Lower bound for masked color
lower_bound = [0,200,0]
# Upper bound for masked color
upper_bound = [10,255,10]

# Creates a boolean mask for color values in the image array
# If it is within the bounds (the color mask) it is true, otherwise false
# mask for the red values
mask_r = (img_array[:, :, 0] >= lower_bound[0]) & (img_array[:, :, 0] <= upper_bound[0])
# mask for the green values
mask_g = (img_array[:, :, 1] >= lower_bound[1]) & (img_array[:, :, 1] <= upper_bound[1])
# mask for blue values
mask_b = (img_array[:, :, 2] >= lower_bound[2]) & (img_array[:, :, 2] <= upper_bound[2])

# Combine the masks through a bitwise AND operator 
# so only values that pass all checks are included
color_mask = mask_r & mask_g & mask_b

# Create a copy of the image array to apply the mask to
masked_image = np.copy(img_array)

# Invert the mask, so only green is allowed through, 
# and set all other colors to black
masked_image[np.logical_not(color_mask)] = [0,0,0]


# Display Original Image, and set title
plt1.imshow(img_array), plt1.set_title('Original Image')

# Display Masked Image, and set title
plt2.imshow(masked_image), plt2.set_title('Masked Image')

#---------------------------#
# Canny Edge Detection Code #
#---------------------------#

# Load test image in grayscale mode
img_bw = cv.imread('image/cvTestImage.jpg', cv.IMREAD_GRAYSCALE)

# Perform an OpenCV canny edge detection algorithm, and save the result
edges = cv.Canny(img_bw,50,150)

# Display Original B&W Image, and set title
plt3.imshow(img_bw,cmap = 'gray'), plt3.set_title('Original Image (B/W)')
# Display Modified Image, and set title
plt4.imshow(edges,cmap = 'gray'), plt4.set_title('Edge Image')

# Print Message describing the 
# Canny Edge Image in context
print("Edges describe the 'bounds' of the objects in view, \n" \
      "which helps the mechanical arm understand the location of objects, \n"
      "and what orientation and bredth the grabbing apperatus must be in order to grip it")

plt.show()