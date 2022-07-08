class library:
    def __init__(self,listfBooks):
        self.books = listfBooks
    def displayAvailableBooks (self):
        print("Books present in this library are: ")
        for book in self.books:
            print("*"+book)
    
    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"you have been issued {bookName} please keep it safe & return it with in 30 day")
            self.books.remove(bookName)
            return True
        else:
            print("sorry, This book is either not available or has already been issued to someone else. please wait until the book is available")
            return False
    def returnBook (self,bookName):
        self.books.append(bookName)
        print("Thanks for returning this book! Hope you enjoyed reading it have a geat day ahead!")

class student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow :")
        return self.book

    def returnBook (self):
        self.book = input("Enter the name of the book you want to return :")
        return self.book

if __name__=="__main__":
    centralibrary = library(["Algorithms","Django","clrs","Python Notes"])
    student = student ()
    #centralibrary.displayAvailableBooks()
    while (True):
        welcomeMsg = '''\n ==== WELCOME TO CENTRAL LIBRARY ====
         please choose an option:

         1. List all the books
         2. Request a books
         3. Add/Return a books
         4. Exit the library'''

        print(welcomeMsg)
        a = int(input("Enter a choice :"))
        if a == 1:
            centralibrary.displayAvailableBooks()
        elif a == 2:
            centralibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing central library have a great day ahead !")
            exit()
        else:
            print("Invalid choice !")