import imageio.v3 as iio  # Import the imageio library

# List of three image file names
filenames = ['image.jpg', 'image 2.jpg', 'image 3.jpg']  

# Empty list to store image data
images = []

# Read each image and append to the images list
for filename in filenames:
    images.append(iio.imread(filename))

# Create a GIF from the images
iio.imwrite('image.gif', images, duration=500, loop=0)
