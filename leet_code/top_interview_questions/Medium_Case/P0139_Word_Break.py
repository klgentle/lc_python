class Solution:
    def wordBreak(self, s, words):
        # ok[i] tells whether s[:i] can be built.
        ok = [True]
        for i in range(1, len(s)+1):
            ok += any(ok[j] and s[j:i] in words for j in range(i)),
        #print(ok)
        return ok[-1]

