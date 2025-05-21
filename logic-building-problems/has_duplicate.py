class Solution:
    def hasDuplicate(self, nums) -> bool:
        dict = {}
        for num in nums:
            if num in dict:
                return True
            else:
                dict[num] = 1
            
        
        
        return False
    
    
    
if __name__ == "__main__":
    obj = Solution()
    print(obj.hasDuplicate([2, 10]))
