"""
990. Satisfiability of Equality Equations
Medium

Given an array equations of strings that represent relationships between variables, each string equations[i] has length 4 and takes one of two different forms: "a==b" or "a!=b".  Here, a and b are lowercase letters (not necessarily different) that represent one-letter variable names.

Return true if and only if it is possible to assign integers to variable names so as to satisfy all the given equations.

 

Example 1:

Input: ["a==b","b!=a"]
Output: false
Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.  There is no way to assign the variables to satisfy both equations.

Example 2:

Input: ["b==a","a==b"]
Output: true
Explanation: We could assign a = 1 and b = 1 to satisfy both equations.

Example 3:

Input: ["a==b","b==c","a==c"]
Output: true

Example 4:

Input: ["a==b","b!=c","c==a"]
Output: false

Example 5:

Input: ["c==c","b==d","x!=z"]
Output: true
"""


import string


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def find(x):
            if x != uf[x]:
                uf[x] = find(uf[x])
            return uf[x]
        uf = {x:x for x in string.ascii_lowercase}
        for a, c, _, b in equations:
            if c == "=":
                uf[find(a)] = find(b)

        return not any(c == "!" and find(a) == find(b) for a, c, _, b in equations)
