import streamlit as st
from game import Game
from human_player import HumanPlayer
from minmax_player import Min_max_Player

# Initialize session state variables
if 'game' not in st.session_state:
    st.session_state.game = None
if 'current_player' not in st.session_state:
    st.session_state.current_player = None
if 'board_state' not in st.session_state:
    st.session_state.board_state = ['-'] * 9
if 'message' not in st.session_state:
    st.session_state.message = "Welcome to Tic-Tac-Toe!"

# Function to start a new game
def start_game(player1_type, player2_type):
    player1 = HumanPlayer(1) if player1_type == 'Human' else Min_max_Player(1)
    player2 = HumanPlayer(2) if player2_type == 'Human' else Min_max_Player(2)
    st.session_state.game = Game(player1, player2)
    st.session_state.current_player = player1
    st.session_state.board_state = ['-'] * 9
    st.session_state.message = f"Player {st.session_state.current_player.number}'s turn."

# Function to handle a player's move
def make_move(position):
    if st.session_state.board_state[position] == '-' and st.session_state.game:
        current_player = st.session_state.current_player
        st.session_state.game.board.mark_space(position, current_player.mark)
        st.session_state.board_state[position] = current_player.mark
        if st.session_state.game.board.has_win(current_player.mark):
            st.session_state.message = f"Player {current_player.number} wins!"
            st.session_state.game = None
        elif st.session_state.game.board.is_full():
            st.session_state.message = "It's a draw!"
            st.session_state.game = None
        else:
            st.session_state.current_player = (
                st.session_state.game.player1
                if st.session_state.current_player == st.session_state.game.player2
                else st.session_state.game.player2
            )
            st.session_state.message = f"Player {st.session_state.current_player.number}'s turn."

# Streamlit UI
st.title("Tic-Tac-Toe")

# Game setup
if st.session_state.game is None:
    st.subheader("Start a New Game")
    player1_type = st.selectbox("Select Player 1 Type", ['Human', 'AI'])
    player2_type = st.selectbox("Select Player 2 Type", ['Human', 'AI'])
    if st.button("Start Game"):
        start_game(player1_type, player2_type)
else:
    st.subheader(st.session_state.message)
    cols = st.columns(3)
    for i in range(3):
        for j in range(3):
            position = 3 * i + j
            if st.session_state.board_state[position] == '-':
                if cols[j].button(" ", key=position):
                    with st_stdout(st.empty()):
                        make_move(position)
            else:
                cols[j].button(st.session_state.board_state[position], key=position, disabled=True)

    if st.session_state.game is None and st.button("Play Again"):
        st.session_state.game = None
        st.session_state.current_player = None
        st.session_state.board_state = ['-'] * 9
        st.session_state.message = "Welcome to Tic-Tac-Toe!"
