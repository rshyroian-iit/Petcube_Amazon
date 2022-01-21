import os
import schedule
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import csv
from datetime import date

with open('final.csv', 'w', newline = '') as niet:
    thewriter = csv.writer(niet)
    thewriter.writerow(['date', 'product_name', 'rank', 'product_asin', 'product_price', 'product_stars', 'product_ratings', '5star', '4star', '3star', '2star', '1star', 'review_number'])

big_arr= []

def scrape_data():

    today = date.today()
    d = today.strftime("%d/%m/%Y")

    os.system("scrapy crawl amazon_spider_bestseller")
    time.sleep(10)

    new_arr = []

    df1 = pd.read_csv("bestsellercsv.csv", header = 0)
    i = 0
    for index, row in df1.iterrows():
        i += 1
        new_arr.append([d, row["product_name"], row["product_rank"]])
    
    os.system("scrapy crawl amazon_spider_products")
    time.sleep(10)

    df2 = pd.read_csv("mycsv.csv", header = 0)
    i = 0
    for index, row in df2.iterrows():
        new_arr[i].append(row["product_asin"])
        new_arr[i].append(row["product_price"])
        new_arr[i].append(row["product_stars"])
        new_arr[i].append(row["product_ratings"])
        new_arr[i].append(row["5star"])
        new_arr[i].append(row["4star"])
        new_arr[i].append(row["3star"])
        new_arr[i].append(row["2star"])
        new_arr[i].append(row["1star"])
        i += 1

    os.system("scrapy crawl amazon_spider_reviews")
    time.sleep(10)

    df3 = pd.read_csv("reviewcsv.csv", header = 0)
    i = 0
    for index, row in df3.iterrows():
        new_arr[i].append(row["review_number"])
        i += 1

    new_arr = sorted(new_arr, key = lambda x: x[2])

    with open('final.csv', 'a', newline = '') as da:
        thewritera = csv.writer(da)
        for row in new_arr:
            thewritera.writerow(row)

    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
            "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

    credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(credentials)

    spreadsheet = client.open('CSV-to-Google-Sheet')

    with open('final.csv', 'r') as file_obj:
        content = file_obj.read()
        client.import_csv(spreadsheet.id, data=content)

#schedule.every().day.at("10:30").do(scrape_data)
schedule.every(0.25).minutes.do(scrape_data)

while True:
    schedule.run_pending()
    time.sleep(1)