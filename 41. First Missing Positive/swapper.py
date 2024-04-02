class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            cur_val = nums[i]
            if cur_val is None or cur_val < 1 or cur_val > len(nums):
                nums[i] = None
                i += 1
            elif cur_val == i + 1:
                i += 1
            else:
                if nums[cur_val-1] == cur_val:
                    nums[i] = None
                else:
                    nums[i] = nums[cur_val-1]
                    nums[cur_val-1] = cur_val
        j = 0
        while j < len(nums):
            if nums[j] != j + 1:
                return j+1
            j += 1
        return j+1
