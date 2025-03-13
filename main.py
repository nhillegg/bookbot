from stats import num_words, get_num_character, sort
import sys
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    elif len(sys.argv) == 2:
        book = get_book_text(sys.argv[1])

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")


    number = num_words(book)
    print("----------- Word Count ----------")
    print(f"Found {number} total words")


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