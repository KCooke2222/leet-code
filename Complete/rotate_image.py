class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):  # number of elements in this layer
                top, bottom = l, r

                # save top-left
                topLeft = matrix[top][l + i]

                # top-left <- bottom-left
                matrix[top][l + i] = matrix[bottom - i][l]

                # bottom-left <- bottom-right
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # bottom-right <- top-right
                matrix[bottom][r - i] = matrix[top + i][r]

                # top-right <- saved top-left
                matrix[top + i][r] = topLeft

            r -= 1
            l += 1