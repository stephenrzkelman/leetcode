class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        remaining_nums = list(range(1,n+1))
        permutation = ""
        while remaining_nums:
            next_num = (k-1)//math.factorial(len(remaining_nums)-1)
            k = k % math.factorial(len(remaining_nums)-1)
            permutation += str(remaining_nums.pop(next_num))
        return permutation
