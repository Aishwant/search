# Pytesseract Installation: python -m pip install pytesseract
# PIL Installation: python -m pip install Pillow 
import pytesseract
from PIL import Image

imageOut=Image.open("test1.jpg")
text=pytesseract.image_to_string(imageOut)
print (text)