class Book:
    def __init__(self, isbn, title, publisher, genre, description, year, author = []):
        self.isbn = isbn
        self.title = title
        self.publisher = publisher
        self.genre = genre
        self.description = description
        self.year = year
        self.author = author
    
    @staticmethod
    def from_dict(source):
        book = Book(source['isbn'], source['title'], source['publisher'], source['genre'], source['description'], source['year'], source['author'])

        return book
    
    def to_dict(self):
        return {
            'isbn': self.isbn,
            'title': self.title,
            'publisher': self.publisher,
            'genre': self.genre,
            'description': self.description,
            'year': self.year,
            'author': self.author,
        }
    
    def __repr__(self):
        return ('ISBN={}, Title={}, Year={}, Author={}'.format(self.isbn, self.title, self.year, self.author))

from enum import Enum
class LevelOfAccess(Enum):
    COMMON_USER = 0
    ADMIN = 1

class User():
    def __init__(self, username, email, password, level):
        self.username = username
        self.email = email
        self.password = password
        self.level = level

    def to_dict(self):
        return {
            'username': self.username,
            'level': self.level,
        }