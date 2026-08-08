class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() # [-4,-1,-1,0,1,2]
        for i, num in enumerate(nums):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if num + nums[l] + nums[r] > 0:
                    r -= 1
                elif num + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    res.append([num,nums[l],nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                            l += 1
            
        return res
        


        









        