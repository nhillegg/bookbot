from stats import num_words, get_num_character

def main():
    book = get_book_text("books/frankenstein.txt")
    number = num_words(book)
    print(f"{number} words found in the document")
    print (get_num_character(book))

def get_book_text(path):
    with open(path) as f:
        file_string = f.read()
        return file_string



main()