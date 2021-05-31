"""
22. Generate Parentheses
Medium

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]
"""


class Solution:
    # 编程要非常注意细节
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self.n = n
        self.backtrace([], 0, 0)
        return self.res


    def backtrace(self, path=[], Open=0, Close=0):
        if len(path) == 2 * self.n:
            self.res.append("".join(path))
            return

        if Open < self.n:
            self.backtrace(path+["("], Open+1, Close)
        if Close < Open:
            self.backtrace(path+[")"], Open, Close+1)



