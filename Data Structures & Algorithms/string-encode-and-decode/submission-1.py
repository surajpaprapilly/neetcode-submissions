class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ''
        for s in strs:
            str_length = len(s)
            output += str(str_length)+ "," + s
        return output
    

    def decode(self, s: str) -> List[str]:
        decoded_str_list = []
        i = 0
        while i < len(s):
            num_of_char_str = s[i]
            decoded_str_section = ""
            while s[i+1] != ",":
                i+=1
                num_of_char_str += s[i]
                
            num_of_char = int(num_of_char_str)

            
            for j in range(i+2,i+1+num_of_char+1):
                decoded_str_section += s[j]
            decoded_str_list.append(decoded_str_section)
            i = i + num_of_char + 2
        return decoded_str_list

            
solution = Solution()
print(solution.encode(["we","say",":","yes","!@#$%^&*()"]))

