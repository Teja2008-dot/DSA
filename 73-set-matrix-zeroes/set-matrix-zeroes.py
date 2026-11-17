class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i == 0:
                        if not isinstance(matrix[i][0], list):
                            matrix[i][0] = [1, 1]
                        matrix[i][0][1] = 0
                    else:
                        matrix[i][0] = 'z'
                    if j == 0:
                        if not isinstance(matrix[0][j], list):
                            matrix[0][j] = [1, 1]
                        matrix[0][j][0] = 0
                    else:
                        matrix[0][j] = 'z'
        for j in range (1, n):
            if matrix[0][j] == 'z':
                for i in range(m):
                    matrix[i][j] = 0

        for i in range (1, m):
            if matrix[i][0] == 'z':
                for j in range(n):
                    matrix[i][j] = 0

        if isinstance(matrix[0][0], list):
            if matrix[0][0][0] == 0:
                for i in range(1, m):
                    matrix[i][0] = 0
        if isinstance(matrix[0][0], list):
            if matrix[0][0][1] == 0:
                for j in range(n):
                    matrix[0][j] = 0
            matrix[0][0] = 0


        

   
    