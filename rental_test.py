import unittest
from rental import Rental, PriceCode
from movie import Movie, MovieCatalog


class RentalTest(unittest.TestCase):
	
	def setUp(self):
		self.new_movie = Movie("Mulan", 2021, ["Action", "Adventure", "Drama"])
		self.regular_movie = Movie("CitizenFour", 2000, ["Action", "Adventure", "Drama"])
		self.children_movie = Movie("Frozen", 2020, ["Action", "Adventure", "Drama", "Children"])
		# with csv test
		self.catalog = MovieCatalog()
		self.movie_mulan = self.catalog.get_movie("Mulan")
		self.movie_tenant = self.catalog.get_movie("A Tenant")
		self.movie_arrival = self.catalog.get_movie("The Arrival")

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie"""
		m = Movie("CitizenFour", 2000, ["Action", "Adventure", "Drama"])
		rental = Rental(m, 3, PriceCode.for_movie(m))
		self.assertEqual("CitizenFour", m.get_title())
		self.assertEqual(PriceCode.normal, rental.get_price_code())
		self.assertEqual(1, rental.renter_points(rental.get_days_rented()))

	def test_rental_price(self):
		rental = Rental(self.new_movie, 1, PriceCode.for_movie(self.new_movie))
		self.assertEqual(rental.rental_price(), 3.0)
		rental = Rental(self.new_movie, 5, PriceCode.for_movie(self.new_movie))
		self.assertEqual(rental.rental_price(), 15.0)
		rental = Rental(self.children_movie, 4, PriceCode.for_movie(self.children_movie))
		self.assertEqual(rental.rental_price(), 3.0)
		rental = Rental(self.regular_movie, 3, PriceCode.for_movie(self.regular_movie))
		self.assertEqual(rental.rental_price(), 3.5)
		rental = Rental(self.movie_mulan, 3, PriceCode.for_movie(self.movie_mulan))
		self.assertEqual(rental.rental_price(), 1.5)
		rental = Rental(self.movie_tenant, 3, PriceCode.for_movie(self.movie_tenant))
		self.assertEqual(rental.rental_price(), 3.5)
		rental = Rental(self.movie_arrival, 3, PriceCode.for_movie(self.movie_arrival))
		self.assertEqual(rental.rental_price(), 3.5)

	def test_rental_points(self):
		rental = Rental(self.new_movie, 1, PriceCode.for_movie(self.new_movie))
		self.assertEqual(rental.renter_points(rental.get_days_rented()), 1)
		rental = Rental(self.new_movie, 5, PriceCode.for_movie(self.new_movie))
		self.assertEqual(rental.renter_points(rental.get_days_rented()), 5)
		rental = Rental(self.children_movie, 4, PriceCode.for_movie(self.children_movie))
		self.assertEqual(rental.renter_points(rental.get_days_rented()), 1)
		rental = Rental(self.regular_movie, 3, PriceCode.for_movie(self.regular_movie))
		self.assertEqual(rental.renter_points(rental.get_days_rented()), 1)
		rental = Rental(self.movie_mulan, 3, PriceCode.for_movie(self.movie_mulan))
		self.assertEqual(rental.renter_points(rental.get_days_rented()), 1)
		rental = Rental(self.movie_tenant, 3, PriceCode.for_movie(self.movie_tenant))
		self.assertEqual(rental.renter_points(rental.get_days_rented()), 1)
		rental = Rental(self.movie_arrival, 3, PriceCode.for_movie(self.movie_arrival))
		self.assertEqual(rental.renter_points(rental.get_days_rented()), 1)
