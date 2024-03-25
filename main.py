def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    #character_count = 

    print(word_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    return len(text.split())

main()

#main()

#I don't understand how any of this works