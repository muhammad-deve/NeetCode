class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            while left < right and not self.isAlnum(s[left]):
                left += 1
            
            while left < right and not self.isAlnum(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True
    
    def isAlnum(self, ch) -> bool:
        if (ord('a') <= ord(ch) <= ord('z')) or (ord('A') <= ord(ch) <= ord('Z')) or (ord('0') <= ord(ch) <= ord('9')):
            return True
        
        return False
    