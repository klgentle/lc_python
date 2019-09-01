class Solution:
    """
    solution 1: Brute force
    for each point caculate the water, with left_max, right_max as the two side border.
        left_max = max(height[0:i])
        right_max = max(height[i+1:height_len])
        water = min(left_max, right_max) - bar_height
    """
    def trap(self, height: List[int]) -> int:
        water_sum = 0
        height_len = len(height)


        left_max = 0
        right_max = 0
        for i, bar_height in enumerate(height):

            if i != 0:
                left_max = max(height[i-1],left_max)

            if i != height_len-1:
                right_max = max(height[i+1:height_len])
            else:
                right_max = 0

            #print(f"i:{i}")
            #print(f"left_max:{left_max}")
            #print(f"right_max:{right_max}")
            water = min(left_max, right_max) - bar_height
            #print(f"water:{max(water,0)}")
            water_sum += max(water,0)

        return water_sum
