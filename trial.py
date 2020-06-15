import subprocess
import sys 

sys.path.append(r"c:\users\lenovo\appdata\local\programs\python\python37-32\lib\site-packages/pip3")

import requests
import csv
import pytesseract
from PIL import Image
import pytesseract
from io import BytesIO


response = requests.get("http://www.edwaittimes.ca/Shared/Images/PublicDashboard.png")
png = Image.open(BytesIO(response.content))



png_str = pytesseract.image_to_string(png) 

png_text = open("something.txt", "w+")
png_text.write(png_str)
png_text.close()

png_text = open("something.txt", "r")

text_list = png_text.readlines()

png_text.close()


with open("open.csv", 'a') as f:
    writer = csv.writer(f)
    writer.writerow(text_list)



    






