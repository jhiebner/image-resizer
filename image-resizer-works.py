from PIL import Image, ImageFilter
import os

directory = '/Users/jordanhiebner/Documents/Python/Test Logos/'
output = '/Users/jordanhiebner/Documents/Python/Resized Logos/'

for filename in os.listdir(directory):
    img = Image.open(directory + filename)
    img = img.resize((115,115))
    img.save(output + filename) 

