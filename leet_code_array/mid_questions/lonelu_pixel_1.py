class Solution:
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        lonlyBlackAmount = 0
        black_rows=[0] * 1500
        black_columns=[0] * 1500
        for rindex, row in enumerate(picture):
            for cindex, column in enumerate(row):
                if column == 'B':
                    black_rows[rindex] =  black_rows[rindex] + 1
                    black_columns[cindex] =  black_columns[cindex] + 1
        for rindex, row in enumerate(picture):
            for cindex, column in enumerate(row):
                if column == 'B' and black_rows[rindex] == 1 and black_columns[cindex] ==1:
                     lonlyBlackAmount = lonlyBlackAmount + 1

        return lonlyBlackAmount




