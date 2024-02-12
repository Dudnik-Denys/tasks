from enum import Flag


MovieGenres = Flag('MovieGenres', ['ACTION', 'COMEDY', 'DRAMA', 'FANTASY', 'HORROR'])


class Movie:
    def __init__(self, name: str, genres: MovieGenres) -> None:
        self.name = name
        self.genres = genres

    def is_genre(self, genre: MovieGenres) -> bool:
        return genre in self.genres

    def __str__(self) -> str:
        return self.name
