def get_num_words(file_contents):
    num_words = len(file_contents.split())
    print(f"Found {num_words} total words")
    

def get_num_letters(file_contents):
    num_letters = {}
    file_contents = file_contents.lower()
    for letter in file_contents:
        if letter in num_letters:
            num_letters[letter] += 1
        else:
            num_letters[letter] = 1
    return num_letters


def list_from_dict(dict):
    list_from_dict = [{"char": key, "num": value} for key, value in dict.items()]
    return list_from_dict


def sort_on(dict):
    return dict["num"]