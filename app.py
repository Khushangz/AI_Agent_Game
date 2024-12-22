import streamlit as st
from tic_tac_toe import Game, HumanPlayer, AlphaBetaPlayer  # Adjust imports based on your file structure

# Initialize players
player1 = HumanPlayer(1)
player2 = AlphaBetaPlayer(2)

# Initialize the game
if 'game' not in st.session_state:
    st.session_state.game = Game(player1, player2)

# Function to handle a player's move
def make_move(row, col):
    if st.session_state.game.board[row][col] == 0:  # Assuming 0 represents an empty cell
        st.session_state.game.board[row][col] = st.session_state.game.current_player
        st.session_state.game.switch_player()
        winner = st.session_state.game.check_winner()
        if winner:
            st.session_state.winner = winner

# Streamlit app layout
st.title("Tic Tac Toe")

# Display the game board
for row in range(3):
    cols = st.columns(3)
    for col in range(3):
        cell_value = st.session_state.game.board[row][col]
        display_value = ' ' if cell_value == 0 else 'X' if cell_value == 1 else 'O'
        if st.button(display_value, key=f"{row}-{col}"):
            make_move(row, col)

# Display game status
if 'winner' in st.session_state:
    if st.session_state.winner == 'Draw':
        st.success("It's a draw!")
    else:
        st.success(f"Player {st.session_state.winner} wins!")
    if st.button("Play Again"):
        st.session_state.game.reset()
        del st.session_state.winner
else:
    st.info(f"Player {st.session_state.game.current_player}'s turn")
