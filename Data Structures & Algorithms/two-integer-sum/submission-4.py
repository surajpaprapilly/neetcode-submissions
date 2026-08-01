class Solution:
    def twoSum(self, nums: List[int], target: int):

        num_to_index_hm = {}

        for index, num in enumerate(nums):
            remaining = target - num
            if remaining in num_to_index_hm:
                return [num_to_index_hm[remaining], index]
            num_to_index_hm[num] = index

        

                
            
        