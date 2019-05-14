class Solution:
    """
    # 139
    Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
    """
    def wordBreak(self, s, wordDict:list)->bool:
        if not s:
            return True
        
        breakp = [0]
        
        for i in range(len(s) + 1):
            for j in breakp:
                if s[j:i] in wordDict:
                    breakp.append(i)
                    break
        print(f"breakp: {breakp}")
        return breakp[-1] == len(s)
