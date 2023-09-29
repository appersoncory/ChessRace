# Author: Cory Apperson
# GitHub username: appersoncory
# Date: 08/17/2023
# Description: A game played on a chess board, where the players race their kings to the top row.

class ChessRaceGame:
    def __init__(self):
        """Initializes the game, creating the board,setting the starting player, and game state,"""
        self._board = {
            # Use a dictionary to represent the board, since each space can only have one piece.
            'a1': 'WK', 'b1': 'WB', 'c1': 'WN', 'd1': None, 'e1': None, 'f1': 'BN', 'g1': 'BB', 'h1': 'BK',
            'a2': 'WR', 'b2': 'WB', 'c2': 'WN', 'd2': None, 'e2': None, 'f2': 'BN', 'g2': 'BB', 'h2': 'BR',
            'a3': None, 'b3': None, 'c3': None, 'd3': None, 'e3': None, 'f3': None, 'g3': None, 'h3': None,
            'a4': None, 'b4': None, 'c4': None, 'd4': None, 'e4': None, 'f4': None, 'g4': None, 'h4': None,
            'a5': None, 'b5': None, 'c5': None, 'd5': None, 'e5': None, 'f5': None, 'g5': None, 'h5': None,
            'a6': None, 'b6': None, 'c6': None, 'd6': None, 'e6': None, 'f6': None, 'g6': None, 'h6': None,
            'a7': None, 'b7': None, 'c7': None, 'd7': None, 'e7': None, 'f7': None, 'g7': None, 'h7': None,
            'a8': None, 'b8': None, 'c8': None, 'd8': None, 'e8': None, 'f8': None, 'g8': None, 'h8': None
        }
        self._turn_color = "WHITE"
        self._game_state = "UNFINISHED"
        self._white_pending_win = False

    def get_board(self):
        """Returns the current chess board"""
        return self._board

    def get_turn_color(self):
        """Gets the color whose turn it is"""
        return self._turn_color

    def set_turn_color(self, color):
        """Sets the turn to the given color"""
        self._turn_color = color

    def get_game_state(self):
        """Returns the state of the game, e.g. 'UNFINISHED', 'WHITE_WON' """
        return self._game_state

    def set_game_state(self, state):
        """Sets the state of the game, e.g. 'UNFINISHED', 'WHITE_WON' """
        self._game_state = state

    def get_white_pending_win(self):
        """Returns whether the white player has a king in the top row, pending a win"""
        return self._white_pending_win

    def set_white_pending_win(self, state):
        """Sets whether the white player has a king in the top row, pending a win"""
        self._white_pending_win = state

    def is_valid_move(self, start, end):
        """Determines if a move is valid."""

        piece = self.get_board()[start]

        if not piece:
            return False  # No piece at the start position

        color = "WHITE" if piece[0] == "W" else "BLACK"

        if color != self.get_turn_color():
            return False  # Wrong player's turn

        if self.get_board()[end]:
            if self.get_board()[start][0] == self.get_board()[end][0]:
                return False  # Destination has a piece of the same color

        # Call the corresponding method for each piece type
        if piece[1] == "K":
            valid = self.is_valid_king_move(start, end)
        elif piece[1] == "R":
            valid = self.is_valid_rook_move(start, end)
        elif piece[1] == "N":
            valid = self.is_valid_knight_move(start, end)
        elif piece[1] == "B":
            valid = self.is_valid_bishop_move(start, end)
        else:
            valid = False

        if valid:
            # Temporarily make the move and check for check status
            captured_piece = self._board[end]
            self.get_board()[end] = piece
            self.get_board()[start] = None
            is_white_in_check = self.is_king_in_check("WHITE")
            is_black_in_check = self.is_king_in_check("BLACK")
            # Revert the move
            self.get_board()[start] = piece
            self.get_board()[end] = captured_piece

            if is_white_in_check or is_black_in_check:
                return False  # Can't make a move that puts own king in check

        return valid

    def is_valid_move_ignoring_checks(self, start, end):
        """Determines if a move is valid, ignoring possible king checks. Used when determining possible king checks."""

        piece = self.get_board()[start]
        # Call the corresponding method for each piece type
        if piece[1] == "K":
            valid = self.is_valid_king_move(start, end)
        elif piece[1] == "R":
            valid = self.is_valid_rook_move(start, end)
        elif piece[1] == "N":
            valid = self.is_valid_knight_move(start, end)
        elif piece[1] == "B":
            valid = self.is_valid_bishop_move(start, end)
        else:
            valid = False

        return valid

    # Placeholder methods for individual piece move validations
    def is_valid_king_move(self, start, end):
        """Return true if this is a valid move for the king"""

        # Get column and row for start and end
        start_col, start_row = ord(start[0]) - ord('a'), int(start[1])
        end_col, end_row = ord(end[0]) - ord('a'), int(end[1])

        # Check if the destination is a neighboring square
        col_diff = abs(start_col - end_col)
        row_diff = abs(start_row - end_row)

        # The king can move to any of its 8 neighboring squares
        if col_diff > 1 or row_diff > 1:
            return False

        return True

    def is_valid_rook_move(self, start, end):
        """Return true if this is a valid move for the rook"""

        current_board = self.get_board()
        start_col, start_row = ord(start[0]) - ord('a'), int(start[1])
        end_col, end_row = ord(end[0]) - ord('a'), int(end[1])

        # Check if the move is either horizontal or vertical
        if start_col != end_col and start_row != end_row:
            return False  # Rook can't move diagonally

        # Check if there's any piece in between the start and end squares
        if start_row == end_row:  # Horizontal move
            step = 1 if start_col < end_col else -1
            for col in range(start_col + step, end_col, step):
                if current_board[chr(col + ord('a')) + str(start_row)]:
                    return False  # There's a piece blocking the path
        else:  # Vertical move
            step = 1 if start_row < end_row else -1
            for row in range(start_row + step, end_row, step):
                if current_board[start[0] + str(row)]:
                    return False  # There's a piece blocking the path

        return True

    def is_valid_knight_move(self, start, end):
        """Return true if this is a valid move for the knight"""

        current_board = self.get_board()
        start_col, start_row = ord(start[0]) - ord('a'), int(start[1])
        end_col, end_row = ord(end[0]) - ord('a'), int(end[1])

        col_diff = abs(start_col - end_col)
        row_diff = abs(start_row - end_row)

        # Check for the "L" shaped move of the knight
        if (col_diff == 2 and row_diff == 1) or (col_diff == 1 and row_diff == 2):
            return True

        return False

    def is_valid_bishop_move(self, start, end):
        """Return true if this is a valid move for the bishop"""

        current_board = self.get_board()
        start_col, start_row = ord(start[0]) - ord('a'), int(start[1])
        end_col, end_row = ord(end[0]) - ord('a'), int(end[1])

        col_diff = abs(start_col - end_col)
        row_diff = abs(start_row - end_row)

        # Check for diagonal movement
        if col_diff != row_diff:
            return False

        col_step = 1 if start_col < end_col else -1
        row_step = 1 if start_row < end_row else -1

        current_col, current_row = start_col + col_step, start_row + row_step

        # Check for any pieces in the path
        while current_col != end_col and current_row != end_row:
            if current_board[chr(current_col + ord('a')) + str(current_row)]:
                return False  # There's a piece blocking the path
            current_col += col_step
            current_row += row_step

        return True

    def is_king_in_check(self, color):
        """Determines if the king of the specified color is in check."""

        current_board = self.get_board()

        # Finding the king's position based on the color
        king_position = None
        for pos, piece in current_board.items():
            if piece:
                if color == "WHITE" and piece[0] == "W":
                    if piece[1] == "K":
                        king_position = pos
                        break
                elif color == "BLACK" and piece[0] == "B":
                    if piece[1] == "K":
                        king_position = pos
                        break

        # Check if any of the opponent's pieces can make a valid move to the king's position
        for pos, piece in current_board.items():
            if piece:
                if (piece[0] == "W" and color == "BLACK") or (piece[0] == "B" and color == "WHITE"):  # Opponent's piece
                    # Temporarily set the piece at the king's position to None to allow capturing move check
                    target_piece = current_board[king_position]
                    current_board[king_position] = None
                    if self.is_valid_move_ignoring_checks(pos, king_position):
                        # Reset the piece at the king's position and return True
                        current_board[king_position] = target_piece
                        print("Can't move here, would put king in check.")
                        return True
                    # Reset the piece at the king's position
                    current_board[king_position] = target_piece
        return False

    def make_move(self, start, end):
        """Moves the piece from the first position to the second position, checking for winners and changing turn."""

        if self.get_game_state() != "UNFINISHED":
            return False

        if not self.is_valid_move(start, end):
            return False

        # move piece and capture if necessary
        self.get_board()[end] = self.get_board()[start]
        self.get_board()[start] = None

        # update game state
        # Check if the moved piece was a King, and if it was moved to the top row.
        if self.get_board()[end][1] == "K" and end[1] == "8":
            if self.get_turn_color() == "WHITE":  # White moved king to the top, they are about to win.
                self.set_white_pending_win(True)
            else:
                if self.get_white_pending_win():  # Black moved king to the top
                    self.set_game_state("TIE")  # Check if white's king is at the top, for a tie.
                else:
                    self.set_game_state("BLACK_WON") # Otherwise, black wins

        # switch turn
        self.set_turn_color("BLACK") if self.get_turn_color() == "WHITE" else self.set_turn_color("WHITE")

        # If it just became white's turn, and white is pending a win, and
        #  black hasn't won, white wins.
        if self.get_white_pending_win() and self.get_game_state() == "UNFINISHED" and self.get_turn_color() == "WHITE":
            self.set_game_state("WHITE_WON")

        return True

    # Optional print board function for debugging
    def print_board(self):
        """Prints the current board state with column labels at the bottom and row labels on the left."""

        for i in range(8, 0, -1):  # Start from the top row (8th) and go downwards
            row = [str(i)]  # Start each row with its row number
            for j in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
                position = j + str(i)
                piece = self.get_board()[position]
                row.append(piece if piece else "..")
            print(" ".join(row))

        # After printing all rows, print the column labels at the bottom
        print("  a  b  c  d  e  f  g  h")


def main():
    game = ChessRaceGame()
    print("Welcome to Chess Racing!")
    game.print_board()

    while game.get_game_state() == "UNFINISHED":
        start_pos = input(f"{game.get_turn_color()}'s turn. Enter start position (e.g. 'a2'): ")
        end_pos = input(f"Enter end position (e.g. 'a3'): ")

        if game.make_move(start_pos, end_pos):
            game.print_board()
        else:
            print("Invalid move. Please try again.")

        game_state = game.get_game_state()
        if game_state != "UNFINISHED":
            if game_state == "TIE":
                print("It's a tie!")
            else:
                print(f"{game_state.replace('_', ' ')}!")
            break


if __name__ == "__main__":
    main()
