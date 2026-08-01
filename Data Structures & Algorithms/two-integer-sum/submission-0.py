class Solution:
    def twoSum(self, nums: List[int], target: int):
        a =[]
        for i in range(len(nums)):
            for s in range(i+1,len(nums)):
                print("i is: ", i ," and s is: ", s)
                if (nums[i] + nums[s] == target) and (i!=s):
                    print(i)
                    print(s)
                    return [i,s]
                
            
        