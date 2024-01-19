class Library:
    Books = list()
    no_of_books = 0

    def addBooks(self, book_name):
        self.Books.append(book_name)
        Library.no_of_books += 1

    def ShowBooks(self):
        print(self.Books)
        print(f"Total number of books is {self.no_of_books}")


obj = Library()

while True:
    print("-------------------")
    print("0.To Exit")
    print("1.Add Books")
    print("2.Show Books")
    print("-------------------")
    x = int(input("Enter the Choice "))
    match x:
        case 0:
            break
        case 1:
            name = input("Enter the name of book ")
            obj.addBooks(name)
            print("Book Added...")
        case 2:
            print("*******************")
            obj.ShowBooks()
            print("*******************")
