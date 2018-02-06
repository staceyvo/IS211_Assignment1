

class Book(object):
    """A class that represents a book."""
    #class attributes
    author = ''
    title = ''
    def __init__(self, title, author):
        """Constructor for the Book class.

        Args:
            author (str): author of the book
            title (str): title of the book

        Attributes:
            author (str): author of the book
            title (str): title of the book
            """
        self.author = author
        self.title = title


    def display(self):
        """displays the title of the book and author

        Args: adds a format to the title and author of a book.
        """
        print('{}, written by {}.'.format(self.title, self.author))

if __name__ == '__main__':
    mice = Book('Of Mice and Men', 'John Steinbeck')
    mockingbird = Book('To Kill a Mockingbird', 'Harper Lee')

    mice.display()
    mockingbird.display()
