class Solution:
    def trap(self, height: List[int]) -> int:
        cur_left_to_right_max = 0
        prev_left_to_right_max = []
        for block in height:
            prev_left_to_right_max.append(cur_left_to_right_max)
            cur_left_to_right_max = max(cur_left_to_right_max, block)
        cur_right_to_left_max = 0
        prev_right_to_left_max = []
        for block in reversed(height):
            prev_right_to_left_max.append(cur_right_to_left_max)
            cur_right_to_left_max = max(cur_right_to_left_max, block)
        prev_right_to_left_max = list(reversed(prev_right_to_left_max))
        water_height = [
            max(0, min(
                prev_left_to_right_max[i]-height[i], 
                prev_right_to_left_max[i]-height[i]
        )) for i in range(len(height))]
        return sum(water_height)
