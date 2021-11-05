# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie
from rental import Rental, PriceCode
from customer import Customer


def make_movies():
    movies = [
        Movie("The Irishman", 1997, "hello"),
        Movie("CitizenFour", 1997, "hello"),
        Movie("Frozen", 1997, "hello"),
        Movie("El Camino", 1997, "hello"),
        Movie("Particle Fever", 1997, "hello")
    ]
    return movies


def set_price_code():
    price_codes = [
        PriceCode.new_release,
        PriceCode.normal,
        PriceCode.children,
        PriceCode.new_release,
        PriceCode.normal
    ]
    return price_codes


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    price_code = set_price_code()
    count = 0
    for movie in make_movies():
        customer.add_rental(Rental(movie, days, price_code[count]))
        days += 1
        count += 1
    print(customer.statement())
