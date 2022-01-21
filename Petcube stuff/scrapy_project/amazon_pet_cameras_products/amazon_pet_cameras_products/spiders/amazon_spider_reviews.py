import scrapy
from ..items import AmazonPetCamerasProductsItem
import csv

number_of_products = 20

with open('reviewcsv.csv', 'w', newline = '') as ak:
    thewriter = csv.writer(ak)
    thewriter.writerow(['product_name', 'review_number'])

temp_list = []


class AmazonSpiderReviewsSpider(scrapy.Spider):
    name = 'amazon_spider_reviews'
    allowed_domains = ['amazon.com']
    start_urls = []
    with open('review_links.txt', 'r') as filehandle:
        filecontents = filehandle.readlines()
        for line in filecontents:
            current_link = line[:-1]
            start_urls.append("https://www.amazon.com" + current_link)

    def parse(self, response):
        items = AmazonPetCamerasProductsItem()
        product_review_number = response.css('#filter-info-section > span').css('::text').getall()
        items['product_review_number'] = product_review_number
        product_name = response.css('#cm_cr-product_info > div > div.a-fixed-left-grid-col.a-col-right > div > div > div.a-fixed-left-grid-col.product-info.a-col-right > div.a-row.product-title > h1 > a').css('::text').getall()
        items['product_name'] = product_name
        temp_list.append([product_name[0], product_review_number[0][15:-8]])
        final_list = temp_list
        if len(final_list) == number_of_products:
            final_list = sorted(final_list, key = lambda x: x[0])
            with open('reviewcsv.csv', 'a', newline = '') as da:
                thewritera = csv.writer(da)
                for i in range(0, len(final_list)):
                    thewritera.writerow([final_list[i][0], final_list[i][1]])
        yield items