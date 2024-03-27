class Solution:
    def singleArrayMedian(self, nums):
        if len(nums) % 2 == 1:
            return nums[len(nums)//2]
        else:
            return (nums[len(nums)//2] + nums[len(nums)//2-1])/2

    def unbalanceArrays(self, nums1, nums2):
        if len(nums1) != len(nums2):
            return nums1, nums2
        else:
            if nums1[-1] >= nums2[-1]:
                nums2.append(nums1[-1])
                return nums1[:-1], nums2
            else:
                nums1.append(nums2[-1])
                return nums1, nums2[:-1]

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if(len(nums1) == 0):
            return self.singleArrayMedian(nums2)
        elif(len(nums2) == 0):
            return self.singleArrayMedian(nums1)
        nums1, nums2 = self.unbalanceArrays(nums1,nums2)
        if(len(nums1) == 0):
            return self.singleArrayMedian(nums2)
        elif(len(nums2) == 0):
            return self.singleArrayMedian(nums1)
        long_nums = nums1 if len(nums1) > len(nums2) else nums2
        short_nums = nums2 if len(nums1)> len(nums2) else nums1
        overall_length = (len(long_nums) + len(short_nums))
        overall_midpoint = overall_length//2
        left = 0
        right = len(short_nums)
        mid = (left + right)//2
        while(left + 1 < right):
            if(short_nums[mid] < long_nums[overall_midpoint - mid - 1]):
                left = mid
                mid = (left + right)//2
            elif(short_nums[mid-1] > long_nums[overall_midpoint - mid]):
                right = mid
                mid = (left + right)//2
            else:
                if overall_length%2 == 1:
                    return min(short_nums[mid], long_nums[overall_midpoint-mid])
                else:
                    upper_median = min(short_nums[mid], long_nums[overall_midpoint-mid])
                    lower_median = max(short_nums[mid-1], long_nums[overall_midpoint-mid-1])
                    return (lower_median + upper_median)/2
        if(short_nums[left] >= long_nums[overall_midpoint - left - 1]):
            if overall_length % 2 == 1:
                return min(short_nums[left], long_nums[overall_midpoint - left])
            else:
                upper_median = min(short_nums[left], long_nums[overall_midpoint - left])
                lower_median = long_nums[overall_midpoint - left - 1] if left == 0 else max(long_nums[overall_midpoint - left - 1], short_nums[left - 1])
                return (lower_median + upper_median)/2
        else:
            if overall_length % 2 == 1:
                if left + 1 < len(short_nums):
                    return min(short_nums[left + 1], long_nums[overall_midpoint - left - 1])
                else:
                    return long_nums[overall_midpoint - left - 1]
            else:
                upper_median = long_nums[overall_midpoint - left - 1] if left + 1 == len(short_nums) else min(long_nums[overall_midpoint - left - 1], short_nums[left + 1])
                lower_median = max(short_nums[left], long_nums[overall_midpoint - left - 2])
                return (lower_median + upper_median)/2

        
        
