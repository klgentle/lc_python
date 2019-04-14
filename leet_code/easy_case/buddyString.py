class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        duplicate = False
        la = len(A)
        if la != len(B) or set(A) != set(B):
            return False
        if len(set(A)) < la:
            duplicate = True
        if duplicate and A == B:
            return True

        diff_list = []
        for i in range(0, la):
            if A[i] != B[i]:
                diff_list.append(i)
        if len(diff_list) != 2:
            return False
        j, k = diff_list[0], diff_list[1]
        return A[j] == B[k] and A[k] == B[j]
