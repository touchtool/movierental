# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie, MovieCatalog
from rental import Rental, PriceCode
from customer import Customer


def make_movies():
    catalog = MovieCatalog()
    movies = [
        catalog.get_movie("The Irishman"),  # Movie("The Irishman", 2021, "hello"),catalog.get_movie("The Irishman")
        catalog.get_movie("CitizenFour"),  # Movie("CitizenFour", 1997, "hello"),
        catalog.get_movie("Frozen"),  # Movie("Frozen", 2001, "hello"),
        catalog.get_movie("El Camino"),  # Movie("El Camino", 2021, "hello"),
        catalog.get_movie("Particle Fever"),  # Movie("Particle Fever", 1997, "hello")
    ]
    return movies


def set_price_code(movie):
    """If movie not in csv then It's will be new release"""
    price_codes = PriceCode.for_movie(movie)
    return price_codes


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        customer.add_rental(Rental(movie, days, set_price_code(movie)))
        days += 1
    print(customer.statement())
