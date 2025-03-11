from stats import get_number_of_words
from stats import get_number_of_characters
from stats import sort_character_by_count
import sys 

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_path = sys.argv[1]

def get_book_text(filepath):
    
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    book_text = get_book_text(book_path)
    word_count = get_number_of_words(book_text)
    char_count = get_number_of_characters(book_text)
    sorted_list = sort_character_by_count(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path} ...")
    print("----------- Word Count ----------") 
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    ## Print each character and count from the sorted list
    for char_dict in sorted_list:
        char = char_dict["char"]
        count = char_dict["count"]
        # Only print alphabetic characters
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")

main()
    