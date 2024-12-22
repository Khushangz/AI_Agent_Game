from board import Board
from player import Player
import sys

class UtilityPlayer(Player):
    def __init__(self, number):
        self.flag=0
        super().__init__(number)

    def evaluate_board(self, board: Board):

        X2, X1, O2, O1 = 0, 0, 0, 0

        # Iterate through each winning line on the board
        for line in board.lines:#O(L) where L is the number of lines
            # if self.mark==1:
            #     p=self.mark
            #     o=self.opponent_mark
            # if self.mark==0:
            #     p=self.opponent_mark
            #     o=self.mark
            x_count = sum(1 for i in line if board.spaces[i] == self.mark)#O(3) 
            o_count = sum(1 for i in line if board.spaces[i] == self.opponent_mark)#O(3)
            if x_count == 2 and o_count == 0:#O(2)
                X2 += 1
            elif x_count == 1 and o_count == 0:#O(2)
                X1 += 1
            elif o_count == 2 and x_count == 0:#O(2)
                O2 += 1
            elif o_count == 1 and x_count == 0:#O(2)
                O1 += 1

        score = 3 * X2 + X1 - (3 * O2 + O1)#O(1)
        return score
    
    def get_next_move(self, board: Board) -> int:
        possible = board.get_open_spaces()
        if board.is_full():#O(1)
            return -1
        # if the board is empty always take a corner
        if len(possible) == 9:#O(1)
            return 0
        # if Human played first always take the center
        # if 4 in possible and len(possible) == 8: #O(2)
        #     self.flag=1
        #     return 4
        
        for victory in [self.mark, self.opponent_mark]:#O(2n)
            for plays in range(len(possible)):#O(n) n being the number of open spaces
                board_copy = board.copy()#O(1)
                board_copy.mark_space(possible[plays], victory)#O(1)
                if board_copy.has_win(victory):#O(1)
                    return possible[plays]

        # for corner in [0, 2, 6, 8]:#O(4)
        #     if corner in possible:#O(1)
        #         return corner
        best_score = -sys.maxsize  # Initialize with the lowest possible score
        best_move = possible[0]

        for move in possible:
            board_copy = board.copy()  # O(1)
            board_copy.mark_space(move, self.mark)  # O(1)

            # Evaluate the board after the move
            score = self.evaluate_board(board_copy)
            # sys.stdout.write(str(score)+"  ")
            if score > best_score:  # Maximize the score
                best_score = score
                best_move = move

        return best_move


    

    #Time Complexity:
    #Best case: O(1) when only one open space
    #Worst case: O(n) where n is the number of open spaces
    #T(n)=O(1)+O(1)+O(2)+O(2)+O(2n)+O(1)+O(1)+O(1)+O(4)+O(1)+O(1)=O(n)
    
