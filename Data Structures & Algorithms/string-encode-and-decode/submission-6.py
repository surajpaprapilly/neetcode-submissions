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
            j = s.index("#",i)
            num_int = int(s[i:j])
            decoded.append(s[j+1:j+num_int+1])
            i = j + num_int + 1
        return decoded

# strs=["we","say",":","yes","!@#$%^&*()"]
# solution = Solution()
# encoded_string = solution.encode(strs);
# decoded_strs = solution.decode(encoded_string);
