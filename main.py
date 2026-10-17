from books import show_books

name = input("Please enter your name: ")
print("welcome", name)

count = int(input("How many books do you want to add? "))

books_list = []

for i in range(count):
    book_name = input("Please enter your book's name: ")
    books_list.append(book_name)

show_books(books_list)