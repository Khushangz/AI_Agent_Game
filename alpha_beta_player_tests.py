import unittest

from alpha_beta_player import AlphaBetaPlayer
from board import Board

Player = AlphaBetaPlayer

class AlphaPlayerTests(unittest.TestCase):
    def test_Board_full(self):
        player = Player(1)
        board = Board()
        board.mark_space(0, "X")
        board.mark_space(1, "O")
        board.mark_space(2, "X")
        board.mark_space(3, "O")
        board.mark_space(4, "X")
        board.mark_space(5, "O")
        board.mark_space(6, "O")
        board.mark_space(7, "X")
        board.mark_space(8, "O")
        move = player.get_next_move(board)
        self.assertEqual(None, move)
    
    def test_one_space(self):
        player = Player(1)
        board = Board()
        board.mark_space(0, "X")
        board.mark_space(1, "O")
        board.mark_space(2, "X")
        board.mark_space(3, "O")
        board.mark_space(4, "X")
        board.mark_space(5, "O")
        board.mark_space(6, "O")
        board.mark_space(7, "X")
        move = player.get_next_move(board)
        self.assertEqual(8, move)

    def test_block(self):
        player = Player(1)
        board = Board()
        board.mark_space(0, "X")
        board.mark_space(1, "X")
        move = player.get_next_move(board)
        self.assertEqual(2, move)

    def test_win(self):
        player = Player(1)
        board = Board()
        board.mark_space(0, "O")
        board.mark_space(1, "O")
        move = player.get_next_move(board)
        self.assertEqual(2, move)

    def test_Utility_Function(self):
        player = Player(1)
        board = Board()
        board.mark_space(0, "O")
        move = player.get_next_move(board)
        self.assertEqual(4, move)
        
    def test_special_case(self):
        player = Player(2)
        board = Board()
        board.mark_space(0, "X")
        board.mark_space(4, "0")
        board.mark_space(8, "X")
        move = player.get_next_move(board)
        self.assertEqual(1, move)

    def test_alpha_function(self):
        player = Player(1)
        board = Board()
        board.mark_space(0, "O")
        board.mark_space(1, "O")
        board.mark_space(3, "X")
        board.mark_space(4, "X")
        alpha = -float('inf')
        beta = float('inf')
        score = player.alpha_beta(board, is_maximizing=True, alpha=alpha, beta=beta)
        self.assertEqual(score, 1)  

    def test_beta_function(self):
        player = Player(1)
        board = Board()
        board.mark_space(0, "O")
        board.mark_space(1, "X")
        board.mark_space(3, "O")
        alpha = -float('inf')
        beta = float('inf')
        score = player.alpha_beta(board, is_maximizing=False, alpha=alpha, beta=beta)
        self.assertEqual(score, -1) 
    
if __name__ == '__main__':
    unittest.main()
