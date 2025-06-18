import sys
from stats import get_num_words, get_num_letters, list_from_dict, sort_on

def get_book_text(path_to_file):
    with open(path_to_file) as file:
       return file.read()
    

def main():
    try:
        path_to_file = sys.argv[1]
    except:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")

    # path_to_file = "./books/frankenstein.txt"
    file_contents = get_book_text(path_to_file)
    
    get_num_words(file_contents)
    num_letters_dict = get_num_letters(file_contents)
    num_letters_list = list_from_dict(num_letters_dict)
    num_letters_list.sort(reverse=True, key=sort_on)
    
    print("--------- Character Count -------")
    for char in num_letters_list:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']}")
    print("============= END ===============")


if __name__=="__main__":
    main()