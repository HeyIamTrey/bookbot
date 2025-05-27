def get_total_words(book):
    total_words = 0
    words = book.split()
    for word in words:
        total_words += 1    
    return total_words

def get_total_char(book):
    total_char = {}
    book = book.lower()
    for char in book:
        if char in total_char:
            total_char[char] += 1
        else:
            total_char[char] = 1
    return total_char

def sorted_char(char):
    # sorted_by_values_desc = dict(sorted(student_scores.items(), key=lambda item: item, reverse=True))
    return dict(sorted(char.items(), key=lambda item: item[1], reverse=True))