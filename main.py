from stats import get_number_of_words
from stats import num_of_chars

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def main():
    book_text = get_book_text("books/frankenstein.txt")
    # print(book_text)
    print(f"Found {get_number_of_words(book_text)} total words")
    letter_count = num_of_chars(book_text)
    print(letter_count)
main()