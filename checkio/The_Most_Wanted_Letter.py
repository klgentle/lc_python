from collections import Counter


def checkio(text: str) -> str:
    text = text.lower()
    text_list = [i for i in text if i.isalpha()]
    text_count_dict = {}
    for i in text_list:
        if i not in text_count_dict:
            text_count_dict[i] = text_list.count(i)
    count_list = [value for key, value in text_count_dict.items()]
    most_frequent_count = max(count_list)
    most_frequent_letters = [
        key for key, value in text_count_dict.items() if value == most_frequent_count
    ]

    # replace this for solution
    return sorted(most_frequent_letters)[0]


if __name__ == "__main__":
    print("Example:")
    print(checkio("Hello World!"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
