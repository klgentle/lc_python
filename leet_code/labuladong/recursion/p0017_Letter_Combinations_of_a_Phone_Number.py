"""
17. Letter Combinations of a Phone Number
Medium

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:

Input: digits = ""
Output: []

Example 3:

Input: digits = "2"
Output: ["a","b","c"]
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        self.res = []
        self.map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"] }

        if len(digits) == 1:
            return self.map.get(digits)
        else:
            self.res = self.map.get(digits[0])
            self.recursion(digits[1:])

        return self.res


    def recursion(self, digits):
        if not digits:
            return []

        res = []
        for i in self.res:
            for j in self.map[digits[0]]:
                res.append("".join([i,j]))
        self.res = res

        return self.recursion(digits[1:])
