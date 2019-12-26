import cv2
import numpy as np

def process(image):
	# Detection process:
	# 1. Convert image to greyscale
	# 2. Cut off bottom part of image (traffic lights are usually in the top 60% of image)
	# 3. Apply top-hat morphology to isolate bright regions
	# 4. Choose bright points from morphology as markers for watershed algorithm
	# 5. Apply watershed algorithm to cull background objects
	# 6. Exact windows around final bright spots from original image and apply image classifier evaluation
	width, height = image.size
	gImage = cv2.cvtColor(image.crop(0,0,width*3/5,height*3/5), cv2.COLOR_BGR2GRAY)
	
