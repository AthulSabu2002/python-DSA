from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        
        return k
    

if __name__ == "__main__":
    obj = Solution()
    
    print(obj.removeElement(nums = [1,1,2,3,4], val = 1))