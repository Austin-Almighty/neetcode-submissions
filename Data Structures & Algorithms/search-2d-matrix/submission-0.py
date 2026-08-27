class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flattened_array = []
        for matrice in matrix:
            flattened_array.extend(matrice)
        head, tail = 0, len(flattened_array)-1
        while head <= tail:
            mid = (head+tail)//2
            if flattened_array[mid] == target:
                return True
            elif flattened_array[mid] < target:
                head = mid + 1
            else:
                tail = mid -1
        
        return False