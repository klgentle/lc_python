class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False

        lb = {"(": ")", "[": "]", "{": "}"}
        queue = []
        for x in s:
            if x in lb:
                queue.append(x)
            else:
                if len(queue) == 0:
                    return False
                top = queue.pop()
                if lb[top] != x:
                    return False

        return len(queue) == 0
