from typing import List


def insertionSort(arr: List[int]) -> List[int]:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    
    return arr

if __name__ == "__main__":
    arr = [6, 8, 4, 5, 3, 2, 1]
    print(insertionSort(arr))