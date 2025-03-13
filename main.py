from stats import num_words, get_num_character, sort

def main():
    book = get_book_text("books/frankenstein.txt")

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")


    number = num_words(book)
    print("----------- Word Count ----------")
    print(f"{number} words found in the document")


    char_count = get_num_character(book)
    sorted_list = sort(char_count)
    print("--------- Character Count -------")
    for item in sorted_list:
        char = item["char"]
        count = item['count'] 
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        file_string = f.read()
        return file_string



main()