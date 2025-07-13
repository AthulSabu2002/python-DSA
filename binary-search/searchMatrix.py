from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        top = 0
        bottom = (rows * cols)  - 1
        
        while top <= bottom:
            middle_index = (top + bottom) // 2

            mid_row = middle_index // cols
            mid_col = middle_index % cols

            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] > target:
                bottom = middle_index - 1
            else:
                top = middle_index + 1
        
        return False
    
if __name__ == "__main__":
    obj = Solution()
    
    print(obj.searchMatrix(matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10))