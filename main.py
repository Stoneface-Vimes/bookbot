def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def get_number_of_words(text):
    number_of_words = text.split()
    return len(number_of_words)

def main():
    book_text = get_book_text("books/frankenstein.txt")
    # print(book_text)
    print(f"Found {get_number_of_words(book_text)} total words")
    
main()