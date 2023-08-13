import scrapy


class BookscrapeSpider(scrapy.Spider):
    name = 'bookscrape'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com']

    def parse(self, response):
        books = response.css('article.product_pod')
        
        for book in books:
            relativeBookURL = book.css("h3 a").attrib["href"]
            if relativeBookURL is not None:
                if "catalogue/" in relativeBookURL:
                    bookURL = 'https://books.toscrape.com/' + relativeBookURL
                else:
                    bookURL = 'https://books.toscrape.com/catalogue/' + relativeBookURL
                yield response.follow(bookURL, callback = self.parseBookPage)
        
        nextPage = response.css("li.next a").attrib["href"]
        if nextPage is not None:
            if "catalogue/" in nextPage:
                nextPageURL = 'https://books.toscrape.com/' + nextPage
            else:
                nextPageURL = 'https://books.toscrape.com/catalogue/' + nextPage
            yield response.follow(nextPageURL, callback = self.parse)

    def parseBookPage(self, response) :
        tableRows = response.css('table tr')
        yield {
            "url" : response.url,
            "title" : response.css('.product_main h1::text').get(),
            "product type" : tableRows[1].css("td ::text").get(),
            "price_excl_tax" : tableRows[2].css("td ::text").get(),
            "price_incl_tax" : tableRows[3].css("td ::text").get(),
            "tax" : tableRows[4].css("td ::text").get(),
            "availability" : tableRows[6].css("td ::text").get(),
            "rating" : response.css("p.star-rating").attrib["class"],
            "price" : response.css("p.price_color ::text").get(),
        }