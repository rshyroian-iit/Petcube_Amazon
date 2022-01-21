import scrapy
from ..items import AmazonPetCamerasProductsItem
import csv

number_of_products = 20

with open('mycsv.csv', 'w', newline = '') as f:
    thewriter = csv.writer(f)
    thewriter.writerow(['product_name', 'product_asin', 'product_price', 'product_stars', 'product_ratings', '5star', '4star', '3star', '2star', '1star', 'product_review'])

temp_list = []

class AmazonSpiderProductsSpider(scrapy.Spider):
    name = 'amazon_spider_products'
    allowed_domains = ['amazon.com']
    start_urls = []
    with open('links.txt', 'r') as filehandle:
        filecontents = filehandle.readlines()
        for line in filecontents:
            current_link = line[:-1]
            start_urls.append("https://www.amazon.com" + current_link)

    def parse(self, response, ):
        items = AmazonPetCamerasProductsItem()

        product_name = response.css('#productTitle').css('::text').getall()
        def filtruem_po_enteram(bazar):
            result = ''
            for i in range(0, len(bazar)):
                if (bazar[i] == "\n"):
                    i += 1
                else:
                    result += bazar[i]
            return result
        product_name = filtruem_po_enteram(filtruem_po_enteram(product_name))
        items['product_name'] = product_name

        product_brand = response.css('#bylineInfo_feature_div .a-spacing-none .a-link-normal').css('::text').getall()
        items['product_brand'] = product_brand

        product_price = response.css('div.a-column.a-span6.a-text-right.a-span-last > span').css('::text').extract()
        if len(product_price) == 0:
            product_price = response.css('#price_inside_buybox').css('::text').extract()
            product_price[0] = product_price[0][1:-1]
        items['product_price'] = product_price

        product_stars = response.css('#acrPopover > span.a-declarative > a > i.a-icon.a-icon-star > span').css('::text').extract()
        items['product_stars'] = product_stars

        product_stars_distribution = response.css('.a-align-center:nth-child(1) .a-link-normal').css('::text').getall()
        def filter_stars(stars):
            result = ['0%', '0%', '0%', '0%', '0%']
            indicator = 4
            for line in stars:
                number = ''
                for i in range(3, len(line)):
                    if line[i] == 't' and line[i - 1] == 's' and line[i - 2] == ' ':
                        indicator = int(line[i - 3])
                    if line[i] == '%':
                        if line[i - 2] != ' ':
                            number = line[i - 2] + line[i - 1] + line[i]
                            result[indicator - 1] = number
                        else:
                            number = line[i - 1] + line[i]
                            result[indicator - 1] = number

            return result
        product_stars_distribution = filter_stars(product_stars_distribution)
        items['product_stars_distribution'] = product_stars_distribution

        product_ratings = response.css('#acrCustomerReviewText').css('::text').extract()
        items['product_ratings'] = product_ratings

        location = response.css('#upsellMirId > b').css('::text').extract()
        if len(location) == 0:
            location = response.css('#deliveryMessageMirId > b').css('::text').extract()
        items['location'] = location

        review_link = response.css('#cr-pagination-footer-0 > a::attr(href)').getall()
        if len(review_link) == 0:
            review_link = response.css('#reviews-medley-footer > div.a-row.a-spacing-extra-large > a::attr(href)').getall()
        items['review_link'] = review_link


        product_asin = response.css('#ASIN').attrib['value']
        items['product_asin'] = product_asin


        product_price.append('0')
        product_stars.append('0')
        temp_list.append([product_name, product_asin, product_price[0], product_stars[0][:3], product_ratings[0][:-7], product_stars_distribution[4], product_stars_distribution[3], product_stars_distribution[2], product_stars_distribution[1], product_stars_distribution[0], review_link[0]])
        final_list = temp_list
        if len(final_list) == number_of_products:
            final_list = sorted(final_list, key = lambda x: x[0])
            f = open('review_links.txt', 'w')
            for j in range(0, len(final_list)):
                final_list[j][10]
                f.write(final_list[j][10] + '\n')
            f.close()
            with open('mycsv.csv', 'a', newline = '') as d:
                thewritera = csv.writer(d)
                product_price.append('0')
                product_stars.append('0')
                for i in range(0, len(final_list)):
                    thewritera.writerow([final_list[i][0], final_list[i][1], final_list[i][2], final_list[i][3], final_list[i][4], final_list[i][5], final_list[i][6], final_list[i][7], final_list[i][8], final_list[i][9], final_list[i][10]])

        yield items