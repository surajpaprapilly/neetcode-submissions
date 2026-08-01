class Solution:
    def twoSum(self, nums: List[int], target: int):
        
        dictionary = {}
        for index, num in enumerate(nums):
            to_be_found = target - num
            if to_be_found in dictionary:
                return [dictionary[to_be_found],index]
            dictionary[num] = index

        

                
            
        