import sys
from stats import get_num_words, get_character_count, get_sorted_character_list

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    return null

def main():
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    word_count = get_num_words(book_text)
    char_count = get_character_count(book_text)
    sorted_char = get_sorted_character_list(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for s in sorted_char:
        print(f"{s['char']}: {s['num']}")
    print("============= END ===============")

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()