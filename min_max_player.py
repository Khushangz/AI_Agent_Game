from board import Board
from player import Player
import sys

class Min_max_Player(Player):
    def __init__(self, number):
        super().__init__(number)
    def get_next_move(self, board: Board) -> int:
        possible_moves = board.get_open_spaces()
        b_s = -float('inf')
        b_m = None
        for move in possible_moves:
            board_copy = board.copy()  
            board_copy.mark_space(move, self.mark)  
            score = self.minimax(board_copy, is_maximizing=False) 

            
            if score > b_s:
                b_s = score
                b_m = move

        return b_m

    def minimax(self, board: Board, is_maximizing: bool) -> int:
        
        if board.has_win(self.mark):  
            return 1
        elif board.has_win(self.opponent_mark): 
            return -1
        elif board.is_full():  
            return 0

        if is_maximizing:
            max_V = -float('inf')
            for move in board.get_open_spaces():
                board_copy = board.copy() 
                board_copy.mark_space(move, self.mark)
                eval = self.minimax(board_copy, is_maximizing=False)
                max_V = max(max_V, eval) 
            return max_V
        else:
            min_V = float('inf')
            for move in board.get_open_spaces():
                board_copy = board.copy()  
                board_copy.mark_space(move, self.opponent_mark)
                eval = self.minimax(board_copy, is_maximizing=True)
                min_V = min(min_V, eval)  
            return min_V
