def get_book_text(file_path):
    with open(file_path) as file:
        file_contents = file.read()
        return file

def main():
    book_to_read = "books/frankenstein.txt"
    book_text = get_book_text(book_to_read)
    print(book_text)
