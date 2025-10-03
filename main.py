from stats import get_number_of_words
from stats import num_of_chars
from stats import sorted_dict

default_filepath = "books/frankenstein.txt"

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def main(): 
    book_text = get_book_text(default_filepath)
    num_of_words = get_number_of_words(book_text)
    letter_count = num_of_chars(book_text)
    sorted_list = sorted_dict(letter_count)

    print(("============ BOOKBOT ============\n"
        f"Analyzing book found at {default_filepath}...\n"
        "----------- Word Count ----------\n"
        f"Found {num_of_words} total words\n"
        "--------- Character Count -------"))
    
    for i in sorted_list:
        #Only prints alphanumeric values of "char"
        if i["char"].isalpha():
            print(i["char"] + ":", + i["num"])
    

main()