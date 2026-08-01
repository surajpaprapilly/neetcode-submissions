class Solution:
    def twoSum(self, nums: List[int], target: int):
        nums_to_index = dict()
        idx_2 = 0
        idx_1 = 0
        for num in nums:
            if target - num in nums_to_index:
                idx_1 = nums_to_index[target - num]
                return [idx_1,idx_2]
            nums_to_index[num] = idx_2
            idx_2 += 1
        return [idx_1,idx_2]



        

        

                
            
        