import requests
from bs4 import BeautifulSoup
import Checkdet as cd

URLS = []

n = int(input("Number of products:"))
for i in range(0,n):
    add = input("Enter the product URL:")
    URLS.append(add)

#print(URLS)


for i in URLS:

        cd.check_data(i)

