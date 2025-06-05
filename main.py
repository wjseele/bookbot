from stats import get_num_words
from stats import get_num_chars
from stats import sort_list
import sys

def get_book_text(file_path):
    with open(file_path) as file:
        file_contents = file.read()
        return file_contents

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_to_read = sys.argv[1]
    
    book_text = get_book_text(book_to_read)
    num_words = get_num_words(book_text)
    char_count = get_num_chars(book_text)
    sorted_list = sort_list(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_to_read}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for letters in range(0, len(sorted_list)):
        char = sorted_list[letters]["char"]
        num = sorted_list[letters]["num"]
        if char.isalpha():
            print(f"{char}: {num}")

    print("============= END ===============")

main()
