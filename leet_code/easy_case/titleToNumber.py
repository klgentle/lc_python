class Solution:
    def titleToNumber(self, s: str) -> int:
        ret = 0
        i = 0
        l = len(s)
        while i < l:
            #ret += 1
            ret += ord(s[i]) - ord('A') +1
            if i < l-1:
                ret *= 26
            i += 1
            
        print(f's:{s}, ret:{ret}')
        return ret


if __name__ == '__main__':
    c = Solution()
    c.titleToNumber("A")
    c.titleToNumber("AA")
    c.titleToNumber("ZY")
