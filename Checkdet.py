import requests
from bs4 import BeautifulSoup


def check_data(URL):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
    
    
   

    page = requests.get(URL,headers=headers)

    soup1 = BeautifulSoup(page.content,"html.parser")
    soup2 = BeautifulSoup(soup1.prettify(),'html.parser')
    title = soup2.find(id = 'productTitle').get_text()
    customer_review = soup2.find(id ='acrCustomerReviewText').get_text()
    clean_title = title.strip()
    customer_review = customer_review.strip()
    import datetime
    today = datetime.date.today()
    data = [clean_title,customer_review,today]
    import csv
    
    


    with open ('AmazonscrapedData.csv', 'a+',newline='',encoding= 'UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)