def get_number_of_words(text):
    number_of_words = text.split()
    return len(number_of_words)

def num_of_chars(text):
    letter_count = {}
    for letter in text:
        if letter.lower() in letter_count:
            letter_count[letter.lower()] += 1
        else:
            letter_count[letter.lower()] = 1
    return letter_count