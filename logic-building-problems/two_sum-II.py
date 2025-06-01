from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(0, len(numbers)):
            complement = target - numbers[i]
            if complement in numbers:
                return [i + 1, numbers.index(complement) + 1]
                
if __name__ == "__main__":
    obj = Solution()
    
    print(obj.twoSum([-1000,-900,-600,-500,-300,-200,-100,0,100,200,300,400,500,600,700,800,900,1000], -1300))