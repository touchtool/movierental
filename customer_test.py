import re
import unittest 
from customer import Customer
from rental import Rental, PriceCode
from movie import Movie


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

	def test_billing(self):
		rental_new_1_day = Rental(self.new_movie, 1, PriceCode.for_movie(self.new_movie))
		rental_regular_1_day = Rental(self.regular_movie, 1, PriceCode.for_movie(self.regular_movie))
		rental_children_1_day = Rental(self.children_movie, 1, PriceCode.for_movie(self.children_movie))
		rental_new_2_day = Rental(self.new_movie, 2, PriceCode.for_movie(self.new_movie))
		rental_regular_2_day = Rental(self.regular_movie, 2, PriceCode.for_movie(self.regular_movie))
		rental_children_3_day = Rental(self.children_movie, 3, PriceCode.for_movie(self.children_movie))
		rental_new_3_day = Rental(self.new_movie, 3, PriceCode.for_movie(self.new_movie))
		rental_regular_3_day = Rental(self.regular_movie, 3, PriceCode.for_movie(self.regular_movie))
		rental_children_4_day = Rental(self.children_movie, 4, PriceCode.for_movie(self.children_movie))
		self.assertEqual(3, rental_new_1_day.rental_price())
		self.assertEqual(2, rental_regular_1_day.rental_price())
		self.assertEqual(1.5, rental_children_1_day.rental_price())
		self.assertEqual(6, rental_new_2_day.rental_price())
		self.assertEqual(2, rental_regular_2_day.rental_price())
		self.assertEqual(1.5, rental_children_3_day.rental_price())
		self.assertEqual(9, rental_new_3_day.rental_price())
		self.assertEqual(3.5, rental_regular_3_day.rental_price())
		self.assertEqual(3, rental_children_4_day.rental_price())

	def test_renter_points(self):
		rental_new = Rental(self.new_movie, 10, PriceCode.for_movie(self.new_movie))
		rental_regular = Rental(self.regular_movie, 10, PriceCode.for_movie(self.regular_movie))
		rental_children = Rental(self.children_movie, 10, PriceCode.for_movie(self.children_movie))
		self.assertEqual(10, rental_new.renter_points(rental_new.get_days_rented()))
		self.assertEqual(1, rental_regular.renter_points(rental_regular.get_days_rented()))
		self.assertEqual(1, rental_children.renter_points(rental_children.get_days_rented()))

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
