# library_system.py
# OOP Mini Project – Simple Library System


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book_name):
        self.books.append(book_name)
        print(f"{book_name} added to library.")

    def show_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            print("-", book)

    def remove_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"{book_name} removed from library.")
        else:
            print("Book not found.")


# creating library object
library = Library()

library.add_book("Python Basics")
library.add_book("Data Science Handbook")
library.add_book("Machine Learning Guide")

library.show_books()

library.remove_book("Python Basics")

library.show_books()
