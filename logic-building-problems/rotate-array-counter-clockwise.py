class Solution:
    def rotateArr(self, arr, d):
        
        d = d % len(arr)
        
        for i in range(d):
            arr = arr[1 :len(arr)] + arr[0 : 1]
        
        return arr


if __name__ == "__main__":
    obj = Solution()
    print(obj.rotateArr([1, 2, 3, 4, 5], 2))