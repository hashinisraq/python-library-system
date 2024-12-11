class Library:
    book_list = []
    
    @classmethod
    def entry_book(cls, book):
        cls.book_list.append(book)

class Book:
    def __init__(self, book_id, title, author, availability=True):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = availability

        Library.entry_book(self)


    def borrow_book(self):
        if self.__availability:
            self.__availability = False
            print(f"Book '{self.__title}' has borrowed successfully.")
        else:
            print(f"Book '{self.__title}' is not available for borrowing.")


    def return_book(self):
        if not self.__availability:
            self.__availability = True
            print(f"Book '{self.__title}' has returned successfully.")
        else:
            print(f"Book '{self.__title}' is not borrowed, so it cannot be returned.")


    def view_book_info(self):
        status = "Not Available"
        if self.__availability:
            status ="Available"
        print(f"ID: {self.__book_id}, Title: {self.__title}, Author: {self.__author}, Availability: {status}")


    def get_book_id(self):
        return self.__book_id

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_availability(self):
        return self.__availability


    def set_availability(self, status):
        self.__availability = status


def display_menu():
    print("\n-----Welcome to the Library-----")
    print("1. View All Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")

book1 = Book(101, "CSE", "John")
book2 = Book(201, "EEE", "Snow")
book3 = Book(301, "ECE", "William")

while True:
    display_menu()
    choice = input("\nEnter your choice: ")

    if choice == '1':
        if not Library.book_list:
            print("\nNo books available in the library.")
        else:
            print("\nLibrary Books:")
            for book in Library.book_list:
                book.view_book_info()

    elif choice == '2':
        book_id = int(input("\nEnter book ID to borrow: "))
        book = None
        for b in Library.book_list:
            if b.get_book_id() == book_id:
                book = b
                break
        if book:
            book.borrow_book()
        else:
            print("\tBook not found.")

    elif choice == '3':
        book_id = int(input("\nEnter book ID to return: "))
        book = None
        for b in Library.book_list:
            if b.get_book_id() == book_id:
                book = b
                break
        if book:
            book.return_book()
        else:
            print("\nBook not found.")

    elif choice == '4':
         print("Exiting the Library system...\n")
         break
    
    else:
         print("\nInvalid choice. Please try again.")