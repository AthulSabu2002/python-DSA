from typing import List

def nextGreaterElement(arr: List[int]) -> List[int]:
    for i in range(len(arr)):
        greater = -1
        
        j = i + 1 if i + 1 <= len(arr) - 1 else 0
        for j in range(j, len(arr)):
            if arr[j] > arr[i]:
                greater = arr[j]
                break
        arr[i] = greater
    
    return arr

if __name__ == "__main__":
    arr = [3, 10, 4, 2, 1, 2, 6, 1, 7, 2, 9]  
    print(nextGreaterElement(arr))