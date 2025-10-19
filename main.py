from stats import get_word_count, get_count_chars, sort_count
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book =get_book_text(filepath)
    wc = get_word_count(book)
    char_count = get_count_chars(book)
    sorted_list = sort_count(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("-------- Word Count --------")
    print(f"Found {wc} total words")
    print("-------- Character Count --------")
    for item in sorted_list:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")


main()
