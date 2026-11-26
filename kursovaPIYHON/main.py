from models import Book

books = [
    Book("Под игото", "Иван Вазов", 1894),
    Book("Бай Ганьо", "Алеко Константинов", 1895),
    Book("Време разделно", "Антон Дончев", 1964),
    Book("Хари Потър", "Дж. К. Роулинг", 2001)
]

print("Всички книги:")

for book in books:
    book.display_info()

print("\nКниги, издадени преди 2000 година:")

for book in books:
    if book.is_old():
        book.display_info()

print("\nКниги, сортирани по година:")

books.sort(key=lambda book: book.year)

for book in books:
    book.display_info()