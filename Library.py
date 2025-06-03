class Library:
    book_list = [] 
    @classmethod
    def entry_book(self, new_book):
        self.book_list.append(new_book)
    @classmethod
    def view_all_books(self):
        for book in self.book_list:
            book.view_book_info()

class Book:
    def __init__(self, book_id, title, author, availability):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = availability
    def borrow_book(self):
        if self.__availability:
            self.__availability = False
            print(f'You have successfully borrowed the book: {self.__title}')
        else:
            print(f'Sorry, {self.__title} is not available.')
    def return_book(self):
        if not self.__availability:
            self.__availability = True
            print(f"You have successfully returned the book: {self.__title}")
        else:
            print(f'The book {self.__title} was not borrowed.')
    def view_book_info(self):
        if self.__availability:
            status='Available'
        else:
            status='Not Available'
        print(f'Book ID: {self.__book_id} || Book Title: {self.__title} || Book Author: {self.__author} || Status: {status}')
    def get_book_id(self):
        return self.__book_id

book1 = Book(101, "Golpoguccho", "Rabindranath Tagore", True)
book2 = Book(102, "Kobor", "Munir Chowdhury", True)
book3 = Book(103, "Feluda", "Satyajit Ray", True)
book4 = Book(104, "100 Best Poems", "Michael Madhusudan", True)
book5 = Book(105, "Kheya", "Jasim Uddin", True)

Library.entry_book(book1)
Library.entry_book(book2)
Library.entry_book(book3)
Library.entry_book(book4)
Library.entry_book(book5)

print("********* Welcome to the Library System *********")
while True:
    print('\nMenu:')
    print('1) View All Books')
    print('2) Borrow Book')
    print('3) Return Book')
    print('4) Exit')

    n = input('Enter your choice (1-4): ')

    if n == '1':
        Library.view_all_books()

    elif n == '2':
        id = int(input('Enter the Book ID you want to borrow: '))
        found = False
        for book in Library.book_list:
            if book.get_book_id() == id:
                book.borrow_book()
                found = True
                break
        if not found:
                print('Invalid Book ID.')

    elif n == '3':
            id = int(input('Enter the Book ID you want to return: '))
            found = False
            for book in Library.book_list:
                if book.get_book_id() == id:
                    book.return_book()
                    found = True
                    break
            if not found:
                print("Invalid Book ID.")

    elif n == '4':
        print('Thank you for using the Library System.')
        break

    else:
        print("Invalid choice. Please select from 1 to 4.")
