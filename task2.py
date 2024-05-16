class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def __str__(self):
        return f"Название: {self.title}\nАвтор: {self.author}\nГод: {self.year}\nЖанр: {self.genre}\n"

    def change_genre(self, new_genre):
        self.genre = new_genre
        print(f"Жанр книги изменен на: {self.genre}")

# Создаем объект класса Book
book = Book("Оно", "Стивен Кинг", 1966, "Ужасы")

# Выводим информацию о книге до изменения жанра
print("Информация о книге до изменения жанра:")
print(book)

# Изменяем жанр книги
book.change_genre("Классика")

# Выводим информацию о книге после изменения жанра
print("Информация о книге после изменения жанра:")
print(book)
