path = "books/frankenstein.txt"


def count_words(text):
    return len(text.split())


def count_letters(text):
    dic = {}
    for i in range(len(text)):
        c = text[i].lower()
        if c in dic.keys():
            dic[c] += 1
        else:
            dic[c] = 0

    return dic


def main():
    with open(path) as f:
        file_contents = f.read()

    char_dic = count_letters(file_contents)

    print(f"--- Begin report of book {path} ---")
    print(f"{count_words(file_contents)} words found in the document\n")

    sorted_char_list = sorted(
        [x for x in char_dic.items() if x[0].isalpha()],
        key=lambda x: x[1],
        reverse=True,
    )

    for x in sorted_char_list:
        print(f"The '{x[0]}' character was found {x[1]} times")

    print("\n--- End report ---")


main()
