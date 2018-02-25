class ToeplitzMAtrix:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for row_index in range(1, len(matrix)):
            for column_index in range(1, len(matrix[row_index])):
                if matrix[row_index][column_index] != matrix[row_index-1][column_index-1]:
                    return False
        return True

    def betterGroupMethod(self, matrix):
        group={}
        for row_index, row in range(1, len(matrix)):
            for column_index, column in range(1, len(row)):
                if row_index-column_index not in group:
                    group.[row_index-column_index] = column
                elif column != group[row_index - column_index]:
                    return False
        return True

    def betterOriginal(self, matrix):
        return all(r==0 or c==0 or matrix[r-1][c-1] == column
                   for r, row in enumerate(matrix)
                   for c , column in enumerate(row))
