class Author:
    _contracts = []

    def __init__(self, name):
        if not isinstance(name, str) or not name:
            raise Exception("Name must be a non-empty string.")
        self.name = name

    def contracts(self):
        """Return a list of contracts associated with this author."""
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        """Return a list of books associated with this author."""
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        """Create a new contract and add it to the author's list."""
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of Book.")
        if not isinstance(date, str):
            raise Exception("Date must be a string.")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer.")
        
        contract = Contract(self, book, date, royalties)
        return contract

    def total_royalties(self):
        """Return the total royalties earned from all contracts."""
        return sum(contract.royalties for contract in self.contracts())



class Book:
    _contracts = []

    def __init__(self, title):
        if not isinstance(title, str) or not title:
            raise Exception("Title must be a non-empty string.")
        self.title = title

    def contracts(self):
        """Return a list of contracts associated with this book."""
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        """Return a list of authors associated with this book."""
        return [contract.author for contract in self.contracts()]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author.")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of Book.")
        if not isinstance(date, str):
            raise Exception("Date must be a string.")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer.")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        """Return all contracts that have the specified date."""
        return [contract for contract in cls.all if contract.date == date]
