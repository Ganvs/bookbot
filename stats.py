def get_num_words(content):
    words = content.split()
    num_words = len(words)
    return f"{num_words} words found in the document"

def get_character_count(content):
    content = content.lower()
    chars = {}

    for c in content:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    
    return chars


#character_count("gustavoO")