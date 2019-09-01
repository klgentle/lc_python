class Solution:
    # danamic
    def trap(self, height: List[int]) -> int:
        water_sum = 0
        height_len = len(height)
        left_max = 0
        right_max = 0
        
        if not height:
            return 0
        
        left_max_list = [height[0]] * height_len
        right_max_list = [height[-1]] * height_len
        for i in range(1, height_len):
            left_max_list[i] = max(left_max_list[i-1], height[i])

        for i in range(height_len-2, -1, -1):
            right_max_list[i] = max(right_max_list[i+1], height[i])

        for i in range(height_len):
            water_sum += min(left_max_list[i], right_max_list[i]) - height[i]
            
        return water_sum
