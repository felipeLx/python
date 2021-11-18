# importing PIL 
from PIL import Image 

import urllib.request
# Downloading dataset
urllib.request.urlretrieve("https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg", "dog.jpg")

# Read image 
img = Image.open('dog.jpg') 
  
# Output Images 
display(img)