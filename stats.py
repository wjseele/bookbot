def get_num_words(book_text):
    words = book_text.split()
    return len(words)

def get_num_chars(book_text):
    lower_book_text = book_text.lower()
    char_count = {}
    for char in lower_book_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(dict):
    return dict["num"]

def sort_list(char_count):
    sorted_char_count = []

    for char in char_count:
        sorted_char_count.append(
            {"char": char, "num": char_count[char]}
        )

    sorted_char_count.sort(reverse=True, key=sort_on)
    return sorted_char_count
