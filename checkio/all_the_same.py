from typing import List, Any


def all_the_same1(elements: List[Any]) -> bool:
    """
    https://py.checkio.org/mission/all-the-same/publications/add/
    """
    # your code here
    if not elements:
        return True

    return len(set(elements)) == 1

def all_the_same(elements: List[Any]) -> bool:
    return elements[1:] == elements[:-1]


if __name__ == "__main__":
    print("Example:")
    print(all_the_same([1, 1, 1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(["a", "a", "a"]) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
