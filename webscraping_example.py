from bs4 import BeautifulSoup
import requests
import subprocess
import urllib.request
from PIL import Image
import io

url = "http://www.iwozhere.com/SRD/Gallery.html"
html = requests.get(url).text # get the html
soup = BeautifulSoup(html, "lxml") # give the html to soup
imagesPath = 'http://www.iwozhere.com/SRD/images/'

# get all the anchor links with the custom class 
# the element or the class name will change based on your case
imgs = soup.findAll("img")
for img in imgs:
    imgUrl = img['src']
    file_name = imgUrl.rsplit('/',1)[1]
    urlString = (imagesPath + file_name)
    response = requests.get(urlString)
    if response.status_code == 200:
        print('response', response.status_code)
