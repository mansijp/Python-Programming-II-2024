class Book:
    def __init__(self, name: str, author: str, genre: str, year: int):
        self.name = name
        self.author = author
        self.genre = genre 
        self.year = year

# -----------------------------
def older_book(book1: Book, book2: Book):
    statement = ''
    if(book1.year < book2.year):
        statement = book1.name + " is older, it was published in " + str(book1.year)
    elif(book2.year < book1.year):
        statement = book2.name + " is older, it was published in " + str(book2.year)
    else:
        statement = book1.name + " and " + book2.name + " were published in " + str(book1.year)
    print(statement)

if __name__ == "__main__":
    python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
    everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
    norma = Book("Norma", "Sofi Oksanen", "crime", 2015)

    older_book(python, everest)
    older_book(python, norma)
