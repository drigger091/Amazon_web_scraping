import requests
from bs4 import BeautifulSoup
import smtplib
import time
import datetime
import json
import csv


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
URL = 'https://www.amazon.in/BULLMER-Regular-Printed-Cotton-Tshirt/dp/B0B71W86QX/ref=sr_1_18?keywords=t-shirt+for+men&qid=1663687983&sprefix=t+shirt%2Caps%2C499&sr=8-18'

page = requests.get(URL,headers=headers)

soup1 = BeautifulSoup(page.content,"html.parser")
soup2 = BeautifulSoup(soup1.prettify(),'html.parser')
title = soup2.find(id = 'productTitle').get_text()


customer_review = soup2.find(id ='acrCustomerReviewText').get_text()





#cleaning the files


clean_title = title.strip()

customer_review = customer_review.strip()
print(clean_title)
print(customer_review)

#importing the data into a csv


#time stamping the data

today = datetime.date.today()
print(today)

header = ['Title','Review ratings',"Date"]
data = [clean_title,customer_review,today]

with open ('AmazonscrapedData.csv', 'w',newline='',encoding= 'UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)










