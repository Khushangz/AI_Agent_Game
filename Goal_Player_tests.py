import unittest
from Goal_player import GoalPlayer
from board import Board


class UtilityPlayerTest(unittest.TestCase):
    def test_Board_full(self):
        player = GoalPlayer(1)
        board=Board()
        board.mark_space(0, "X")
        board.mark_space(1, "O")
        board.mark_space(2, "X")
        board.mark_space(3, "O")
        board.mark_space(4, "X")
        board.mark_space(5, "O")
        board.mark_space(6, "O")
        board.mark_space(7, "X")
        board.mark_space(8, "O")
        move=player.get_next_move(board)
        self.assertEqual(-1, move)
    
    def test_one_space(self):
        player = GoalPlayer(1)
        board=Board()
        board.mark_space(0, "X")
        board.mark_space(1, "O")
        board.mark_space(2, "X")
        board.mark_space(3, "O")
        board.mark_space(4, "X")
        board.mark_space(5, "O")
        board.mark_space(6, "O")
        board.mark_space(7, "X")
        move=player.get_next_move(board)
        self.assertEqual(8, move)

    def test_block(self):
        player = GoalPlayer(1)
        board=Board()
        board.mark_space(0, "X")
        board.mark_space(1, "X")
        move=player.get_next_move(board)
        self.assertEqual(2, move)

    def test_win(self):
        player = GoalPlayer(1)
        board=Board()
        board.mark_space(0, "O")
        board.mark_space(1, "O")
        move=player.get_next_move(board)
        self.assertEqual(2, move)

    def test_Centre_Capture(self):
        player = GoalPlayer(1)
        board=Board()
        board.mark_space(0, "O")
        move=player.get_next_move(board)
        self.assertEqual(4, move)

    
if __name__ == '__main__':
    unittest.main()