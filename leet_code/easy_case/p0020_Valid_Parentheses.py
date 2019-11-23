from typing import List, Any
from pysnooper import snoop


class Solution:
    @snoop()
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        if len(s) % 2 == 1:
            return False

        pair_bracket = {"(": ")", "{": "}", "[": "]", ")": "(", "}": "{", "]": "["}
        bracket_stock = []
        bracket_stock.append(s[0])

        # bracket put into stock
        for i in range(1, len(s)):
            # is pair, bracket_stock pop
            if bracket_stock and pair_bracket.get(s[i]) == bracket_stock[-1]:
                bracket_stock.pop()
            else:
                bracket_stock.append(s[i])

        if len(bracket_stock) == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    o = Solution()
    s = "()[]{}"
    o.isValid(s)
