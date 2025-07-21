def get_num_words(content):
    words = content.split()
    num_words = len(words)
    return f"{num_words} words found in the document"