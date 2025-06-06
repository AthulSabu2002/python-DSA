from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m = 0
        l, r = 0, len(heights) - 1
        
        while l < r:
            m = max(min(heights[l], heights[r]) * (r - l), m)
            
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return m
    
if __name__ == "__main__":
    obj = Solution()
    
    print(obj.maxArea([1,7,2,5,4,7,3,6]))