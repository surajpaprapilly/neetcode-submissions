class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + "#" + s
        return encoded_string


    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s)-1:
            j = i
            while s[j] != "#": # e.g 5#Hello5#World, 
                j += 1         #     0123456789
            num_str = ""
            for k in range(i,j):
                num_str += s[k]
            num_int = int(num_str)
            decoded.append(s[j+1:j+num_int+1])
            i = j + num_int + 1
        return decoded

# strs=["we","say",":","yes","!@#$%^&*()"]
# solution = Solution()
# encoded_string = solution.encode(strs);
# decoded_strs = solution.decode(encoded_string);
