class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Название: {self.title}\nАвтор: {self.author}\nГод: {self.year}\n"

# Создаем объекты класса Book
book = Book("Оно", "Стивен Кинг", 1966)

# Выводим информацию о книге
print(book)
