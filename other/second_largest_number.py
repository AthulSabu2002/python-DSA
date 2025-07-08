class Solution:
    def getSecondLargest(self, arr):
        second_largest = -1
        
        arr.sort()
        
        for i in range(len(arr)-1, -1, -1):
           if arr[i] > arr[i - 1]:
               second_largest = arr[i-1]
               break
           
        return second_largest



if __name__ == "__main__":
    obj = Solution()
    print(obj.getSecondLargest([12, 35, 1, 10, 34, 1]))