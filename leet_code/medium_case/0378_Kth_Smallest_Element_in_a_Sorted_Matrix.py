import heapq


class Solution:
    def kthSmallest(self, matrix: list, k: int) -> int:
        length = len(matrix)
        counter = 0
        ref = []
        
        for i in range(length):
            for j in range(length):
                ref.append(matrix[i][j])
                
        heapq.heapify(ref)
        for i in range(k):
            result = heapq.heappop(ref)
        print(result)
        return result


if __name__ == '__main__':
    a = Solution()
    mat =[[1,5,9],[10,11,13],[12,13,15]]
    k =8 
    a.kthSmallest(mat,k)
