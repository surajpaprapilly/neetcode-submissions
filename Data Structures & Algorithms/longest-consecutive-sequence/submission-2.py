class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        if len(nums) == 0:
            return 0
        else:
            longest_consec_seq_len = 1
            for num in nums:
                left_neighbour = num - 1
                right_neighbour = num + 1
                if left_neighbour not in nums_set and right_neighbour in nums_set:
                    consec_seq_len = 1
                    seq_int = right_neighbour
                    while seq_int in nums_set:
                        consec_seq_len += 1
                        seq_int += 1
                    if consec_seq_len > longest_consec_seq_len:
                        longest_consec_seq_len = consec_seq_len
                else:
                    continue
            return longest_consec_seq_len
