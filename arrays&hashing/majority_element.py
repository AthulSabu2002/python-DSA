from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = 0
        
        dict = {}
        
        for i, num in enumerate(nums):
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
            
            if dict[num] > m:
                ele = nums[i]
                m = dict[num]
                
        return ele
    

if __name__ == "__main__":
    obj = Solution()
    
    print(obj.majorityElement(nums = [5,5,1,1,1,5,5]))