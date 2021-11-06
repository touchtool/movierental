import csv


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

    def is_genre(self, genres: str):
        return genres in self.genre

    def __str__(self):
        return self.title


class MovieCatalog:
    """Get movie from csv file."""
    def __init__(self):
        self.MOVIE_CSV = []
        self.title_csv = []
        file = open('movies.csv')
        movie_csv = csv.DictReader(file)
        for row in movie_csv:
            self.MOVIE_CSV.append(row)
        file.close()

    def get_movie(self, title: str):
        if type(title) != str:
            raise TypeError("Movie require string type")
        for i in range(len(self.MOVIE_CSV)):
            self.title_csv.append(self.MOVIE_CSV[i]['title'])
        for i in range(len(self.MOVIE_CSV)):
            if title in self.title_csv:
                if self.MOVIE_CSV[i]['title'] == title:
                    return Movie(self.MOVIE_CSV[i]['title'], self.MOVIE_CSV[i]['year'], self.MOVIE_CSV[i]['genres'])
            if title not in self.title_csv:
                if {"id": "-", "title": title, "year": "-", "genres": "-"} not in self.MOVIE_CSV:
                    self.MOVIE_CSV.append({"id": "-", "title": title, "year": 2021, "genres": "-"})
                    return Movie(self.MOVIE_CSV[-1]['title'], self.MOVIE_CSV[-1]['year'], self.MOVIE_CSV[-1]['genres'])
