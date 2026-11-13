class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __eq__(self, other):
        return self.author == other.author and self.title == other.title

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return self.num_pages + other.num_pages

    def __contains__(self, item):
        return item in self.title or item in self.author

    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "pages":
            return self.num_pages
        else:
            return f"Key '{key}' not found"

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter", "J.K. Rowling", 233)
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S Lewis", 172)

print(book3)
print(book1 == book2)
print(book2 < book3)
print(book3 > book1)
print(book1 + book2)
print("Lion" in book3)
print(book1["title"])
print(book2["author"])
print(book3["pages"])
print(book1["key"])
