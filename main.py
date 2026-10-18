from books import show_books, save_books, load_books
from dotenv import load_dotenv
import os

load_dotenv()

name = input("Please enter your name: ")
print("welcome", name)

admin_mode = input("Do you want to enter admin mode? (yes/no) ")

if admin_mode == "yes":
    password = input("Enter admin password: ")
    if password == os.getenv("BOOK_MANAGER_ADMIN_PASSWORD"):
        print("admin mode activated")
    else:
        print("wrong password")

count = int(input("How many books do you want to add? "))

books_list = load_books()

for i in range(count):
    book_name = input("Please enter your book's name: ")
    books_list.append(book_name)

show_books(books_list)
save_books(books_list)