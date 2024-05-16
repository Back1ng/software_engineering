def analyze_text(filename):
    with open(filename, 'r') as file:
        text = file.read()

    letter_count = sum(1 for char in text if char.isalpha())
    word_count = len(text.split())
    line_count = text.count('\n') + 1

    result = f"Файл содержит:\n{letter_count} букв\n{word_count} слов\n{line_count} строк"
    print(result)


if __name__ == "__main__":
    analyze_text('input.txt')
