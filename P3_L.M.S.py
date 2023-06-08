import os
import speak
class Library:
    def __init__(self, list_of_books):
        self.books = list_of_books
    
    def display_available_books(self):
        try:
            print("BOOKS PRESENT IN THE LIBRARY ARE:  ")
            verticalTable = "  ".join(self.books)
            Table = "\n".join(f"{book}" for book in self.books)
            speak.speak(f"BOOKS PRESENT IN THE LIBRARY ARE:   {verticalTable}")
            print(Table)
        except Exception as e:
            print (f"An error occured: {e}")
    def issue_book(self, book_name):
        try:
            if book_name in self.books:
                borrower_name = input("Enter the name of the borrower: ")
                speak.speak("BOOK IS BORROWED BY: " + borrower_name)
                borrower_address = input("Enter the address of the borrower: ")
                speak.speak("Address of the borrower is "+borrower_address)
                borrower_contact = input("Enter the contact number of the borrower: ")
                speak.speak("Contact of the borrower is "+borrower_contact)
                book_file = book_name + ".txt"
                with open(book_file, "w") as book:
                    book.write(f"Name: {borrower_name}\nAddress: {borrower_address}\nContact number: {borrower_contact}")
                print("Your book has been issued")
                speak.speak("Your book has been issued")
                self.books.remove(book_name)
            else:
                speak.speak("The book is not present or might be borrowed by someone")
                print("The book is not present or might be borrowed by someone")

        except Exception as e:
            print (f"An error occured: {e}")

    def return_book(self, book_name):
        try:
            self.books.append(book_name)
            speak.speak("The book has been successfully returned")
            print("The book has been successfully returned")

            os.remove(book_name + ".txt")
        except Exception as e:
            print (f"An error occured: {e}")

    def add_book(self, book_name):
        try:
            a = input("Enter Administrator Password: ")
            if a == "ks@1673#":
                self.books.append(book_name)
                speak.speak("The book has been successfully added to the library")
                print("The book has been successfully added to the library")

            else:
                speak.speak("Wrong password")
                print("Wrong password")

        except Exception as e:
            print (f"An error occured: {e}")

    def find_book(self):
        try:
            book_name = input("Enter the name of the requested book: ")
            speak.speak("Enter the name of requested book")
            if book_name in self.books:
                speak.speak("Book is present in the library")
                print("Book is present in the library")

            else:
                speak.speak("Book is not present in the library or is borrowed by someone")
                print("Book is not present in the library or is borrowed by someone")

        except Exception as e:
            print (f"An error occured: {e}")

class Student:
    def request_book(self):
        try:
            speak.speak("Enter the name of the book you want to borrow")
            book_to_issue = input("Enter the name of the book you want to borrow: ")
            return book_to_issue
        except Exception as e:
            print (f"An error occured: {e}")

    def return_book(self):
        try:
            speak.speak("Enter the name of the book you want to return")
            book_to_return = input("Enter the name of the book you want to return: ")

            return book_to_return
        except Exception as e:
            print (f"An error occured: {e}")


if __name__ == "__main__":
    with open('D:\Python\Python Course\Project 3\list_of_books.txt', 'r') as f:
        books = f.read().split('\n')

    library = Library(books)
    student = Student()

    welcome_msg = '''\n Welcome to Library Management System
    Please choose an option:
    1.         List all the books                
    2.         Find a book                                                                    
    3.        Request a book                                                                          
    4.       Return a book                                     
    5.      Add a book (only for manager)                           
    6.       Update book_list.txt                         
    7.      Exit                                                     
    '''

    while True:
        speak.speak(welcome_msg)
        print(welcome_msg)

        choice = int(input("Enter a choice: "))

        if choice == 1:
            library.display_available_books()
        elif choice == 2:
            library.find_book()
        elif choice == 3:
            library.issue_book(student.request_book())
        elif choice == 4:
            library.return_book(student.return_book())
        elif choice == 5:
            speak.speak("Enter the book you want to add")
            book_to_add = input("Enter the book you want to add: ")
            library.add_book(book_to_add)
        elif choice == 6:
            try:
                speak.speak("Book list file has been updated.")
                print("Book list file has been updated.")
                with open('list_of_books.txt', 'w') as f:
                    f.write('\n'.join(library.books))
            except Exception as e:
                print (f"An error occured: {e}")
        elif choice == 7:
            speak.speak("Thanks for choosing this Library. Have a great day ahead!")
            print("Thanks for choosing this Library. Have a great day ahead!")
            with open('list_of_books.txt', 'w') as f:
                f.write('\n'.join(library.books))
            break
        else:
            print("Invalid Choice!")
