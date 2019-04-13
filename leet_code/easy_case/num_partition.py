from collections import Counter


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) <= 1 or len(deck) > 26:
            return False
        a = Counter(deck).most_common()
        num_list = [i[1] for i in a]
        num_list.sort()
        print("num_list:", num_list)
        if len(set(num_list)) == 1 or num_list in (
            [2, 4],
            [4, 6],
            [3, 3, 3],
            [4, 8],
            [2, 6],
            [2, 8],
            [2, 10],
        ):

            x = set(num_list)
            print("X: ", x)
            return True
        return False

    # num_list 满足 2， 3，5，7，9的倍数，元素全部满足就可以
