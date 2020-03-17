from bs4 import BeautifulSoup
import requests
import subprocess
import urllib.request
from PIL import Image
import io
import os

url = "http://www.iwozhere.com/SRD/Gallery.html"
html = requests.get(url).text # get the html
soup = BeautifulSoup(html, "lxml") # give the html to soup
imagesPath = 'http://www.iwozhere.com/SRD/images/'
dest_dir = './images'

# get all the anchor links with the custom class 
# the element or the class name will change based on your case
imgs = soup.findAll("img")
for img in imgs:
    imgUrl = img['src']
    file_name = imgUrl.rsplit('/',1)[1]
    urlString = (imagesPath + file_name)
    response = requests.get(urlString, stream=True)
    if response.status_code == 200:
        print('response', response.status_code)
        path = os.path.join(dest_dir, file_name)
        with open(path, 'wb') as imageFile:
            for blob in response.iter_content(1024):
                imageFile.write(blob)
