from rental import PriceCode


class Movie:
    """
    A movie available for rent.
    """
    def __init__(self, title, year, genre):
        # Initialize a new movie.
        # if not isinstance(price_code, PriceCode):
        #     raise TypeError(f"Movie has unrecognized priceCode {price_code}")
        self.title = title
        self.year = year
        self.genre = genre
        # self.price_code = price_code

    def get_title(self):
        return self.title

    def is_genre(self) -> str:
        return type(self.genre)==type(str)

    def __str__(self):
        return self.title
