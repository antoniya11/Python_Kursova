class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        print(f"{self.title} - {self.author} ({self.year})")

    def is_old(self):
        return self.year < 2000