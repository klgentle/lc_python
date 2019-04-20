#! python3
from collections import Counter
from pprint import pprint


class Solution:
    def findNumberOfLIS(self, nums) -> int:
        # def findNumberOfLIS(self, nums: List[int]) -> int:
        """
        to looking for increase sub set, conside each point of the list, 
        for each point create one increase list, if one element is large than it append it at end,
        if min than it then add it before.
        """
        # questoins:
        # how to put element in the first position of one list? [1] + [2,3] = [1,2,3](lst = nums[i] + lst)
        # special cases1 (equal) [2,2,2]:
        nums_len = len(nums)
        if nums_len == 0:
            return 0
        elif nums_len == 1:
            return 1
        if len(set(nums)) == 1:
            return len(nums)
        # special case2 (decrease) [5,4,3,2,1] TODO
        num2 = []
        # num2 like [[],[],...,[]]
        # initialize
        for i in range(0, len(nums)):
            num2.append([])
        for j in range(0, len(nums)):
            num2[j].append(nums[j])
            for i in range(0, len(nums)):
                if nums[i] < nums[j] and nums[i] < num2[j][0]:
                    num2[j] = [nums[i]] + num2[j]
                if nums[i] > nums[j] and nums[i] > num2[j][-1]:
                    num2[j].append(nums[i])
            # print('end i, num2: ', num2)
        print("num2 _________________:")
        pprint(num2)
        target_list = []
        for i in num2:
            if i not in target_list:
                target_list.append(i)
        print("target_list: ", target_list)
        target_len_list = [len(i) for i in target_list]
        max_len = max(target_len_list)
        count = Counter(target_len_list).most_common()

        # only on when duplicate value in the max_len sub then count duplicate times: TODO
        target_list_long = []
        for i in target_list:
            if len(i) == max_len:
                target_list_long.append(i)
        print("target_list_long: ", target_list_long)
        pop_list = []  # [i[0] for i in target_list_long]
        # to deal with duplicate value
        # return target+to_add


if __name__ == "__main__":
    a = Solution()
    l1 = [1, 2, 4, 3, 5, 4, 7, 2]
    l2 = [1, 1, 1, 2, 2, 2, 3, 3, 3]
    a.findNumberOfLIS(l1)
