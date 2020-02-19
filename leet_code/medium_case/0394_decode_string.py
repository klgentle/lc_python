class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curString = ""
        curNum = 0

        for c in s:
            if c.isdigit():
                curNum = curNum * 10 + int(c)
            elif c == "[":
                stack.append(curString)
                stack.append(curNum)
                curString = ""
                curNum = 0
            elif c == "]":
                num = stack.pop()
                preString = stack.pop()
                curString = preString + curString * num
            else:
                curString += c

        print("out:", curString)
        return curString


a = Solution()
s = "3[a2[c]]"
print("input:", s)
a.decodeString(s)
