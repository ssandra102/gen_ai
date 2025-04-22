"""tic tac toe - 2 player"""

import random


class TicTacToe:
    def __init__(self):
        self.board = [[' ' for i in range(3)] for j in range(3)]
        # self.board = [['x',' ',' '],[' ','o','o'],['x',' ','x']]
        self.current_winner = None
        self.player = 'x'
        self.opponent = 'o'
        self.score = 0

    def print_board(self):
        print("\n")
        for i in self.board:
            print(f'{i}')
        print("\n")

    def is_move_left(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    return True
        return False
    
    def check_winner(self):
        # check row-wise
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != ' ':
                self.current_winner = self.board[row][0]
                if self.current_winner == self.player:
                    self.score = 10
                else:
                    self.score = -10
                return self.score
        
        # check column-wise
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                self.current_winner = self.board[0][col]
                if self.current_winner == self.player:
                    self.score = 10
                else:
                    self.score = -10
                return self.score
            
        # check diagonal-wise
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            self.current_winner = self.board[0][0]
            if self.current_winner == self.player:
                self.score = 10
            else:
                self.score = -10
            return self.score
        
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            self.current_winner = self.board[0][2]
            if self.current_winner == self.player:
                self.score = 10
            else:
                self.score = 10
            return self.score
        
        return 0


    def minimax(self, depth, isMax):
        # implement min-max algorithm
        score = self.check_winner()
        if score == 10:
            return score
        if score == -10:
            return score
        
        if (not self.is_move_left()): # if there are no more moves left 
            return 0

        if isMax:
            # maximizer's move
            best = -1000
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = self.player
                        best = max(best, self.minimax(depth+1, not isMax))
                        self.board[i][j] = ' ' # undo the move
            return best
        
        else:
            # minimizer's move
            best = 1000
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = self.opponent
                        best = min(best, self.minimax(depth+1, not isMax))
                        self.board[i][j] = ' '
            return best

    def play_game(self):
        best_val = -1000
        best_move = (-1, -1)

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = self.player
                    move_val = self.minimax(0, False)
                    self.board[i][j] = ' '

                    if move_val > best_val:
                        best_move = (i, j)
                        best_val = move_val
        return best_move

if __name__ == '__main__':
    gameplay = TicTacToe()
    gameplay.print_board()
    print(gameplay.play_game())