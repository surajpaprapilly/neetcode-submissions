class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = {c for c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'}
        left_pointer = 0
        right_pointer  = len(s) - 1
        
        while left_pointer <= right_pointer:
            left_pointer_has_alpn = s[left_pointer] in alphanumeric
            right_pointer_has_alpn = s[right_pointer] in alphanumeric
            if not left_pointer_has_alpn:
                left_pointer += 1
            if not right_pointer_has_alpn:
                right_pointer -= 1
            if left_pointer_has_alpn and right_pointer_has_alpn:
                if s[left_pointer].lower() == s[right_pointer].lower():
                    left_pointer += 1
                    right_pointer -=1
                else:
                    return False
        return True
            
        