class Solution:
    def twoSum(self, nums: List[int], target: int):
        
        dictionary = {}
        for index, num in enumerate(nums):
            dictionary[num] = index 
        for idx in range(len(nums)):
            to_be_found = target - nums[idx]
            if to_be_found in dictionary and idx!= dictionary[to_be_found]:
                return [idx, dictionary[to_be_found]]
        

                
            
        