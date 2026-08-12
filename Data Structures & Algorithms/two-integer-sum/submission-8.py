class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_set = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums_set.keys():
                return [nums_set[complement],i]
            if nums[i] in nums_set.keys():
                continue
            else:
                nums_set[nums[i]] = i
        