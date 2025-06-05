from stats import get_num_words

def get_book_text(file_path):
    with open(file_path) as file:
        file_contents = file.read()
        return file_contents

def main():
    book_to_read = "books/frankenstein.txt"
    book_text = get_book_text(book_to_read)
    num_words = get_num_words(book_text)
    print(f"{num_words} words found in the document")

main()
