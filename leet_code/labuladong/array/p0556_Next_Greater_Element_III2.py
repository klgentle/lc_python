"""
556. Next Greater Element III
Medium

Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.



Example 1:

Input: n = 12
Output: 21

Example 2:

Input: n = 21
Output: -1

"""


class Solution:
    def nextGreaterElement(self, n):
        """ 
        example:
        234157641
        index:
        012345678
        i=5, v=7
        j=5
        5 7641
        6 7541
        """
        digits = list(str(n))
        i = len(digits) - 1
        # find the position to modify i-1 (Turning point)
        while i-1 >= 0 and digits[i] <= digits[i-1]:
            i -= 1
            
        if i == 0: return -1
        
        j = i
        # find the smallest value large than digits[i-1] 
        while j+1 < len(digits) and digits[j+1] > digits[i-1]:
            j += 1
        
        # swap smallest value with turning point
        digits[i-1], digits[j] = digits[j], digits[i-1]
        # reverse the value, to make in order
        digits[i:] = digits[i:][::-1]
        ret = int(''.join(digits))
        
        return ret if ret < 1<<31 else -1
