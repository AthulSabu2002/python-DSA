from typing import List


def bubbleSort(arr: List[int]) -> List[int]:
    for i in range(0, len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

if __name__ == "__main__":
    arr = [8, 6, 7, 5, 4, 3, 2, 1]
    print(bubbleSort(arr))