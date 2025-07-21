def get_num_words(content):
    words = content.split()
    num_words = len(words)
    return num_words

def get_character_count(content):
    content = content.lower()
    chars = {}

    for c in content:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    
    return chars

def sort_on(items):
    return items["num"]

def get_sorted_character_list(character_count):
    sorted_chars = []

    for c in character_count:
        if c.isalpha():
            sorted_chars.append({
                "char": c,
                "num": character_count[c]
            })
    
    sorted_chars.sort(reverse=True, key=sort_on)

    return sorted_chars


#character_count("gustavoO")