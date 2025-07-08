class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(k):
            l = 0
            r = len(k) - 1
            
            while l < r:
                if k[l] != k[r]:
                    return False
                l += 1
                r -= 1
            
            return True
        
        if isPalindrome(s):
            return True
        
        for i in range(0, len(s)):
            res = isPalindrome(s[:i] + s[i+1:])
            
            if res:
                return True
        
        return False


if __name__ == "__main__":
    obj = Solution()
    
    print(obj.validPalindrome(s = "abbad"))