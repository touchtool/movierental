import csv


MOVIE_CSV = []
file = open('movies.csv')
movie_csv = csv.DictReader(file)
for row in movie_csv:
    MOVIE_CSV.append(row)
file.close()


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
        return type(self.genre) == type(str)

    def __str__(self):
        return self.title


class MovieCatalog:
    """Get movie from csv file."""
    def get_movie(self, title: str):
        for i in range(len(MOVIE_CSV)):
            if MOVIE_CSV[i]['title'] == title:
                return MOVIE_CSV[i]

