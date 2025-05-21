from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count, prod = 0, 1
        
        for num in nums:
            if num:
                prod *= num
            else:
                zero_count += 1
        
        if zero_count > 1:
            return [0] * len(nums)
        
        res = [0] * len(nums)
        
        for i, c in enumerate(nums):
            if zero_count:
                if c == 0:
                    res[i] = prod
            else:
                res[i] = prod // c                    
        
        return res
    
    
if __name__ == '__main__':
    obj = Solution()

    nums = list(map(int, input().split(",")))
    
    print(nums)
    
    print(obj.productExceptSelf(nums))