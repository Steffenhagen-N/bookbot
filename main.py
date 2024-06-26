def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    character_count = get_character_count(text)

    print("")
    print(f"--- Begin report for {book_path} ---")
    print("")
    print("\033[36m" f"{word_count:,} " "\033[0m" "words found in text")
    print("")
    for character in character_count:
        print("The " "\033[32m" f"{character} " "\033[0m" "character "
              "was found " "\033[36m" 
              f"{character_count[character]:,} " "\033[0m" "times")
    print("")
    print("--- End report ---")

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
            if letter.isalpha():
                if letter in char_dic:
                    char_dic[letter] += 1
                else:
                    char_dic[letter] = 1

    sorted_dictionary = dict(sorted(char_dic.items(), key=lambda x: x[1], reverse=True))
    return sorted_dictionary
    


main()