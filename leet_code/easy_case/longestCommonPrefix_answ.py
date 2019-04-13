class Solution:
    def longestCommonPrefix(self, strs: "List[str]") -> "str":
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        prefix, chars = "", zip(*strs)
        print("zip(*strs):", chars)
        print("enumerate(chars):", enumerate(chars))
        for i, group in enumerate(chars):
            ch = group[0]
            for j in range(1, len(group)):
                if group[j] != ch:
                    return prefix
            print("prefix:", prefix)
            prefix += strs[0][i]
        return prefix


if __name__ == "__main__":
    a = Solution()
    s = ["flower", "flow", "flight"]
    s1 = ["a"]
    s2 = ["aaa", "aa", "aaa"]
    a.longestCommonPrefix(s)
