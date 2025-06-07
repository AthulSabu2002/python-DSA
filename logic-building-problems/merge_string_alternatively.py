class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        
        n = min(len(word1), len(word2))
        i = 0
        
        while(i < n):
            res += (word1[i])
            res += (word2[i])

            i += 1
        
        if (len(word1) < len(word2)):
            res += (word2[n:])
        else:
            res += (word1[n:])
            
        return res
    
if __name__ == "__main__":
    obj = Solution()
    
    print(obj.mergeAlternately(word1 = "abc", word2 = "xyz"))