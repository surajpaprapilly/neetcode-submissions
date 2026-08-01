class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        mapS = {}
        # {'r':2,'a':2,'c':2,'e':1}
        #{'b':2,'c':2}
        if len(s) != len(t):
            return False
    
        for letter in s:
            if letter in mapS:
                mapS[letter] += 1
            else:
                mapS[letter] = 1
        
        mapT = {}
        for char in t:
            if char not in mapS:
                return False
            if char in mapT:
                if mapT[char] + 1 > mapS[char]:
                    return False
                mapT[char] += 1
            else:
                mapT[char] = 1 
        return True 
        