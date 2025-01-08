class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def reverseArray(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start+=1
            end-=1
            
        return arr
    
    def rotateArr(self, arr, d):
        n = len(arr)
        
        d = d % n
        
        self.reverseArray(arr, 0, d-1)
        
        self.reverseArray(arr, d, n-1)
        
        self.reverseArray(arr, 0, n-1)
        
        
        return arr
    
    
if __name__ == "__main__":
    obj = Solution()
    print(obj.rotateArr([1, 2, 3, 4, 5], 2))