class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        
        while start < end:
            print("1", s[start], "2", s[end])
            if ord(s[start].lower()) >= ord('a') and ord(s[start].lower()) <= ord('z') or ord(s[start]) >= ord("0") and ord(s[start]) <= ord("9"):
                if ord(s[end].lower()) >= ord("a") and ord(s[end].lower()) <= ord("z")or ord(s[end]) >= ord("0") and ord(s[end]) <= ord("9"):
                    if s[start].lower() != s[end].lower():
                        return False
                    start += 1
                    end -= 1
                else:
                    end -= 1
            else:
                start += 1
                
        return True

if __name__ == "__main__":
    obj = Solution()
    
    print(obj.isPalindrome("0P"))