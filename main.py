import sys
from stats import get_total_words
from stats import get_total_char
from stats import sorted_char

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book = get_book_text(book_path)
    total_words = get_total_words(book)
    total_char = get_total_char(book)
    sorted_chars = sorted_char(total_char)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for char in sorted_chars:
        if char.isalpha():
            print(f"{char}: {sorted_chars[char]}")
    print("============= END ===============")

main()