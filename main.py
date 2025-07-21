from stats import get_num_words

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    return null

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    print(book_text)

#main()
print(get_num_words(get_book_text("./books/frankenstein.txt")))