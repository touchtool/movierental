from rental import PriceCode


class Movie:
    """
    A movie available for rent.
    """
    def __init__(self, title, price_code):
        # Initialize a new movie.
        if not isinstance(price_code, PriceCode):
            raise TypeError(f"Movie has unrecognized priceCode {price_code}")
        self.title = title
        self.price_code = price_code

    def get_price_code(self):
        # get the price code
        return self.price_code

    def get_title(self):
        return self.title

    def renter_points(self, days):
        return self.price_code.frequency_point(days)

    def __str__(self):
        return self.title
