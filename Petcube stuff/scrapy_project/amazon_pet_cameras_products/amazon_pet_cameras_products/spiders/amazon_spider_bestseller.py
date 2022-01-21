import scrapy
from ..items import AmazonPetCamerasProductsItem
import csv


class AmazonSpiderBestsellerSpider(scrapy.Spider):
    name = 'amazon_spider_bestseller'
    allowed_domains = ['amazon.com']
    start_urls = [
        'https://www.amazon.com/gp/bestsellers/pet-supplies/17440052011/ref=sr_bs_0_17440052011_1'
    ]

    def parse(self, response):
        items = AmazonPetCamerasProductsItem()
        product_links = response.css('.a-link-normal').getall()
        def filtruem_linki(bazari):
            results = []
            for bazar in bazari:
                result = ''
                add = False
                for i in range(5, len(bazar) - 1):
                    if bazar[i - 5] == 'r' and bazar[i - 4] == 'e' and bazar[i - 3] == 'f' and bazar[i - 2] == '=' and bazar[i - 1] == '"' and bazar[i + 1] != 'p' and bazar[i + 2] != 'r' and bazar[i + 2] != 'o':
                        add = True
                    if bazar[i] == '"' and bazar[i + 1] == '>':
                        add = False
                    if add == True:
                        result += bazar[i]
                results.append(result)
            return results
        product_links = filtruem_linki(product_links)
        links = []
        links.append(product_links[0])
        for link in product_links:
            if len(link) != 0:
                if link != links[-1]:
                    links.append(link)
        product_links = links[0:20]
        items['product_links'] = product_links
        f = open('links.txt', 'w')
        for link in product_links:
            f.write(link + '\n')
        f.close()

        product_name = response.css('.zg-text-center-align').getall()
        def filtruem_namei(bazari):
            results = []
            for bazar in bazari:
                result = ''
                add = False
                for i in range(5, len(bazar) - 1):
                    if bazar[i - 5] == 'a' and bazar[i - 4] == 'l' and bazar[i - 3] == 't' and bazar[i - 2] == '=' and bazar[i - 1] == '"':
                        add = True
                    if bazar[i] == '"' and bazar[i + 1] == ' ':
                        add = False
                    if add == True:
                        new_str = bazar[i]
                        if bazar[i] == '\u2013':
                            new_str = ' '
                        if bazar[i] == '\uff0c':
                            new_str = ' '
                        result += new_str
                results.append(result)
            return results
        product_name = product_name[1:21]
        product_name = filtruem_namei(product_name)
        items['product_name'] = product_name
        product_rank = response.css('.zg-badge-text::text').extract()
        items['product_rank'] = product_rank
        final_list = []
        for i in range(0, len(product_name)):
            final_list.append([product_name[i], product_rank[i][1:]])
 
        final_list = sorted(final_list, key = lambda x: x[0])

        with open('bestsellercsv.csv', 'w', newline = '') as f:
            thewriter = csv.writer(f)
            thewriter.writerow(['product_name', 'product_rank'])
            for i in range(0, len(final_list)):
                thewriter.writerow([final_list[i][0], final_list[i][1]])
        yield items