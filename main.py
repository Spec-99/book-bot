def get_book_text(filepath):
    
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    
def get_number_of_words(text):
    return len(text.split())

def main():
    path = "books/frankenstein.txt"
    book_text = get_book_text(path)
    word_count = get_number_of_words(book_text)
    print(f"{word_count} words found in the document")

main()
    