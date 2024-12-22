import streamlit as st
from tic_tac_toe import TicTacToeGame  # Import your game logic

# Initialize the game
if 'game' not in st.session_state:
    st.session_state.game = TicTacToeGame()

# Function to handle a player's move
def make_move(row, col):
    if st.session_state.game.make_move(row, col):
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
        if cell_value == '':
            if cols[col].button(" ", key=f"{row}-{col}"):
                make_move(row, col)
        else:
            cols[col].button(cell_value, key=f"{row}-{col}", disabled=True)

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
