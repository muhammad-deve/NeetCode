class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ""
        for c in s:
            if ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9'):
                new_string += c.lower()  # Convert to lowercase for comparison
        
        return new_string == new_string[::-1]