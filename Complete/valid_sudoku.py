class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Use hash map to check duplicates

        # Check rows
        for row in board:
            counts = defaultdict(int)
            for index in row:
                if index == '.': continue
                counts[index] += 1
                if counts[index] > 1:
                    return False


        # Check columns
        for i in range(len(board[0])):
            counts = defaultdict(int)
            for row in board:
                index = row[i]
                if index == '.': continue
                counts[index] += 1
                if counts[index] > 1:
                    return False


        # Check grids (n^2 9^2 = 81, 3^4 = 81)
        # 3x3 row outer, columen outer
        for co in range(3):
            for ro in range(3):
                counts = defaultdict(int)
                #3x3 inside row innner, column inner
                for ci in range(3):
                    for ri in range(3):
                        index = board[co*3 + ci][ro*3 + ri]
                        if index == '.': continue
                        counts[index] += 1
                        if counts[index] > 1:
                            return False
                        
        return True
                

            