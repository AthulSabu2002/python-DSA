from typing import List

def selectionSort(arr: List[int]) -> List[int]:
    for i in range(0, len(arr)):
        
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        
        arr[i], arr[min] = arr[min], arr[i]
                 
    return arr


if __name__ == "__main__":
    arr = [7, 8, 5, 4, 3, 2, 1]
    print(selectionSort(arr))