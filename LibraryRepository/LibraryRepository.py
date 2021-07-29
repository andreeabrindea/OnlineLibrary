from typing import List
from Book.Book import Book


class LibraryRepository:

    def __init__(self, book_list: List[Book] = []):
        # constructor
        self.__books = []
        for book in book_list:
            self.__books.append(book)

    def __len__(self) -> int:
        return len(self.__books)

    def __str__(self) -> str:
        '''
        Returns:
        --------
        string representation of the current book repository instance
        '''
        books = []
        for book in self.__books:
            books.append(str(book))
        return str(books)

    def __eq__(self, other) -> bool:
        '''
        Defines if two BookRepository instances are equal or not

        Args:
        -----
            @other: BookRepository
                another BookRepository instance to compare to the current

        Returns:
        --------
            bool
                True if the two objects attribute are the same, False otherwise
        '''
        if len(self) != len(other):
            return False
        for index in range(len(self)):
            if self.__books[index] != other.__books[index]:
                return False
        return True

    def get_list(self) -> List[Book]:
        '''
        Return the list of books

        Returns:
        --------
            list[Book]
                list of books in the current repository
        '''
        return self.__books


    def add_book(self, book: Book):
        """"
        Adds a book to the repository
        Input: book - object of type Book
        """
        self.__books.append(book)

    def add_new_book(self, id: int, name: str, author: str, year: int, ISBN:str, category:str, quantity: int=0):
     self.__books.append(Book(id, name, author, year, ISBN, category, quantity))