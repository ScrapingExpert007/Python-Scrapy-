import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["toscrape.com"]
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        self.log("I just visited: " + response.url)

        for quote in response.css('div.quote'):
            item = {
                'author_name': quote.css('small.author::text').extract_first(),
                'text': response.css('span.text::text').extract_first(),
                'tags': response.css('a.tag::text').extract()
            }
            yield item


"""
scrapy runspider quotes.py
scrapy runspider quotes.py -o quotes.json
more quotes.json

"""
