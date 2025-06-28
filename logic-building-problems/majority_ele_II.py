from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        d = {}
        for num in nums:
            if num in d:
              d[num] += 1
            else:
                d[num] = 1
        
        n = len(nums) // 3
        
        for k, v in d.items():
            if v >= n:
                res.append(k)  
        
        return res
    
if __name__ == "__main__":
    obj = Solution()
    
    print(obj.majorityElement(nums = [5,2,3,2,2,2,2,5,5,5]))