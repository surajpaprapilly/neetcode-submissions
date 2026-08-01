class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_list = {}
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord("a")] += 1
            if tuple(count) in anagram_list:
                anagram_list[tuple(count)].append(s)
            else:
                anagram_list[tuple(count)] = [s]
        return list(anagram_list.values())
            
        