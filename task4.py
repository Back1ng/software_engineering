def load_banned_words(file_path):
    with open(file_path, 'r') as file:
        return set(word.strip().lower() for word in file)

def replace_banned_words(sentence, banned_words):
    for banned_word in banned_words:
        sentence = sentence.replace(banned_word, '*' * len(banned_word))
    return sentence

def main():
    banned_words = load_banned_words('banned_words.txt')
    sentence = "Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!!"
    replaced_sentence = replace_banned_words(sentence.lower(), banned_words)
    print(replaced_sentence)

if __name__ == "__main__":
    main()
