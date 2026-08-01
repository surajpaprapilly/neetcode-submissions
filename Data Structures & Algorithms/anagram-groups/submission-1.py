class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. sort the string
        # 2. if the sorted string appears in the dictionary then append the string to the list
        # 3. Else add the string to a list and have that as the value, where key is sorted string
        anagram_dict = {}
        final_ls = []
        for string in strs:
            sorted_str = ''.join(sorted(string))
            if sorted_str in anagram_dict:
                ls = anagram_dict[sorted_str]
                ls.append(string)
                anagram_dict[sorted_str] = ls
            else:
                anagram_dict[sorted_str] = [string]
        
        for key,value in anagram_dict.items():
            final_ls.append(value)
        return final_ls

            
        
            
        