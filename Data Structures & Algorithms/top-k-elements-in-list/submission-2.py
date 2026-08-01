class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # [1,2,2,3,3,3] k=2
        # hm = {1:1,2:2,3:3}

        num_to_freq_map = {}
        for num in nums:
            if num in num_to_freq_map:
                num_to_freq_map[num] += 1
            else:
                num_to_freq_map[num] = 1
        
        freq_list = [[] for _ in range(len(nums) + 1)]
        for number,frequency in num_to_freq_map.items():
            freq_list[frequency].append(number)

        res = []
        for i in range(len(freq_list)-1,0,-1):
            for item in freq_list[i]:
                if k == 0:
                    break
                else:
                    res.append(item)
                    k -= 1
        
        return res
                    


                

        