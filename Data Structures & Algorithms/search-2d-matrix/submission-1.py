class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix) 
        cols = len(matrix[0])

        head, tail = 0, rows*cols-1

        while head <= tail:
            mid = (head + tail) //2

            row = mid // cols
            col = mid % cols

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                head = mid + 1
            else:
                tail = mid - 1
        return False
        