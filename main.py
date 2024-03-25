def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    character_count = get_character_count(text)

    print(character_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    return len(text.split())

def get_character_count(text):
    char_dic = {}
    lower_text = text.lower()
    lower_text_words = lower_text.split()
    for word in lower_text_words:
        for letter in word:
            if letter in char_dic:
                char_dic[letter] += 1
            else:
                char_dic[letter] = 1

    return char_dic
    


main()