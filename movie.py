from enum import Enum


class PriceCode(Enum):
    """An enumeration for different kinds of movies and their behavior"""
    new_release = {"price": lambda days: 3.0*days, "frp": lambda days: days}
    normal = {"price": lambda days: 2+(1.5*(days-2)) if days > 2 else 2, "frp": lambda days: 1}
    children = {"price": lambda days: 1.5 + 1.5*(days-3) if days > 3 else 1.5, "frp": lambda days: 1}

    def frequency_point(self, days: int) -> float:
        """Return the rental point for a given number of days"""
        points = self.value["frp"]
        return points(days)

    def price(self, days: int) -> float:
        "Return the rental price for a given number of days"""
        pricing = self.value["price"]    # the enum member's price formula
        return pricing(days)


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
