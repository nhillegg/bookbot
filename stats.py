def num_words(book):
    words = book.split()
    word_count = len(words)
    return word_count

def get_num_character(book):
    char_count = {}
    for char in book:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1

        else:
            char_count[char] = 1
    return char_count