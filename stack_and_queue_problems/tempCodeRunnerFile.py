from typing import List

def nextGreaterElement(arr: List[int]) -> List[int]:
    result = [-1] * len(arr)
    
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[i]:
                result[i] = arr[j]
                break
    
    return result

if __name__ == "__main__":
    arr = [3, 10, 4, 2, 1, 2, 6, 1, 7, 2, 9]  
    print(nextGreaterElement(arr))