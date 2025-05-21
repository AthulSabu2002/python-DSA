class Solution:
    def remove_duplicates(self, nums):
        if not nums:
            return 0

        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[j - 1]:
                nums[j] = nums[i]
                j += 1

        return j

if __name__ == "__main__":
    obj = Solution()
    print("Number of unique elements:", obj.remove_duplicates([2, 10, 10, 30, 30, 30]))
