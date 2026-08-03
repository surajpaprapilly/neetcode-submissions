class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Map number to frequency
        # 2. Each index of a list stores the number where index = frequency
        # 3. Iterate through this list from the back until length of result list is = k

        num_to_freq = {}
        freq_list = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            num_to_freq[num] = 1 + num_to_freq.get(num,0)

        for num, freq in num_to_freq.items():
            freq_list[freq].append(num)


        res = []
        for i in range(len(nums), 0, -1):
            for n in freq_list[i]:
                res.append(n)
                if len(res) == k:
                    return res


        