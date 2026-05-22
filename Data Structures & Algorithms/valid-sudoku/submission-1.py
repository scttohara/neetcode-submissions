class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #checks rows
        for row in board:
            already_seen = set()

            for position_in_row in row:
                if position_in_row == ".":
                    continue
                elif position_in_row in already_seen:
                    return False
                else:
                    already_seen.add(position_in_row)
        
        #checks columns
        position = 0
        position_2 = 0
        while position < len(board):
            already_seen = set()

            while position_2 < len(board[position]):
                
                if board[position_2][position] == ".":
                    position_2 += 1
                    continue
                elif board[position_2][position] in already_seen:
                    return False
                else:
                    already_seen.add(board[position_2][position])
                
                position_2 += 1

            position_2 = 0
            position += 1

        #checks squares
        for square in range(9):
            square_set = set()
            for row_in_square in range(3):
                for column_in_square in range(3):
                    test1 = square // 3
                    test2 = square % 3
                    row = (square // 3) * 3 + row_in_square
                    column = (square % 3) * 3 + column_in_square

                    if board[row][column] == ".":
                        continue
                    if board[row][column] in square_set:
                        return False

                    square_set.add(board[row][column])

        return True