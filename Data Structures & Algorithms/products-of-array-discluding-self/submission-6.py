class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Naive approach: For each index multiply all remaining values O(N^2)
        # Another approach: Multiply all numbers and divide by nums[i]
        # If there is 0 then product of all numbers will be 0 (except the position(s) of 0)

        # If there is 0 then you cannot divide by nums[i] when nums[i] = 0. Handle as special case

        # Pre fix Post fix approach:
        # First pass calculate the prefix sum
        # Second pass multiply by the postfix sum at each index


        prefix_sum = 1
        n = len(nums)
        res = [1] * n
        for i in range(n):
            res[i] = prefix_sum
            prefix_sum *= nums[i]
        
        postfix_sum = 1
        for j in range(n - 1,-1,-1):
            res[j] *= postfix_sum
            postfix_sum *= nums[j]
        return res

# Time complexity: O(N) --> 1 pass for Prefix and 1 pass for Postfix

# Space complexity: O(1) --> Only output array as the additional memory used, which is not counted.







