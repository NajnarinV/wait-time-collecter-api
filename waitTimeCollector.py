import subprocess
import sys 

sys.path.append(r"c:\users\lenovo\appdata\local\programs\python\python37-32\lib\site-packages/pip3")

import requests
import csv
import pytesseract
from PIL import Image
import pytesseract
from io import BytesIO


def adjusted_wait_times():
    response = requests.get("http://www.edwaittimes.ca/Shared/Images/PublicDashboard.png")
    png = Image.open(BytesIO(response.content))

    prepPNG = png.crop((1200,50,1600,1650))

    png_text = pytesseract.image_to_string(prepPNG)

    f = open("something.txt", "w")
    f.write(png_text)
    f.close

    f = open("something.txt", "r")
    png_list = f.readlines()
    f.close()

    while len(png_list)<8:
        png_list.append(" ")
    
    return png_list

def combine_lists():

    hospitalNames = ["Vancouver General Hospital", "St. Pauls Hospital", "Richmond Hospital", "Lions Gate Hospital", "Mount Saint Joseph Hospital", "UBC Hospital","City Centre Urgent Primary Care Centre", "North Vancouver Urgent and Primary Care Centre"]

    combine = dict(zip(hospitalNames, adjusted_wait_times()))

    for key in combine:
        if (combine[key][-1] == "\n"):
            combine[key] = combine[key][:-1]

    return combine


















    






