from typing import List

def nextSmallerElement(arr: List[int]) -> List[int]:
    result = [-1] * len(arr)
    for i in range(len(arr)):
        smallest = -1
        
        for j in range(i, -1, -1):
            if arr[j] < arr[i]:
                smallest = arr[j]
                break
        result[i] = smallest
    
    return result

if __name__ == "__main__":
    arr = [3, 10, 4, 2, 1, 2, 6, 1, 7, 2, 9]  
    print(nextSmallerElement(arr))