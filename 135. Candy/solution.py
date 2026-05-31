class Solution:
    def candy(self, ratings: List[int]) -> int:
        left_to_right_longest_increasing_subarrays = [0]
        current_longest_left_to_right_increasing_subarray = 0
        right_to_left_longest_increasing_subarrays = [0]
        current_longest_right_to_left_increasing_subarray = 0
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                current_longest_left_to_right_increasing_subarray += 1
            else:
                current_longest_left_to_right_increasing_subarray = 0
            if ratings[len(ratings) - 1 - i] > ratings[len(ratings) - i]:
                current_longest_right_to_left_increasing_subarray += 1
            else:
                current_longest_right_to_left_increasing_subarray = 0
            left_to_right_longest_increasing_subarrays.append(
                current_longest_left_to_right_increasing_subarray
            )
            right_to_left_longest_increasing_subarrays.append(
                current_longest_right_to_left_increasing_subarray
            )
        right_to_left_longest_increasing_subarrays.reverse()
        total_candies = 0
        for i in range(len(left_to_right_longest_increasing_subarrays)):
            total_candies += 1 + max(
                left_to_right_longest_increasing_subarrays[i], 
                right_to_left_longest_increasing_subarrays[i]
            )
        return total_candies
