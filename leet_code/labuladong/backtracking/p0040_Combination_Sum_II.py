40. Combination Sum II
"""
Medium

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]

"""


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if min(candidates) > target:
            return []
        if sum(candidates) < target:
            return []
        
        self.res = []
        self.backtrace(sorted(candidates), target, [], 0)
        return self.res
    
    
    def backtrace(self, cands, target, path, index):
        if target < 0:
            return
        if target == 0:
            self.res.append(path)
            return
        for i in range(index,len(cands)):
            # pass duplicate value
            if i > index and cands[i] == cands[i-1]:
                continue
            if cands[i] > target:
                break
            # i + 1: number only be used once
            self.backtrace(cands, target - cands[i], path+[cands[i]], i+1)
