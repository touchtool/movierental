import re
import unittest 
from customer import Customer
from rental import Rental
from movie import Movie


class CustomerTest(unittest.TestCase): 
	""" Tests of the Customer class"""
	
	def setUp(self):
		"""Test fixture contains:
		
		c = a customer
		movies = list of some movies
		"""
		self.c = Customer("Movie Mogul")
		self.new_movie = Movie("Mulan", Movie.NEW_RELEASE)
		self.regular_movie = Movie("CitizenFour", Movie.REGULAR)
		self.children_movie = Movie("Frozen", Movie.CHILDREN)

	def test_billing(self):
		rental_new_1_day = Rental(self.new_movie, 1)
		rental_regular_1_day = Rental(self.regular_movie, 1)
		rental_children_1_day = Rental(self.children_movie, 1)
		rental_new_2_day = Rental(self.new_movie, 2)
		rental_regular_2_day = Rental(self.regular_movie, 2)
		rental_children_3_day = Rental(self.children_movie, 3)
		rental_new_3_day = Rental(self.new_movie, 3)
		rental_regular_3_day = Rental(self.regular_movie, 3)
		rental_children_4_day = Rental(self.children_movie, 4)
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
		self.assertEqual(10, Rental(self.new_movie, 10).renter_points())
		self.assertEqual(1, Rental(self.regular_movie, 10).renter_points())
		self.assertEqual(1, Rental(self.children_movie, 10).renter_points())

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
		self.c.add_rental(Rental(self.new_movie, 4))  # days
		stmt = self.c.statement()
		matches = re.match(pattern, stmt.replace('\n', ''), flags=re.DOTALL)
		self.assertIsNotNone(matches)
		self.assertEqual("12.00", matches[1])
