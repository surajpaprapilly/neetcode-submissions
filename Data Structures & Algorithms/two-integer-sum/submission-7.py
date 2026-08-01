class Solution:
    def twoSum(self, nums: List[int], target: int):
        nums_to_index = dict()
        for i,num in enumerate(nums):
            complement = target - num
            if complement in nums_to_index:
                return [nums_to_index[complement],i]
            nums_to_index[num] = i



        

        

                
            
        