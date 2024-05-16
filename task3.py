class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def display_info(self):
        print(f"Название: {self.title}")
        print(f"Автор: {self.author}")
        print(f"Год: {self.year}")
        print(f"Жанр: {self.genre}")
        print()

    def change_genre(self, new_genre):
        self.genre = new_genre
        print(f"Изменить жанр для: {self.genre}")

class EBook(Book):
    def __init__(self, title, author, year, genre, file_format):
        super().__init__(title, author, year, genre)
        self.file_format = file_format

    def convert_to_format(self, new_format):
        print(f"Конвертация книги в {new_format} формат...")
        self.file_format = new_format
        print("Конвертация завершена.")

    def display_info(self):
        super().display_info()  # Вызываем метод display_info() из родительского класса
        print(f"Формат: {self.file_format}\n")

ebook = EBook("Оно", "", 1925, "Ужасы", "PDF")
ebook.display_info()
ebook.convert_to_format("EPUB")
ebook.display_info()