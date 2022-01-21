#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 16:52:07 2019

@author: robert.shyroian
"""

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import time
import requests

start_time = time.time()

my_url = 'https://www.amazon.com/s?k=camera&ref=nb_sb_noss_2'

 # prepare headers
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}


    # fetching the url, raising error if operation fails
try:
    response = requests.get(my_url, headers=headers)
except requests.exceptions.RequestException as e:
    print(e)
print(response.text)
exit()

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
print(page_soup.h1)
#containers = page_soup.findAll("div", {"class" : "item-container"})
#filename = "products1.csv"
#f = open(filename, "w")

#headers = "brand_name,product_name,shipping_price\n"

#f.write(headers)
#j = 0
#for container in containers:
#    j += 1
#    print(j)
#    brand_name = container.find("a", {"class" : "item-brand"}).img["title"]
#    product_name = container.find("a", {"class" : "item-title"}).text
#    shipping_price = container.find("li", {"class" : "price-ship"}).text.strip()
#    f.write(brand_name + "," + product_name.replace("," , "|") + "," + shipping_price + "\n")
#    print(brand_name + "," + product_name.replace("," , "|") + "," + shipping_price + "\n")

########
#i = 2

#print(i)
#print(time.time() - start_time)
#while i < 3:
#    while time.time() - start_time < 10:
#        if time.time() - start_time > 9.5:
#            print(time.time() - start_time)
#    my_url = 'https://www.newegg.com/p/pl?Submit=StoreIM&Depa=1&Category=38&Page=' + str(i) + '&PageSize=36'
##    my_url = 'https://www.newegg.com/p/pl?Submit=StoreIM&page=' + str(i) + '&Depa=1&Category=38'
#    print(my_url)
#    uClient = uReq(my_url)
#    page_html = uClient.read()
#    uClient.close()
#    page_soup = soup(page_html, "html.parser")
#    print(page_soup)
#    containers = page_soup.findAll("div", {"class" : "item-container "})
#    
#    print(len(containers))
#    
#    for container in containers:
#        j += 1
#        print(j)
#        brand_name = container.find("a", {"class" : "item-brand"}).img["title"]
#        product_name = container.find("a", {"class" : "item-title"}).text
#        shipping_price = container.find("li", {"class" : "price-ship"}).text.strip()
#        f.write(brand_name + "," + product_name.replace("," , "|") + "," + shipping_price + "\n")
#        print(brand_name + "," + product_name.replace("," , "|") + "," + shipping_price + "\n")
#    
#    i += 1
##########

f.close()