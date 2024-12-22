from player import Player
from board import Board



class AlphaBetaPlayer(Player):
    def __init__(self, number):
        super().__init__(number)

    def get_next_move(self, board: Board) -> int:
        b_s = -float('inf')
        b_m = None  
        alpha = -float('inf')
        beta = float('inf')

        for move in board.get_open_spaces():
            board_copy = board.copy() 
            board_copy.mark_space(move, self.mark)
            score = self.alpha_beta(board_copy, is_maximizing=False, alpha=alpha, beta=beta) 
            if score > b_s:
                b_s = score
                b_m = move

            alpha = max(alpha, score)

        return b_m

    def alpha_beta(self, board: Board, is_maximizing: bool, alpha: int, beta: int) -> int:
        if board.has_win(self.mark): 
            return 1
        elif board.has_win(self.opponent_mark): 
            return -1
        elif board.is_full():  
            return 0

        if is_maximizing:
            max_v = -float('inf')
            for move in board.get_open_spaces():
                board_copy = board.copy()
                board_copy.mark_space(move, self.mark)  
                v = self.alpha_beta(board_copy, is_maximizing=False, alpha=alpha, beta=beta)
                max_v = max(max_v, v) 
                alpha = max(alpha, v) 
                if beta <=max_v:
                    break  
            return max_v
        else:
            v_m = float('inf')
            for move in board.get_open_spaces():
                board_copy = board.copy()
                board_copy.mark_space(move, self.opponent_mark) 
                v = self.alpha_beta(board_copy, is_maximizing=True, alpha=alpha, beta=beta)
                v_m = min(v_m, v)  
                beta = min(beta, v) 
                if alpha >= v_m:
                    break  
            return v_m
