def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    return null

def words_count(content):
    words = content.split()
    num_words = len(words)
    return f"{num_words} words found in the document"

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    print(book_text)

#main()
print(words_count(get_book_text("./books/frankenstein.txt")))