from board import Board
from player import Player
import sys
import random
 # this code has a time complexity of O(n^2) where n is the number of open spaces
class GoalPlayer(Player):
    def __init__(self, number):
        super().__init__(number)


    def get_next_move(self, board: Board) -> int:
        possible = board.get_open_spaces()# O(n) where n is the number of open spaces
        if board.is_full():#O(1)
            return -1
        if 4 in possible and len(possible) == 8: #O(1)
            self.flag=1
            return 4
        for victory in [self.mark, self.opponent_mark]:#O(n)
            for plays in range(len(possible)):#O(n)
                board_copy = board.copy()#O(1)
                board_copy.mark_space(possible[plays], victory)#O(1)
                if board_copy.has_win(victory):#O(1)
                    return possible[plays]
       
        ran=random.choice(possible)#O(n)

        return ran
    
    # Time Complexity:
    # Best case: O(1) when only one open space
    # Worst case: O(n) where n is the number of open spaces
    # T(n)=O(n)+O(n)+O(1)+O(1)+O(1)+O(1)=O(n)

