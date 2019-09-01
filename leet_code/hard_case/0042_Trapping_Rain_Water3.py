class Solution:
    # danamic use to cycle
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        sum_water = 0
        height_len = len(height)
        left_max = [height[0]] * height_len
        right_max = [height[-1]] * height_len
        water = [0] * height_len
        
        for i in range(1, height_len):
            left_max[i] = max(left_max[i-1], height[i])
            
        for i in range(height_len-2, -1, -1):
            # from max to min, init max index first, use max index, not min
            right_max[i] = max(right_max[i+1], height[i])
            water[i] = min(right_max[i], left_max[i]) - height[i]
            
        water[-1] = min(right_max[-1], left_max[-1]) - height[-1]
        return sum(water)
