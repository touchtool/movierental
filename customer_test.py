import re
import unittest 
from customer import Customer
from rental import Rental, PriceCode
from movie import Movie, MovieCatalog


class CustomerTest(unittest.TestCase): 
	""" Tests of the Customer class"""
	
	def setUp(self):
		"""Test fixture contains:
		
		c = a customer
		movies = list of some movies
		"""
		self.c = Customer("Movie Mogul")
		self.new_movie = Movie("Mulan", 2021, ["Action", "Adventure", "Drama"])
		self.regular_movie = Movie("CitizenFour", 2000, ["Action", "Adventure", "Drama"])
		self.children_movie_new_release = Movie("Frozen", 2021, ["Action", "Adventure", "Drama", "Children"])
		self.children_movie = Movie("Frozen", 2020, ["Action", "Adventure", "Drama", "Children"])
		# with movie csv
		self.catalog = MovieCatalog()
		self.movie_mulan = self.catalog.get_movie("Mulan")
		self.movie_tenant = self.catalog.get_movie("A Tenant")
		self.movie_arrival = self.catalog.get_movie("The Arrival")

	def test_billing(self):
		rental = Rental(self.new_movie, 1, PriceCode.for_movie(self.new_movie))
		self.assertEqual(3, rental.rental_price())
		rental = Rental(self.regular_movie, 1, PriceCode.for_movie(self.regular_movie))
		self.assertEqual(2, rental.rental_price())
		rental = Rental(self.children_movie, 1, PriceCode.for_movie(self.children_movie))
		self.assertEqual(1.5, rental.rental_price())
		rental = Rental(self.new_movie, 2, PriceCode.for_movie(self.new_movie))
		self.assertEqual(6, rental.rental_price())
		rental = Rental(self.regular_movie, 2, PriceCode.for_movie(self.regular_movie))
		self.assertEqual(2, rental.rental_price())
		rental = Rental(self.children_movie, 3, PriceCode.for_movie(self.children_movie))
		self.assertEqual(1.5, rental.rental_price())
		rental = Rental(self.new_movie, 3, PriceCode.for_movie(self.new_movie))
		self.assertEqual(9, rental.rental_price())
		rental = Rental(self.regular_movie, 3, PriceCode.for_movie(self.regular_movie))
		self.assertEqual(3.5, rental.rental_price())
		rental = Rental(self.children_movie, 4, PriceCode.for_movie(self.children_movie))
		self.assertEqual(3, rental.rental_price())
		rental = Rental(self.movie_mulan, 4, PriceCode.for_movie(self.movie_mulan))
		self.assertEqual(3, rental.rental_price())
		rental = Rental(self.movie_arrival, 4, PriceCode.for_movie(self.movie_arrival))
		self.assertEqual(5, rental.rental_price())
		rental = Rental(self.movie_tenant, 4, PriceCode.for_movie(self.movie_tenant))
		self.assertEqual(5, rental.rental_price())

	def test_renter_points(self):
		rental = Rental(self.new_movie, 10, PriceCode.for_movie(self.new_movie))
		self.assertEqual(10, rental.renter_points(rental.get_days_rented()))
		rental = Rental(self.regular_movie, 10, PriceCode.for_movie(self.regular_movie))
		self.assertEqual(1, rental.renter_points(rental.get_days_rented()))
		rental = Rental(self.children_movie, 10, PriceCode.for_movie(self.children_movie))
		self.assertEqual(1, rental.renter_points(rental.get_days_rented()))
		rental = Rental(self.movie_tenant, 10, PriceCode.for_movie(self.movie_tenant))
		self.assertEqual(1, rental.renter_points(rental.get_days_rented()))
		rental = Rental(self.movie_mulan, 10, PriceCode.for_movie(self.movie_mulan))
		self.assertEqual(1, rental.renter_points(rental.get_days_rented()))
		rental = Rental(self.movie_arrival, 10, PriceCode.for_movie(self.movie_arrival))
		self.assertEqual(1, rental.renter_points(rental.get_days_rented()))

	def test_statement(self):
		stmt = self.c.statement()
		# visual testing
		print(stmt)
		# get total charges from statement using a regex
		pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
		matches = re.match(pattern, stmt, flags=re.DOTALL)
		self.assertIsNotNone(matches)
		self.assertEqual("0.00", matches[1])
		# add a rental
		self.c.add_rental(Rental(self.new_movie, 4, PriceCode.for_movie(self.new_movie)))  # days
		stmt = self.c.statement()
		matches = re.match(pattern, stmt.replace('\n', ''), flags=re.DOTALL)
		self.assertIsNotNone(matches)
		self.assertEqual("12.00", matches[1])
