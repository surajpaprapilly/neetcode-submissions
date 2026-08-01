class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        zeros = 0
        for num in nums:
            if num == 0:
                zeros +=1
                continue
            total_product = total_product * num
        res = []
        for num in nums:
            if zeros == 1:    
                if num == 0:
                    res.append(total_product//1)
                else:
                    res.append(0)
            elif zeros >= 2:
                res.append(0)
            else:
                res.append(total_product//num)

        return res

        