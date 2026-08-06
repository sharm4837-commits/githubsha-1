class Solution:
    def palindromeCheck(self, s):
        return self.helper(s, 0, len(s) - 1)
    
    def helper(self, s, left, right):
        
        if left >= right:
            return True
        
        
        if s[left] != s[right]:
            return False
        
        
        return self.helper(s, left + 1, right - 1)