from stats import get_num_words
from stats import get_num_chars
from stats import sort_list

def get_book_text(file_path):
    with open(file_path) as file:
        file_contents = file.read()
        return file_contents

def main():
    book_to_read = "books/frankenstein.txt"
    book_text = get_book_text(book_to_read)
    num_words = get_num_words(book_text)
    char_count = get_num_chars(book_text)
    sorted_list = sort_list(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_to_read}")
    print(f"{num_words} words found in the document")

main()
