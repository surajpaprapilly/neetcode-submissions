class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_seq_len = 0
        for num in nums:
            if num - 1 not in nums_set:
                num_in_seq = num
                seq_len = 1
                while num_in_seq + 1 in nums_set:
                    seq_len += 1
                    num_in_seq += 1
                max_seq_len = max(seq_len,max_seq_len)
        return max_seq_len

