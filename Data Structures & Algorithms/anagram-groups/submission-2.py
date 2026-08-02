class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. encode the frequency of each characters in a list e.g. eat -> 1 e, 1 a, 1 t. Use this as the key
        # 2. Append the string to the value of the key (which is a list)
        # 3. Return the values.

        anagram_dict = defaultdict(list)

        for s in strs:
            freq_list = [0] * 26
            for c in s:
                idx = ord(c) - ord("a")
                freq_list[idx] += 1
            anagram_dict[tuple(freq_list)].append(s)
        return list(anagram_dict.values())
        