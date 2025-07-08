class Solution:
    def scoreOfString(self, s: str) -> int:
        score, i = 0, 1
        curr_score = ord(s[0])
        while i < len(s):
            adj_score = abs(ord(s[i]) - ord(s[i - 1]))
            score += adj_score  
            i += 1  
        
        return score
    
    
    
if __name__ == "__main__":
    obj = Solution()
    
    print(obj.scoreOfString("hello"))