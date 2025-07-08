from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        strs.sort()
        
        min = len(strs[0])
        for i in range(1, len(strs)):
            if len(strs[i]) < min:
                min = len(strs[i])
        
        
        for i in range(min):
             if strs[0][i] != strs[-1][i]:
                return strs[0][:i]
        return strs[0]


if __name__ == "__main__":
    obj = Solution()
    
    print(obj.longestCommonPrefix(strs=["abc","abcde","abcdef"]))