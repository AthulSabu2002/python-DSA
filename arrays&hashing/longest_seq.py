from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        
        store = set(nums)
    
        for num in nums:
            curr = num
            streak = 0
            while curr in store:
                streak += 1
                curr += 1
            res = max(streak, res)
        return res
    
if __name__ == "__main__":
    obj = Solution()
    print("dd", obj.longestConsecutive([2,20,4,10,3,4,5]))