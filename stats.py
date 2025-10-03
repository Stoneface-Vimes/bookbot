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

def sorted_dict(letter_count):
    unsorted_list = []
    sorted_list = []
    for letter in letter_count:
        unsorted_list.append({"char": letter,
                              "num": letter_count[letter]})
    # Using a lambda function to sort by the list of dicts by each dicts value
    return sorted(unsorted_list, key=lambda char: char["num"], reverse=True)
    
