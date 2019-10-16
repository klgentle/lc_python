import re


def test_re_search(test_str: str):
    if re.search(
        r"(\w*.)?M\s*=\s*(')?1(')?\s*AND\s+(\w*.)?S\s*=\s*(')?1(')?",
        test_str,
        flags=re.IGNORECASE,
    ):
        print("find")
    else:
        print("not find")


if __name__ == "__main__":
    # test_re_search("          AND C.M = 1 AND C.S = 1")
    test_re_search("          AND M = '1' AND S = '1'")
