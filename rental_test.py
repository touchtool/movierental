import unittest
from customer import Customer
from rental import Rental, PriceCode
from movie import Movie


class RentalTest(unittest.TestCase):
	
	def setUp(self):
		self.new_movie = Movie("Mulan", PriceCode.new_release)
		self.regular_movie = Movie("CitizenFour", PriceCode.normal)
		self.children_movie = Movie("Frozen", PriceCode.children)

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie"""
		m = Movie("CitizenFour", PriceCode.normal)
		self.assertEqual("CitizenFour", m.get_title())
		self.assertEqual(PriceCode.normal, m.get_price_code())

	def test_rental_price(self):
		rental = Rental(self.new_movie, 1)
		self.assertEqual(rental.rental_price(), 3.0)
		rental = Rental(self.new_movie, 5)
		self.assertEqual(rental.rental_price(), 15.0)
		rental = Rental(self.children_movie, 4)
		self.assertEqual(rental.rental_price(), 3.0)
		rental = Rental(self.regular_movie, 3)
		self.assertEqual(rental.rental_price(), 3.5)

	def test_rental_points(self):
		rental = Rental(self.new_movie, 1)
		self.assertEqual(rental.movie.renter_points(rental.days_rented), 1)
		rental = Rental(self.new_movie, 5)
		self.assertEqual(rental.movie.renter_points(rental.days_rented), 5)
		rental = Rental(self.children_movie, 4)
		self.assertEqual(rental.movie.renter_points(rental.days_rented), 1)
		rental = Rental(self.regular_movie, 3)
		self.assertEqual(rental.movie.renter_points(rental.days_rented), 1)
