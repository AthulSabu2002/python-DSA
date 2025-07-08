from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in nums[i+1:]:
                return [i, i+1 + nums[i+1:].index(complement)]
    

if __name__ == "__main__":
    obj = Solution()
    print(obj.twoSum([3, 4, 5, 6], 7))