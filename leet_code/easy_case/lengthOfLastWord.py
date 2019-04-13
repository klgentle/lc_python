class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lst = s.strip().split(" ")
        print(lst)
        return len(lst[-1]) if bool(lst) else 0


if __name__ == "__main__":
    a = Solution()
    a.lengthOfLastWord("a ")
