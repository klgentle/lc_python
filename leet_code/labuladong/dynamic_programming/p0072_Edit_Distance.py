"""
72. Edit Distance
Hard

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

    Insert a character
    Delete a character
    Replace a character

 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
"""


class Solution:
    """"""
    def minDistance(self, word1: str, word2: str) -> int:
        self.memo = {}

        def dp(i, j):
            if (i, j) in self.memo:
                return self.memo[(i, j)]

            # base case
            if i == -1:
                return j + 1
            if j == -1:
                return i + 1

            if word1[i] == word2[j]:
                self.memo[(i, j)] = dp(i-1, j-1)
            else:
                self.memo[(i, j)] = min(
                    dp(i, j-1) + 1,         # insert
                    dp(i-1, j) + 1,         # delete
                    dp(i-1, j-1) + 1        # replace
                )
            return self.memo[(i, j)]

        return dp(len(word1)-1, len(word2)-1)
