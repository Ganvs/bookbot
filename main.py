from stats import get_num_words, get_character_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    return null

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    word_count = get_num_words(book_text)
    char_count = get_character_count(book_text)
    print(word_count)
    print(char_count)

main()