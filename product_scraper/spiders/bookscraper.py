import csv
import scrapy


class BookscraperSpider(scrapy.Spider):
    name = "bookscraper"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]
    rows = []

    def parse(self, response):

        with open("products.csv", "w") as csvfile:
            """
            Initially write the column names in the csv file.
            """
            csvwriter = csv.writer(csvfile)
            fields = ["Product Name ", " Price ", " Rating "]
            csvwriter.writerow(fields)

        for book in response.css("article.product_pod"):
            """
            Extract the title, price and rating for each books from response.
            """
            title = book.css("a::attr(title)").get()
            price = book.css("p.price_color::text").get()
            rating = self.get_rating(book)
            self.write_to_csv(title, price, rating)

    def get_rating(self, book):
        """
        Extracts the ratings from the books using the class name.
        """
        rating_class = book.css("p::attr(class)").get()
        if rating_class == "star-rating One":
            return 1
        elif rating_class == "star-rating Two":
            return 2
        elif rating_class == "star-rating Three":
            return 3
        elif rating_class == "star-rating Four":
            return 4
        elif rating_class == "star-rating Five":
            return 5

    def write_to_csv(self, title, price, rating):
        """
        Append product details in csv file.
        """
        with open("products.csv", "a") as csvfile:
            rows = [[title, price, rating]]
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(rows)
