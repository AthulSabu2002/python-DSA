class Solution:
    def reverseArray(self, arr):
        i = 0
        while i < (len(arr)) // 2:
            arr[i], arr[len(arr) - i - 1] = arr[len(arr) - i - 1], arr[i]
            i+=1
        
        return arr


if __name__ == "__main__":
    obj = Solution()
    print(obj.reverseArray([1, 2, 3, 4, 5]))
    