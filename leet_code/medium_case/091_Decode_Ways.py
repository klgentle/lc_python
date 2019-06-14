from pysnooper import snoop


class Solution:
    """
    s = '226'
    set[0] = 2
    set[1] = [[2,2],[22]]
    set[2] = [[2,26],[22,6],[2,2,6]]
    """

    @snoop()
    def numDecodings(self, s: str) -> int:
        if not s or int(s) < 1:
            return 0
        elif int(s) < 10:
            return 1

        dic = {}
        for i in range(0, 26):
            dic[str(i)] = chr(ord("A") + i)
        # init and init the first 2
        set = [[]] * len(s)
        print(f"set:{set}")
        set[0] = s[0]
        set[1].append([set[0], s[1]])
        if s[0:2] in dic.keys():
            set[1].append([s[0:2]])

        for i in range(2, len(s)):
            # 上一个结果加一个 or 上上一个加2个： set[i] = set[i-1] + s[i] or set[i-2] + s[i-1:i+1]
            for d in set[i - 1]:
                # 处理单个数字
                # error will change set[i-1] #d.append(s[i])   # d is a list
                new = d + [s[i]]
                if new not in set[i]:
                    set[i].append()

                # 处理两位数的字符
                last = d[-1] + s[i]
                if last in dic.keys():
                    new = d[0:-1] + [new]
                    if new not in set[i]:
                        set[i].append(new)

            print(f"i:{i}")

        print(set)
        return len(set[-1])


if __name__ == "__main__":
    a = Solution()
    s = "1001"
    a.numDecodings(s)
