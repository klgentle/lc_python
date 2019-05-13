import pysnooper

class Solution:
    @pysnooper.snoop()
    def generate(self, numRows: int) -> list:
        if not numRows:
            return []
        ret = [[1],[1,1]]
        for j in range(2,numRows):
            row = [1]
            last_list = ret[-1]
            print(f"len(last_list):{len(last_list)}")
            for i in range(1,len(last_list)):
                row.append(last_list[i-1]+last_list[i])
            ret.append(row + [1])
        print(f"ret:{ret}")
        return ret


if __name__ == "__main__":
    a = Solution()
    a.generate(5)
