# not optimal, but good logic

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:   
        def walk_path(index, pos, walked):
            if index == len(word):
                return True

            i, j = pos
            directions = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]

            # check next letter exist
            for direction in directions:
                i, j = direction
                if 0 <= i < len(board) and 0 <= j < len(board[0]):
                    if board[i][j] == word[index] and direction not in walked:
                        if walk_path(index + 1, direction, walked + [(i, j)]):
                            return True
            
            return False # no path works out


        # linear search first letter
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == word[0]:
                    # walk path of first letter
                    if walk_path(1, (i, j), [(i, j)]):
                        return True

        return False


        
