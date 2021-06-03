from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.request
import os

page_number = 1
image_number = 2000
total_pages = 1

while page_number <= total_pages:
    site = ""
    html = urlopen(site)
    bs = BeautifulSoup(html, 'html.parser')

    images = bs.find_all('img')

    for img in images:
        if img.has_attr('src'):
            source = img['src']
            print(source)
            if source == "":
                continue
            fullfilename = os.path.join(
                'C:/', "picture" + str(counter) + ".jpg")

            urllib.request.urlretrieve(source, fullfilename)
            counter = counter + 1

    page_number = page_number + 1
