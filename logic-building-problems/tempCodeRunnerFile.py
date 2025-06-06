class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * ((2 * len(nums)) - 1)
        
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i + len(nums) - 1] = nums[i]
        
        return ans