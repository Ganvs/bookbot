from stats import get_num_words, get_character_count, get_sorted_character_list

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    return null

def main():
    file_path = "./books/frankenstein.txt"
    book_text = get_book_text(file_path)
    word_count = get_num_words(book_text)
    char_count = get_character_count(book_text)
    sorted_char = get_sorted_character_list(char_count)

    print(f"""
============ BOOKBOT ============
Analyzing book found at {file_path}
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------
{sorted_char}
""")

main()