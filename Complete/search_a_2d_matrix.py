class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        h = len(matrix)
        w = len(matrix[0])

        def matrix_val(pos):
            return matrix[pos // w][pos % w]

        min = 0
        max = h * w - 1

        while min <= max:
            i = (min + max) // 2
            if matrix_val(i) == target:
                return True
            elif matrix_val(i) > target:
                max = i - 1
            else:
                min = i + 1

        return False  # target not found