class Book:
    def __init__(self, new_id, name, author, year, ISBN, category, quantity):
        self.__id = new_id
        self.__name = name
        self.__author = author
        self.__year = year
        self.__category = category
        self.__ISBN = ISBN
        self.__quantity = quantity

    def set_id(self, new_id):
        self.__id = new_id

    def get_id(self):
        return self.__id

    def set_name(self, name):
        self.__name = []
        self.__name = name

    def get_name(self):
        return self.__name

    def set_author(self, author):
        self.__author = []
        self.__author = author

    def get_author(self):
        return self.__author

    def set_year(self, date):
        self.__year = date

    def get_year(self):
        return self.__year

    def set_category(self, category):
        self.__category = category

    def get_category(self):
        return self.__category

    def set_ISBN(self, isbn):
        self.__ISBN = []
        self.__ISBN = isbn

    def get_IBAN(self):
        return self.__ISBN

    def set_quantity(self, q):
        self.__quantity = q

    def get_quantity(self):
        return self.__quantity
