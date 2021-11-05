import logging
from enum import Enum


class Rental:
	"""
	A rental of a movie by customer.
	From Fowler's refactoring example.

	A realistic Rental would have fields for the dates
	that the movie was rented and returned, from which the
	rental period is calculated.
	But for simplicity of the example only a days_rented
	field is used.
	"""

	def __init__(self, movie, days_rented):
		"""Initialize a new movie rental object for
		a movie with known rental period (daysRented).
		"""
		self.movie = movie
		self.days_rented = days_rented

	def get_movie(self):
		return self.movie

	def get_days_rented(self):
		return self.days_rented

	def rental_price(self):
		return self.movie.price_code.price(self.days_rented)


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
