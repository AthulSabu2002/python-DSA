from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[List[int]]:
        seen = set()
        pairs = []
        for num in numbers:
            complement = target - num
            if complement in seen:
                pairs.append([complement, num])
            seen.add(num)
        return pairs

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  
            
            target = -nums[i]
            two_sum_results = self.twoSum(nums[i+1:], target)
            for pair in two_sum_results:
                triplet = [nums[i]] + pair
                if triplet not in res:
                    res.append(triplet)
        return res


if __name__ == "__main__":
    obj = Solution()
    print(obj.threeSum([-4, -1, -1, 0, 1, 2]))