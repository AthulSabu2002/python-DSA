from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * (2 * len(nums))
        
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i + len(nums)] = nums[i]
        
        return ans
            
            
if __name__ == "__main__":
    obj = Solution()
    
    print(obj.getConcatenation(nums = [1,4,1,2]))